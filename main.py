import json
from flask import Flask, request, make_response

app = Flask(__name__)


# POST method to set a JSON object as a cookie
@app.route('/setcookies', methods=['POST'])
def set_cookie():
    # Get JSON data from the request body
    data = request.get_json()  # This expects JSON data in the body

    if not data or 'username' not in data:
        return "Username is required to set the cookie", 400  # Error if no username

    # Convert the JSON data to a string to store in the cookie
    json_data = json.dumps(data)  # Convert Python dict to JSON string

    # Create a response object and set the cookie
    resp = make_response(f"Cookie set for {data['username']}")
    resp.set_cookie('userdata', json_data)  # Set the 'userdata' cookie with JSON data

    return resp  # Return the response with the cookie


# GET method to retrieve the JSON data from the cookie
@app.route('/getcookies', methods=['GET'])
def get_cookie():
    # Retrieve the cookie containing the JSON string
    json_data = request.cookies.get('userdata')

    if json_data:
        # Convert the JSON string back to a Python dictionary
        data = json.loads(json_data)
        return f"Hello, {data['username']}! Your cookie data is working."
    else:
        return "No user data cookie found."


if __name__ == '__main__':
    app.run(debug=True)
