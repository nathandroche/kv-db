from threading import Lock

class backendDatabase:

    @staticmethod
    def init():
        return backendDatabase()

    def __init__(self):
        self.db = {}
        self.lock = Lock()
        self.closed = False

    def put(self, key, value):
        if self.closed:
            return 1
        else:
            with self.lock:
                self.db[key] = value
        return 0

    def get(self, key):
        if self.closed:
            return 1
        else:
            with self.lock():
                queryResults = self.db[key]
        return queryResults

    def delete(self, key):
        if self.closed:
            return 1
        else:
            with self.lock():
                del self
        return 0

    def close(self):
        if self.closed:
            return
        else:
            self.flush()
            with self.lock():
                self.closed = True
    
    def stats(self):
        return ""

    def flush(self):
        with self.lock():
            self.db.clear()
        return 0
