import re

class InputParser:
    @staticmethod
    def extract_dates(input_str):
        return re.findall(r"\d{4}-\d{2}-\d{2}", input_str)

    @staticmethod
    def extract_phones(input_str):
        return re.findall(r"\+?\d{1,4}[-.\s]?\(?\d+\)?[-.\s]?\d+[-.\s]?\d+", input_str)
