# coding: utf-8

# Copyright 2015-2018 Vincent Jacques <vincent@vincent-jacques.net>

master_doc = "index"
project = "Draw\nTurksHead"
author = '<a href="http://vincent-jacques.net/">Vincent Jacques</a>'
copyright = ('2013-2017 {} <script>var jacquev6_ribbon_github="DrawTurksHead"</script>'.format(author) +
             '<script src="https://jacquev6.github.io/ribbon.js"></script>')
extensions = []


nitpicky = True
nitpick_ignore = [
    ("py:class", "cairo.Context"),
]


# https://github.com/bitprophet/alabaster
# html_theme_path
extensions.append("alabaster")
html_theme = "alabaster"
html_sidebars = {
    "**": ["about.html", "navigation.html", "searchbox.html"],
}
html_theme_options = {
    "github_user": "jacquev6",
    "github_repo": project,
    "travis_button": True,
}
html_logo = "logo.png"


# http://sphinx-doc.org/ext/autodoc.html
extensions.append("sphinx.ext.autodoc")
# autoclass_content
autodoc_member_order = "bysource"
# autodoc_default_flags
# autodoc_docstring_signature
# autodoc_mock_imports
add_module_names = False
add_class_names = False


# http://sphinx-doc.org/ext/doctest.html
extensions.append("sphinx.ext.doctest")
# doctest_path
# doctest_global_setup
# doctest_global_cleanup
# doctest_test_doctest_blocks


# http://sphinx-doc.org/latest/ext/math.html
extensions.append("sphinx.ext.mathjax")
# mathjax_path

# http://matplotlib.org/devel/documenting_mpl.html#module-matplotlib.sphinxext.plot_directive
extensions.append("matplotlib.sphinxext.plot_directive")
plot_include_source = True
plot_html_show_source_link = False
# plot_pre_code
# plot_basedir
plot_formats = [("png", 160)]
plot_html_show_formats = False
# plot_rcparams
# plot_apply_rcparams
# plot_working_directory
# plot_template
