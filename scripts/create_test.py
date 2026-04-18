import setup_path #pylint: disable=unused-import

from mastery.exams import Exam
from mastery.question_db import open_question_db

student_name = "alessandro"

my_exam = Exam(q_bank = open_question_db(), name = student_name)

my_exam.generate_exam()