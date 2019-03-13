#!/usr/bin/env python3


def read_file(filepath, line_delimiter=None):
    with open(filepath, "r") as file_stream:
        data = file_stream.read()

    return data.split(line_delimiter) if line_delimiter != None else data


def save_file(filepath, data):
    with open(filepath, "w+") as file_stream:
        for entry in data:
            file_stream.write(entry)

    return True
