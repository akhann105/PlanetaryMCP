from pymongo import MongoClient
from dotenv import load_dotenv
import os

# Load MongoDB connection string
load_dotenv()

# Connect to MongoDB
client = MongoClient(os.getenv("MONGO_URI"))

# Select database and collection
db = client["sample_guides"]
planets = db["planets"]

# Display one planet
print(planets.find_one())