# coding: utf-8

# Copyright 2013-2015 Vincent Jacques <vincent@vincent-jacques.net>

import os
import sys
sys.path.append(os.path.dirname(__file__))
import algorithm_images
algorithm_images.create(os.path.dirname(__file__))


master_doc = "index"
project = "DrawTurksHead"
author = '<a href="http://vincent-jacques.net/contact">Vincent Jacques</a>'
copyright = "2013-2015 {}".format(author)
extensions = []


nitpicky = True
# nitpick_ignore


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
    "github_banner": True,
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
doctest_test_doctest_blocks=True


# http://sphinx-doc.org/latest/ext/math.html
extensions.append("sphinx.ext.mathjax")
# mathjax_path
