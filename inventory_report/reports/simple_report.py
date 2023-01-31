from datetime import date
from collections import Counter


class SimpleReport:
    @classmethod
    def generate(cls, data):
        manufacturing_dates = [
            product["data_de_fabricacao"] for product in data
        ]
        earliest_manufacturing_date = sorted(manufacturing_dates)[0]

        today = str(date.today())
        expiration_dates = [
            product["data_de_validade"]
            for product in data
            if product["data_de_validade"] >= today
        ]
        closest_expiration_date = sorted(expiration_dates)[0]

        companies = [product["nome_da_empresa"] for product in data]
        companie_most_common = Counter(companies).most_common()[0][0]

        return (
            f"Data de fabricação mais antiga: {earliest_manufacturing_date}\n"
            f"Data de validade mais próxima: {closest_expiration_date}\n"
            f"Empresa com mais produtos: {companie_most_common}"
        )
