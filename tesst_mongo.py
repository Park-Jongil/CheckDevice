import pymongo
from pymongo import MongoClient

#몽고DB연동
def main():
    try :
        client = MongoClient("mongodb://127.0.0.1:27017")
        #디비 연결
        db = client['Gasi']
        collection = db['DeviceInfo']
        doc = collection.find()
        for i in doc:
            print(i)
        print("Mongo DB 접속성공 및 종료")

    except: 
        print("Mongo DB 접속실패")
        return None
#        traceback.print_exc() 


if __name__ == '__main__':
    main()
