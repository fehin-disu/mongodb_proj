from task2_build import task2_build
from task2_query import task2_query
import json 
import time 
def main(): 
    print("Task 2")
    dbEmb = task2_build()
    task2_query(dbEmb)
    print("-----------------Task2 done----------")
main()