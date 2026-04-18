import setup_path #pylint: disable=unused-import

from mastery.test import Test
from mastery.questions.open_question_db import open_question_db

student_name = "alessandro"

my_test = Test(q_bank = open_question_db(), name = student_name)

my_test.generate_test()