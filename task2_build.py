import pymongo
import time
from pymongo import MongoClient
from pymongo import TEXT
import json
def task2_build(): 
    # Ask for input
    port = int(input("Enter port number: "))
    client = MongoClient("mongodb://localhost:"+str(port))
    client = MongoClient("localhost", port)

    start = time.time()  
    db = client["MP2Embd"]  # create db 
    
    # Drop messages if exists 
    if 'messages' in db.list_collection_names():
        db.drop_collection('messages')

    messages_collection = db.messages

    # Getting the data: sender.json
    with open('senders.json', 'r') as senders_file:
        senders_data = json.load(senders_file)

    #creating a dictionary with key as the sender_id and sender_info as the value so that it is easier to search when creating the embed messages
    senders_dict ={}
    for sender in senders_data:
        sender_id = sender['sender_id']
        senders_dict[sender_id]=sender
    file_data = [] 

    with open('messages.json', 'r', encoding ='utf-8') as file2:
        for line in file2: 
            if '[' in line or ']' in line:
                pass # do nothing
            else: 
                line = line.rstrip(',\n')
                line = json.loads(line)
                # embedding the sender information to a new field: 'sender_info'
                sender_id = line.get("sender")
                line['sender_info']= senders_dict[sender_id]
                file_data.append(line)

    # Create collection messages
    # Define batch size
    batch_size = 5000

    # Insert data in batches
    for i in range(0, len(file_data), batch_size):
        batch = file_data[i:i+batch_size]
        db.messages.insert_many(batch)
    end = time.time()
    print("Time required to do the embed message: ",(end-start)*1000)
    return db

