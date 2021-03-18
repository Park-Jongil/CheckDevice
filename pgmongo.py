import pymongo
from pymongo import MongoClient
from datetime import datetime
import psycopg2
import sys

def create_postgres_connection(host_product,dbname,user,password,port):
    try:
        product_connection_string = "dbname={dbname} user={user} host={host} password={password} port={port}"\
                                .format(dbname=dbname,
                                        user=user,
                                        host=host_product,
                                        password=password,
                                        port=port)    
        product = psycopg2.connect(product_connection_string)
        return product
    except:
        print("Postgres DB Connection Error")
        return None

def main():
    Test_DB = create_postgres_connection("127.0.0.1","StreamDB","postgres","1331","5432")
    MongoDB = MongoClient("mongodb://127.0.0.1:27017")
    if (Test_DB != None and MongoDB != None) :
        print("PostgresSQL Connection Success")
        MonDB = MongoDB['Gasi']
        collection = MonDB['MoveTable']
        cur = Test_DB.cursor()
        cur.execute('SELECT name, age, secret, power1, power2, power3 FROM "TestDB"')
        rows = cur.fetchall()
        if (rows != None and len(rows) > 0) :
            for row in rows :
                collection.insert_one( {"name":str(row[0]),"age":str(row[1]) } )
                print("  name = " + str(row[0]) + " : " + str(row[1]) )  
    else :
        print("PostgresSQL Connection Failure")
    
    Test_DB.close()

if __name__ == '__main__':
    main()
