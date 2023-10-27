import unittest
from main import json_sniffer

class TestDataTypes(unittest.TestCase):
    def test_string_data(self):
        data = {
            "key1": "value1",
            "key2": "value2",
        }
        schema = json_sniffer(data)
        expected_schema = {
            "key1": {
                "type": "STRING",
                "tag": "",
                "description": "",
                "required": False
            },
            "key2": {
                "type": "STRING",
                "tag": "",
                "description": "",
                "required": False
            }
        }
        self.assertEqual(schema, expected_schema)

    def test_integer_data(self):
        data = {
            "count": 42,
            "quantity": 100,
        }
        schema = json_sniffer(data)
        expected_schema = {
            "count": {
                "type": "INTEGER",
                "tag": "",
                "description": "",
                "required": False
            },
            "quantity": {
                "type": "INTEGER",
                "tag": "",
                "description": "",
                "required": False
            }
        }
        self.assertEqual(schema, expected_schema)

    def test_enum_data(self):
        data = ["A", "B", "C"]
        schema = json_sniffer(data)

        expected_schema = {
            "": {
                "type": "ENUM",
                "tag": "",
                "description": "",
                "required": False
            },
            "[0]": {
                "type": "STRING",
                "tag": "",
                "description": "",
                "required": False
            },
            "[1]": {
                "type": "STRING",
                "tag": "",
                "description": "",
                "required": False
            },
            "[2]": {
                "type": "STRING",
                "tag": "",
                "description": "",
                "required": False
            }
        }

        self.assertEqual(schema, expected_schema)

    def test_json_sniffer(self):
        data = {
            "string_key": "ABC",
            "int_key": 123,
            "enum_key": ["A", "B", "C"],
            "object_key": {"nested_key": "XYZ"}
        }
        schema = json_sniffer(data)

        expected_schema = {
            "string_key": {
                "type": "STRING",
                "tag": "",
                "description": "",
                "required": False
            },
            "int_key": {
                "type": "INTEGER",
                "tag": "",
                "description": "",
                "required": False
            },
            "enum_key": {
                "type": "ENUM",
                "tag": "",
                "description": "",
                "required": False
            },
            "enum_key[0]": {
                "type": "STRING",
                "tag": "",
                "description": "",
                "required": False
            },
            "enum_key[1]": {
                "type": "STRING",
                "tag": "",
                "description": "",
                "required": False
            },
            "enum_key[2]": {
                "type": "STRING",
                "tag": "",
                "description": "",
                "required": False
            },
            "object_key": {
                "type": "OBJECT",
                "tag": "",
                "description": "",
                "required": False
            },
            "object_key.nested_key": {
                "type": "STRING",
                "tag": "",
                "description": "",
                "required": False
            }
        }

        self.assertEqual(schema, expected_schema)


if __name__ == '__main__':
    unittest.main()
