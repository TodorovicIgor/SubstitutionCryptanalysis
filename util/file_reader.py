import os
from util.cipher import transform


def read_file(name):
    ret = ""
    temp = os.path.join(os.path.dirname(__file__), "../", "test/", name)
    file_reader = open(temp, "r", encoding="utf8")
    line = file_reader.readline()
    while line:
        print("reading line")
        ret += transform(line)
        line = file_reader.readline()
    return ret