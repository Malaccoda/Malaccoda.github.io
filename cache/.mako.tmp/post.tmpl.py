# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1638068366.8441844
_enable_loop = True
_template_filename = 'themes/monospace/templates/post.tmpl'
_template_uri = 'post.tmpl'
_source_encoding = 'utf-8'
_exports = ['extra_head', 'content']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace('helper', context._clean_inheritance_tokens(), templateuri='post_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'helper')] = ns

    ns = runtime.TemplateNamespace('pheader', context._clean_inheritance_tokens(), templateuri='post_header.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'pheader')] = ns

    ns = runtime.TemplateNamespace('comments', context._clean_inheritance_tokens(), templateuri='comments_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'comments')] = ns

    ns = runtime.TemplateNamespace('math', context._clean_inheritance_tokens(), templateuri='math_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'math')] = ns

def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, 'base.tmpl', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        comments = _mako_get_namespace(context, 'comments')
        post = context.get('post', UNDEFINED)
        math = _mako_get_namespace(context, 'math')
        pheader = _mako_get_namespace(context, 'pheader')
        helper = _mako_get_namespace(context, 'helper')
        date_format = context.get('date_format', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        def extra_head():
            return render_extra_head(context._locals(__M_locals))
        _link = context.get('_link', UNDEFINED)
        messages = context.get('messages', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer('\n')
        __M_writer('\n')
        __M_writer('\n')
        __M_writer('\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'extra_head'):
            context['self'].extra_head(**pageargs)
        

        __M_writer('\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_extra_head(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        helper = _mako_get_namespace(context, 'helper')
        post = context.get('post', UNDEFINED)
        def extra_head():
            return render_extra_head(context)
        math = _mako_get_namespace(context, 'math')
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer(str(helper.twitter_card_information(post)))
        __M_writer('\n')
        if post.meta('keywords'):
            __M_writer('    <meta name="keywords" content="')
            __M_writer(filters.html_escape(str(post.meta('keywords'))))
            __M_writer('"/>\n')
        __M_writer(str(math.math_styles_ifpost(post)))
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        comments = _mako_get_namespace(context, 'comments')
        post = context.get('post', UNDEFINED)
        math = _mako_get_namespace(context, 'math')
        pheader = _mako_get_namespace(context, 'pheader')
        helper = _mako_get_namespace(context, 'helper')
        date_format = context.get('date_format', UNDEFINED)
        def content():
            return render_content(context)
        _link = context.get('_link', UNDEFINED)
        messages = context.get('messages', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n    <div class="post">\n    ')
        __M_writer(str(pheader.html_title()))
        __M_writer('\n        <div class="meta" style="background-color: rgb(234, 234, 234); ">\n        <span class="authordate">\n            ')
        __M_writer(str(messages("Posted:")))
        __M_writer(' <time class="published" datetime="')
        __M_writer(str(post.date.isoformat()))
        __M_writer('">')
        __M_writer(str(post.formatted_date(date_format)))
        __M_writer('</time>\n')
        if not post.meta('password'):
            __M_writer('               [<a href="')
            __M_writer(str(post.source_link()))
            __M_writer('" id="sourcelink">')
            __M_writer(str(messages("Source")))
            __M_writer('</a>]\n')
        __M_writer('        </span>\n        <br>\n')
        if post.tags:
            __M_writer('                <span class="tags">')
            __M_writer(str(messages("Tags")))
            __M_writer(':&nbsp;\n')
            for tag in post.tags:
                __M_writer('                    <a class="tag" href="')
                __M_writer(str(_link('tag', tag)))
                __M_writer('"><span>')
                __M_writer(str(tag))
                __M_writer('</span></a>\n')
            __M_writer('                </span>\n                <br>\n')
        __M_writer('        <span class="authordate">\n            ')
        __M_writer(str(pheader.html_translations(post)))
        __M_writer('\n        </span>\n        </div>\n    ')
        __M_writer(str(post.text()))
        __M_writer('\n    ')
        __M_writer(str(helper.html_pager(post)))
        __M_writer('\n')
        if not post.meta('nocomments'):
            __M_writer('        ')
            __M_writer(str(comments.comment_form(post.permalink(absolute=True), post.title(), post.base_path)))
            __M_writer('\n')
        __M_writer('    ')
        __M_writer(str(math.math_scripts_ifpost(post)))
        __M_writer('\n    </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "themes/monospace/templates/post.tmpl", "uri": "post.tmpl", "source_encoding": "utf-8", "line_map": {"23": 2, "26": 3, "29": 4, "32": 5, "38": 0, "55": 2, "56": 3, "57": 4, "58": 5, "59": 6, "64": 13, "69": 44, "75": 7, "84": 7, "85": 8, "86": 8, "87": 9, "88": 10, "89": 10, "90": 10, "91": 12, "92": 12, "98": 14, "112": 14, "113": 16, "114": 16, "115": 19, "116": 19, "117": 19, "118": 19, "119": 19, "120": 19, "121": 20, "122": 21, "123": 21, "124": 21, "125": 21, "126": 21, "127": 23, "128": 25, "129": 26, "130": 26, "131": 26, "132": 27, "133": 28, "134": 28, "135": 28, "136": 28, "137": 28, "138": 30, "139": 33, "140": 34, "141": 34, "142": 37, "143": 37, "144": 38, "145": 38, "146": 39, "147": 40, "148": 40, "149": 40, "150": 42, "151": 42, "152": 42, "158": 152}}
__M_END_METADATA
"""
