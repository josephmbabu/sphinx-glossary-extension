.. _HelloWorld:

**************************
Hello World
**************************

There are reasons that Hello World is the most common first program to write when you are learning a programming language: 

* There are precursors you need before you can ever write a program. 
   * Installing the programming language.
   * Learning the IDE, we'll come back to that one.
   * Learning some initial terminology and acronyms like IDE - Integrated Development Environment.
   * Okay, back to learning the IDE, if there is one and if not, how to write the program. 
   * Learning the minimum amount of syntax to get the first Hello World running.
* The psychological advantage of having a success under your belt, so you are ready to move on to other challenges, particular to start considering the language. 

You may not be thinking of Sphinx as a programming language, since it is for documentation. But Sphinx is an advanced markup-language with syntax that needs to be followed like a programming language. In the 1980s Sphinx would have been called a 4th generation language. Sphinx also uses some other advanced markup-languages like reStructuredText. So when, I, Dr. Petrillo, wanted to start using Sphinx, my first desire was to get Hello World running. Once I was over that hump, I knew that I could turn to other documentation to build on my newfound knowledge and with practice, become proficient in Sphinx. 

Windows OS: If you are running on a Windows system you need to install Sphinx in the Python directory under Script and then put that new directory in path so Windows would find the new programs. Note, this is not needed on a Linux system. 

.. todo::
   Test out the windows environment to see if more needs to be explained here. 

Decide the name you will give the directory where you will put your documenation. In our example we are using Sphinx. Remember on a Linux sysem the directory names are case-sensitive. 

In a terminal do the following (remember that the > represent the terminal prompt and you do not type that character):

.. code::

   > mkdir sphinx 
   > cd 
   > sphinx-quickstart

.. todo::
   Check if mkdir and cd work in windows?

The following are the questions you'll be asked. Answer yours like we answer here. You'll see what each of these mean as we play around the different features. 

.. definition:: Jaguar

   The jaguar (Panthera onca) is a big cat, a feline in the Panthera genus, and is the only extant Panthera species native to the Americas.

