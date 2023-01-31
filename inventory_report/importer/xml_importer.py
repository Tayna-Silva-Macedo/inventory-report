import xmltodict

from inventory_report.importer.importer import Importer


class XmlImporter(Importer):
    @classmethod
    def import_data(cls, file_path):
        if not file_path.endswith(".xml"):
            raise ValueError("Arquivo inválido")

        with open(file_path) as file:
            reader = file.read()
            return xmltodict.parse(reader)["dataset"]["record"]
