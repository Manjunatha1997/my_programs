import redis
import pickle

r = redis.StrictRedis(host='localhost',port=6379,password=None)



def set_json(value):
	key, value = list(value.items())[0]
	x = pickle.dumps(value)
	return r.set(key,x)

def get_json(key):
	x = r.get(key)
	return pickle.loads(x)


x = set_json({'name':'manju'})
print(x)

res = get_json('name')
print(res)




