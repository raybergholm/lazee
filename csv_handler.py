#!/usr/bin/env python3

import csv

def csv_to_json(header, data):
    json_data = []
    for line in data:
        entry = {field: line[index] for index, field in enumerate(header)}
        json_data.append(entry)
    return json_data

def from_csv_file(filepath, delimiter=";", quotechar="\"", has_header=True):
    header = None
    data = []
    with open(filepath, mode="r", newline="") as file_stream:
        reader = csv.reader(file_stream, delimiter=delimiter, quotechar=quotechar)
        if has_header:
            for index, row in enumerate(reader):
                if index == 0:
                    header = row
                else:
                    data.append(row)
        else:
            data = [row for row in reader]
    return (header, data)

def to_csv_file(filepath, data, header=None, delimiter=";", quotechar="\""):
    with open(filepath, mode="w+", newline="") as file_stream:
        writer = csv.writer(file_stream, delimiter=delimiter, quotechar=quotechar)

        if header != None:
            writer.writerow(header)
        
        for entry in data:
            writer.writerow(entry)
    return True