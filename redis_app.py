from flask import Flask, jsonify
import redis

app = Flask(__name__)

# Connect to Redis
client = redis.Redis(
    host="localhost",
    port=6379,
    db=0,
    decode_responses=True
)


# Record a user query
@app.route("/query/<user>", methods=["POST"])
def record_query(user):
    client.incr("total_queries")
    client.sadd("active_users", user)

    return jsonify({"message": "Query recorded"})


# Get the total number of queries
@app.route("/queries", methods=["GET"])
def get_queries():
    total = client.get("total_queries")
    return jsonify({"total_queries": int(total or 0)})


# Get the number of unique users
@app.route("/users", methods=["GET"])
def get_users():
    return jsonify({
        "active_users": client.scard("active_users")
    })


# Start the Flask server
if __name__ == "__main__":
    app.run(port=5002)