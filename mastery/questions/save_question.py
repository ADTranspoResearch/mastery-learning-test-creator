import pandas as pd
from mastery.config import ROOT

def read_question():
    question_path = ROOT / "new_question.txt"
    with open(question_path, 'r', encoding='utf-8') as f:
        content = f.read()
    return content

def add_question(df: pd.DataFrame):
    competency = input("what is the competency of the question (only 1)")
    content = read_question()
    df.loc[len(df)] = [competency, content]
    return df
