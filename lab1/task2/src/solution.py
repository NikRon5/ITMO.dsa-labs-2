from utils.file_utlis import read_from_file, write_to_file
from utils.time_memory_utlis import measure_time_and_memory


input_path = "../txtf/input.txt"
output_path = "../txtf/output.txt"


@measure_time_and_memory
def min_refuels(d, m, n, stops):
    stops += [d] # Добавляем точку назначения в конец списка
    refuels = 0 # Счетчик заправок
    last_refuel = 0 # Позиция последней заправки

    # Проходим по всем заправочным станциям
    for i in range(n):
        # Проверяем, сможем ли мы доехать до следующей станции
        if stops[i+1] - last_refuel > m:
            # Если не можем, проверяем, можем ли доехать до текущей станции
            if stops[i] - last_refuel <= m:
                # Если можем, заправляемся здесь
                refuels += 1
                last_refuel = stops[i]
            else:
                # Если не можем доехать даже до текущей станции, то маршрут невозможен
                return -1

    return refuels


def main():
    # Чтение входных данных из файла
    input_data = read_from_file(input_path)

    # Извлечение параметров из входных данных
    d = input_data[0]
    m = input_data[1]
    n = input_data[2]
    stops = input_data[3]

    # Вычисление результата
    result = min_refuels(d, m, n, stops)

    # Запись результата в выходной файл
    output_data = str(result)
    write_to_file(output_path, output_data)


if __name__ == "__main__":
    main()