import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import plotly.express as px
import os


def plotData(data: pd.DataFrame, start=0, stop=10000) -> None:
    print("Plotting data...")
    working_data = data.iloc[start:stop]
    indicies = pd.DataFrame()
    indicies["time"] = (
        pd.to_datetime(working_data.index) - pd.to_datetime(working_data.index[0])
    ).total_seconds()

    y = working_data
    y.index = indicies["time"]
    y.plot()
    plt.ylim(-4, 9)
    plt.legend(loc="upper right")
    plt.show()
    print("Data has been plotted successfully.")
    ##return data


def getData(file: str) -> pd.DataFrame:
    path = f"C:\\Users\\leand\\Desktop\\10o\\Data Mining\\Project\\Dataset\\{file}"  # "\\".join(os.getcwd().split("\\")[:-1]) + f"\\Dataset\\{file}"
    file = open(path, "r")
    data = pd.read_csv(file)
    return data


if __name__ == "__main__":
    # length = 30000
    # data = pd.DataFrame(columns=["random"])
    # data["random"] = np.random.randint(-2, 3, length)
    # data.index = [
    #     pd.Timestamp(f"2021-01-01 {i//3600}:0{i%3600//60}:0{i%60}") for i in range(length)
    # ]

    data = getData("S006.csv")

    # print(data.head())
    data = pd.concat([data, pd.DataFrame(index=[np.nan])])
    data = pd.concat([data, pd.DataFrame(index=[np.nan])])
    data = pd.concat([data, data.head()])
    # print(data.tail(10))
    # print(data.tail(10).index.isna().cumsum())
    split_by = data.index.isna().cumsum()
    print(split_by[-10:])
    print(data.tail(10))
    print("\n")

    dataframes = [
        dataframe
        for _, dataframe in data.groupby(split_by)
        if not dataframe.dropna().empty
    ]

    for df in dataframes:
        print(df.tail())
    # print(data.groupby(groups)[0].tail())
    # grouped = data.groupby(split_by)
    # for key in grouped.groups.keys():
    #     df = grouped.get_group(key).dropna()
    #     if df.empty:
    #         continue
    #     print(df.tail())
    # new = [df for df in data.groupby(groups)]
    # print(new)
    # for df in new:
    #     print(df.tail())
    # data = pd.concat([data, data])
    # print(data)
    # data = data.dropna().groupby(data.isna().cumsum())
    # print(type(data))
    # print(pd.to_datetime(data["timestamp"][0]))
    # plotData(data, 0, data.shape[0])
