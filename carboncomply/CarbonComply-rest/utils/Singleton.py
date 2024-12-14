import threading

lock = threading.Lock()


class Singleton(type):
    _instances = {}
    _singleton_locks = {}

    def __call__(cls, *args, **kwargs):
        # double-checked locking pattern (https://en.wikipedia.org/wiki/Double-checked_locking)
        if cls not in cls._instances:
            cls._singleton_locks[cls] = threading.Lock()
            with cls._singleton_locks[cls]:
                if cls not in cls._instances:
                    cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]