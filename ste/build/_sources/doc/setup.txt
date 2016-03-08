
.. _setup:

*****************************
Setup
*****************************

Locate terminology.py
============================

/home/admin2/it@houghton.academy/syncPetrillo/Jobs/Courses/Sphinx/sge/sphinx-glossary-extension/sge/source


conf.py is /home/admin2/it@houghton.academy/syncPetrillo/Jobs/Courses/Sphinx/sge/sphinx-glossary-extension/SphinxCourse/source

termx.py is /home/admin2/it@houghton.academy/syncPetrillo/Jobs/Courses/Sphinx/sge/sphinx-glossary-extension/sge/

sys.path.insert(0,os.path.abspath('../../sge'))

inserts the absolute path of termx.py into the system path relative to the conf.py we are running


sys.path.insert(0,"/home/admin2/it@houghton.academy/syncPetrillo/Jobs/Courses/Sphinx/sge/sphinx-glossary-extension/sge/")


Edit conf.py
=======================


.. _moreWords:

Changing number of words in the "term"
===========================================

The extension ships with the number of words in the term being a maximum of 15. You can change this by editing the extension, file terminology.py. Find this line::

   optional_arguments = 14

Then change the 14 to the number you desire. Remember, the count starts at 0, hence setting to 14 gives you up to 15 words in the term.



