import csv
import json

from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:
    @classmethod
    def import_data(cls, file_path, report_type):
        with open(file_path) as file:
            if file_path.endswith(".csv"):
                reader = csv.DictReader(file)
                data = list(reader)

            elif file_path.endswith(".json"):
                data = json.load(file)

        if report_type == "simples":
            return SimpleReport.generate(data)
        elif report_type == "completo":
            return CompleteReport.generate(data)
