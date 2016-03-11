import re
from docutils import nodes
from docutils.parsers.rst import Directive
from sphinx.util.compat import make_admonition
from sphinx.domains.std import StandardDomain
from sphinx.domains import Index
from sphinx.locale import _

class definition(nodes.Admonition, nodes.Element):
    pass

class definitionlist(nodes.General, nodes.Element):
    pass

class DefinitionIndex(Index):
    """
    Adds terminologies to the index
    """
    name = 'definitionindex'
    localname = 'Definition Index'
    shortname = 'definitions'

    def generate(self,  docnames = None):

        collapse = False
        content = []

        for i in self.domain.data['objects']:
            dirtype, name = i
            print name
            docname, anchor = self.domain.data['objects'][i]
            #print docname
            entries = [name, 0, docname, anchor, '','','']
            letter = name[0]
            content.append((letter, [entries]))
        return (content, collapse)

def visit_definition_node(self, node):
    self.visit_admonition(node)

def depart_definition_node(self, node):
    self.depart_admonition(node)

class DefinitionlistDirective(Directive):

    def run(self):
        return [definitionlist('')]

class DefinitionDirective(Directive):

    # this enables content in the directive
    has_content = True

    # Allows 15 directive arguments max, requires 1
    required_arguments = 1
    optional_arguments = 14
    final_argument_whitespace = False

    def run(self):
        env = self.state.document.settings.env

        targetid = "definition-%d" % env.new_serialno('definition')
        targetnode = nodes.target('', '', ids=[targetid])
        ad = make_admonition(definition, self.name, [_(" ".join(self.arguments))], self.options,
                             self.content, self.lineno, self.content_offset,
                             self.block_text, self.state, self.state_machine)

        # definition_all_definitions must be set to True in config.py
        if not hasattr(env, 'definition_all_definitions'):
            env.definition_all_definitions = []
        env.definition_all_definitions.append({
            'docname': env.docname,
            'lineno': self.lineno,
            'definition': ad[0].deepcopy(),
            'target': targetnode,
        })

        return [targetnode] + ad

def purge_definitions(app, env, docname):
    if not hasattr(env, 'definition_all_definitions'):
        return
    env.definition_all_definitions = [definition for definition in env.definition_all_definitions
                          if definition['docname'] != docname]

def process_definition_nodes(app, doctree, fromdocname):
    if not app.config.definition_include_definitions:
        for node in doctree.traverse(definition):
            node.parent.remove(node)

    # Replace all definitionlist nodes with a list of the collected definitions.
    # Augment each definition with a backlink to the original location.
    env = app.builder.env

    for node in doctree.traverse(definitionlist):
        if not app.config.definition_include_definitions:
            node.replace_self([])
            continue

        # The array to store all the definitions accross the site
        # Structure: [term_info_1, term_reference_1, term_info_2, term_reference_2, ... term_info_n, term_reference_n]
        content = []

        # Loop through each definition in the site environment
        for definition_info in env.definition_all_definitions:
            para = nodes.paragraph()
            filename = env.doc2path(definition_info['docname'], base=None)
            description = (
                _('(The original entry is located in %s, line %d and can be found ') %
                (filename, definition_info['lineno']))
            para += nodes.Text(description, description)

            # Create a reference
            newnode = nodes.reference('', '')
            innernode = nodes.emphasis(_('here'), _('here'))
            newnode['refdocname'] = definition_info['docname']
            newnode['refuri'] = app.builder.get_relative_uri(
                fromdocname, definition_info['docname'])
            newnode['refuri'] += '#' + definition_info['target']['refid']
            newnode.append(innernode)
            para += newnode
            para += nodes.Text('.)', '.)')

            # The data to enter into the definitionlist array
            input_list = [definition_info['definition'], para]

            # Add the input to the definitionlist in order
            content = __insert_in_order(input_list, content)

            # Insert into the definitionlist
            # content.append(definition_info['definition'])
            # content.append(para)
            
        # for item2 in content:
        #     title = __get_title_from_definition_info(item2.__str__())
        #     if len(title) > 0:
        #         print title[0]

        node.replace_self(content)

# Insert a definition into a definitionlist in order
def __insert_in_order(the_input, the_list):
    new_list =[]
    is_inserted = False

    # print "Entered list:"
    # for i in xrange(len(the_list)):
    #     print "\t",i,":",the_list[i]

    for item in xrange(len(the_list)):
        if the_list[item].__str__().find('<definition') != -1:
            input_title = __get_title_from_definition_info(the_input[0].__str__())[0]
            item_title = __get_title_from_definition_info(the_list[item].__str__())[0]
            if item_title > input_title:
                # Insert our entry into content
                new_list = the_list[:item] + the_input +  the_list[item:]
                # print input_title,"is less than",item_title,"so:"
                # for i in xrange(len(new_list)):
                #     print "\t",i,":",new_list[i]
                is_inserted = True
                break

    if not is_inserted:
        new_list = the_list
        new_list += the_input
        # print "End of list, so:"
        # for i in xrange(len(new_list)):
        #     print "\t",i,":",new_list[i]

    #print "Added: " + __get_title_from_definition_info(the_input[0].__str__())[0]

    return new_list

# Search the title of the definition object
def __get_title_from_definition_info(info):
    return re.findall('(?<=<title>)(.*?)(?=<\/title>)', info)


def setup(app):
    """
    Todo:
        Fix it so that it adds definitions to the index domain using the our custom 'definition' directive
    """
    app.add_object_type('definition', 'dir', 'single: %s; definition')
    # app.add_index_to_domain('std', DefinitionIndex)
    # StandardDomain.initial_data['labels']['definitionindex'] = ('std-definitionindex', '', 'Definition Index')
    # StandardDomain.initial_data['anonlabels']['definitionindex'] = ('std-definitionindex', '')
    
    app.add_config_value('definition_include_definitions', False, 'html')
    app.add_node(definitionlist)
    app.add_node(definition,
                 html=(visit_definition_node, depart_definition_node),
                 latex=(visit_definition_node, depart_definition_node),
                 text=(visit_definition_node, depart_definition_node))

    app.add_directive('definition', DefinitionDirective)
    app.add_directive('definitionlist', DefinitionlistDirective)
    app.connect('doctree-resolved', process_definition_nodes)
    app.connect('env-purge-doc', purge_definitions)

    return {'version': '0.1'}   # identifies the version of our extension
