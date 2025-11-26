from flask import Flask, request, jsonify
from flask_cors import CORS
import work

app = Flask(__name__)
# coming back to config once domains are decided on
CORS(app, resources={r"/*": {"origins": "*"}})

@app.route("/", methods=["POST"])
def calculate_and_view():
    res = request.get_json()
    number = int(res.get("number"))
    mod = int(res.get("mod"))
    if number == None or mod == None:
        return jsonify({"error": "Missing 'number' or 'mod'"}), 400

    inverse, works = work.find_mod_inverse(number, mod, True, False)
    print({
        "inverse": inverse,
        "works": works
    })
    return jsonify({
        "inverse": inverse,
        "works": works
    }), 200

if __name__ == "__main__":
    app.run(debug=True)