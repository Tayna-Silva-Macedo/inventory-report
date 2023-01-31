from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):
    @classmethod
    def generate(cls, data):
        report = super().generate(data)

        companies_counter = cls.companies_counter(data)

        report += "\nProdutos estocados por empresa:\n"

        for company, quantity in companies_counter.items():
            report += f"- {company}: {quantity}\n"

        return report
