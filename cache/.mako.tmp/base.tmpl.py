# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1636912286.6118984
_enable_loop = True
_template_filename = 'themes/monospace/templates/base.tmpl'
_template_uri = 'base.tmpl'
_source_encoding = 'utf-8'
_exports = ['extra_head', 'content', 'belowtitle', 'extra_js']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace('base', context._clean_inheritance_tokens(), templateuri='base_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'base')] = ns

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, 'base')._populate(_import_ns, ['*'])
        def belowtitle():
            return render_belowtitle(context._locals(__M_locals))
        def extra_head():
            return render_extra_head(context._locals(__M_locals))
        set_locale = _import_ns.get('set_locale', context.get('set_locale', UNDEFINED))
        content_footer = _import_ns.get('content_footer', context.get('content_footer', UNDEFINED))
        len = _import_ns.get('len', context.get('len', UNDEFINED))
        template_hooks = _import_ns.get('template_hooks', context.get('template_hooks', UNDEFINED))
        messages = _import_ns.get('messages', context.get('messages', UNDEFINED))
        lang = _import_ns.get('lang', context.get('lang', UNDEFINED))
        abs_link = _import_ns.get('abs_link', context.get('abs_link', UNDEFINED))
        body_end = _import_ns.get('body_end', context.get('body_end', UNDEFINED))
        def content():
            return render_content(context._locals(__M_locals))
        def extra_js():
            return render_extra_js(context._locals(__M_locals))
        blog_title = _import_ns.get('blog_title', context.get('blog_title', UNDEFINED))
        license = _import_ns.get('license', context.get('license', UNDEFINED))
        base = _mako_get_namespace(context, 'base')
        search_form = _import_ns.get('search_form', context.get('search_form', UNDEFINED))
        translations = _import_ns.get('translations', context.get('translations', UNDEFINED))
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer(str(set_locale(lang)))
        __M_writer('\n')
        __M_writer(str(base.html_headstart()))
        __M_writer('\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'extra_head'):
            context['self'].extra_head(**pageargs)
        

        __M_writer('\n')
        __M_writer(str(template_hooks['extra_head']()))
        __M_writer('\n</head>\n<body class="home blog">\n    <div id="wrap" style="width:850px">\n        <div id="container" style="width:560px">\n            ')
        __M_writer(str(template_hooks['page_header']()))
        __M_writer('\n            ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\n        </div>\n        <div id="sidebar">\n            <!--Sidebar content-->\n            <h1 id="blog-title">\n                <a href="')
        __M_writer(str(abs_link('/')))
        __M_writer('" title="')
        __M_writer(str(blog_title))
        __M_writer('">')
        __M_writer(str(blog_title))
        __M_writer('</a>\n            </h1>\n            ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'belowtitle'):
            context['self'].belowtitle(**pageargs)
        

        __M_writer('\n            <ul class="unstyled">\n            <li>')
        __M_writer(str(license))
        __M_writer('</li>\n            ')
        __M_writer(str(base.html_navigation_links()))
        __M_writer('\n            <li>')
        __M_writer(str(search_form))
        __M_writer('</li>\n            ')
        __M_writer(str(template_hooks['menu']()))
        __M_writer('\n            ')
        __M_writer(str(template_hooks['menu_alt']()))
        __M_writer('\n            </ul>\n        </div>\n        <div id="footer">\n            ')
        __M_writer(str(content_footer))
        __M_writer('\n            ')
        __M_writer(str(template_hooks['page_footer']()))
        __M_writer('\n        </div>\n    </div>\n    ')
        __M_writer(str(base.late_load_js()))
        __M_writer("\n    <script>\n    baguetteBox.run('div#content', {\n        ignoreClass: 'islink',\n        captions: function(element) {\n            return element.getElementsByTagName('img')[0].alt;\n    }});\n    </script>\n    ")
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'extra_js'):
            context['self'].extra_js(**pageargs)
        

        __M_writer('\n    ')
        __M_writer(str(body_end))
        __M_writer('\n    ')
        __M_writer(str(template_hooks['body_end']()))
        __M_writer('\n</body>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_extra_head(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'base')._populate(_import_ns, ['*'])
        def extra_head():
            return render_extra_head(context)
        __M_writer = context.writer()
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'base')._populate(_import_ns, ['*'])
        def content():
            return render_content(context)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_belowtitle(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'base')._populate(_import_ns, ['*'])
        def belowtitle():
            return render_belowtitle(context)
        messages = _import_ns.get('messages', context.get('messages', UNDEFINED))
        base = _mako_get_namespace(context, 'base')
        translations = _import_ns.get('translations', context.get('translations', UNDEFINED))
        len = _import_ns.get('len', context.get('len', UNDEFINED))
        __M_writer = context.writer()
        __M_writer('\n')
        if len(translations) > 1:
            __M_writer('            <small>\n                ')
            __M_writer(str(messages("Also available in:")))
            __M_writer('&nbsp;\n                ')
            __M_writer(str(base.html_translations()))
            __M_writer('\n            </small>\n')
        __M_writer('            ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_extra_js(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'base')._populate(_import_ns, ['*'])
        def extra_js():
            return render_extra_js(context)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "themes/monospace/templates/base.tmpl", "uri": "base.tmpl", "source_encoding": "utf-8", "line_map": {"23": 2, "26": 0, "54": 2, "55": 3, "56": 3, "57": 4, "58": 4, "63": 7, "64": 8, "65": 8, "66": 13, "67": 13, "72": 14, "73": 19, "74": 19, "75": 19, "76": 19, "77": 19, "78": 19, "83": 28, "84": 30, "85": 30, "86": 31, "87": 31, "88": 32, "89": 32, "90": 33, "91": 33, "92": 34, "93": 34, "94": 38, "95": 38, "96": 39, "97": 39, "98": 42, "99": 42, "104": 50, "105": 51, "106": 51, "107": 52, "108": 52, "114": 5, "122": 5, "128": 14, "141": 21, "153": 21, "154": 22, "155": 23, "156": 24, "157": 24, "158": 25, "159": 25, "160": 28, "166": 50, "179": 166}}
__M_END_METADATA
"""
