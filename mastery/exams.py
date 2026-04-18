import pandas as pd
from mastery.config import ROOT
from mastery.question_db import question_db

class Exam:
    def __init__(self, question_bank: pd.DataFrame, name="Student_1"):
        self.name = name
        self.question_bank = question_bank
        self.avail_pol = self.question_bank.df["pol"].unique()

    def generate_exam(self, desired_pols):

        exam_q = []
        for pol in desired_pols:

            # This needs to be here to make the sample actually sample randomly
            subset = self.question_bank.df[self.question_bank.df["pol"] == pol]
            # This needs to be here to make the sample actually sample randomly
            exam_q.append(
                f"{self.question_bank.df.loc[self.question_bank.df["pol"] == pol, "question"]
                .sample(n=1)
                .iloc[0]
                }\n"
            )
        exam_path = ROOT / f"{self.name}_exam.txt"
        with open(exam_path, 'w', encoding='utf-8') as f:
            f.writelines(exam_q)
        print(f"{self.name}'s exam generated.")

    def exam_from_pols(self, pol_mask):
        available_pols = self.question_bank.get_pols()
        desired_pols = available_pols[pol_mask]

        self.generate_exam(desired_pols)
