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


/*

Add Equipment
^^^^^^^^^^^^^

Notice we didn't put blank lines so the commands are written as paragraphs which are harder to read. 

\*/


INSERT INTO tblEquipment (id,name,locationId) VALUES (1,'Desktop01',1);
INSERT INTO tblEquipment (id,name,locationId) VALUES (2,'Desktop02',1);
INSERT INTO tblEquipment (id,name,locationId) VALUES (3,'Desktop03',1);


INSERT INTO tblEquipment (id,name,locationId) VALUES (11,'Desktop11',2);
INSERT INTO tblEquipment (id,name,locationId) VALUES (21,'Desktop21',3);
INSERT INTO tblEquipment (id,name,locationId) VALUES (22,'Desktop22',3);



