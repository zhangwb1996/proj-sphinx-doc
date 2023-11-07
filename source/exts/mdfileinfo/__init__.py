import os
from datetime import datetime
import time

# def get_file_time(app, docname):
#     """
#     This function gets the creation and modification time of the source file
#     and adds it to the context for use in the template.
#     """
#     src_file = app.env.doc2path(docname)
#     ctime = os.path.getctime(src_file)
#     mtime = os.path.getmtime(src_file)
#     ctime_str = datetime.datetime.fromtimestamp(ctime).strftime('%Y-%m-%d %H:%M:%S')
#     mtime_str = datetime.datetime.fromtimestamp(mtime).strftime('%Y-%m-%d %H:%M:%S')
#     app.builder.env.found_docs[docname].update({'ctime': ctime_str, 'mtime': mtime_str})

# def setup(app):
#     app.connect('env-updated', get_file_time)

def get_file_time(app, docname):
    """
    获取文件的创建时间和修改时间
    """
    doc_path = app.env.doc2path(docname)
    ctime = os.path.getctime(doc_path)
    mtime = os.path.getmtime(doc_path)
    # return time.ctime(ctime), time.ctime(mtime)
    return datetime.fromtimestamp(ctime), datetime.fromtimestamp(mtime)

def setup(app):
    """
    注册Sphinx扩展
    """
    app.connect('html-page-context', add_file_time_to_context)
    app.add_config_value('file_time_format', '%Y-%m-%d %H:%M:%S', 'html')

def add_file_time_to_context(app, pagename, templatename, context, doctree):
    """
    将文件的创建时间和修改时间添加到HTML上下文中
    """
    if not app.builder or app.builder.format != 'html':
        return
    docname = context.get('pagename')
    if not docname:
        return
    ctime, mtime = get_file_time(app, docname)
    # context['file_create_time'] = ctime
    # context['file_modified_time'] = mtime
    context['file_create_time'] = ctime.strftime(app.config.file_time_format)
    context['file_modified_time'] = mtime.strftime(app.config.file_time_format)