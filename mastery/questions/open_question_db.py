import pandas as pd

from mastery.config import DATA_DIR


## This should be a class.

def open_question_db():
    question_path = DATA_DIR / "questions.csv"
    question_df = pd.read_csv(question_path, index_col="index")
    return question_df

def save_question_db(df: pd.DataFrame):
    question_path = DATA_DIR / "questions.csv"
    df.to_csv(question_path)
    print("Question bank saved.")