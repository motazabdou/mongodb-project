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


# initial function that allows user to choose a task to be perfomer
def show_menu():
    print("")
    print("1. Add a record")
    print("2. Find a record by name")
    print("3. Edit a record")
    print("4. Delete a record")
    print("Exit menu")

    option = input("Enter option: ")
    return option 


# helper function that will enable obtaining record, then inserting it into relevant function
def get_record():
    print("")
    first = input("Enter first name: ")
    last = input("Enter last name: ")

    try:
        doc = coll.find_one({"first": first.lower(), "last": last.lower()})
    except:
        print("Error accessing the database")

    if not doc:
        print("")
        print("Error! No results found.")

    return doc


# function that adds new entry, will be called when user selects option 1
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
        "gender": gender,
        "hair_color": hair_color,
        "occupation": occupation,
        "nationality": nationality
    }

    try:
        coll.insert_one(new_doc)
        print("")
        print("Document inserted")
    except:
        print("Error accessing the database")


#function that finds records, it calls the get_record function, finds record, and loops through document to print key: value
def find_record():
    doc = get_record()
    if doc:
        print("")
        for k, v in doc.items():
            if k != "_id":
                print(k.capitalize() + ":" + v.capitalize())


def edit_record():
    doc = get_record()
    if doc:
        update_doc = {}
        print("")
        for k, v in doc.items():
            if k != "_id":
                update_doc[k] = input(k.capitalize() + " [" + v + "]")

                if update_doc[k] == "":
                    update_doc[k] = v

        try:
            coll.update_one(doc, {"$set": update_doc})
            print("")
            print("Document updated")

        except:
            print("Error accessing database")


#function to delete a document
def delete_record():
    doc = get_record()
    if doc:
        print("")
        for k, v in doc.items():
            if k != "_id":
                print(k.capitalize() + ": " + v.capitalize())

        print("")
        confirmation = input("Is this the document that you would like to delete?\nY/N")
        print("")

        if confirmation.lower() == "y":
            try:
                coll.remove(doc)
                print("Document deleted")
            except:
                print("Error accessing database")

        else:
            print("Document not deleted")


            


def main_loop():
    while True:
        option = show_menu()
        if option == "1":
            add_record()
        elif option == "2":
            find_record()
        elif option == "3":
            edit_record()
        elif option == "4":
            delete_record()
        elif option == "5":
            conn.close()
            break
        else:
            print("Invalid option")
        print("")


conn = mongo_connect(MONGO_URI)

coll = conn[DATABASE][COLLECTION]

main_loop()