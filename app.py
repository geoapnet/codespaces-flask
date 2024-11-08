from flask import Flask, Response, jsonify
from flask_cors import CORS
import geopandas as gpd

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes
file_name = 'countries.geojson'
world_data = gpd.read_file(file_name)

@app.route("/")
def send_home():
    return 'Hello World'

@app.route("/get-country/<country>")
def send_country(country):
    # Filter for the requested country
    feature = world_data[world_data['ADMIN'] == country]
    if feature.empty:
        return jsonify({"error": "Country not found"}), 404  # Return 404 if country is not found

    feature_json = feature.to_json()
    return Response(feature_json, content_type='application/json')

if __name__ == "__main__":
    app.run(port=5005)
