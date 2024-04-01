[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/Fozs_Okj)
# CMPUT 291 Mini Project 2 - Winter 2024  
Group member names and ccids (3-4 members)  
  elykah, Elykah Tejol  
  adhikar2, Sandhya Adhikari  
  fehintol, Fehintola Disu  

# Group work break-down strategy
Note: We worked on the tasks through Discord/in-person together. 

- Elykah worked on Task 1, step 1 (2 hours) 
- Sandhya worked on Task 1, step 2 (2 hours) 
- Fehintola worked on Task 1, step 3 (2 hours)
- Sandhya, Elykah, and Fehintola worked on Task 1, step 4 (3 hours)
- Elykah worked on error handling for step 4 (1 1/2 hour)
- Sandhya worked on Task 2, step 1 (2 hours)
- Sandhya worked on Task 2, step 2 (2 hours)
- Elykah worked on main.py and reviewed the files (2 hours)
- Elykah worked on starting report.pdf (1/2 hour)
- Sandhya worked on making two different main functions for task1 and task 2 and updating the report for that part(1 1/2 hour)
  
# Code execution guide
Prerequisites before running the code: MongoDB server must be running and you know the port number
For task1:
  Run the python file named task1.py
  It will ask for the post number, please provide your MongoDB server’s port number
  Task 1 is now running
For task1:
  Run the python file named task2.py
  It will ask for the post number, please provide your MongoDB server’s port number
  Task 2 is now running


# AI Agents
Sandhya did not use AI for this assignment.
Fehintola used Claude.ai to aid in understanding how indices work in MongoDB
Prompt Question: how do i create indices for fields "sender" and "text" in messages collection. 
Output:
To create indices for the fields "sender" and "text" in the messages collection, you can use the following code:
```python
# Create index for "sender" field in messages collection
messages.create_index("sender")

# Create text index for "text" field in messages collection
messages.create_index([("text", "text")])

```
# Collaborations
Names of anyone you have collaborated with (as much as it is allowed within the course policy) or a line saying that you did not collaborate with anyone else.  
We did not collaborate with anyone else. 
