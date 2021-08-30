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

def show_menu():
    print("")
    print("1. Add a record")
    print("2. Find a record by name")
    print("3. Edit a record")
    print("4. Delete a record")
    print("Exit menu")

    option = input("Enter option: ")
    return option 


def add_record():
    print("")
    first = input("Enter first name: ")
    last = input("Enter last name: ")
    dob = input("Enter date Of birth (DD/MM/YYYY): ")
    gender = input("Enter gender (m/f): ")
    hair_color = input("Enter hair color: ")
    occupation = input("Enter occupation: ")
    nationality = input("Enter Nationality: ")

    new_doc = {
        "first": first.lower(),
        "last": last.lower(),
        "dob": dob,
        "gender": gender.lower(),
        "hair_color": hair_color.lower(),
        "occupation": occupation.lower(),
        "nationality": nationality.lower
    }

    try:
        coll.insert(new_doc)
        print("")
        print("Document inserted")
    except:
        print("Error accessing the database")


def main_loop():
    while True:
        option = show_menu()
        if option == "1":
            add_record()
        elif option == "2":
            print("You have selected option 2")
        elif option == "3":
            print("You have selected option 3")
        elif option == "4":
            print("You have selected option 4")
        elif option == "5":
            conn.close()
            break
        else:
            print("Invalid option")
        print("")


conn = mongo_connect(MONGO_URI)

coll = conn[DATABASE][COLLECTION]

main_loop()