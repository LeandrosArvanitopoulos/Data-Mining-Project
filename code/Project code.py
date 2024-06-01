import pandas as pd
import os


def printSHit():
    print("Shit")


def findFiles(path, output="output.csv"):
    files = [
        file
        for file in os.listdir(path)
        if file.endswith(".csv") and file != output and file != "outputEnglish.csv"
    ]
    return files


def openFilesWithPd(path, files):
    for file in files:
        full_file = open(path + "\\" + file, "r")
        current_data = pd.read_csv(full_file)
        current_data.set_index("timestamp", inplace=True)
        if "data" not in locals():
            data = current_data
        else:
            data = pd.concat([data, current_data], axis=0)

    print(data.head())
    print(data.describe())

    data.to_csv(path + "\\output.csv", sep=",", encoding="utf-16")
    print("The data has been saved to output.csv")


if __name__ == "__main__":
    path = "\\".join(os.path.dirname(__file__).split("\\")[:-1]) + "\Dataset"
    files = findFiles(path)
    ##print(*files, sep="\n")
    print("The files at the path have been opened")

    openFilesWithPd(path, files)
