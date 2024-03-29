
from pymongo import MongoClient
import json 
import time 


def task1_build(): 

    # -------- Step 1 start -------- 

    # Ask port input
    port = int(input("Enter port number: "))
    client = MongoClient("mongodb://localhost:"+str(port))
    client = MongoClient("localhost", port)

    # Create a database MP2Norm (will account for if it exists/not)
    db = client["MP2Norm"] 

    start_time = time.time() # Start the clock for reading the data for step 1

    # Create collection messages, drop if exists 

    collist = db.list_collection_names() # Get the list of collections 
    if "messages" in collist: 
        msg = db["messages"]
        msg.drop() # drop messages if it exists 

    messages = db["messages"] # create the collection

    # Open messages.json and store its data, read line by line to account for memory
    msg_data = [] 
    with open('messages.json', 'r') as file:
        for line in file: 
            if '[' in line or ']' in line:
                pass # do nothing
            else: 
                line = line.rstrip(',\n')
                msg_data.append(json.loads(line.strip())) # Adding the data in 

    # Define batch size
    batch_size = 5000

    # Insert data in batches to the database (5k/batch)
    for i in range(0, len(msg_data), batch_size):
        batch = msg_data[i:i+batch_size] # Double Check: Python accounts for out of bounds and stops automatically.
        messages.insert_many(batch) # pushing to db

    end_time=time.time() # done for step 1 

    print(f"Time taken for step 1 : {(end_time - start_time) * 1000} ms")
    # -------- Step 2 start -------- 

    start_time2 = time.time() # start timer for senders

    # Create new collection: senders, drop if exists 
    if "senders" in collist: 
        senders = db["senders"]
        senders.drop() # drop senders if exists

    senders = db["senders"] # creating the collection 

    # Please account for memory handling here 
    with open('senders.json', 'r') as file: 
        sender_data = json.load(file)


    senders.insert_many(sender_data) # Can insert into db in one batch

    end_time2 = time.time() # end timer for senders

    print(f"\nTime taken for step 2 : {(end_time2 - start_time2) * 1000} ms")

    return db


      