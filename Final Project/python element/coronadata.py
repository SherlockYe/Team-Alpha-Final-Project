import json
with open('timeseries.json','r') as f:
      json_text = f.read()


# Decode the JSON string into a Python dictionary.
corona_data = json.loads(json_text)


# Encode the Python dictionary into a JSON string.
new_json_string = json.dumps(corona_data, indent=4)
print(new_json_string)


