import csv
import json
import xmltodict

from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:
    @classmethod
    def read_csv(cls, file):
        reader = csv.DictReader(file)
        return list(reader)

    @classmethod
    def read_json(cls, file):
        return json.load(file)

    @classmethod
    def read_xml(cls, file):
        reader = file.read()
        return xmltodict.parse(reader)["dataset"]["record"]

    @classmethod
    def generate_report(cls, data, report_type):
        if report_type == "simples":
            return SimpleReport.generate(data)
        elif report_type == "completo":
            return CompleteReport.generate(data)
        else:
            raise ValueError("Formato de arquivo inválido!")

    @classmethod
    def import_data(cls, file_path, report_type):
        with open(file_path) as file:
            if file_path.endswith(".csv"):
                data = cls.read_csv(file)

            elif file_path.endswith(".json"):
                data = cls.read_json(file)

            elif file_path.endswith(".xml"):
                data = cls.read_xml(file)

        return cls.generate_report(data, report_type)
