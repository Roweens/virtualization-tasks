from flask import Flask
import redis
from pymongo import MongoClient

app = Flask(__name__)

@app.route("/")
def hello():
    r = redis.Redis(host='redis', port=6379)
    r.set('foo', 'bar')
    redis_value = r.get('foo').decode('utf-8')

    client = MongoClient('mongodb1', 27017)
    db = client.test_database
    collection = db.test_collection
    collection.insert_one({"message": "Hello, MongoDB!"})
    mongo_count = collection.count_documents({})

    return f"Hello from Python! Redis: {redis_value}, MongoDB records: {mongo_count}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
