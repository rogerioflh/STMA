# Gerenciamento de mídias e relações públicas da equipe
class MediaManager:
    press_releases = []  # Lista para armazenar releases de mídia

    def __init__(self, title, content, date):
        self.title = title
        self.content = content
        self.date = date
        MediaManager.press_releases.append(self)  # Adiciona à lista de releases

    def __str__(self):
        return (
            f" Título: {self.title}\n"
            f" Conteúdo: {self.content}\n"
            f" Data: {self.date}"
        )