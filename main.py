from pymongo import MongoClient
from task1_build import task1_build
from task1_query import task1_query
import json 
import time 
def main(): 
    db = task1_build()
    task1_query(db)

main()