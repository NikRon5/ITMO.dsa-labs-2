from utils.file_utlis import read_from_file, write_to_file
from utils.time_memory_utlis import measure_time_and_memory


input_path = "../txtf/input.txt"
output_path = "../txtf/output.txt"


@measure_time_and_memory
def prefix_func(s):
    n = len(s)
    prefix = [0] * n
    for i in range(1, n):
        j = prefix[i - 1]
        while j > 0 and s[i] != s[j]:
            j = prefix[j - 1]
        if s[i] == s[j]:
            j += 1
        prefix[i] = j
    return prefix


def main():
    # Reading input file
    input_data = read_from_file(input_path)

    # Algorithm
    s = input_data

    result = prefix_func(s)

    # Writing output file
    output_data = " ".join(str(x) for x in result)
    write_to_file(output_path, output_data)


if __name__ == "__main__":
    main()