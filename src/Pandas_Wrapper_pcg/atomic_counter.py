import threading
class AtomicCounter:
    def __init__(self):
        self._lock = threading.Lock()
        self._counter = 0

    def increment(self):
        with self._lock:
            self._counter += 1
            return self._counter
