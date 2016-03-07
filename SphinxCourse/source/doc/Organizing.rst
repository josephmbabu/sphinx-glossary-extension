.. _organizing:

*****************************************
Organizing your work
*****************************************

.. index::
   single: toctree; explained

Table of Contents Tree (toctree directive)
===============================================

In this chapter we will explore how the toctree works. We will not exhaust the options, but get it to the point were we can organize our work. 

.. index::
   single: TOC; means table of contents
   single: table of contents; see also TOC

.. glossary::

   TOC standards for table of contents. 

* First we will build a template page that we can use to start other pages. In an editor make the following page. Name it template.rst and save it in the source folder with the index.rst. 

.. index::
   pair: heading; symbols

.. code::

   .. _template:

   ########################
   Template for Pages
   ########################

   The # above and below are used for Parts headings. 

   This is an empty page that we can use to build other pages. 

   We also uses it to keep track of some of our most used formatting so can find it quickly. 

   *****************
   Chapters
   *****************

   Sections
   ==================

   Subsections
   --------------------

   Subsubsections
   ^^^^^^^^^^^^^^^^^^^^^^^^^

   Paragraphs
   """"""""""""""""""""

As you work with Sphinx you can save whatever you desire in the template to help you make pages. The above is just an example. You do not need to include all the heading examples if you do not desire. 

Tibits::
   * The lines (symbols) have to be at least as long as the title. 
   * The above and below lines needs to be the same length.
   * The hierarchy of symbols is not fixed. That is, if you use = first in your document and then use # later, the = becomes heading 1 and the # becomes a lower level heading. 

.. todo::

   Test this more. Concerning the last tidbit, the heading methods systems to be dynamic. If you throw in a ## now it will not be at the top of the list. See if it can be the top by putting it in the first file or something. Find out how this works and decide what to do. 

.. index::
   triple: bookmark; target; label name
   pair: cross-reference; label name
   pair: cross-reference; target
   pair: cross-reference; bookmark

.. _cross-reference:

Cross-referencing
----------------------

The first line, ``.. _template:``, is a label name (also called a target) for cross-referencing purpose. It other applications this is often called a bookmark. The underscore and one : indicating it as a reference. (Directives have two colons :.) Having a label name means we can refer to this file from other pages by including::

:ref:`template`

Notice that the underscore does not proceed the name when you use it. 

.. Warning::

   Label names need to be directly above the section title. There should not be anything between them besides a blank line.

* In a terminal run ``sphinx-build -b html source build``

The -b html tells sphinx-build to create a website with html. There are other formats that you can build like PDF. We can consider those later. We just wanted to give you the reason for the -b html to help you remember the syntax so when we tell you to rebuild the site, you know to use this command and options. The other two options are the location of the source files and the next is where to put the results. Hence, we are telling sphinx-build that the source files are in source and we want the result in the build directory.

You will notices a _template directory in the source directory. Do not confuse this with the file we just created. 

* Refresh the Hello World Welcome page in your browser.

Do you see the template page?

Getting files to show up in the TOC
=========================================

.. index::
   pair: TOC; alphabetically

The template file did not show up. Add to the index.rst after the line :maxdepth: 2 add the following code::

   :glob:

   *

Be sure that these are indented the same about as the :maxdepth: option.

* rebuild the site and reload the Hello World wlecome page. 

|pencil| Now add serveral pages to determine:

* Do the other pages show up?
* What order do the show up?
* Does it matter if the file name begins with a capital letter or not?

.. index::
   single: TOC; in a given order

When you are creating a book the chapters do not tend to be in aphabetical order. To have your chapters in the order you want, you list them as part of the toctree directive. 

.. index::
   pair: directive; explained

This is the first time to use a directive so we should an idea of how they work in general::

   .. directive type:: directive
      block

The general format of the block is::

   [options]

   Data

With toctree we have in the index.rst file, we already have the options of :maxdepth: and :glob:, which we added just above to get the alphabetic listing. Now we will make order by:

