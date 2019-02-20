import matplotlib.pyplot as mp
import pandas as pd
import numpy as np
# function to open excel and pass it to data frame
def FetchData():
    path = "F:/MachineLearning/GameOfThronesData/battles.csv"
    MD = pd.read_csv(path)
    return MD
# function to take only important info from dataframe and make new dataframe
def FeaturePicker(BigData):
    SmallData = BigData[["battle_number","battle_type","attacker_size","defender_size","attacker_outcome","attacker_king"]]
    return SmallData
# function to return clean data
def DataCleanser(UCData):
    CData = UCData.fillna({
        "attacker_size" : UCData["attacker_size"].mean(),
        "defender_size" : UCData["defender_size"].mean(),
        "attacker_outcome" : 'none'})
    return CData
# function to return probability of winning
def probable(df,key):
    df1 = df[df["battle_type"] == key]
    list1 = df1.loc[:"attacker_outcome"]
    total = len(list1)
    winper = len(df1[df1["attacker_outcome"] == "win"])
    return (winper/total)
def probable1(df,key):
    df1 = df[df["attacker_king"] == key]
    list1 = df1.loc[:"attacker_outcome"]
    total = len(list1)
    winper = len(df1[df1["attacker_outcome"] == "win"])
    return (winper/total)
# Function to plot the data
def DataPlotter(df):
    df1 = df[df["attacker_outcome"] == "win"]
    df2 = df[df["attacker_outcome"] == "loss"]
    x1 = df1.loc[:,"attacker_size"]
    y1 = df1.loc[:,"defender_size"]
    x2 = df2.loc[:,"attacker_size"]
    y2 = df2.loc[:,"defender_size"]
    # Plot the data of x and y
    mp.plot(x1,y1,'go')
    mp.plot(x2,y2,'ro')
    mp.ylabel('size of defender army')
    mp.xlabel('size of attacker army')
    #mp.axis(0,4,0,16)
    # Add a legend
    mp.legend()
    # Show the plot
    mp.show()
if __name__ == "__main__":
    MainData = FetchData()
    #print(MainData)
    PlotData = FeaturePicker(MainData)
    #print(PlotData)
    king = input("What is your name my king?")
    inp = input("What is the type of battle that you are fighting? ambush/pitched battle/razing/siege ")
    alpha = probable(PlotData,inp)
    inp1 = input("Who is Going to be your Partner King? Balon/Euron Greyjoy,Joffrey/Tommen Baratheon,Robb Stark,Stannis Baratheon")
    beta = probable1(PlotData,inp1)
    print("Chance of you king",king,"winning the battle in GOT Realm is ",alpha*beta)
    CleanData = DataCleanser(PlotData)
    #print(CleanData)
    #DataPlotter(CleanData)

    
    
