import os
import pymongo

#grab hidden environment variables, but only if we have a file called env.py that exists in our root directory
if os.path.exists("env.py"):
    import env


#to make code cleaner, set three constants, python constants are written in capital letters
#MONGO_URI = environment variable created in env.py
#DATABASE = "Name of Database"
#COLLECTION = "celebrities"

MONGO_URI = os.environ.get("MONGO_URI")
DATABASE = "myFirstDB" 
COLLECTION = "celebrities"

#connecting the database:
def mongo_connect(url):
    try:
        conn = pymongo.MongoClient(url)
        print("Mongo is connected")
        return conn

    except pymongo.errors.ConnectionFailure as e:
        print("Could not connect to MongoDB: %s") % e

conn = mongo_connect(MONGO_URI)

coll = conn[DATABASE][COLLECTION]

#to insert new document, remember unlike in the mongo shell, keys also need to be wrapped in quotes:
# new_doc = {"first": "douglas", "last": "adams", "dob": "11/03/1952", "gender": "m", "hair_color": "black", "occupation": "writer", "nationality": "british"}

new_docs = [{
    "first": "terry",
    "last": "pratchet",
    "dob": "28/04/1948",
    "gender": "m",
    "hair_color": "not much",
    "occupation": "writer",
    "nationality": "british"
},
{
    "first": "george",
    "last": "rr martin",
    "dob": "20/09/1948",
    "gender": "m",
    "hair_color": "white",
    "occupation": "writer",
    "nationality": "american"
}]

# coll.insert_many(new_docs)
coll.update_one({"last": "pratchet"}, {"$set": {"hair_color": "maroon"}})
documents = coll.find()
#this documents variable will return a mongodb object, also called a cursor

#need to iterate over that data/cursor to unpackage it
for doc in documents:
    print(doc)
