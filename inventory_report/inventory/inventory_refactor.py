from collections.abc import Iterable

from inventory_report.inventory.inventory_iterator import InventoryIterator
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class InventoryRefactor(Iterable):
    def __init__(self, importer):
        self.importer = importer
        self.data = []

    def __generate_report(self, report_type):
        if report_type == "simples":
            return SimpleReport.generate(self.data)
        elif report_type == "completo":
            return CompleteReport.generate(self.data)
        else:
            raise ValueError("Tipo de relatório inválido!")

    def import_data(self, file_path, report_type):
        data_imported = self.importer.import_data(file_path)
        self.data.extend(data_imported)
        return self.__generate_report(report_type)

    def __iter__(self):
        return InventoryIterator(self.data)
