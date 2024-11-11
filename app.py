from flask import Flask, request, jsonify

app = Flask(__name__)

def reformat_to_nested(data):
    nested_result = {}

    # Process each dictionary in the input array
    for item in data:
        category = item.get("category")
        sub_category = item.get("sub_category")
        
        # Initialize nested dictionary structure if not already present
        if category not in nested_result:
            nested_result[category] = {}
        
        if sub_category not in nested_result[category]:
            nested_result[category][sub_category] = []

        # Add the dictionary item to the nested structure
        nested_result[category][sub_category].append({
            "id": item["id"],
            "name": item["name"]
        })
    
    return nested_result

# route reformat-array only method post
@app.route('/reformat-array', methods=['POST'])
def reformat_array():
    # Get JSON data from the request
    data = request.get_json()

    # Check if the data is a list of dictionaries
    if not isinstance(data, list) or not all(isinstance(i, dict) for i in data):
        return jsonify({"error": "Input should be a list of dictionaries"}), 400

    # Reformat the data into the nested structure
    nested_data = reformat_to_nested(data)

    return jsonify(nested_data), 200

if __name__ == '__main__':
    app.run(debug=True)
