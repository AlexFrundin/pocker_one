import pymongo

c=pymongo.MongoClient()

cs=c.PhoneBook.Contact.find
