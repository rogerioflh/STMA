# Sports Team Management App

## Implementation of system requested in software project discipline

**Student** : Marta Mirely Nascimento dos Santos

**Teacher** : Baldoíno Fonseca

**How to run the project** : 

* Clone the repository using: 

 `git clone -project address`

 * Access the project folder:

 `cd project`

 * Run the file main.py:

 `python main.py`

**Required resources** : Any version from Python 3 onwards

**Implemeted features:**

* Register sports team profile: Create a profile with the team information that will be managed through the application;

This feature allows teams to register in the application to start managing their sectors; We have the **team class**  with the following attributes: name, CNPJ, contact, address and person in charge. In addition to the register methods, for teams that are not yet registered in the application, they can change information in their own profile or simply consult information.

* Equipment Inventory Management: Tracking and managing sports equipment;

In this functionality we will use the **inventory class**, where we will have the attributes object type, sector, responsible team, registration date, date of last use; In addition to the methods register new object, check availability and request object;

* Training Schedule Management: Organizing and managing training sessions;

In this functionality we will have the **training class**, with the attributes type, date, time, duration, location, professional, status; In addition to the methods: schedule and mark as completed

* Match Scheduling: Organizing and scheduling matches or tournaments;

In this functionality we will have the **competition class**, which will represent commitments in tournaments or matches, having the attributes type, location, date, time and opponent; In addition to the methods, schedule commitment and check status.


