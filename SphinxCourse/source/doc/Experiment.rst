.. _Experimenting:

*************************
Experimenting
*************************

.. index::
   single: image; explained
   pair: image; directive

.. _imageimage:

image image
============

:ref:`pysite:tut-morecontrol`

From http://docutils.sourceforge.net/docs/ref/rst/directives.html#image::

   Directive Type:	"image"
   Doctree Element:	image
   Directive Arguments:	One, required (image URI).
   Directive Options:	Possible.
   Directive Content:	None.

   An "image" is a simple picture:
   
   .. image:: picture.png

   Inline images can be defined with an "image" directive in a substitution definition
   
   The URI for the image source file is specified in the directive argument. As with 
   hyperlink targets, the image URI may begin on the same line as the explicit markup 
   start and target name, or it may begin in an indented text block immediately 
   following, with no intervening blank lines. If there are multiple lines in the 
   link block, they are stripped of leading and trailing whitespace and joined together.
   
   Optionally, the image link block may contain a flat field list, the image options. 
   For example:

   .. image:: picture.jpeg
      :height: 100px
      :width: 200 px
      :scale: 50 %
      :alt: alternate text
      :align: right

   The following options are recognized:
   
   alt : text
   Alternate text: a short description of the image, displayed by applications that 
   cannot display images, or spoken by applications for visually impaired users.

   height : length
   The desired height of the image. Used to reserve space or scale the image vertically.
   When the "scale" option is also specified, they are combined. For example, a height
   of 200px and a scale of 50 is equivalent to a height of 100px with no scale.

   width : length or percentage of the current line width
   The width of the image. Used to reserve space or scale the image horizontally. 
   As with "height" above, when the "scale" option is also specified, they are combined.

   scale : integer percentage (the "%" symbol is optional)
   The uniform scaling factor of the image. The default is "100 %", i.e. no scaling.
   
   If no "height" or "width" options are specified, the Python Imaging Library (PIL) may
   be used to determine them, if it is installed and the image file is available.

   align : "top", "middle", "bottom", "left", "center", or "right"

   The alignment of the image, equivalent to the HTML <img> tag's "align" attribute. The
   values "top", "middle", and "bottom" control an image's vertical alignment (relative
   to the text baseline); they are only useful for inline images (substitutions). 
   The values "left", "center", and "right" control an image's horizontal alignment,
   allowing the image to float and have the text flow around it. The specific behavior
   depends upon the browser or rendering software used.

   target : text (URI or reference name)

   Makes the image into a hyperlink reference ("clickable"). The option argument may be a
   URI (relative or absolute), or a reference name with underscore suffix (e.g. `a name`_).

   and the common options :class: and :name:.


We typically put our images in a directory called source/images. This means our image directive would look like::

   .. image:: ../images/picture.png

|pencil| try to include some images into your site. Feel free to copy some images from our images directory. Also, remember you can see our source code by going to a page with an image and pressing the Show Source link.

.. index::
   pair: todo; extension
   single: todo; explained
   pair: todo; directive

.. comment: We've include the single and pair on the following index because we want the word substitution to be a hyperlink too. 

.. index:: 
   pair: substitution; |
   single: substitution

Substitutions
==================

Have you wondered if we insert an image every time you see a graphic of a |pencil|? 

Look at the source and see what we use. You find ``|pencil|``. This is known as a substitution. It can be used for more than images. Read the Substitution second on the :ref:`sld:rst-primer` page. 


To do 
========

There is a todo extension which we added when we did the sphinx-quickstart. To use it build a file as::

   .. _todo:

   ###########
   To do list
   ###########

   .. warning:: You need to update this file before a build if you want to see a new list.
   You can simple put in a space and save the file for it to rebuild.

   .. todolist::

Be sure to read the warning. This will help you from getting frustrated. 

* Save the file as doc/todo.rst 
* Include the file in our doc/doc.rst

Now add the todo directive someone such as::

   .. todo::

      This is just to show how to use the todo extension.

* Now rebuild your site and look at your todo list. 

.. todo::

   This is just to show how to use the todo extension.

If the todo extension is not working, make sure the todo extension is in the conf.py. If so, then make sure you have the spacing right with all your directives.

* Now add a todo in another file.
* Rebuild the site.

Does your todo show up?

* Edit the todo.rst, simple put a space in and delete it and save so the file date of saving is changed.
* Rebuild the site now. 

Does your todo show up now?


.. index::
   single: links

.. _links:

List-tables
=================

This section is from `geoserver`_.

