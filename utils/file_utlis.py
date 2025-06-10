import os
import sys


def read_from_file(path):
    current_script_dir = os.path.dirname(sys.argv[0])
    abs_path = os.path.abspath(os.path.join(current_script_dir, path))
    f = open(abs_path)
    lines = f.read().strip().split('\n')
    f.close()

    data = []
    for line in lines:
        t_line = []
        for x in line.split():
            try:
                t_line.append(int(x))
            except ValueError:
                t_line.append(x)
        if len(t_line) == 1: data.append(t_line[0])
        else: data.append(t_line)
    if len(data) == 1: data = data[0]

    return data


def write_to_file(path, data):
    current_script_dir = os.path.dirname(sys.argv[0])
    abs_path = os.path.abspath(os.path.join(current_script_dir, path))
    f = open(abs_path, 'w')
    f.write(data)
    f.close()