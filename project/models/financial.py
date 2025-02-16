
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

    def set_annual_revenue(self, revenue):
        """Define o faturamento anual."""
        self.annual_revenue = revenue

    def set_monthly_revenue(self, revenue):
        """Define o faturamento mensal."""
        self.monthly_revenue = revenue

    def add_monthly_expense(self, category, amount):
        """Adiciona um gasto mensal a uma categoria específica."""
        if category in self.monthly_expenses:
            self.monthly_expenses[category] += amount
        else:
            raise ValueError(f"Categoria '{category}' não existe.")

    def get_monthly_expenses(self):
        """Retorna todos os gastos mensais."""
        return self.monthly_expenses

    def get_total_monthly_expenses(self):
        """Retorna o total de gastos mensais."""
        return sum(self.monthly_expenses.values())

    def get_financial_summary(self):
        """Retorna um resumo financeiro."""
        return {
            "Faturamento Anual": self.annual_revenue,
            "Faturamento Mensal": self.monthly_revenue,
            "Gastos Mensais": self.monthly_expenses,
            "Total de Gastos Mensais": self.get_total_monthly_expenses(),
            "Saldo Mensal": self.monthly_revenue - self.get_total_monthly_expenses(),
        }

    def add_financial_record(self, description, amount, date):
        """Adiciona um registro financeiro."""
        record = {
            "description": description,
            "amount": amount,
            "date": date,
        }
        Financial.financial_records.append(record)

    def get_financial_records(self):
        """Retorna todos os registros financeiros."""
        return Financial.financial_records

    def __str__(self):
        """Representação textual da classe."""
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