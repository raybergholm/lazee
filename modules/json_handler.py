#!/usr/bin/env python3

import json


def json_to_csv(data, field_list=None, delimiter=";"):
    # if no field_list is supplied, it will build it from the first item in the list. Doing it this way means that the key order will vary!
    header = [key for key in data[0].keys(
    )] if field_list == None else field_list

    csv_data = []
    for line in data:
        entry = [str(line[field]) if field in line else "" for field in header]
        csv_data.append("%s\n" % delimiter.join(entry))
    return csv_data


# supply a field list to filter the JSON data, otherwise it will return the whole body as-is
def from_json_file(filepath, field_list=None):
    data = None
    with open(filepath, newline="") as file_stream:
        data = json.loads(file_stream.read())

        if field_list:
            filtered = []
            for entry in data:
                filtered_entry = {entry for key,
                                  value in data.items() if entry in field_list}
                filtered.append(filtered_entry)

    return data


def to_json_file(filepath, data, field_list=None):
    with open(filepath, mode="w+", newline="") as file_stream:
        json_data = json.dumps(data)
        file_stream.write(json_data)
    return True
