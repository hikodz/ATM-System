
# library i need import
import firebase_admin
from firebase_admin import credentials,firestore
from google.cloud.firestore_v1.base_query import FieldFilter



cred = credentials.Certificate("/Users/HikoDz/Desktop/ATM-System/backend/firebase_config.json")
firebase_admin.initialize_app(cred,{'databaseURL':'https://atm-system-6ae9e-default-rtdb.firebaseio.com/'})
db = firestore.client()


class DataBaseUsage:
    def UploadData(self,document:str, data:dict, collection:str="Customer")-> bool:
        try:
            db.collection(collection).document(document).set(data)
            return True
        except:
            return False


    def SearchData(self,id:str, password:str="", collection:str="Customer",atm=False):
        try:
            collection = db.collection(collection)
            status = collection.where(filter=FieldFilter("ID", "==", id)).get()
            convert_data = [data.to_dict()  for data in status ]
            if (convert_data and password == convert_data[0]["Password"] and password) or (atm and convert_data):
                return convert_data[0]
            return []
        except:
            return False

    def UpdataData(self,id:str,data= {}, collection:str="Customer")-> bool:
        try:
            db.collection(collection).document(id).update(data)
            return True
        except:
            return False
            # print(chalk.red("There is no connection to the server"))
    def SearchCard(self,card:str,cvv:str):
        try:
            collection = db.collection("Customer")
            docs = collection.stream()
            for doc in docs:
                cards = doc.to_dict().get("Cart")
                for _, info in cards.items():
                    if info["card"] == card and info["cvv"] == cvv :
                        return doc.to_dict()
            return False
        except:
            return False


    def RomoveData(self,id:str, collection:str="Customer")-> bool:
        try:
            db.collection(collection).document(id).delete()
            return True
        except:
            return False
