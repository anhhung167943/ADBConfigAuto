class Controller:
    def __init__(self, name):
        self.name = name
        self.device = None

    def run(self):
        self.device = adb_connect()