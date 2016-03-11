import re
from docutils import nodes
from docutils.parsers.rst import Directive
from sphinx.util.compat import make_admonition
from sphinx.domains.std import StandardDomain
from sphinx.domains import Index
from sphinx.locale import _

class terminology(nodes.Admonition, nodes.Element):
    pass

class terminologylist(nodes.General, nodes.Element):
    pass

# class TerminologyIndex(Index):
#     """
#     Adds terminologies to the index
#     """
#     name = 'terminologyindex'
#     localname = 'Terminology Index'
#     shortname = 'terminologies'

#     def generate(self,  docnames = None):

#         collapse = False
#         content = []

#         for i in self.domain.data['objects']:
#             dirtype, name = i
#             print name
#             docname, anchor = self.domain.data['objects'][i]
#             #print docname
#             entries = [name, 0, docname, anchor, '','','']
#             letter = name[0]
#             content.append((letter, [entries]))
#         return (content, collapse)

def visit_terminology_node(self, node):
    self.visit_admonition(node)

def depart_terminology_node(self, node):
    self.depart_admonition(node)

class TerminologylistDirective(Directive):

    def run(self):
        return [terminologylist('')]

class TerminologyDirective(Directive):

    # this enables content in the directive
    has_content = True

    # Allows 15 directive arguments max, requires 1
    required_arguments = 1
    optional_arguments = 14
    final_argument_whitespace = False

    def run(self):
        env = self.state.document.settings.env

        targetid = "terminology-%d" % env.new_serialno('terminology')
        targetnode = nodes.target('', '', ids=[targetid])
        ad = make_admonition(terminology, self.name, [_(" ".join(self.arguments))], self.options,
                             self.content, self.lineno, self.content_offset,
                             self.block_text, self.state, self.state_machine)

        # terminology_all_terminologies must be set to True in config.py
        if not hasattr(env, 'terminology_all_terminologies'):
            env.terminology_all_terminologies = []
        env.terminology_all_terminologies.append({
            'docname': env.docname,
            'lineno': self.lineno,
            'terminology': ad[0].deepcopy(),
            'target': targetnode,
        })

        return [targetnode] + ad

def purge_terminologies(app, env, docname):
    if not hasattr(env, 'terminology_all_terminologies'):
        return
    env.terminology_all_terminologies = [terminology for terminology in env.terminology_all_terminologies
                          if terminology['docname'] != docname]

def process_terminology_nodes(app, doctree, fromdocname):
    if not app.config.terminology_include_terminologies:
        for node in doctree.traverse(terminology):
            node.parent.remove(node)

    # Replace all terminologylist nodes with a list of the collected terminologies.
    # Augment each terminology with a backlink to the original location.
    env = app.builder.env

    for node in doctree.traverse(terminologylist):
        if not app.config.terminology_include_terminologies:
            node.replace_self([])
            continue

        # The array to store all the terminologies accross the site
        # Structure: [term_info_1, term_reference_1, term_info_2, term_reference_2, ... term_info_n, term_reference_n]
        content = []

        # Loop through each terminology in the site environment
        for terminology_info in env.terminology_all_terminologies:
            para = nodes.paragraph()
            filename = env.doc2path(terminology_info['docname'], base=None)
            description = (
                _('(The original entry is located in %s, line %d and can be found ') %
                (filename, terminology_info['lineno']))
            para += nodes.Text(description, description)

            # Create a reference
            newnode = nodes.reference('', '')
            innernode = nodes.emphasis(_('here'), _('here'))
            newnode['refdocname'] = terminology_info['docname']
            newnode['refuri'] = app.builder.get_relative_uri(
                fromdocname, terminology_info['docname'])
            newnode['refuri'] += '#' + terminology_info['target']['refid']
            newnode.append(innernode)
            para += newnode
            para += nodes.Text('.)', '.)')

            # The data to enter into the terminologylist array
            input_list = [terminology_info['terminology'], para]

            # Add the input to the terminologylist in order
            content = __insert_in_order(input_list, content)

            # Insert into the terminologylist
            # content.append(terminology_info['terminology'])
            # content.append(para)
            
        # for item2 in content:
        #     title = __get_title_from_terminology_info(item2.__str__())
        #     if len(title) > 0:
        #         print title[0]

        node.replace_self(content)

# Insert a terminology into a terminologylist in order
def __insert_in_order(the_input, the_list):
    new_list =[]
    is_inserted = False

    # print "Entered list:"
    # for i in xrange(len(the_list)):
    #     print "\t",i,":",the_list[i]

    for item in xrange(len(the_list)):
        if the_list[item].__str__().find('<terminology') != -1:
            input_title = __get_title_from_terminology_info(the_input[0].__str__())[0]
            item_title = __get_title_from_terminology_info(the_list[item].__str__())[0]
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

    #print "Added: " + __get_title_from_terminology_info(the_input[0].__str__())[0]

    return new_list

# Search the title of the terminology object
def __get_title_from_terminology_info(info):
    return re.findall('(?<=<title>)(.*?)(?=<\/title>)', info)


def setup(app):
    """
    Todo:
        Fix it so that it adds terminologies to the index domain using the our custom 'terminology' directive
    """
    app.add_object_type('terminology', 'dir', 'single: %s; terminology')
    # app.add_index_to_domain('std', TerminologyIndex)
    # StandardDomain.initial_data['labels']['terminologyindex'] = ('std-terminologyindex', '', 'Terminology Index')
    # StandardDomain.initial_data['anonlabels']['terminologyindex'] = ('std-terminologyindex', '')
    
    app.add_config_value('terminology_include_terminologies', False, 'html')
    app.add_node(terminologylist)
    app.add_node(terminology,
                 html=(visit_terminology_node, depart_terminology_node),
                 latex=(visit_terminology_node, depart_terminology_node),
                 text=(visit_terminology_node, depart_terminology_node))

    app.add_directive('terminology', TerminologyDirective)
    app.add_directive('terminologylist', TerminologylistDirective)
    app.connect('doctree-resolved', process_terminology_nodes)
    app.connect('env-purge-doc', purge_terminologies)

    return {'version': '0.1'}   # identifies the version of our extension
