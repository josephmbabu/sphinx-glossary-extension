
.. _setup:

*****************************
Setup
*****************************

To use this extension, you need to:

* place the terminology.py script somewhere
* edit the conf.py 

Place terminology.py
============================

If you downloaded :download:`sve.zip <../zipped/ste.zip>`, you can unzip it and read this documentation on your system. You will find the terminlogy.py in /build/downloads/ folder. 

Otherwise you saved terminology.py using the method under :ref:`download`. 

You now need to decide where you want to place the terminology.py script on your system so that it is found you do a build. For example:

* in the same directory as the conf.py
* in a directory that you want to reference for multiple Sphinx projects
* with the Sphinx software or another location you know is already in system path

For this Sphinx site, we have placed terminology in our code and have included it in the site so you can look at the code and comments. This is shown in our conf.py. 



Edit conf.py
=======================

If you downloaded our

You need to make three changes to conf.py:

* set the path to terminology.py
* 








/home/admin2/it@houghton.academy/syncPetrillo/Jobs/Courses/Sphinx/sge/sphinx-glossary-extension/sge/source


conf.py is /home/admin2/it@houghton.academy/syncPetrillo/Jobs/Courses/Sphinx/sge/sphinx-glossary-extension/SphinxCourse/source

termx.py is /home/admin2/it@houghton.academy/syncPetrillo/Jobs/Courses/Sphinx/sge/sphinx-glossary-extension/sge/

sys.path.insert(0,os.path.abspath('../../sge'))

inserts the absolute path of termx.py into the system path relative to the conf.py we are running


sys.path.insert(0,"/home/admin2/it@houghton.academy/syncPetrillo/Jobs/Courses/Sphinx/sge/sphinx-glossary-extension/sge/")


**********************
Optional changes
**********************

Terminology list hyperlink
======================================

You can change the appearance of the hyperlink at ... ~~~


.. _moreWords:

Changing number of words in the "term"
===========================================

The extension ships with the number of words in the term being a maximum of 15. You can change this by editing the extension, file terminology.py. Find this line::

   optional_arguments = 14

Then change the 14 to the number you desire. Remember, the count starts at 0, hence setting to 14 gives you up to 15 words in the term.



.. _moreWords:

Changing number of words in the "term"
===========================================

The extension ships with the number of words in the term being a maximum of 15. You can change this by editing the extension, file terminology.py. Find this line::

   optional_arguments = 14

Then change the 14 to the number you desire. Remember, the count starts at 0, hence setting to 14 gives you up to 15 words in the term.



