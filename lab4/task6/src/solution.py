from utils.file_utlis import read_from_file, write_to_file
from utils.time_memory_utlis import measure_time_and_memory


input_path = "../txtf/input.txt"
output_path = "../txtf/output.txt"


@measure_time_and_memory
def z_func(s):
    n = len(s)
    z = [0] * n # Массив Z-функции
    l, r = 0, 0 # Границы самого правого отрезка совпадения

    for i in range(1, n):
        # Если текущий индекс внутри отрезка [l, r], берем минимум из оставшейся длины отрезка и z[i-l]
        if i <= r:
            z[i] = min(r - i + 1, z[i - l])

        # Пытаемся расширить текущее совпадение вручную
        while i + z[i] < n and s[z[i]] == s[i + z[i]]:
            z[i] += 1

        # Если нашли более правый отрезок совпадения, то обновляем границы
        if i + z[i] - 1 > r:
            l, r = i, i + z[i] - 1

    return z[1:]


def main():
    # Чтение входных данных из файла
    input_data = read_from_file(input_path)

    # Извлечение параметров из входных данных
    s = input_data

    # Вычисление результата
    result = z_func(s)

    # Запись результата в выходной файл
    output_data = " ".join(str(x) for x in result)
    write_to_file(output_path, output_data)


if __name__ == "__main__":
    main()