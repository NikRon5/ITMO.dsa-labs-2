from utils.file_utlis import read_from_file, write_to_file
from utils.time_memory_utlis import measure_time_and_memory

input_path = "../txtf/input.txt"
output_path = "../txtf/output.txt"


@measure_time_and_memory
def largest_number(nums):
    nums = list(map(str, nums))
    nums.sort(key=lambda x: x * 4, reverse=True)
    max_num = "".join(nums)
    return max_num if max_num[0] != "0" else "0"

def main():
    # Reading input file
    input_data = read_from_file(input_path)

    # Algorithm
    n = input_data[0]
    nums = input_data[1]
    result = largest_number(nums)

    # Writing output file
    output_data = result
    write_to_file(output_path, output_data)

if __name__ == "__main__":
    main()