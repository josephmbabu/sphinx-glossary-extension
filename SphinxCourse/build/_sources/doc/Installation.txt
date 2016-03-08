.. _Installation:

**************************
Installation
**************************

JOSEPH IS HERE!


We will begin the Sphinx installation in this chapter. But as we experiment with Sphinx we may find that we've missed some pieces and will need to add them as we go.

.. Glossary:: Term
   Here is my definition.
   I think i'll try multiple lines.

.. Note::
   Teacher, please show the student where the Sphinx folder is that contains the course and the documentation. Then guide them to the build/intro.html file. We could put a link to the intro.html file but at this point we want to get the students comfortable navigating the directory/folder structure because they will be doing that quite a bit. 

|pencil| Open the Sphinx documentation at the intro.html. Read this page and do the following:

* While you read, make a list of terms that are important to using Sphinx. If you know what the term means, make a brief note about it. The idea is not how much you know, but to see the terms you do know or don't know and how Sphinx applies them. You should make an electronic list, such as in a spreadsheet or document. Or, you could make a list that the class can build and improve as you go along. This class list could be on a board in the classroom, or if you have a cloud, it can be a shared document/spreadsheet. 
* Make three lists labeled "Need Now", "Probably Will Need Later", "Do Not Know" and put the topics on the Introduction page under the list you think it fits.

The thing we need now is to be sure we have the prerequisites. If the system you are using is set up by TEN3, you'll have the prerequisites. If it is your own system, you'll need to find out if you have Python and the supporting libraries. 

We use Python 3 for our courses, but Sphinx will work with Python 2 or Python 3. 

Linux
=============

If you are setting up your own system. Here are the commands you will need. Again, if you are using a TEN3 system that has been setup for this course, then you do not need to do the following. 

From the Terminal: [#f1]_

* sudo apt-get install python3
* sudo apt-get install sqlite3
* sudo apt-get install idle3
* sudo apt-get install python-pip 
* sudo apt-get install python3-docutils
* sudo apt-get install python3-jinja2
* sudo apt-get install python3-pygments
* sudo pip install Sphinx

.. glossary:: ABC123
   The ABC123 should be in index



.. termx:: Title

   go back to other document and see if I need to load pip on this newer python or test it. 

Or you can use the Synaptic Package Manager or the software loading method used by the Linux distro you are using, such as the Ubuntu Software Center. 

.. index::
   pair: ABC456; pig

.. termx:: Lion
   
   My system seems to be using Python 2. I'm not sure how to clean that up before we build a linux iso for the course? ajp

.. termx:: Term1
   
   Example term for todox.

.. termxlist::

.. index::
   pair: ABC456; pig


Windows
==========

* Install Python. If it is 3.4 or beyond, it already has pip on it. If not, then install pip. 

   * Python has a very useful pip command which can download and install 3rd-party libraries with a single command. This is provided by the Python Packaging Authority(PyPA). 
   * To install pip go to http://sphinx-doc.org/latest/install.html and search for https://bootstrap.pypa.io/get-pip.py then download it somewhere. After download, invoke the command prompt, go to the directory with get-pip.py and run this command:
   * C:\> python get-pip.py
* the docutils, Jinja2, Pygments libraries. 

* C:\> pip install sphinx. You may have to find the pip.exe. I found it under Python33\Scripts. Change to that directory and run the command there to test it. Then decide where you want to put the program and other folders. You may not decide this until you've done some testing in the tutorial. Then you may want to add the sphinx to your path if you are using Windows.


.. rubric:: Footnotes

.. [#f1] A terminal is also known as a console or the command line. 



.. |pencil| image:: ../images/Pencil.png
          :align: middle
          :alt: Try It
          :width: 38 px

.. glossary:: ABC123
   The ABC123 should be in index
