# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "Samy-O's Portfoli-O"
copyright = '2023, Samy-O'
author = 'Samy-O'
release = '0.1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['sphinx_immaterial',
              'sphinx_design',]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', 'food/template.rst']



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

rst_prolog = """
:hide-footer:
"""

html_theme = 'sphinx_immaterial'
html_static_path = ['_static']
html_css_files = ['custom.css']


# -- Material theme options --------------------------------------------------
# https://sphinx-immaterial.readthedocs.io/en/latest/
html_theme_options = {
    "icon": {
        "repo": "fontawesome/brands/github",
    },
    "site_url": "https://samy-o.github.io/portfolio/",
    "repo_url": "https://github.com/Samy-O/portfolio",
    "repo_name": "Rep-O",
    "repo_type": "github",
    "edit_uri": "blob/main/docs",
    "globaltoc_collapse": False,
    "features": [
        # "navigation.expand",
        # "navigation.tabs",
        # "toc.integrate",
        "navigation.sections",
        # "navigation.instant",
        # "header.autohide",
        "navigation.top",
        # "navigation.tracking",
        # "search.highlight",
        "search.share",
        "toc.follow",
        "toc.sticky",
        "content.tabs.link",
        "announce.dismiss",
    ],
    "palette": [
        {
            "media": "(prefers-color-scheme: light)",
            "scheme": "default",
            "primary": "teal",
            "accent": "blue-grey",
            "toggle": {
                "icon": "material/weather-night",
                "name": "Switch to dark mode",
            },
        },
        {
            "media": "(prefers-color-scheme: dark)",
            "scheme": "slate",
            "primary": "teal",
            "accent": "blue-grey",
            "toggle": {
                "icon": "material/weather-sunny",
                "name": "Switch to light mode",
            },
        },
    ],
    # BEGIN: version_dropdown
    "version_dropdown": False,
    # "version_info": [
    #     {
    #         "version": "https://sphinx-immaterial.rtfd.io",
    #         "title": "ReadTheDocs",
    #         "aliases": [],
    #     },
    #     {
    #         "version": "https://jbms.github.io/sphinx-immaterial",
    #         "title": "Github Pages",
    #         "aliases": [],
    #     },
    # ],
    # END: version_dropdown
    "toc_title_is_page_title": True,
    # BEGIN: social icons
    "social": [
        {
            "icon": "fontawesome/brands/github",
            "link": "https://github.com/Samy-O/portfolio",
            "name": "Source on github.com",
        },
        {
            "icon": "fontawesome/brands/linkedin",
            "link": "https://www.linkedin.com/in/samy-oubouaziz-8a172958/",
        },
    ],
    # END: social icons
}
