from nicegui import ui
from mastery.ui.pages.utils import go
from mastery.question_db import question_bank
from mastery.exams import Exam


@ui.page('/exam')
def exam():
    ui.button('home', on_click=lambda: go('/'))
    ui.label("Generate an evaluation").classes("text-h2")
    pols = list(question_bank.get_pols())
    pol_checkboxes = []
    for pol in pols:
        pol_checkboxes.append(ui.checkbox(pol))
    ui.button("confirm", on_click=lambda: Exam(question_bank).exam_from_pols([state.value for state in pol_checkboxes]))
