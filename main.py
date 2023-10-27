import json

def json_sniffer(data, prefix="", is_array=False):
    schema = {}
    if isinstance(data, dict):
        for key, value in data.items():
            new_prefix = f"{prefix}.{key}" if prefix else key
            if key != "attributes":
                if isinstance(value, str):
                    data_type = "STRING"
                elif isinstance(value, int):
                    data_type = "INTEGER"
                else:
                    data_type = "ARRAY" if isinstance(value, list) else "OBJECT" if isinstance(value, dict) else None
                schema[new_prefix] = {
                    "type": data_type,
                    "tag": "",
                    "description": "",
                    "required": False
                }
            if isinstance(value, (dict, list)):
                schema.update(json_sniffer(value, prefix=new_prefix))
    elif isinstance(data, list):
        data_type = "ENUM" if all(isinstance(item, str) for item in data) else "ARRAY" if all(isinstance(item, dict) for item in data) else None
        if data_type == "ENUM":
            schema[prefix] = {
                "type": data_type,
                "tag": "",
                "description": "",
                "required": False
            }
            for i, item in enumerate(data):
                new_prefix = f"{prefix}[{i}]"
                schema[new_prefix] = {
                    "type": "STRING",
                    "tag": "",
                    "description": "",
                    "required": False
                }
        else:
            if data_type:
                schema[prefix] = {
                    "type": data_type,
                    "tag": "",
                    "description": "",
                    "required": False
                }
            for i, item in enumerate(data):
                new_prefix = f"{prefix}[{i}]"
                schema.update(json_sniffer(item, prefix=new_prefix, is_array=True))
    
    return schema

def process_and_save(input_file, output_file):
    with open(input_file, "r") as json_file:
        input_data = json.load(json_file)

    message_schema = json_sniffer(input_data["message"])

    with open(output_file, "w") as output_file:
        json.dump(message_schema, output_file, indent=4)

    print("Schema extracted and saved to", output_file)

# Process data_1.json and save the result to schema_1.json
process_and_save("./data/data_1.json", "./schema/schema_1.json")

# Process data_2.json and save the result to schema_2.json
process_and_save("./data/data_2.json", "./schema/schema_2.json")
