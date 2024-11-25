import json

# Load JSON data
with open("alerts.json") as file:
    data = json.load(file)

# Extract relevant fields
alerts = []
for hit in data["hits"]["hits"]:
    source = hit["_source"]
    alerts.append({
        "timestamp": source["@timestamp"],
        "alert_name": source["alert_name"],
        "source_ip": source["source"]["ip"],
        "source_port": source["source"]["port"],
        "destination_ip": source["destination"]["ip"],
        "destination_port": source["destination"]["port"],
        "severity": source["details"]["severity"]
    })

# Save transformed data to a new JSON file
with open("transformed_alerts.json", "w") as file:
    json.dump(alerts, file, indent=2)
