import setup_path#pylint: disable=unused-import

from mastery.questions.open_question_db import save_question_db, open_question_db
from mastery.questions.save_question import add_question

question_df = open_question_db()

question_df = add_question(question_df)

save_question_db(question_df)