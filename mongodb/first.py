import pymongo


client = pymongo.MongoClient('mongodb://127.0.0.1:27017')


db = client['emp']

info = db.information


record = {
	'firstname' : 'manju',
	'lastname' : 'reddy',
	'dept' : 'tech'
}

info.insert_one(record)

res = db.information.find({'firstname':'manju'})


print(res)

for i in res:
	print(i)



