import os
import glob


def get_file_data(path):
    f = open(path)
    return f.read()


class FilesRunner:
    input_path = "txtf/input.txt"
    output_path = "txtf/output.txt"
    home_dir = "ITMO.dsa-labs-2"

    def __init__(self, files_filter):
        home_path = os.path.join(os.getcwd().split(self.home_dir)[0], self.home_dir)
        os.chdir(home_path)
        self.__files_filter = files_filter

    def run(self):
        # Get files by glob filter
        files = list(glob.iglob(self.__files_filter))

        # Running all files
        for file in files:
            # .py is not needed
            file = file.replace(".py", "")

            # Splitting path
            t = file.split('\\')

            # For better output
            task = t[-3].replace("task", "Задание ")

            print("---------------------------")
            print(f"{task}: {t[-1]}.py")

            # Input file data
            input_data = get_file_data(os.path.join('/'.join(t[:-2]), self.input_path))

            # Getting path and running file
            file_path = '.'.join(t)
            exit_code = os.system(f"python -m {file_path}")

            # Output file data
            output_data = get_file_data(os.path.join('/'.join(t[:-2]), self.output_path))

            if exit_code == 0:
                print("\nВвод: ")
                print(input_data)
                print("\nВывод: ")
                print(output_data)
            else:
                print(f"\n{task}: {t[-1]}.py - Ошибка ❌")
            print("---------------------------\n")
