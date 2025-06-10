from utils.file_utlis import read_from_file, write_to_file
from utils.time_memory_utlis import measure_time_and_memory

input_path = "../txtf/input.txt"
output_path = "../txtf/output.txt"


@measure_time_and_memory
def max_lectures(requests):
    requests.sort(key=lambda x: x[1])

    c = 0
    last_end = 0
    for start, end in requests:
        if start >= last_end:
            c += 1
            last_end = end
    return c

def main():
    # Reading input file
    input_data = read_from_file(input_path)

    # Algorithm
    n = input_data[0]
    requests = input_data[1:]
    result = max_lectures(requests)

    # Writing output file
    output_data = str(result)
    write_to_file(output_path, output_data)

if __name__ == "__main__":
    main()