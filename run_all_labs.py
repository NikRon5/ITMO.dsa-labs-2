import glob
from utils.files_runner import FilesRunner

print("Запуск заданий всех лабораторных работ")

labs = list(glob.iglob("lab*/"))
for lab in labs:
    print(f"\n\nЛабораторная №{lab.replace('lab', '')[:-1]}")
    fr = FilesRunner(f"{lab}task*/src/*.py")
    fr.run()