* Delete the :glob: option. 
* Replace the * with the names of your files in the order you desire. Put one file name per line and make sure you indent them all the same about as the options are indented (typically 3 or 4 spaces). 

.. Note::

   The order you choose is the order that the previous and next button will use. That is, toctree makes is so that your files can be worked through in the order you gave them. The user will not need to return to the TOC to know what file is next.


Directories
==============

Let's assume you are developing a system that uses Python code and SQL code. You may want to keep your documentaiton and system organized with sub-directories of the source directory, such as pcode, scode and doc. 

|pencil| Set up the following directors and then put files in each of them. The files can be simple copies of the template file with the file name, label name (that is, the ``.. _template:``) and chapter title changed::

   * source/pcode
   * source/scode
   * source/doc

* Rebuild the site and reload the Hello World Welcome page.

Do you see the new directories and files?

* In the pcode directory, add a file pcode.rst with the following::

   .. _pcode:

   Programmer Documentation 
   =======================================

   Contents:

   .. toctree::
      :maxdepth: 10
      :glob:

      *

* Now add into index.rst after the file names you have listed the line::

   pcode/pcode

Which means in the pcode directory access the pcode.rst file.

For the files in pcode directory, what order are they in the TOC and why? [#f1]_

|pencil| Read :ref:`sld:toctree-directive` page and explain what will happen if you put de* the line before the * in your pcode.rst file. [#f2]_


.. index::
   single: SQL; adding SQL files
   single: adding; SQL files

Adding SQL files
================

The easiest way to add your SQL files is to take advantage of the fact that they are text files and many of database managers that read in SQL from a text file do not care what the extension of the file is. So we name our files as name.sql.rst. This way the toctree directive will process the files. 

.. Note::

   We are assuming that you have the source file suffix set to **.rst**. This should be the case if you followed our direction. .rst is the default when you run sphinx-quickstart. It can be changed in the conf.py which we've not discussed yet. 

* Create a file as follows and give it the name equipLocData.sql.rst. Store the file in the scode directory.

.. _sqlExample:

.. code::

   --equipLocData.sql
   ------------------
   /*

   Setting up the equipment and location portion of the equipment subsystem. 

       .. index::
          single: equipLocData
          single: SQL; equipLocData
          single: equipment subsystem; equipLocData

   This is just an example that we can put Sphinx commands in an SQL document if we:

   * Give the file an rst extension so they are evaluated. 
   * The first two lines in the file should be a subsection title because this is seen as a comment::

      --equipLocData
      --------------

   * Use the multiple line comment / * and \* / for your other comments. (Do not include spaces between the slashes and stars. We did that so there is not an error when SQL processes this file.)
   * You can add formatting, indexing and so forth inside the comments.

   \*/


INSERT INTO tblLocation (id,name,detail) VALUES (1,'room 105','math class');

INSERT INTO tblLocation (id,name,detail) VALUES (2,'room 107','science class');

INSERT INTO tblLocation (id,name,detail) VALUES (3,'room 209','art class');


What we have done here is take advantage that SQL uses -- as a comment and the Sphinx uses -- for a heading. This way we can start our files with something that Sphinx recognizes and can process. 

Then we take advantage of the multiple line comment (/* and \*/) available in SQL so we can add our Sphinx mark-up language in the comments and have them show as we desire. If we desire, we can even include pictures with the image directive. 

We double space the INSERT commands to make them easy for you to read. We could leave them single line but Sphinx would make them into a single paragraph which is harder to read. As far as SQL is concerned, they can be all on one line. It will still process them. 

.. index::
   triple: \; escape; showing reserved characters
   single: SQL; escape sequence in comments
   triple: backslash; SQL; \

Typically, you would not have \\\*/ to end a comment in SQL. We included the first backslash as an escape for Sphinx. If we do not include that slash then Sphinx will give you a warning that you started and emphasis and didn't end it. You can use this switch for other characters you want to show. For an example, look at the source of this paragraph and you'll see we used the slash to show both the star and the slash. 

|pencil| Try it. Take off the \\ slash and rebuild the site. You'll see the warning. You will also see another warning which will discuss next.

We are doing this extra work so we do not have superfluous (warnings that are not real). That way we can focus on warnings we do get and work to get our site working properly. 

.. Note::
   Making changes to a page and rebuilding the site to see what happens is a great way to learn Sphinx and any programming language.

.. index::
   single: warning; document isn't included in any toctree
   single: toctree; document isn't included in any toctree
   single: document isn't included in any toctree

Now let's consider the warning that ends with *source/scode/equipLocData.sql.rst:: WARNING: document isn't included in any toctree*. Let's try to think through this. What files have we already used the toctree directive?

In those files, how have we include the .rst files in their directories?

Okay, we've used two methods. In doc.rst we included in the order we want them. In the index.rst we've referenced the doc.rst in its directory. Prior to this we've also used :glob: to show all the .rst files in a directory in alphabetically order - kind-of - it is case-sensitive so the capital letters are before the lowercase letters. 

* Use the :glob: method and create a scode.rst file so show the files in the pcode folder. 
* Rebuild the site. Did it work or did you get an warning?

You should have got a warning the scode.rst is not in any toctree. 

* Look back at the index.rst and decide what to do. Then rebuild the site. [#f3]_

.. index::
   pair: how to; index

Indexing
===========

We put a simple example of indexing in the SQL code :ref:`above <sqlExample>`. 

* Rebuild the site.
* Go to the index and find the entries for the SQL you just added. 

Indexing is very important to organizing your work. An index that is more than just the words used, but indexes concepts allows people to find what they need. This is more powerful than just a search. You should think about the different ways someone may be looking for the material and including index entries for these. Again, indexing the concepts rather than just the words is very powerful.

|pencil| Find and read the indexing section on :ref:`this page <sld:metadata>`. Test out the single, pair, triple and see options. At least once in your testing use the inline :index: method. 

|pencil| Convert the document/spreadsheet you have been developing with the terms you are learning into a text file. Call it myGlossary.rst. Put the words you have it this file using the formatting we've learned thus far or look up new directives and try them out if you desire. Index each of the words so they show up in the index as you desire. You can even use another language if you prefer. 

.. Warning::

   If you make it your habit to index just above a section, you will want to keep in mind that if the section also has a label name, to be sure to put the index directive above the label name. Label names need to be directly above the section title. 

.. index::
   pair: rebuild; site
   pair: no targets are out of date; site
   single: rebuild; build succeeded with no warnings

Rebuild Site
======================

no targets are out of date
--------------------------------

* In a terminal run ``sphinx-build -b html source build``
* Do it again, run ``sphinx-build -b html source build``

Notice the line ``no targets are out of date.``. This means that there were no files changed so they were not rebuilt. The significance of this can be seen in this example. Let's say the following happens when I'm build this course.

* In a file (abc.rst) we make a label ``.. _blah:``. 
* We reference the new label the Expeirment.rst file.
* We rebuild the site and get no warnings.
* A week later we decided to change the label in abc.rst to ``.. _blahblah:``.
* We rebuild the site and get no warnings. 

However, we do have a problem. sphinx-build only rebuilds files that were changed. Hence, Experiment.rst's link is out-of-date and points to blah, but blah doesn't exist any longer. If we had made a change to Experiment.rst then the rebuild would have given us a warning on this unknown label.

.. Note::

   Things to keep in mind:

   * Keep in mind that if you want to see changes in a file, you need to save it again so it is rebuilt.
   * You need to think of what side-effects might occor when you change things like labels. 


build succeeded with no warnings
-------------------------------------

.. important::

   When you do a build or rebuild, it is important to get ``build succeeded.`` with no warnings as the last line.

If you do get warnings, you should clean them up so you know your site is working properly.




.. rubric:: Footnotes

.. [#f1] They are in alphabetic order because we used the :glob: and \*.  

.. [#f2] All the files starting with de will be listed before the other files in the folder.

.. [#f3] Be sure to include pcode/pcode in the index.rst file so your pcode.rst is processed. 

.. |pencil| image:: ../images/Pencil.png
          :align: middle
          :alt: Try It
          :width: 38 px
