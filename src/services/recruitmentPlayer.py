import json

class RecruitmentProspect:
    def __init__(self, name, position, age, stats=None):
        self._name = name
        self._position = position
        self._age = age
        self._stats = stats or {}

    # Getters e Setters
    @property
    def name(self):
        return self._name

    @property
    def position(self):
        return self._position

    @property
    def age(self):
        return self._age

    @property
    def stats(self):
        return self._stats

    def evaluate(self, evaluation):
        self._stats["evaluation"] = evaluation

    def to_dict(self):
        return {
            "name": self._name,
            "position": self._position,
            "age": self._age,
            "stats": self._stats
        }

    def __str__(self):
        return (
            f" Nome da possível contratação: {self._name}\n"
            f" Posição em que atua: {self._position}\n"
            f" Idade: {self._age}\n"
            f" Estatísticas: {self._stats}"
        )


class RecruitmentFacade:
    _prospects = []

    @classmethod
    def load(cls, filename="recruitment_data.json"):
        try:
            with open(filename, "r") as file:
                data = json.load(file)
                cls._prospects = [
                    RecruitmentProspect(
                        item["name"], item["position"], item["age"], item.get("stats")
                    )
                    for item in data
                ]
        except FileNotFoundError:
            print(f"Arquivo {filename} não encontrado. Iniciando com lista vazia.")
        except json.JSONDecodeError:
            print(f"Erro ao carregar {filename}. O arquivo pode estar corrompido.")

    @classmethod
    def save(cls, filename="recruitment_data.json"):
        with open(filename, "w") as file:
            json.dump([p.to_dict() for p in cls._prospects], file, indent=4)

    @classmethod
    def add_prospect(cls, name, position, age, stats=None):
        prospect = RecruitmentProspect(name, position, age, stats)
        cls._prospects.append(prospect)
        cls.save()
        return prospect

    @classmethod
    def evaluate_prospect(cls, name, evaluation):
        prospect = cls.get_by_name(name)
        if prospect:
            prospect.evaluate(evaluation)
            cls.save()
            return True
        return False

    @classmethod
    def get_by_name(cls, name):
        return next((p for p in cls._prospects if p.name == name), None)

    @classmethod
    def list_prospects(cls):
        for p in cls._prospects:
            print(p)

    @classmethod
    def remove_prospect(cls, name):
        prospect = cls.get_by_name(name)
        if prospect:
            cls._prospects.remove(prospect)
            cls.save()
            print(f"Prospecto '{name}' removido.")
            return True
        print(f"Prospecto '{name}' não encontrado.")
        return False
