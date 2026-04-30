# Assessment Task 1 - 9CT-Task-1
Does going to a co-ed highschool affect grades?

**Hypothesis:** Only Boys and Girls highschools get higher grades
## Identifying and Defining

### Functional Requirements 

Data Loading: Consider aspects such as ability to load certain file types and handling errors in file loading (e.g. incorrect format, missing files).

Data Cleaning: Does the system need to handle missing values or allow for filtering, sorting and grouping of data?

Data Analysis: What kind of statistical analysis does the system need to allow for (e.g. mean, median, mode)?

Data Visualisation: How will the data need to be visualised (e.g. Pandas dataframes / Matplotlib chart types)?

Data Reporting: What output should the system include, and do we need to store the final dataset somewhere (e.g. .csv or .txt file)?


### Non-Functional Requirements
#### Usability
What is required from the User Interface and a 'README' document?

Requirements from the User Interface is to be able to do a variety of functions such as showing the marks/grades of different years, showing graphs and charts that compare co-ed schools to all boys and/or all girl schools. The README document needs to be able to inform the User how to operate the Interface.
#### Reliability
What is required from the system when providing information to the user on errors and ensuring data integrity?

#### Use Case
Actor: User

Goal: To access and interact with existing data through the program’s user interface.

Preconditions:

The dataset has already been preloaded into the system by an administrator / programmer.

The user has access to the system interface.

The user knows how to operate and use the interface due to the README document

Main Flow:

User opens the program and is presented with a text-based menu.

User selects one of the following options:
a. View visualisation (e.g., chart or graph of selected data)
b. Search or filter data based on specific criteria
c. Update a data entry (e.g., change a value or correct an error)

System performs the requested action and outputs to user.

Postconditions:

User has viewed and/or interacted with the data.

Any valid updates are saved by the system.

Data remains available for further queries or analysis.