class Repository:
    def __init__(self):
        self.data = []

    def add(self, item):
        self.data.append(item)

    def get_all(self):
        return self.data

    def filter(self, condition):
        return [item for item in self.data if condition(item)]
#Інкапсуляція