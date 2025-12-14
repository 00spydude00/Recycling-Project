import json
from pathlib import Path

DATA_PATH = Path(__file__).parent / "data" / "recycling-rules.json"

with open(DATA_PATH) as f:
    recycling_data = json.load(f)

city_input = input("which city bud?").title()

if city_input not in recycling_data:
    print("shit is not in there buddy")

else:
    user_city_rules = recycling_data[city_input]
    print(user_city_rules)
