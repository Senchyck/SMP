import json
import csv

class DataSaver:
    @staticmethod
    def save_to_json(data, filename):
        with open(filename, 'w') as file:
            json.dump(data, file, indent=4)

    @staticmethod
    def save_to_csv(data, filename, headers):
        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(headers)
            writer.writerows(data)
