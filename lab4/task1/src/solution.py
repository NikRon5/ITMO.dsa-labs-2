from utils.file_utlis import read_from_file, write_to_file
from utils.time_memory_utlis import measure_time_and_memory


input_path = "../txtf/input.txt"
output_path = "../txtf/output.txt"


@measure_time_and_memory
def naive_pattern_search(p, t):
    len_p = len(p)
    occurrences = [] # Позиции вхождения

    for i in range(len(t) - len_p + 1):
        # Сравниваем подстроку текста с искомой подстрокой
        if t[i:i + len_p] == p:
            occurrences.append(i + 1) # Добавляем

    return [len(occurrences), occurrences]


def main():
    # Чтение входных данных из файла
    input_data = read_from_file(input_path)

    # Извлечение параметров из входных данных
    p = input_data[0]
    t = input_data[1]

    # Вычисление результата
    result = naive_pattern_search(p, t)

    # Запись результата в выходной файл
    output_data = str(result[0]) + "\n"
    output_data += " ".join(str(x) for x in result[1])
    write_to_file(output_path, output_data)


if __name__ == "__main__":
    main()