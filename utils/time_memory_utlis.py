import time
import tracemalloc


def measure_time_and_memory(func):
    def wrapper(*args, **kwargs):
        tm = TimeMemory()

        tm.start()
        result = func(*args, **kwargs)
        tm.print()

        return result

    return wrapper


class TimeMemory:
    def __init__(self):
        self.t_start = 0
        self.is_started = False

    def start(self):
        tracemalloc.start()
        self.t_start = time.perf_counter()
        self.is_started = True

    # In seconds
    def get_time(self):
        if self.is_started:
            t_end = time.perf_counter() - self.t_start
            return round(t_end, 5)
        else:
            return 0

    # In MB
    def get_memory(self):
        if self.is_started:
            memory = tracemalloc.get_traced_memory()
            return round(memory[1]/2**20, 6)
        else:
            return 0

    def get_time_memory(self):
        return self.get_time(), self.get_memory()

    def print(self):
        t_end, memory = self.get_time_memory()

        print(f"Время выполнения: {t_end} c")
        print(f"Пик памяти: {memory} МБ")

    def reset(self):
        tracemalloc.stop()
        self.start()