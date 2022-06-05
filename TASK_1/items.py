from scrapy_jsonschema.item import JsonSchemaItem


#This is a JsonSchemaItem wich is provided by the 'scrapy_jsonschema' module.
#'scrapy_jsonschema' provides a powerful JSON Schema Validator.
#It takes the custom schema from the JsonSchemaItem and validates the data.
#If the data is missing or if it's not the type that we set in the jsonschema
#the item gets removed and it doesn't reach the DeviceSQLitePipeline wich stores
#the items in the database.

class DeviceItem(JsonSchemaItem):
    jsonschema =     {
        "$schema": "http://json-schema.org/draft-04/schema#",
        "title": "Product",
        "description": "Gplay.bg products",
        "type": "object",
        "properties": {
            "product_number": {
                "description": "The unique identifier for the product",
                "type": "string"
            },
            "category": {
                "description": "Name of the category",
                "type": "string"
            },
            "subcategory": {
                "description": "Name of the subcategory",
                "type": "string"
            },
            "name": {
                "description": "Name of the product",
                "type": "string"
            },
            "subtitle": {
                "description": "Name of the subtitle",
                "type": "string"
            },
            "price": {
                "description": "Price of the product",
                "type": "number"
            },
        },
        "required": ["product_number", "category", "subcategory", "name", "subtitle", "price"]
    }
