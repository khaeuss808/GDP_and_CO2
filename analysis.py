import pandas as pd
import seaborn.objects as so
import matplotlib.pyplot as plt
from matplotlib import style

url = "https://media.githubusercontent.com/media/nickeubank/MIDS_Data/master/World_Development_Indicators/wdi_small_tidy_2015.csv"
try:
    df = pd.read_csv(url)
except Exception as e:
    print(f"Error loading data: {e}")
    exit()

columns = [
    "Mortality rate, infant (per 1,000 live births)",
    "GDP per capita (constant 2010 US$)",
    "Country Name",
]
df = df[columns].dropna() 

print(df.head())

gdp_mortality_chart = (
    so.Plot(df, x="GDP per capita (constant 2010 US$)", y="Mortality rate, infant (per 1,000 live births)")
    .add(so.Line(), so.PolyFit(order=2))  
    .add(so.Dot()) 
    .label(title="GDP and Infant Mortality Rate",
           x="GDP per capita (constant 2010 US$)",
           y="Mortality Rate (per 1,000 live births)")
    .theme({**style.library["seaborn-v0_8-whitegrid"]})  
)

gdp_mortality_chart.show()

plt.show()
