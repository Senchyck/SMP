class HistoryLogger:
    def __init__(self):
        self.history = []

    def log(self, request, response):
        self.history.append({"request": request, "response": response})

    def get_history(self):
        return self.history
