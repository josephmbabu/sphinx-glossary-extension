.. _Management:

**************************
Management
**************************

This page is how to management the updating of this extension. 

If you make changes to this extension, be sure to:

* Update this documentation.
* Follow the :ref:`rebuilding process <rebuild>`. 

.. todo::
   Find out how to place the current version of the extension on this page. 

.. _rebuild:

Rebulding Process
=====================

* Make changes to the site.
* If this is a new release update the number in conf.py
* delete the build directory. 
* ``sphinx-build -b html source build`` to get a new build directory
* Compress the build director and name it sde.zip
* Upload the new version to TEN3 site pointed to in the 03intro.rst and the 07setup.rst files. 



***************************
Updates Desired
***************************

* We may want to reconsider the zipping and downloading method.
* We might want to add an option to have the term added to the general index automatically. This option would be able to be turned on our off so the user could decide what typing of indexing they want to use for the site they are building. For example, if they are using it as a basic glossary and they just want to add a list of the glossary terms, then they would turn automatic indexing on. 

.. todo::
   Publish the extension with Sphinx or elsewhere. We should probably wait until the indexing is working before we do this.

