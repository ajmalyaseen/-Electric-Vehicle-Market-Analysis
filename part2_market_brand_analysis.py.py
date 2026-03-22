import pandas as pd

df=pd.read_csv('ElectricCarData_Clean.csv')

#Which brand has the highest number of unique models listed in this dataset?
unique_models=df.groupby('Brand')['Model'].nunique()
print(unique_models.idxmax(),unique_models.max())

""" output:Tesla  13 """

print("----------------------------------------")

# Identify the most expensive and the least expensive electric cars in the 
most_exp_car=df.loc[df['PriceEuro'].idxmax(),['Brand','Model','PriceEuro']]
least_exp_car=df.loc[df['PriceEuro'].idxmin(),['Brand','Model','PriceEuro']]

print("Most Expensive Car: ")
print(most_exp_car,"\n")
print("least expensive car: ")
print(least_exp_car)

""" output:
Most Expensive Car: 
Brand           Tesla 
Model        Roadster 
PriceEuro       215000
Name: 51, dtype: object 

least expensive car: 
Brand                SEAT 
Model        Mii Electric 
PriceEuro            20129
Name: 44, dtype: object """

print("----------------------------------------")

#List all car models that offer 7 seats.
seven_seater=df[df['Seats']==7]
print(seven_seater.loc[:,["Brand","Model","Seats","PriceEuro"]])

""" output: 
        Brand                           Model   Seats  PriceEuro
21     Tesla    Model Y Long Range Dual Motor      7      58620
54     Tesla               Model X Long Range      7      85990
61     Tesla   Model Y Long Range Performance      7      65620
66    Nissan                  e-NV200 Evalia       7      33246
81     Tesla              Model X Performance      7     102990
84  Mercedes                     EQV 300 Long      7      70631 """


print("----------------------------------------")
#Determine which PlugType is the most common among all the vehicles listed.
vc = df["PlugType"].value_counts()
print(vc.index[0], vc.iloc[0])

""" output:Type 2 CCS 90 """