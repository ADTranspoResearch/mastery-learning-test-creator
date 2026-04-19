from nicegui import ui

from mastery.ui.pages.utils import go
from mastery.question_db import add_question_standalone

@ui.page('/question')
def question():
    ui.button('home', on_click=lambda: go('/'))
    ui.label("Add a new question").classes("text-h2")
    pol = ui.input(label="Target Progression of Learning:").classes('w-96')
    quest = ui.textarea(label="Question body:").classes('w-full')
    def confirm(pol_text, quest_text):
        if len(pol_text) ==0 or len(quest_text) ==0:
            with ui.dialog() as dialog, ui.card():
                ui.label('POL or Question text cannot be blank.')
                ui.button('Close', on_click=dialog.close)
            dialog.open()
        else:
            ui.label("Question saved to bank.")
            add_question_standalone(pol_text, quest_text)
    ui.button("confirm", on_click=lambda: confirm(pol.value, quest.value))

    