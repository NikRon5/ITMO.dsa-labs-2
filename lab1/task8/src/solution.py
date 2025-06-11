from utils.file_utlis import read_from_file, write_to_file
from utils.time_memory_utlis import measure_time_and_memory


input_path = "../txtf/input.txt"
output_path = "../txtf/output.txt"


@measure_time_and_memory
def max_lectures(requests):
    # Сортируем лекции по времени окончания
    requests.sort(key=lambda x: x[1])

    c = 0 # Счетчик выбранных лекций
    last_end = 0 # Время окончания последней выбранной лекции

    for start, end in requests:
        # Если текущая лекция начинается после окончания последней выбранной
        if start >= last_end:
            c += 1 # Увеличиваем счетчик
            last_end = end # Обновляем время окончания последней лекции
    return c


def main():
    # Чтение входных данных из файла
    input_data = read_from_file(input_path)

    # Извлечение параметров из входных данных
    n = input_data[0]
    requests = input_data[1:]

    # Вычисление результата
    result = max_lectures(requests)

    # Запись результата в выходной файл
    output_data = str(result)
    write_to_file(output_path, output_data)


if __name__ == "__main__":
    main()