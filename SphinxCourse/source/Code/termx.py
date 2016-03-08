from docutils import nodes
import re

class termx(nodes.Admonition, nodes.Element):
    pass

class termxlist(nodes.General, nodes.Element):
    pass

def visit_termx_node(self, node):
    self.visit_admonition(node)

def depart_termx_node(self, node):
    self.depart_admonition(node)

from docutils.parsers.rst import Directive

class TermxlistDirective(Directive):

    def run(self):
        return [termxlist('')]

from sphinx.util.compat import make_admonition
from sphinx.locale import _

class TermxDirective(Directive):

    # this enables content in the directive
    has_content = True

    # Allows 15 directive arguments max, requires 1
    required_arguments = 1
    optional_arguments = 14
    final_argument_whitespace = False

    def run(self):
        env = self.state.document.settings.env

        targetid = "termx-%d" % env.new_serialno('termx')
        targetnode = nodes.target('', '', ids=[targetid])
        print 'arguments:'
        print self.arguments
        ad = make_admonition(termx, self.name, [_(" ".join(self.arguments))], self.options,
                             self.content, self.lineno, self.content_offset,
                             self.block_text, self.state, self.state_machine)

        if not hasattr(env, 'termx_all_termxs'):
            env.termx_all_termxs = []
        env.termx_all_termxs.append({
            'docname': env.docname,
            'lineno': self.lineno,
            'termx': ad[0].deepcopy(),
            'target': targetnode,
        })

        return [targetnode] + ad

def purge_termxs(app, env, docname):
    if not hasattr(env, 'termx_all_termxs'):
        return
    env.termx_all_termxs = [termx for termx in env.termx_all_termxs
                          if termx['docname'] != docname]

def process_termx_nodes(app, doctree, fromdocname):
    if not app.config.termx_include_termxs:
        for node in doctree.traverse(termx):
            node.parent.remove(node)

    # Replace all termxlist nodes with a list of the collected termxs.
    # Augment each termx with a backlink to the original location.
    env = app.builder.env

    for node in doctree.traverse(termxlist):
        if not app.config.termx_include_termxs:
            node.replace_self([])
            continue

        content = []

        for termx_info in env.termx_all_termxs:
            para = nodes.paragraph()
            filename = env.doc2path(termx_info['docname'], base=None)
            description = (
                _('(The original entry is located in %s, line %d and can be found ') %
                (filename, termx_info['lineno']))
            para += nodes.Text(description, description)

            # Create a reference
            newnode = nodes.reference('', '')
            innernode = nodes.emphasis(_('here'), _('here'))
            newnode['refdocname'] = termx_info['docname']
            newnode['refuri'] = app.builder.get_relative_uri(
                fromdocname, termx_info['docname'])
            newnode['refuri'] += '#' + termx_info['target']['refid']
            newnode.append(innernode)
            para += newnode
            para += nodes.Text('.)', '.)')

            input_list = [termx_info['termx'], para]
            content = __insert_in_order(input_list, content)

            # Insert into the termxlist
            # content.append(termx_info['termx'])
            # content.append(para)

        # newlist = sorted(content, key=lambda x: x, reverse=True)
        node.replace_self(content)

def __insert_in_order(the_input, the_list):
    new_list =[]
    is_inserted = False

    for item in xrange(len(the_list)):
        if the_list[item].__str__().find('<termx') != -1:
            input_title = __get_title_from_termx_info(the_input[0].__str__())[0]
            item_title = __get_title_from_termx_info(the_list[item].__str__())[0]
            if item_title > input_title:
                # Insert our entry into content
                new_list = the_input + the_list[:item] + the_list[item:]
                is_inserted = True

    if not is_inserted:
        new_list.append(the_input[0])
        new_list.append(the_input[1])

    return new_list

def __get_title_from_termx_info(info):
    return re.findall('(?<=<title>)(.*?)(?=<\/title>)', info)


def setup(app):
    app.add_config_value('termx_include_termxs', False, 'html')

    app.add_node(termxlist)
    app.add_node(termx,
                 html=(visit_termx_node, depart_termx_node),
                 latex=(visit_termx_node, depart_termx_node),
                 text=(visit_termx_node, depart_termx_node))

    app.add_directive('termx', TermxDirective)
    app.add_directive('termxlist', TermxlistDirective)
    app.connect('doctree-resolved', process_termx_nodes)
    app.connect('env-purge-doc', purge_termxs)

    return {'version': '0.1'}   # identifies the version of our extension