Bulleted lists can sometimes be cumbersome and hard to follow.  When dealing with a long list of items, use list-tables.  For example, to talk about a list of options, create a table that looks like this:

.. list-table::
   :widths: 20 80
   :header-rows: 1
   
   * - Shapes
     - Description
   * - Square
     - Four sides of equal length, 90 degree angles
   * - Rectangle
     - Four sides, 90 degree angles
    
This is done with the following code::

   .. list-table::
      :widths: 20 80
      :header-rows: 1
      
      * - Shapes
        - Description
      * - Square
        - Four sides of equal length, 90 degree angles
      * - Rectangle
        - Four sides, 90 degree angles

.. index::
   triple: blank line; adding line in output; |

Adding a blank line
=====================

If you find you want a blank line in your output, use the virtical bar with a blank line before and after::

   ~blank line
   |
   ~blank line


Links
===========

There are three types of links: internal, external and intersphinx. 

.. index::
   pair: cross-reference; internal link
   single: cross-reference; a bit more detail
   single: links; internal links
   single: links; cross-reference

Internal Links
-----------------

:ref:`cross-reference`

:ref:`Read this section and then come back to this page <cross-reference>`

Look at the source of this page for the two ways I linked to the cross-referencing section. With the first I just used the label name and the section title appears for us as the link. With the second I put typed in the text I wanted to show as the link and then referred to the cross-reference label name. 

We can include label names anywhere in a file. When we reference it from another location we jump to that exact stop in the page. 


.. index::
   pair: external links; hyperlink
   single: links; external links

External Links
---------------

External links are links to the Internet. If you put a proper URL in the text like http://www.ten3.org, then Sphinx will automatically make it a hyperlink to the Internet.

You can choose to have different text show on your site for the external like using a format like::

   `Link text <http://example.com/>`_ 

For example, we can make it so just see `ten3.org <http://www.ten3.org>`_. 

.. index::
   single: links; intersphinx
   single: intersphinx
   single: label name; intersphinx
   pair: conf.py; intersphinx

Intersphinx
----------------

Intersphinx is a cool feature where you can use link to other Sphinx sites no matter where they are in the world using the sites label names. 

This takes a bit of work to set up, but it gives you some nice flexibility. For example, let's say you referred to a site 27 times in your site. If these were URLs and the site moves (and they do, more often than you'd believe), you'd need to find each the 27 occurrences and fix them. But if they were intersphinx links, you'd only have to change it in your conf.py and you'd be done. Also using the label names is a nice short-hand. 

The first thing you need to do is to put the location of the other Sphinx site into your conf.py. For this site we have::

   #3# sld stands for Sphinx Local Documentation; pysite refers to the python website, we didn't use py
   #3# because that is already assigned to the python domain for local code.
   intersphinx_mapping = {
      'sld': ('file:///home/admin2/it@houghton.academy/insyncLimited/Sphinx/Sphinx1.3.3.Doc/build', None),
      'pysite': ('https://docs.python.org/', None)
   }

sld refers to another Sphinx site on this computer. That is what file:/// means. pysite refers to the Internet as we can determine by the https://. 

.. Warning::

   Notice that there is a trailing slash / for the https:// site but not for the local files:/// site. 

We can now use links like::

   :ref:`pysite:tut-if` and :ref:`sld:rst-primer` 

That will produce these results :ref:`pysite:tut-if` and :ref:`sld:rst-primer`.

There are three Sphinx sites on this machine - this one, the Sphinx documentation we reference and your site. 

* Add the Sphinx documentation site and this site to your conf.py so you can do intersphinx with them from your site. Use the short-hand ten3 for outsite, such as we used pysite for the Python site.

Now you can add a link to this site. For example, put in your site somewhere::

   :ref:`ten3:links`

* Rebuild your site.

Where you put that link should be the word **Links** which is a hyperlink to our site. 

.. index::
   pair: glossary; directive

Glossary
==========

reStructuredText provides a :ref:`glossary directive <sld:glossary-directive>` which allows you to highlight words and define them. However, it does not automatically build a glossary. If you look at the Sphinx documentation's :ref:`glossary`, you will see they just built a simple page that used the glossary directive for formatting. 

Another approach would be to build a glossary page and make each word a section title and give them a label name that way you can reference the terms any time you want to. 

|pencil| Fix the glossary you build for yourself to follow one of the formats above. 

If you are a programmer, you could consider building a sphinx extenion that allows you to put the glossary entries where the term is first used and then builds the glossary page similiar to they way the todo extension works. See :ref:`sld:extensions` for more info.

