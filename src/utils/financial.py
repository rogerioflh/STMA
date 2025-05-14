import json
from datetime import datetime
import os
from src.utils.file_handler import ensure_dir_exists

class Financial:
    def __init__(self):
        self._annual_revenue = 0
        self._monthly_revenue = 0
        self._financial_records = []
        self._monthly_expenses = {
            "folha_pagamento": 0,
            "saude": 0,
            "alimentacao": 0,
            "manutencao": 0,
            "viagens": 0,
        }
        self._financial_goals = {}

    @property
    def annual_revenue(self):
        return self._annual_revenue

    @annual_revenue.setter
    def annual_revenue(self, value):
        if value < 0:
            raise ValueError("O faturamento anual não pode ser negativo.")
        self._annual_revenue = value

    @property
    def monthly_revenue(self):
        return self._monthly_revenue

    @monthly_revenue.setter
    def monthly_revenue(self, value):
        if value < 0:
            raise ValueError("O faturamento mensal não pode ser negativo.")
        self._monthly_revenue = value

    @property
    def financial_records(self):
        return self._financial_records

    @property
    def monthly_expenses(self):
        return self._monthly_expenses

    @property
    def financial_goals(self):
        return self._financial_goals

    def add_financial_record(self, record_type, category, amount, date):
        if record_type.lower() not in ["gasto", "lucro"]:
            raise ValueError("Tipo de registro inválido. Use 'gasto' ou 'lucro'.")
        self._financial_records.append({
            "type": record_type.lower(),
            "category": category,
            "amount": amount,
            "date": date,
        })
        self.save_to_json()

    def get_monthly_summary(self, month, year):
        monthly = [
            r for r in self._financial_records
            if datetime.strptime(r["date"], "%d/%m/%Y").month == month and
               datetime.strptime(r["date"], "%d/%m/%Y").year == year
        ]
        return self._generate_summary(monthly)

    def get_semester_summary(self, semester, year):
        start = (semester - 1) * 6 + 1
        end = start + 5
        semester_records = [
            r for r in self._financial_records
            if start <= datetime.strptime(r["date"], "%d/%m/%Y").month <= end and
               datetime.strptime(r["date"], "%d/%m/%Y").year == year
        ]
        return self._generate_summary(semester_records)

    def get_annual_summary(self, year):
        annual = [
            r for r in self._financial_records
            if datetime.strptime(r["date"], "%d/%m/%Y").year == year
        ]
        return self._generate_summary(annual)

    def _generate_summary(self, records):
        expenses = sum(r["amount"] for r in records if r["type"] == "gasto")
        revenue = sum(r["amount"] for r in records if r["type"] == "lucro")
        return {
            "total_expenses": expenses,
            "total_revenue": revenue,
            "balance": revenue - expenses
        }

    def set_financial_goal(self, goal_type, target_amount):
        if goal_type.lower() not in ["gasto", "lucro"]:
            raise ValueError("Tipo de meta inválido. Use 'gasto' ou 'lucro'.")
        self._financial_goals[goal_type.lower()] = target_amount
        self.save_to_json()

    def check_goals(self):
        results = {}
        for goal, target in self._financial_goals.items():
            total = sum(r["amount"] for r in self._financial_records if r["type"] == goal)
            achieved = total >= target if goal == "lucro" else total <= target
            results[goal] = {
                "target": target,
                "actual": total,
                "achieved": achieved,
            }
        return results

    def save_to_json(self, filename="data/financial.json"):
        ensure_dir_exists(filename)
        with open(filename, "w") as file:
            json.dump(self.to_dict(), file, indent=4)

    @classmethod
    def load_from_json(cls, filename="data/financial.json"):
        try:
            with open(filename, "r") as file:
                data = json.load(file)
            inst = cls()
            inst._annual_revenue = data.get("annual_revenue", 0)
            inst._monthly_revenue = data.get("monthly_revenue", 0)
            inst._financial_records = data.get("financial_records", [])
            inst._monthly_expenses = data.get("monthly_expenses", {})
            inst._financial_goals = data.get("financial_goals", {})
            return inst
        except (FileNotFoundError, json.JSONDecodeError):
            print(f"Arquivo {filename} inválido ou não encontrado. Criando novo objeto.")
            return cls()

    def reset_financial_data(self):
        """Novo método: reseta todos os dados financeiros para os valores padrão."""
        self.__init__()  # Reinicializa todos os atributos com os valores padrão
        self.save_to_json()

    def to_dict(self):
        return {
            "annual_revenue": self._annual_revenue,
            "monthly_revenue": self._monthly_revenue,
            "financial_records": self._financial_records,
            "monthly_expenses": self._monthly_expenses,
            "financial_goals": self._financial_goals,
        }

    def __str__(self):
        return (
            f"Resumo Financeiro:\n"
            f"Faturamento Anual: R${self._annual_revenue:.2f}\n"
            f"Faturamento Mensal: R${self._monthly_revenue:.2f}\n"
            f"Gastos Mensais:\n"
            + "\n".join(
                f"  - {k.replace('_', ' ').capitalize()}: R${v:.2f}"
                for k, v in self._monthly_expenses.items()
            )
        )
