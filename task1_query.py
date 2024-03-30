import pymongo
import time
from pymongo import MongoClient
import json


def task1_query(db):

    messages = db['messages']
    senders = db['senders']
    # Step 3: Display the requested information
    print("\nQ1: Return the number of messages that have 'ant' in their text.")

    # ---------- Query 1, no indexing
    try:
        start_time = time.time()
        count = messages.count_documents({"text": {"$regex": "ant"}}, maxTimeMS=120000) # accounting for maxTime
        end_time = time.time()
        print(f"Number of messages with 'ant' in text: {count}")
        print(f"Time taken before indexing: {(end_time - start_time) * 1000} ms")

    except pymongo.errors.ExecutionTimeout as e: # Catch max time error
        print("Query 1 takes more than two minutes.")
    

    # ---------- Query 2, no indexing
    print("\nQ2: Find the nick name/phone number of the sender who has sent the greatest number of messages.")

    start_time = time.time()
    pipeline = [
        {"$group": {"_id": "$sender", "count": {"$sum": 1}}},
        {"$sort": {"count": -1}},
        {"$limit": 1},
        {"$project": {"sender": "$_id", "count": 1, "_id": 0}}
    ]
    try:
        start_time = time.time()
        result = list(messages.aggregate(pipeline, maxTimeMS=120000))
        end_time = time.time()
        print(f"Sender with the most messages: {result[0]['sender']} ({result[0]['count']} messages)")
        print(f"Time taken before indexing: {(end_time - start_time) * 1000} ms")
    except pymongo.errors.ExecutionTimeout:
        print("Query 2 takes more than two minutes.")



    # ---------- Query 3, no indexing
    print("\nQ3: Return the number of messages where the sender's credit is 0.")

    start_time = time.time()
    pipeline3 = [
        {"$lookup": {"from": "senders", "localField": "sender", "foreignField": "sender_id", "as": "sender_details"}},
        {"$match": {"sender_details.credit": 0}},
        {"$count": "count"}
    ]
    try:
        result = list(messages.aggregate(pipeline3, maxTimeMS=120000))
        end_time = time.time()
        print(f"Number of messages where sender's credit is 0: {result[0]['count']}")
        print(f"Time taken before indexing: {(end_time - start_time) * 1000} ms")
    except pymongo.errors.ExecutionTimeout:
        print("Query 3 takes more than two minutes.")

    # ---------- Query 4, no indexing    
    try: 
        print("\nQ4: Double the credit of all senders whose credit is less than 100.")
        start_time = time.time()
        senders.update_many({"credit": {"$lt": 100}}, {"$mul": {"credit": 2}})
        end_time = time.time()
        print("Credits doubled for senders with credit less than 100.")
        print(f"Time taken: {(end_time - start_time) * 1000} ms")
    except pymongo.errors.ExecutionTimeout:
        print("Query 4 takes more than two minutes.")

    #---------- REPEAT QUERIES 1 TO 3 WITH INDEXING
        

    # Create the indexes
        
    # Create text index for "text" field in messages collection
    messages.create_index([("text", "text")])

    # Create index for "sender" field in messages collection
    messages.create_index("sender")

    # Create index for "sender_id" field in senders collection
    senders.create_index("sender_id")
    
    #----------QUERY 1 After indexing
    
    print("\nQ1: Return the number of messages that have 'ant' in their text.")

    try:
        start_time = time.time()
        count = messages.count_documents({"text": {"$regex": "ant"}}, maxTimeMS=120000) # accounting for maxTime
        end_time = time.time()
        print(f"Number of messages with 'ant' in text: {count}")
        print(f"Time taken after indexing: {(end_time - start_time) * 1000} ms")

    except pymongo.errors.ExecutionTimeout as e: # Catch max time error
        print("Query 1 (after indexing) takes more than two minutes.")

    #----------QUERY 2 After indexing
    
    print("\nQ2: Find the nick name/phone number of the sender who has sent the greatest number of messages.")

    # Create index for "sender" field in messages collection
    messages.create_index("sender")

    # After indexing
    try: 
        start_time = time.time()
        result = list(messages.aggregate(pipeline, maxTimeMS=120000))
        end_time = time.time()
        print(f"Sender with the most messages: {result[0]['sender']} ({result[0]['count']} messages)")
        print(f"Time taken after indexing: {(end_time - start_time) * 1000} ms")
    except pymongo.errors.ExecutionTimeout:
        print("Query 2 (after indexing) takes more than two minutes.")

    #----------QUERY 3 After indexing
    
    print("\nQ3: Return the number of messages where the sender's credit is 0.")

    try:


        start_time = time.time()
        result = list(messages.aggregate(pipeline3, maxTimeMS=120000))
        end_time = time.time()
        print(f"Number of messages where sender's credit is 0: {result[0]['count']}")
        print(f"Time taken after indexing: {(end_time - start_time) * 1000} ms")

    except pymongo.errors.ExecutionTimeout:
        print("Query 3 (after indexing) takes more than two minutes.")