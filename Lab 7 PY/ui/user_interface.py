from prettytable import PrettyTable

class UserInterface:
    @staticmethod
    def display_table(data, headers):
        table = PrettyTable(headers)
        for row in data:
            table.add_row(row)
        print(table)

    @staticmethod
    def get_user_input(prompt):
        return input(prompt)
