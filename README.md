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
- Fehintola and Elykah reviewed the requirements as well as worked on the report.pdf (2 hours)
  
  
# Code execution guide
Prerequisites before running the code: MongoDB server must be running and you know the port number

For task1:
- Run the python file named task1.py
- It will ask for the post number, please provide your MongoDB server’s port number
- Task 1 is now running
  
For task1:
- Run the python file named task2.py
- It will ask for the post number, please provide your MongoDB server’s port number
- Task 2 is now running


# AI Agents
- Sandhya did not use AI for this assignment.
  
- Fehintola used Claude.ai to aid in understanding how indices work in MongoDB
Prompt Question: how do i create indices for fields "sender" and "text" in messages collection. 

Output:
To create indices for the fields "sender" and "text" in the messages collection, you can use the following code:
```python
# Create index for "sender" field in messages collection
messages.create_index("sender")

# Create text index for "text" field in messages collection
messages.create_index([("text", "text")])

```

- Elykah used ChatGPT to ask about json loading & insertMany
  
Prompt Question: Data should be inserted in small batches (say 5k-10k messages per batch) using insertMany command in MongoDB. 

What does this mean? I thought insertMany just inserted all here

Here's my code

    # -- Insert data from "messages,.json" to messages collection 
    with open('messages.json') as file:
        file_data = json.load(file)

    msg_col = db["messages"] # Create collection messages
    msg_col.insert_many(file_data) # add the values in 
      
but file_data contains ALL the data from json right? but we are just slowly inserting it to the database

Output: Yes, you are correct. In your current implementation, insert_many() inserts all the data from the JSON file into the MongoDB collection at once. However, the statement you mentioned about inserting data in small batches using insert_many refers to breaking up the data into smaller subsets and inserting them sequentially.

Here's how you can modify your code to insert data in batches:
```
import json

# Define the batch size
batch_size = 5000

# Open the JSON file
with open('messages.json') as file:
    file_data = json.load(file)

# Create collection messages
msg_col = db["messages"]

# Split the data into batches
for i in range(0, len(file_data), batch_size):
    batch = file_data[i:i+batch_size]
    msg_col.insert_many(batch)
```

# Collaborations
Names of anyone you have collaborated with (as much as it is allowed within the course policy) or a line saying that you did not collaborate with anyone else.  
We did not collaborate with anyone else. 
