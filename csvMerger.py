import pandas as pd


def mainCsvMerger():
    df = pd.read_csv("2009-2014.csv")
    df2 = pd.read_csv("2015-2017.csv")
    df = pd.concat([df, df2])
    df2 = pd.read_csv("2018.csv")
    df = pd.concat([df, df2])
    df2 = pd.read_csv("2019-2022.csv")
    df = pd.concat([df, df2])

    df.drop_duplicates()

    df.to_csv("mediumArchive.csv", index=False)










