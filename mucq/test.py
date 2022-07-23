import json
def write_json(object, filename):
    object_json = json.dumps(object)
    json_file = open(filename, "r").read()
    json_file += str(object)
    json_file.write(object_json)

write_json({'product_name': False}, 'mucq.json')