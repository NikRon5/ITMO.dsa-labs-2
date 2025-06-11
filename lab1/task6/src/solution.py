from utils.file_utlis import read_from_file, write_to_file
from utils.time_memory_utlis import measure_time_and_memory


input_path = "../txtf/input.txt"
output_path = "../txtf/output.txt"


@measure_time_and_memory
def largest_number(nums):
    # Преобразуем числа в строки
    nums = list(map(str, nums))

    # Сортировка: умножаем строковое представление числа на 4 и сортируем в обратном порядке
    nums.sort(key=lambda x: x * 4, reverse=True)

    # Объединяем отсортированные числа в строку
    max_num = "".join(nums)

    # Если все числа нули
    return max_num if max_num[0] != "0" else "0"


def main():
    # Чтение входных данных из файла
    input_data = read_from_file(input_path)

    # Извлечение параметров из входных данных
    n = input_data[0]
    nums = input_data[1]

    # Вычисление результата
    result = largest_number(nums)

    # Запись результата в выходной файл
    output_data = result
    write_to_file(output_path, output_data)


if __name__ == "__main__":
    main()