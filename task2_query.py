import pymongo
import time
from pymongo import MongoClient
from pymongo import TEXT
import json
def task2_query(db): 
    
    # -----------Query 1----------- # 
    messages = db["messages"]
    print("\nQ1: Return the number of messages that have 'ant' in their text.")
    try:
        start_time = time.time()
        count = messages.count_documents({"text": {"$regex": "ant"}}, maxTimeMS=120000) # accounting for maxTime
        end_time = time.time()
        print(f"Number of messages with 'ant' in text: {count}")
        print(f"Time taken for query 1 after embed: {(end_time - start_time) * 1000} ms")

    except pymongo.errors.ExecutionTimeout as e: # Catch max time error
        print("Query 1 takes more than two minutes.")

    # -----------Query 2----------- # 
    print("\nQ2: Find the nick name/phone number of the sender who has sent the greatest number of messages.")

    start_time = time.time()
    pipeline = [
        {"$group": {"_id": "$sender", "count": {"$sum": 1}}},
        {"$sort": {"count": -1}},
        {"$limit": 1},
        
    ]
    try:
        start_time = time.time()
        result = list(messages.aggregate(pipeline, maxTimeMS=120000))
        end_time = time.time()
        for sender in result:
            print(f"The sender with the most messages is {sender['_id']} with {sender['count']} messages.")
        print(f"Time taken for query 2 after embed: {(end_time - start_time) * 1000} ms")
    except pymongo.errors.ExecutionTimeout:
        print("Query 2 takes more than two minutes.")

    # -----------Query 3----------- # 
    pipeline3 = [
    {'$match': {'sender_info.credit': 0}},  # Match messages where sender's credit is 0
    {'$count': 'num_messages' } # Count the number of matched messages
    ]
    
    print("\nQ3: Return the number of messages where the sender's credit is 0.")
    try:
        start_time = time.time()
        result = list(messages.aggregate(pipeline3, maxTimeMS=120000))
        end_time = time.time()
        for r in result:
            print(f"The number of messages where the sender's credit is 0: {r['num_messages']}")
        print(f"Time taken after embed for query 3: {(end_time - start_time) * 1000} ms")
    except pymongo.errors.ExecutionTimeout:
        print("Query 2 takes more than two minutes.")


    # -----------Query 4----------- # 
    try: 
        print("\nQ4: Double the credit of all senders whose credit is less than 100.")
        start_time = time.time()
        messages.update_many({'sender_info.credit': {'$lt': 100}},{'$mul': {'sender_info.credit': 2}})
        end_time = time.time()
        print("Credits doubled for senders with credit less than 100.")
        print(f"Time taken for query 4 with embed: {(end_time - start_time) * 1000} ms")
    except pymongo.errors.ExecutionTimeout:
        print("Query 4 takes more than two minutes.")
