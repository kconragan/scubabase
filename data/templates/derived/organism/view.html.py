from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 4
_modified_time = 1220241982.239388
_template_filename='/Users/elemental/Sites/Scuba/scuba/templates/derived/organism/view.html'
_template_uri='/derived/organism/view.html'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from webhelpers.html import escape
_exports = ['extrahead', 'title']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    pass
def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, '/base/index.html', _template_uri)
def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        h = context.get('h', UNDEFINED)
        c = context.get('c', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'\n')
        # SOURCE LINE 4
        __M_writer(u' \n')
        # SOURCE LINE 9
        __M_writer(u'\n<h1>Name: ')
        # SOURCE LINE 10
        __M_writer(escape(c.content['name']))
        __M_writer(u'</h1>\n<img src="http://www.freebase.com/api/trans/image_thumb')
        # SOURCE LINE 11
        __M_writer(escape(c.content['/common/topic/image'][0]['id']))
        __M_writer(u'?maxheight=200&mode=fit&maxwidth=200" alt="photo of ')
        __M_writer(escape(c.content['/common/topic/image'][0]['name']))
        __M_writer(u'" />\n<dl>\n  <dt>Higher Classification:</dt>\n  <dd>')
        # SOURCE LINE 14
        __M_writer(escape(c.content['higher_classification']))
        __M_writer(u'</dd>\n  <dt>Scientific Name:</dt>\n  <dd>')
        # SOURCE LINE 16
        __M_writer(escape(c.content['scientific_name']))
        __M_writer(u'</dd>\n</dl>\n\n<h3>Organisms related to ')
        # SOURCE LINE 19
        __M_writer(escape(c.content['name']))
        __M_writer(u':</h3>\n\n<ul>\n')
        # SOURCE LINE 22
        for organism in c.related:
            # SOURCE LINE 23
            if not c.content['name'] == organism['name'][0]:
                # SOURCE LINE 24
                __M_writer(u'    <li><a href="')
                __M_writer(escape(h.format_guid(organism['guid'])))
                __M_writer(u'" title="View ')
                __M_writer(escape(organism['name'][0]))
                __M_writer(u'">')
                __M_writer(escape(organism['name'][0]))
                __M_writer(u'</a></li>\n')
        # SOURCE LINE 27
        __M_writer(u'</ul>\n\n<form action="/organism/view/" method="get" accept-charset="utf-8">\n  <input type="text" name="freebase-suggest" id="search-input" />\n  <p><input type="submit" value="Continue &rarr;"></p>\n</form>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_extrahead(context):
    context.caller_stack._push_frame()
    try:
        h = context.get('h', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 5
        __M_writer(u'\n<link rel="stylesheet" href="')
        # SOURCE LINE 6
        __M_writer(escape(h.url_for('/css/freebase-controls.css')))
        __M_writer(u'" type="text/css" media="screen" />\n<script type="text/javascript" src="')
        # SOURCE LINE 7
        __M_writer(escape(h.url_for('/js/freebase.suggest.js')))
        __M_writer(u'"></script>\n<script type="text/javascript" src="')
        # SOURCE LINE 8
        __M_writer(escape(h.url_for('/js/common.js')))
        __M_writer(u'"></script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context):
    context.caller_stack._push_frame()
    try:
        c = context.get('c', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 2
        __M_writer(u'\n  ')
        # SOURCE LINE 3
        __M_writer(escape(c.content['name']))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