.. index:: 
   single: table; creating
   single: list-table

Tables
===============

|pencil| Try make a list given the way it is explained on the :ref:`rst-primer` page. 

Another way to do lables is shown on .. _target list-table: http://docutils.sourceforge.net/docs/ref/rst/directives.html#list-table. We've included it here in case you do not have Internet access::

   Directive Type:	"list-table"
   Doctree Element:	table
   Directive Arguments:	1, optional (table title).
   Directive Options:	Possible (see below).
   Directive Content:	A uniform two-level bullet list.
   (New in Docutils 0.3.8. This is an initial implementation; further ideas may 
   be implemented in the future.)

   The "list-table" directive is used to create a table from data in a uniform 
   two-level bullet list. "Uniform" means that each sublist (second-level list) 
   must contain the same number of list items.

   Example:

   .. list-table:: Frozen Delights!
      :widths: 15 10 30
      :header-rows: 1

      * - Treat
        - Quantity
        - Description
      * - Albatross
        - 2.99
        - On a stick!
      * - Crunchy Frog
        - 1.49
        - If we took the bones out, it wouldn't be
          crunchy, now would it?
      * - Gannet Ripple
        - 1.99
        - On a stick!
   The following options are recognized:

   widths : integer [integer...]
   A comma- or space-separated list of relative column widths. The default is 
   equal-width columns (100%/#columns).
   
   header-rows : integer
   The number of rows of list data to use in the table header. Defaults to 0.
   
   stub-columns : integer
   The number of table columns to use as stubs (row titles, on the left). Defaults to 0.
   
   and the common options :class: and :name:.

|pencil| Try using list-table as well.

.. index::
   single: comment; in Sphinx

Comments
============

.. index::
   single: sidebar

.. sidebar:: Sidebars
   :subtitle: Are fun too

   You can easily add sidebars too. The block of text in the sidebar is parsed/interpreted. That means, it is interpreted like other text in your file. You can include inline markup like **bold** or can show literal blocks which are not parsed such as::

      * The markup is **not** parsed in a literal block.

   * But the rest of the block is parsed. We used a \* to build this line. 


If you want to put comments on your page that do now show up in the resulting site, then begin them with .. and a space. Anything not recognized by Sphinx is ignored. However, as a good habit it is a good idea to start them with comment such as::

   .. comment: blah blah blah ... 

This works because comment is not recognized. 

.. comment: here is an example of something not showing up.

.. index::
   triple: slash; backslash; escape
   single: escape; sequence

The sidebar introduces important terms and the concepts of literal and parsed blocks. A literal block is one that is shown just like it was typed. The mark-up language is not parsed. To mark means to work through it and translate it to the meaning give by the markup language syntax such as: \*\*would normally bold this section\*\*. 

You may be wondering how we got the two stars (\*) together without them showing up as bold. We used what is called an escape character, which is a backslash (\\) before the character. So if we want a star somewhere with use a backslash before it. Look at the source code to see this. 

|pencil| Read :ref:`parsed-literal` and explain what this directive does with the new terms you just learned. 

.. index::
   pair: reference; url

References
===============

.. target-notes::

.. _`geoserver`: http://docs.geoserver.org/latest/en/docguide/sphinx.html   

If you look at the source of this page, you will see that we used the target-notes directive to name the site we referred to and then label name in the body of the page as a short-hand instead of the long link.


More reStructuredText
=====================

Look up on :ref:`rstDirectives` page and find out how to make a box labeled tip. [#f1]_


Tip of the Iceburg
=====================

When a sailor sees an iceberg, they are seeing what is above the water. That is the tip of the iceberg. What is under the water is nearly 9 times bigger than what is above the water. So when someone says you have just touched the tip of an iceberg, it means you've just begun to learn about the options. That is the case here. We've got you started on a journey. The :ref:`Sphinx documentation <contents>` is a good start on learning more but there are other documents the Sphinx documentation refers to that you can also read to find out more options in Sphinx. We've also included :ref:`morerst` a lot more options for you if you want to dress up your site more.

The best thing to do is to experiment with the different features and to keep notes on your own Sphinx site for quick reference.



Clean up
============

Clean up your site so you can use it for the course you are in. For example, if you are in networking then set up the site so you can document your network as you build it. If you are in programming, you can keep track of what you learn in your site. 



.. rubric:: Footnotes

.. [#f1] You'll find the answer under Specific Admonitions.

.. include:: ../supporting/imageSubstitutions.txt
