from utils.file_utlis import read_from_file, write_to_file
from utils.time_memory_utlis import measure_time_and_memory


input_path = "../txtf/input.txt"
output_path = "../txtf/output.txt"


@measure_time_and_memory
def remove_brackets(s):
    # Открывающие скобки соответствующие закрывающим
    pairs = {
        ")": "(",
        "]": "[",
        "}": "{"
    }
    stack = [] # Стек для хранения индексов открывающих скобок
    remove = set() # Множество для хранения индексов скобок, которые нужно удалить

    for i, char in enumerate(s):
        if char in '([{': # Если это открывающая скобка, добавляем ее индекс в стек
            stack.append(i)
        elif char in ')]}':
            if stack and s[stack[-1]] == pairs[char]: # Если пара найдена
                stack.pop() # Удаляем ее из стека
            else:
                remove.add(i) # Помечаем закрывающую скобку для удаления

    # Открывающие скобки не имеющие пары помечаем для удаления
    remove.update(stack)

    # Исключаем помеченные для удаления скобки
    result = ''.join(s[i] for i in range(len(s)) if i not in remove)
    return result


def main():
    # Чтение входных данных из файла
    input_data = read_from_file(input_path)

    # Извлечение параметров из входных данных
    s = input_data

    # Вычисление результата
    result = remove_brackets(s)

    # Запись результата в выходной файл
    output_data = result
    write_to_file(output_path, output_data)


if __name__ == "__main__":
    main()