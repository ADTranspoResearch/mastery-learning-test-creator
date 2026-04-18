from nicegui import ui

from mastery.ui.pages.utils import go
from mastery.question_db import question_bank

@ui.page('/')
def home():
    ui.label("Mastery Learning Evaluation Tool").classes("text-h2")

    ui.button("Add question to bank", on_click=lambda: go('/question'))
    ui.button("Generate new Evaluation", on_click=lambda: go('/exam'))
