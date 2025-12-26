import json
from pathlib import Path
from flask import Flask, render_template

app = Flask(__name__)

DATA_PATH = Path(__file__).parent / "data" / "recycling-rules.json"

with open(DATA_PATH) as f:
    recycling_data = json.load(f)

@app.route("/", methods=["GET"])
def show_homepage():
    city="Provo"
    rules=recycling_data[city]
    return render_template(
        "index.html",
        city=city,
        rules=rules
    )
# city_input = input("Which city? (Utah county only)").title()

# if city_input not in recycling_data:
    # print("City not found.")

# else:
    # user_city_rules = recycling_data[city_input]
    # print(user_city_rules)
