

<!-- PROJECT LOGO -->
<br />
<div align="center" fontsize>

  <h3 align="center" size="" >DNA Phase Project 4</h3>

  <p align="center" >
    By team 37 
    <br />
    Sai Satvik , Rushil kaul , Sreenivas B Papireddy
    <br />
    <br />
  </p>
</div>



<!-- ABOUT THE PROJECT -->

### How to Run

This file contains a felicity.sql file which be used to create the databases with some (contains data) and the other file felicity.py which is the driver code. The python code connects with sql through socket using username and password. 

Open project directory in terminal and write this command 
```sh
  python3 felicity.py
  ```

------------



# First Menu

These are the menu options you will recieve first all the options.
  ```sh
    Connected to Felicity dbms
    1. Retrieval
    2. Analysis
    3. Modify
    Enter choice> 

  ```

## 1. Retrieval
These are the menu options you will recieve after selecting this option.
```bash
    1. Selection of Data
	2. Projection
	3. Search student (with name/roll number)
	4. Auto Scheduler
	5. Auto Scheduler for individual events
	6. Net revenue(include Aggregation)
	Enter choice> 

  ```
### 1. Selection of Data

>Will give more options on which table you want to view with some additional data than those stored in sql.

### 2. Projection

>Query on tables with conditions.

### 3. Search student (with name/roll number)

>Can search for student dbms with just name or rollnumber  .

### 4. Auto Scheduler

>Erases and create a new scheduler table which is a timetable of all the events that have been approved.

### 5. Auto Scheduler for individual events

>Add a event to the schudler which is not already present in the scheduler allocats only if ther are free slots available.

### 5. Net revenue(include Aggregation)

>Prints total profit or loss in conducting the Fest.


----------------------
<br></br>
## 2. Analysis
These are the menu options you will recieve after selecting this option.
```bash
    1. Net revenue
	2. Expenditure by each club on events
	Enter choice> 

	Enter choice> 

  ```
### 1. Net revenue

>Prints total profit or loss in conducting the Fest.

### 2. Expenditure by each club on events

>Prints the expenses by each club during the fest.



----------------------
<br></br>
## 3. Modify
These are the menu options you will recieve after selecting this option.
```bash
    1. Insert Data
	2. Updation
	3. Delete Data
	Enter choice> 

  ```
### 1.Insert Data

>Will give more options on which table you want to insert data into .

### 2. Updation

>Will give more options on which table you want to update data into .

### 3. Delete Data

>Will give more options to delete values in certain tables .


