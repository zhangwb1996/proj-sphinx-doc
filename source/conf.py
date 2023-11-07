# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import sys
import os
sys.path.append(os.path.abspath('exts'))

project = 'zhangwb1996.github.io<br>lnvokerr\'s notes'
copyright = '2023, lnvokerr'
author = 'lnvokerr'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

# extensions = ['recommonmark', 'sphinx_markdown_tables']
extensions = [
    'myst_parser',
    "utterances",
    "mdfileinfo"
]

templates_path = ['_templates']
exclude_patterns = ["my-notes/草稿","*/**/README.md"]
language = 'zh_CN'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# html_theme = 'alabaster'
html_theme = 'sphinx_rtd_theme'
# html_theme_path = ["../../sphinx-theme/sphinx_rtd_theme"]
html_static_path = ['_static', 'my-notes/assets',]
html_css_files = [
    'assets/custom.css',
]
html_js_files = [
    'assets/custom.js',
    'assets/timestamp.js',
]
html_theme_options = {
    # Toc options
    'collapse_navigation': False,
    'sticky_navigation': True,
    'navigation_depth': 6,
    'includehidden': True,
    'titles_only': False,
    # "github_url": "https://github.com/zhangwb1996/zhangwb1996.github.io/issues",
    # 'analytics_id': 'G-XXXXXXXXXX',  # Provided by Google in your dashboard
    # 'analytics_anonymize_ip': False,
    # 'logo_only': False,
    # 'display_version': True,
    # 'prev_next_buttons_location': 'bottom',
    # 'style_external_links': False,
    # 'vcs_pageview_mode': '',
    # 'style_nav_header_background': 'white',
    # # Toc options
    # 'collapse_navigation': True,
    # 'sticky_navigation': True,
    # 'includehidden': True,
    # 'titles_only': False
}
html_split_index = True
# html_use_opensearch = "https://github.com/zhangwb1996/zhangwb1996.github.io/issues"

# html_context = {
#     "display_github": True,  # Integrate GitHub
#     # "github_user": "zhangwb1996",  # Username
#     # "github_repo": "zhangwb1996",  # Repo name
#     # "github_version": "main",  # Version
#     # "conf_py_path": "/issues/",  # Path in the checkout to the docs root
# }
html_show_sourcelink = False
source_suffix = {
    '.rst': 'restructuredtext',
    '.txt': 'markdown',
    '.md': 'markdown',
}
comments_config = {
    "utterances": {
        # "src": "https://utteranc.es/client.js",
        "repo": "zhangwb1996/zhangwb1996.github.io",
        "theme": "github-light",
        # "issue-term": "pathname",
        # "theme": "github-light",
        # "crossorigin": "anonymous",
        # "optional": "config",
    }
}

# display_toc =True
# numfig = True