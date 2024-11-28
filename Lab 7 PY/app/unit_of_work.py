class UnitOfWork:
    def __init__(self, repository):
        self.repository = repository
        self.new_items = []

    def register_new(self, item):
        self.new_items.append(item)

    def commit(self):
        for item in self.new_items:
            self.repository.add(item)
        self.new_items = []
#групування кількох операцій