# coding: utf-8

# Copyright 2015 Vincent Jacques <vincent@vincent-jacques.net>

master_doc = "index"
project = "Pynamixel"
author = '<a href="http://vincent-jacques.net/contact">Vincent Jacques</a>'
copyright = "2015 {}".format(author)
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
# @todoc logo


# http://sphinx-doc.org/ext/autodoc.html
extensions.append("sphinx.ext.autodoc")
# autoclass_content
autodoc_member_order = "bysource"
autodoc_default_flags = ["members"]
# autodoc_docstring_signature
# autodoc_mock_imports
add_module_names = False
add_class_names = False


# http://sphinx-doc.org/ext/doctest.html
extensions.append("sphinx.ext.doctest")
# doctest_path
doctest_global_setup = """
# This setup is for README.rst's doctests.
# @todo Find a way to put that new actual doctests. See the message of the commit that introduced this line.
import MockMockMock
import Pynamixel
hardware_mock = MockMockMock.Engine().create("hardware")
hardware = hardware_mock.object

hardware_mock.expect.send([0xFF, 0xFF, 0x01, 0x05, 0x03, 0x1E, 0x00, 0x02, 0xD6])
hardware_mock.expect.receive(4).andReturn([0xFF, 0xFF, 0x01, 0x02])
hardware_mock.expect.receive(2).andReturn([0x00, 0xFC])

hardware_mock.expect.send([0xFF, 0xFF, 0x01, 0x04, 0x02, 0x2E, 0x01, 0xC9]).andReturn(None)
hardware_mock.expect.receive(4).andReturn([0xFF, 0xFF, 0x01, 0x03])
hardware_mock.expect.receive(3).andReturn([0x00, 0x01, 0xFA])
"""
# doctest_global_cleanup
doctest_test_doctest_blocks = True


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
