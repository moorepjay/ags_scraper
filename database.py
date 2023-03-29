from pymongo import MongoClient
import csv
from constants import LOST_ARK_CLEANED_MASTER_FILE, NEW_WORLD_CLEANED_MASTER_FILE, CONNECTION_STRING


# Function takes both of our master files and uploads them to their respective mongodb collection.
def upload_csv_to_mongo(database):
    master_files = [LOST_ARK_CLEANED_MASTER_FILE, NEW_WORLD_CLEANED_MASTER_FILE]

    client = MongoClient(CONNECTION_STRING)

    db = client[database]

    csvfile = open(master_files[0], 'r', encoding="utf-8")
    reader = csv.DictReader(csvfile)
    header = ['Date', 'Region', 'Server', 'Seller', 'Price', 'USD']
    collection = db['lost_ark']

    # Lost Ark loop.
    for each in reader:
        row = {}
        for field in header:
            row[field] = each[field]
        collection.insert_one(row)

        print("The following document has been uploaded to {0}: {1} ".format(row, collection))

    csvfile = open(master_files[1], 'r', encoding="utf-8")
    reader = csv.DictReader(csvfile)
    header = ['Date', 'Region', 'Server', 'Seller', 'Price', 'USD']
    collection = db['new_world']

    # New World loop.
    for each in reader:
        row = {}
        for field in header:
            row[field] = each[field]
        collection.insert_one(row)

        print("The following document has been uploaded to {0}: {1} ".format(row, collection))

