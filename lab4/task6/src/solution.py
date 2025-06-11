from utils.file_utlis import read_from_file, write_to_file
from utils.time_memory_utlis import measure_time_and_memory


input_path = "../txtf/input.txt"
output_path = "../txtf/output.txt"


@measure_time_and_memory
def z_func(s):
    n = len(s)
    z = [0] * n
    l, r = 0, 0
    for i in range(1, n):
        if i <= r:
            z[i] = min(r - i + 1, z[i - l])
        while i + z[i] < n and s[z[i]] == s[i + z[i]]:
            z[i] += 1
        if i + z[i] - 1 > r:
            l, r = i, i + z[i] - 1
    return z[1:]


def main():
    # Reading input file
    input_data = read_from_file(input_path)

    # Algorithm
    s = input_data

    result = z_func(s)

    # Writing output file
    output_data = " ".join(str(x) for x in result)
    write_to_file(output_path, output_data)


if __name__ == "__main__":
    main()