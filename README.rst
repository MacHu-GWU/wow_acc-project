
.. image:: https://readthedocs.org/projects/wow-acc/badge/?version=latest
    :target: https://wow-acc.readthedocs.io/en/latest/
    :alt: Documentation Status

.. image:: https://github.com/MacHu-GWU/wow_acc-project/actions/workflows/main.yml/badge.svg
    :target: https://github.com/MacHu-GWU/wow_acc-project/actions?query=workflow:CI

.. image:: https://codecov.io/gh/MacHu-GWU/wow_acc-project/branch/main/graph/badge.svg
    :target: https://codecov.io/gh/MacHu-GWU/wow_acc-project

.. image:: https://img.shields.io/pypi/v/wow-acc.svg
    :target: https://pypi.python.org/pypi/wow-acc

.. image:: https://img.shields.io/pypi/l/wow-acc.svg
    :target: https://pypi.python.org/pypi/wow-acc

.. image:: https://img.shields.io/pypi/pyversions/wow-acc.svg
    :target: https://pypi.python.org/pypi/wow-acc

.. image:: https://img.shields.io/badge/Release_History!--None.svg?style=social
    :target: https://github.com/MacHu-GWU/wow_acc-project/blob/main/release-history.rst

.. image:: https://img.shields.io/badge/STAR_Me_on_GitHub!--None.svg?style=social
    :target: https://github.com/MacHu-GWU/wow_acc-project

------

.. image:: https://img.shields.io/badge/Link-Document-blue.svg
    :target: https://wow-acc.readthedocs.io/en/latest/

.. image:: https://img.shields.io/badge/Link-API-blue.svg
    :target: https://wow-acc.readthedocs.io/en/latest/py-modindex.html

.. image:: https://img.shields.io/badge/Link-Install-blue.svg
    :target: `install`_

.. image:: https://img.shields.io/badge/Link-GitHub-blue.svg
    :target: https://github.com/MacHu-GWU/wow_acc-project

.. image:: https://img.shields.io/badge/Link-Submit_Issue-blue.svg
    :target: https://github.com/MacHu-GWU/wow_acc-project/issues

.. image:: https://img.shields.io/badge/Link-Request_Feature-blue.svg
    :target: https://github.com/MacHu-GWU/wow_acc-project/issues

.. image:: https://img.shields.io/badge/Link-Download-blue.svg
    :target: https://pypi.org/pypi/wow-acc#files


Welcome to ``wow_acc`` Documentation
==============================================================================
.. image:: https://wow-acc.readthedocs.io/en/latest/_static/wow_acc-logo.png
    :target: https://wow-acc.readthedocs.io/en/latest/

Data model for World of Warcraft account, realm and character.

Usage example:

.. code-block:: python

    from wow_acc.api import (
        Account,
        Realm,
        Character,
        Dataset,
    )

    # your code here


.. _install:

Install
------------------------------------------------------------------------------

``wow_acc`` is released on PyPI, so all you need is to:

.. code-block:: console

    $ pip install wow-acc

To upgrade to latest version:

.. code-block:: console

    $ pip install --upgrade wow-acc
