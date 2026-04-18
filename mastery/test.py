import pandas as pd
from mastery.config import ROOT

class Test:
    def __init__(self, q_bank: pd.DataFrame, name=None):
        self.name = name
        self.q_bank = q_bank
        self.avail_pol = self.q_bank["pol"].unique()

    def generate_test(self):
        
        for i, pol in enumerate(self.avail_pol):
            print(f"{i+1}. {pol}")
        print("Select all desired POLs using a string of POL numbers (ex: 123)")
        pol_index_str = input("desired POLs: ")
        desired_pols = []
        for pol_index in pol_index_str:
            desired_pols.append(self.avail_pol[int(pol_index) - 1])

        test_q = []
        for pol in desired_pols:
            test_q.append(
                f"{self.q_bank.loc[self.q_bank["pol"] == pol, "question"]
                .sample(n=1)
                .iloc[0]
                }\n"
            )
        test_path = ROOT / f"{self.name}_test.txt"
        with open(test_path, 'w', encoding='utf-8') as f:
            f.writelines(test_q)
        print(f"{self.name}'s test generated.")
