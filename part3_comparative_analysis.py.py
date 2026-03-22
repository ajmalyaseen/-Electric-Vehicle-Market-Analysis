import pandas as pd

df=pd.read_csv('ElectricCarData_Clean.csv')

""" Calculate and compare the average Range, Top Speed, and Efficiency for each PowerTrain type (AWD,
RWD, FWD). """

stats=df.groupby('PowerTrain')[['Range_Km','TopSpeed_KmH','Efficiency_WhKm']].mean().reset_index()
stats = stats.rename(columns={
    'Range_Km'       : 'Avg_Range',
    'TopSpeed_KmH'   : 'Avg_TopSpeed',
    'Efficiency_WhKm': 'Avg_Efficiency'
})

print(stats.round(2))


""" output:   
PowerTrain  Avg_Range  Avg_TopSpeed  Avg_Efficiency
                                         
AWD            426.46        216.90          206.76
FWD            268.24        148.76          175.57
RWD            299.40        162.40          180.44 """

print("-------------------------------------------")

# Find the average price for each BodyStyle (SUV, Hatchback, Sedan, etc.).
stats=df.groupby('BodyStyle')['PriceEuro'].mean().round(2).reset_index()
stats=stats.rename(columns={"PriceEuro":"AvgPrice"})
print(stats)

""" output:
BodyStyle   AvgPrice
0     Cabrio   92488.33
1  Hatchback   34893.16
2   Liftback   83375.80
3        MPV   41906.00
4     Pickup   58333.33
5        SPV   47292.33
6        SUV   53982.53
7      Sedan   99966.90
8    Station  150000.00 """

print("-------------------------------------------")
#Compare the average price of cars that have RapidCharge capability versus those that do not.

stats=df.groupby('RapidCharge')['PriceEuro'].mean().round(2).reset_index()
stats=stats.rename(columns={"PriceEuro":"AvgPrice"})
print(stats)

""" output:
  RapidCharge  AvgPrice
0          No  26154.40
1         Yes  57324.68 """


print("-------------------------------------------")
""" Analyze the relationship between a car's acceleration and its top speed. Does a faster 0-100 time usually
mean a higher top speed? """


correlation=df['AccelSec'].corr(df['TopSpeed_KmH']).round(1)
print(f"Correlation: {correlation}")
print("Conclusion: YES! Faster acceleration = Higher Top Speed!")
print(f"Strong negative correlation of {correlation} proves this!")

""" output:Correlation: -0.8
Conclusion: YES! Faster acceleration = Higher Top Speed!
Strong negative correlation of -0.8 proves this! """