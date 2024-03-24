from bson.objectid import ObjectId
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://artnatalia17:123MD@cluster0.dffiwwa.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

db = client.book


def read_all_records():
    """
    Function to read all records from the collection.
    """
    records = db.cats.find()
    for record in records:
        print(record)


def find_cat_by_name(name):
    """
    Function to find a cat by its name.
    """
    cat = db.cats.find_one({"name": name})
    if cat:
        print(cat)
    else:
        print("Cat not found.")


def update_cat_age(name, new_age):
    """
    Function to update the age of a cat by its name.
    """
    db.cats.update_one({"name": name}, {"$set": {"age": new_age}})
    print(f"The age of {name} has been updated to {new_age}.")


def add_feature_to_cat(name, new_feature):
    """
    Function to add a new feature to the list of features of a cat by its name.
    """
    db.cats.update_one({"name": name}, {"$push": {"features": new_feature}})
    print(f"A new feature '{new_feature}' has been added to {name}.")


def delete_cat_by_name(name):
    """
    Function to delete a cat record from the collection by its name.
    """
    db.cats.delete_one({"name": name})
    print(f"{name}'s record has been deleted from the collection.")


def delete_all_records():
    """
    Function to delete all records from the collection.
    """
    db.cats.delete_many({})
    print("All records have been deleted from the collection.")


# Test the functions
read_all_records()
find_cat_by_name("Liza")
update_cat_age("Liza", 5)
add_feature_to_cat("Liza", "green eyes")
delete_cat_by_name("Lama")
delete_all_records()
