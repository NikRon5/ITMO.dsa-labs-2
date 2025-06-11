from utils.file_utlis import read_from_file, write_to_file
from utils.time_memory_utlis import measure_time_and_memory


input_path = "../txtf/input.txt"
output_path = "../txtf/output.txt"


@measure_time_and_memory
def prefix_func(s):
    n = len(s)
    prefix = [0] * n # Массив префикс-функции

    for i in range(1, n):
        j = prefix[i - 1] # Начинаем с предыдущего значения префикс-функции

        # Пока не найдем совпадение или не дойдем до начала
        while j > 0 and s[i] != s[j]:
            j = prefix[j - 1] # "Откатываем" j по префикс-функции

        # Если символы совпали, увеличиваем длину совпадающего префикса
        if s[i] == s[j]:
            j += 1

        # Записываем полученное значение
        prefix[i] = j

    return prefix


def main():
    # Чтение входных данных из файла
    input_data = read_from_file(input_path)

    # Извлечение параметров из входных данных
    s = input_data

    # Вычисление результата
    result = prefix_func(s)

    # Запись результата в выходной файл
    output_data = " ".join(str(x) for x in result)
    write_to_file(output_path, output_data)


if __name__ == "__main__":
    main()