.. code::

   Welcome to the Sphinx 1.3.1 quickstart utility.

   Please enter values for the following settings (just press Enter to
   accept a default value, if one is given in brackets).

   Enter the root path for documentation. 
   Root path for the documentation [.]:

   You have two options for placing the build directory for Sphinx output.
   Either, you use a directory "_build" within the root path, or you separate
   "source" and "build" directories within the root path.
   Separate source and build directories (y/n) [n]: y

   Inside the root directory, two more directories will be created; "_templates"
   for custom HTML templates and "_static" for custom stylesheets and other static
   files. You can enter another prefix (such as ".") to replace the underscore.
   Name prefix for templates and static dir [_]: 

   The project name will occur in several places in the built documentation.
   Project name: Hello World
   Author name(s): Baba Computer

   Sphinx has the notion of a "version" and a "release" for the
   software. Each version can have multiple releases. For example, for
   Python the version is something like 2.5 or 3.0, while the release is
   something like 2.5.1 or 3.0a1.  If you don't need this dual structure,
   just set both to the same value.
   Project version: 0.1
   Project release [0.1]: 0.1.1

   If the documents are to be written in a language other than English,
   you can select a language here by its language code. Sphinx will then
   translate text that it generates into that language.

   For a list of supported codes, see
   http://sphinx-doc.org/config.html#confval-language.
   Project language [en]: 

   The file name suffix for source files. Commonly, this is either ".txt"
   or ".rst".  Only files with this suffix are considered documents.
   Source file suffix [.rst]: 

   One document is special in that it is considered the top node of the
   "contents tree", that is, it is the root of the hierarchical structure
   of the documents. Normally, this is "index", but if your "index"
   document is a custom template, you can also set this to another filename.
   Name of your master document (without suffix) [index]: 

   Sphinx can also add configuration for epub output:
   Do you want to use the epub builder (y/n) [n]: 

   Please indicate if you want to use one of the following Sphinx extensions:
   autodoc: automatically insert docstrings from modules (y/n) [n]: y
   doctest: automatically test code snippets in doctest blocks (y/n) [n]: y
   intersphinx: link between Sphinx documentation of different projects (y/n) [n]: y
   todo: write "todo" entries that can be shown or hidden on build (y/n) [n]: y
   coverage: checks for documentation coverage (y/n) [n]: 
   pngmath: include math, rendered as PNG images (y/n) [n]: 
   mathjax: include math, rendered in the browser by MathJax (y/n) [n]: 
   ifconfig: conditional inclusion of content based on config values (y/n) [n]: 
   viewcode: include links to the source code of documented Python objects (y/n) [n]: 

   A Makefile and a Windows command file can be generated for you so that you
   only have to run e.g. `make html' instead of invoking sphinx-build
   directly.
   Create Makefile? (y/n) [y]: 
   Create Windows command file? (y/n) [y]: 

   Creating file .\source\conf.py.
   Creating file .\source\index.rst.
   Creating file .\Makefile.
   Creating file .\make.bat.

   Finished: An initial directory structure has been created.

   You should now populate your master file .\source\index.rst and create other documentation
   source files. Use the Makefile to build the docs, like so:
      make builder
   where "builder" is one of the supported builders, e.g. html, latex or linkcheck.

The Windows batch files we made will not be useful as we work on Linux. However, they are useful to look at to see how things work. They also can be used as a quick reminder of the commands to use.


Trying Out Your Hello World
==============================

* List the directors (ls command in Linux) and you see you now have a source and build directory.
* In a terminal run ``sphinx-build -b html source build``
* Change the build directory
* Double-click on index.html file and it will open in a browser. [#f1]_

.. image:: ../images/HelloWorld.png
          :alt: WARNING: HelloWorld.png missing

Sphinx works like a programming language that compiles code. When you change part of the programming code, you need to recompile the code to make a new executable code. We told sphinx-quickstart to use to folders - source and build. The source is where you put the source "code", that is the orginal files. Then when you do a ``sphinx-build -b html source build`` command the files in the source directory is processed by Sphinx and put into the build folder. 

* Either open the index.html in an editor [#f2]_ or choose to view the source code in your browser and you will see something like the following, though it may be color coded to help you read the code.

.. code::

   <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
     "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
   <html xmlns="http://www.w3.org/1999/xhtml">
     <head>
       <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
       <title>Welcome to Hello World’s documentation! &mdash; Hello World 0.1.1 documentation</title>
       <link rel="stylesheet" href="_static/alabaster.css" type="text/css" />
       <link rel="stylesheet" href="_static/pygments.css" type="text/css" />
       <script type="text/javascript">
         var DOCUMENTATION_OPTIONS = {
           URL_ROOT:    './',
           VERSION:     '0.1.1',
           COLLAPSE_INDEX: false,
           FILE_SUFFIX: '.html',
           HAS_SOURCE:  true
       </script>
       <script type="text/javascript" src="_static/jquery.js"></script>
       <script type="text/javascript" src="_static/underscore.js"></script>
       <script type="text/javascript" src="_static/doctools.js"></script>
       <link rel="top" title="Hello World 0.1.1 documentation" href="#" />
     <meta name="viewport" content="width=device-width, initial-scale=0.9, maximum-scale=0.9">
     </head>
     <body role="document">  
       <div class="document">
         <div class="documentwrapper">
           <div class="bodywrapper">
             <div class="body" role="main">
     <div class="section" id="welcome-to-hello-world-s-documentation">
   <h1>Welcome to Hello World&#8217;s documentation!<a class="headerlink" href="#welcome-to-hello-world-s-documentation" title="Permalink to this headline">¶</a></h1>
   <p>Contents:</p>
   <div class="toctree-wrapper compound">
   <ul class="simple">
   </ul>
   </div>
   </div>
   <div class="section" id="indices-and-tables">
   <h1>Indices and tables<a class="headerlink" href="#indices-and-tables" title="Permalink to this headline">¶</a></h1>
   <ul class="simple">
   <li><a class="reference internal" href="genindex.html"><span>Index</span></a></li>
   <li><a class="reference internal" href="py-modindex.html"><span>Module Index</span></a></li>
   <li><a class="reference internal" href="search.html"><span>Search Page</span></a></li>
   </ul>
   </div>
             </div>
           </div>
         </div>
         <div class="sphinxsidebar" role="navigation" aria-label="main navigation">
           <div class="sphinxsidebarwrapper">
     <h3><a href="#">Table Of Contents</a></h3>
     <ul>
   <li><a class="reference internal" href="#">Welcome to Hello World&#8217;s documentation!</a></li>
   <li><a class="reference internal" href="#indices-and-tables">Indices and tables</a></li>
   </ul>
   <div class="relations">
   <h3>Related Topics</h3>
   <ul>
     <li><a href="#">Documentation overview</a><ul>
     </ul></li>
   </ul>
   </div>
     <div role="note" aria-label="source link">
       <h3>This Page</h3>
       <ul class="this-page-menu">
         <li><a href="_sources/index.txt"
               rel="nofollow">Show Source</a></li>
       </ul>
      </div>
   <div id="searchbox" style="display: none" role="search">
     <h3>Quick search</h3>
       <form class="search" action="search.html" method="get">
         <input type="text" name="q" />
         <input type="submit" value="Go" />
         <input type="hidden" name="check_keywords" value="yes" />
         <input type="hidden" name="area" value="default" />
       </form>
       <p class="searchtip" style="font-size: 90%">
       Enter search terms or a module, class or function name.
       </p>
   </div>
   <script type="text/javascript">$('#searchbox').show(0);</script>
           </div>
         </div>
         <div class="clearer"></div>
       </div>
       <div class="footer">
         &copy;2015, Baba Computer.
         Powered by <a href="http://sphinx-doc.org/">Sphinx 1.3.3</a>
         &amp; <a href="https://github.com/bitprophet/alabaster">Alabaster 0.7.6</a>
      
         |
         <a href="_sources/index.txt"
             rel="nofollow">Page source</a>
       </div>
     </body>
   </html>

* Go the the source folder and open the index.rst file which will look like this:

.. code::

   .. Hello World documentation master file, created by
      sphinx-quickstart on Sat Dec 26 18:08:33 2015.
      You can adapt this file completely to your liking, but it should at least
      contain the root `toctree` directive.

   Welcome to Hello World's documentation!
   =======================================

   Contents:

   .. toctree::
      :maxdepth: 2

   Indices and tables
   ==================

   * :ref:`genindex`
   * :ref:`modindex`
   * :ref:`search`

index.rst is 21 lines long where as index.html is 114 lines. The rst file was used to develop the index.html file. Before we explore how it works, let's have a bit of success. Do the following:

* Change the world Hello to Hi on the line which as **Welcome to Hellow World's documentation!**
* In the terminal:
   * Make sure you are still in the Sphinx (or whatever you named yours) directory
   * run ``sphinx-build -b html source build``
* In your browser, refresh the index.html page (usually with F5) and you'll be able to see the change you made to the picture. 


Markup Language 
========================

Let's consider the index.rst that you changed.

Sphinx uses a markup language. You use markup languages all the time. Or at least you use the result of a markup language. One of the major formats for pages on the Internet is html which stands for Hypertext Markup Language which is what we saw with the index.html file. There are lots of markup languages. Another very popular one is XML which stands for Extensible Markup Language. XML essentially allows people to make their own markup language. The reason there are so many markup languages they each have different strengths. Sphinx took the powerful and seasoned reStructuredText markup language and added features that allow you to relate files and document code. 

In the index.rst example above has = under "Welcome to Hello World's documentation!" which makes it a title. A key point is that number of = has to be at least as long as the text for it to work.

|pencil| Read the :ref:`rst-primer` and find what the other header marks in addition to the = we have already seen. Place what you find in your document or spreadsheet where you are keeping the Sphinx terms of which you are keeping track. 

.. index::
   pair: toctree; directive

``.. toctree::`` is called a directive. This tells Sphinx to make a table of contents and the ``:maxdepth:`` is an option that says to have the table of contents to level two of the headers. 


We will be learning this markup as we go along. 

Now here is a cool thing. If you search this page you will find a link ``Show Source``. Clicking on that link will show you the Sphinx markup I used to build this page. This is a great way to learn Sphinx markup, by looking at pages you like.


Read the Manual 
==================

Read the First Steps with Sphinx of the Sphinx documentaiton. This will cover some of the things we have covered. It will also cover some other things. Again, do not try to understand it all now. Just keep track of terms like you did in the previous chapter. (Note: we did not put a directly link into our local copy of our Sphinx documentation because there is no local reference in the file. We did not edit the file because it is a copied from Sphinx so we are using it as is.)

.. rubric:: Footnotes

.. [#f1] If double-clicking doesn't open it, then open a browser and use File > Open to open the index.html file.

.. [#f2] You can use any simple text editor you are familar with or you can use LibreOffice or OpenOffice and save your work in text format. 

.. |pencil| image:: ../images/Pencil.png
          :align: middle
          :alt: Try It
          :width: 38 px
