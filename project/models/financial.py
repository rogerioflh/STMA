import json
#Gerenciamento financeiro da equipe
class Financial:
    financial_records = []  

    def __init__(self):
        self.annual_revenue = 0  
        self.monthly_revenue = 0  
        self.monthly_expenses = {
            "folha_pagamento": 0, 
            "saude": 0,  
            "alimentacao": 0,  
            "manutencao": 0,  
            "viagens": 0, 
        }
        Financial.financial_records.append(self) 
        Financial.save_to_json()

    def set_annual_revenue(self, revenue):
        self.annual_revenue = revenue
        Financial.save_to_json()

    def set_monthly_revenue(self, revenue):
        self.monthly_revenue = revenue
        Financial.save_to_json()

    def add_monthly_expense(self, category, amount):
        if category in self.monthly_expenses:
            self.monthly_expenses[category] += amount
            Financial.save_to_json()
        else:
            raise ValueError(f"Categoria '{category}' não existe.")

    def get_monthly_expenses(self):
        return self.monthly_expenses

    def get_total_monthly_expenses(self):
        return sum(self.monthly_expenses.values())

    def get_financial_summary(self):
        return {
            "Faturamento Anual": self.annual_revenue,
            "Faturamento Mensal": self.monthly_revenue,
            "Gastos Mensais": self.monthly_expenses,
            "Total de Gastos Mensais": self.get_total_monthly_expenses(),
            "Saldo Mensal": self.monthly_revenue - self.get_total_monthly_expenses(),
        }

    def add_financial_record(self, description, amount, date):
        record = {
            "description": description,
            "amount": amount,
            "date": date,
        }
        Financial.financial_records.append(record)

    def get_financial_records(self):
        return Financial.financial_records

    @classmethod
    def save_to_json(cls, filename="financial.json"):
        """Salva os dados financeiros em um arquivo JSON."""
        with open(filename, "w") as file:
            json.dump([finance.to_dict() for finance in cls.financial_records], file, indent=4)

    @classmethod
    def load_from_json(cls, filename="financial.json"):
        """Carrega os dados financeiros de um arquivo JSON."""
        try:
            with open(filename, "r") as file:
                data = json.load(file)
                cls.financial_records = []
                for item in data:
                    finance = Financial()
                    finance.set_annual_revenue(item["annual_revenue"])
                    finance.set_monthly_revenue(item["monthly_revenue"])
                    for category, amount in item["monthly_expenses"].items():
                        finance.add_monthly_expense(category, amount)
                    cls.financial_records.append(finance)
        except FileNotFoundError:
            print(f"Arquivo {filename} não encontrado. Iniciando com lista vazia.")

    def to_dict(self):
        """Converte o objeto FinancialManager em um dicionário."""
        return {
            "annual_revenue": self.annual_revenue,
            "monthly_revenue": self.monthly_revenue,
            "monthly_expenses": self.monthly_expenses
        }
    def __str__(self):
        summary = self.get_financial_summary()
        return (
            f" Resumo Financeiro:\n"
            f" Faturamento Anual: R${summary['Faturamento Anual']:.2f}\n"
            f" Faturamento Mensal: R${summary['Faturamento Mensal']:.2f}\n"
            f" Gastos Mensais:\n"
            f"   - Folha de Pagamento: R${summary['Gastos Mensais']['folha_pagamento']:.2f}\n"
            f"   - Saúde: R${summary['Gastos Mensais']['saude']:.2f}\n"
            f"   - Alimentação: R${summary['Gastos Mensais']['alimentacao']:.2f}\n"
            f"   - Manutenção: R${summary['Gastos Mensais']['manutencao']:.2f}\n"
            f"   - Viagens: R${summary['Gastos Mensais']['viagens']:.2f}\n"
            f" Total de Gastos Mensais: R${summary['Total de Gastos Mensais']:.2f}\n"
            f" Saldo Mensal: R${summary['Saldo Mensal']:.2f}"
        )