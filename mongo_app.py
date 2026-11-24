from flask import Flask, jsonify
from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

# Connect to MongoDB
client = MongoClient(os.getenv("MONGO_URI"))
db = client["sample_guides"]
planets = db["planets"]


# Get all planets
@app.route("/planets", methods=["GET"])
def get_planets():
    result = list(planets.find({}, {"_id": 0}))
    return jsonify(result)


# Find planets containing a specific atmospheric gas
@app.route("/atmosphere/<gas>", methods=["GET"])
def get_atmosphere(gas):
    result = list(planets.find(
        {"mainAtmosphere": gas},
        {"_id": 0, "name": 1, "mainAtmosphere": 1}
    ))
    return jsonify(result)


# Find planets that have rings
@app.route("/rings", methods=["GET"])
def get_rings():
    result = list(planets.find(
        {"hasRings": True},
        {"_id": 0, "name": 1}
    ))
    return jsonify(result)


# Get mean temperatures and positions from the Sun
@app.route("/temperature", methods=["GET"])
def get_temperature():
    result = list(planets.find(
        {},
        {"_id": 0, "name": 1, "orderFromSun": 1,
         "surfaceTemperatureC.mean": 1}
    ).sort("orderFromSun", 1))
    return jsonify(result)


# Start the Flask server
if __name__ == "__main__":
    app.run(port=5001)