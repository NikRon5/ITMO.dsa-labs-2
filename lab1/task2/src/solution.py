from utils.file_utlis import read_from_file, write_to_file
from utils.time_memory_utlis import measure_time_and_memory

input_path = "../txtf/input.txt"
output_path = "../txtf/output.txt"


@measure_time_and_memory
def min_refuels(d, m, n, stops):
    stops += [d]
    refuels = 0
    last_refuel = 0

    for i in range(n):
        if stops[i+1] - last_refuel > m:
            if stops[i] - last_refuel <= m:
                refuels += 1
                last_refuel = stops[i]
            else:
                return -1

    return refuels

def main():
    # Reading input file
    input_data = read_from_file(input_path)

    # Algorithm
    d = input_data[0]
    m = input_data[1]
    n = input_data[2]
    stops = input_data[3]
    result = min_refuels(d, m, n, stops)

    # Writing output file
    output_data = str(result)
    write_to_file(output_path, output_data)

if __name__ == "__main__":
    main()