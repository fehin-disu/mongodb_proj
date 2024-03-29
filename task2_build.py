import pymongo
import time
from pymongo import MongoClient
from pymongo import TEXT
import json
def task2(): 
    # INPUT FOR PORT, i want this to be executed later since it may be overwhelming

    # port = int(input("Enter port number: "))
    # client = MongoClient("mongodb://localhost:"+str(port))
    # client = MongoClient("localhost", port)

    # TEMP Create the client
    port = int(input("Enter port number: "))
    client = MongoClient("mongodb://localhost:"+str(port))
    client = MongoClient("localhost", port)

    start = time.time() 
    db = client["MP2Embd"] 
    if 'messages' in db.list_collection_names():
        db.drop_collection('messages')
        print("inside_drop")  #Delete this
    messages_collection = db.messages
    #getting the data sender.json
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
                # do nothing?
                pass
            else: 
                line = line.rstrip(',\n')
                line = json.loads(line)
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
task2()