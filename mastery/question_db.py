import pandas as pd
from mastery.config import ROOT
from mastery.config import DATA_DIR


def add_question_standalone(pol, content):
    question_path = DATA_DIR / "questions.csv"
    df = pd.read_csv(question_path, index_col="index")
    df.loc[len(df)] = [pol, content]
    df.to_csv(question_path)


class question_db:
    def __init__(self):
        ## Check if a db exists if not create one.
        question_path = DATA_DIR / "questions.csv"
        self.df = pd.read_csv(question_path, index_col="index")

    def save_question_db(self, df: pd.DataFrame):

        question_path = DATA_DIR / "questions.csv"
        self.df.to_csv(question_path)
        print("Question bank saved.")

    def add_question(self, pol, content):

        self.df.loc[len(self.df)] = [pol, content]
        self.save_question_db(self.df)

    def get_pols(self):
        pols = self.df['pol'].unique()
        return pols
    
question_bank = question_db()