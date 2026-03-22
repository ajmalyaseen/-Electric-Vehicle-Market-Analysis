import pandas as pd

df=pd.read_csv('ElectricCarData_Clean.csv')

#Identify which car model has the fastest 0-100 km/h acceleration (the lowest AccelSec value).
fastest_car=df.sort_values(['AccelSec'])
print(fastest_car.head(1))

""" OutPut:      Brand      Model  AccelSec  ...  Segment  Seats  PriceEuro
51  Tesla   Roadster        2.1  ...        S      4     215000 """

print("---------------------------")

#Which car has the highest TopSpeed_KmH?
topspeed_car=df.sort_values(['TopSpeed_KmH'])
print(topspeed_car[['Brand','TopSpeed_KmH']].tail(1))

""" output:     Brand  TopSpeed_KmH
51  Tesla            410 """

print("---------------------------")

#Find the car with the longest Range_Km.
longest_range_car=df.sort_values(['Range_Km'])
print(longest_range_car[['Brand','Range_Km']].tail(1))

""" output:    Brand  Range_Km
51  Tesla        970 """


print("---------------------------")
#Which vehicle has the best (lowest) Efficiency_WhKm?

lowest_Efficiency=df.sort_values(['Efficiency_WhKm'])
print(lowest_Efficiency[['Brand','Efficiency_WhKm']].head(1))

""" output:        Brand  Efficiency_WhKm
48  Lightyear               104 """