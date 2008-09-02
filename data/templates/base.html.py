from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 4
_modified_time = 1220147634.908525
_template_filename='/Users/elemental/Sites/Scuba/scuba/templates/base.html'
_template_uri='/base.html'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from webhelpers.html import escape
_exports = []


def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        self = context.get('self', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN"\n\t"http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">\n\n<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">\n<head>\n\t<meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>\n\n\t<title>')
        # SOURCE LINE 8
        __M_writer(escape(self.title()))
        __M_writer(u'</title>\n\t\n</head>\n\n<body>\n\n')
        # SOURCE LINE 14
        __M_writer(escape(self.body()))
        __M_writer(u'\n\n<div id="footer">\n  &copy; Kai Conragan\n</div>\n\n</body>\n</html>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


