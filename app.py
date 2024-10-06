from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

# Route to handle /say requests
@app.route('/say', methods=['GET'])
def say_keyword():
    # Get the keyword from the query string
    keyword = request.args.get('keyword')

    if not keyword:
        return jsonify({"message": "No keyword provided"}), 400

    # Forward the request to API Gateway that triggers Lambda
    api_gateway_url = "https://nhye8gbzt9.execute-api.us-east-1.amazonaws.com/say"
    params = {"keyword": keyword}
    
    # Forwarding the request to AWS Lambda via API Gateway
    response = requests.get(api_gateway_url, params=params)

    return jsonify(response.json()), response.status_code

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
