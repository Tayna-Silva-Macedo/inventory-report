import sys

from inventory_report.inventory.inventory_refactor import InventoryRefactor
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter


def get_importer(file_path):
    if file_path.endswith(".csv"):
        return CsvImporter
    elif file_path.endswith(".json"):
        return JsonImporter
    elif file_path.endswith(".xml"):
        return XmlImporter


def main():
    if len(sys.argv) != 3:
        return sys.stderr.write("Verifique os argumentos\n")

    file_path = sys.argv[1]
    report_type = sys.argv[2]

    importer = get_importer(file_path)

    report = InventoryRefactor(importer).import_data(file_path, report_type)

    print(report, end="")
