from nicegui import ui

from mastery.ui.pages.utils import go
from mastery.question_db import question_bank


@ui.page("/view_questions")
def view_question():
    ui.button('home', on_click=lambda: go('/'))
    for i, row in question_bank.df.iterrows():
        ui.label(f"{row['pol']}: {row['question']}") 
