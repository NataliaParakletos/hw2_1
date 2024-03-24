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

result_one = db.cats.insert_one(
    {
        "name": "barsik",
        "age": 3,
        "features": ["ходить в капці", "дає себе гладити", "рудий"],
    }
)

print(result_one.inserted_id)

result_many = db.cats.insert_many(
    [
        {
            "name": "Lama",
            "age": 2,
            "features": ["ходить в лоток", "не дає себе гладити", "сірий"],
        },
        {
            "name": "Liza",
            "age": 4,
            "features": ["ходить в лоток", "дає себе гладити", "білий"],
        },
                {
            "name": "Bobik",
            "age": 3,
            "features": ["ходить в лоток", "дає себе гладити", "чорний"],
        },
                {
            "name": "Sharik",
            "age": 7,
            "features": ["ходить в лоток", "не дає себе гладити", "біло-рудий"],
        },
    ]
)
print(result_many.inserted_ids)