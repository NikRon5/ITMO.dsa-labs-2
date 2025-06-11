from utils.files_runner import FilesRunner

lab_id = 4

print(f"Лабароторная №{lab_id}. Задания\n")

fr = FilesRunner(f"lab{lab_id}/task*/src/*py")
fr.run()