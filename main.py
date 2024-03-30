from pymongo import MongoClient
from task1_build import task1_build
from task1_query import task1_query
from task2_build import task2_build
from task2_query import task2_query
import json 
import time 
def main(): 
    print("Task 1")
    db = task1_build()
    task1_query(db)
    print("Task 2")
    dbEmb = task2_build()
    task2_query(dbEmb)
main()