import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import geopandas as gpd
import plotly.express as px
from numpy import array
import plotly.graph_objects as go
from plotly.subplots import make_subplots

data = pd.read_csv("WBL_1971-2023_.csv")
data.head()
data.info()

data["MOBILITY"].describe()

data_2023 = data[data["Report Year"]==2023]

data_2023.plot()

data_2023.columns

x = data_2023['MOBILITY'].tolist()
x.sort()

plt.plot(x)
plt.show()

y = data['MOBILITY'].tolist()
y.sort()

df = pd.DataFrame(data)

geometry = gpd.points_from_xy(df.MOBILITY, df.PENSION)

gdf = gpd.GeoDataFrame(df, geometry=geometry)
ax = gdf.plot(column='MOBILITY', cmap='cool', legend=True)

ax.set_axis_off()
plt.show()

px.bar(data_2023,x ='Economy',y="WBL INDEX")

data_region_2023 = data_2023.groupby("Region")[["Economy"]].count().reset_index().rename(columns={'Economy':"Country"})

data_region_income =  data_2023.groupby(['Region',"Income Group"])[['Report Year']].count().reset_index().rename(columns={'Report Year':"Country"})

px.bar(data_region_income, x="Region",y="Country", color="Income Group")

data_income_2023 =  data_2023.groupby('Income Group')[['Economy']].count().reset_index().rename(columns={'Economy':"Country"})

plt.figure(figsize=(10,4))
sns.barplot(data=data_income_2023,x ='Income Group',y="Country" )

px.bar(data_income_2023,x ='Income Group',y="Country")

data_2023.describe().T

data_turkey=data[data['Economy']=="Türkiye"]

data_2= data_turkey.T

px.line(data_turkey,x ='Report Year',y="WBL INDEX" )

fig = make_subplots (rows=5, cols=1,
    subplot_titles=("Is the law free of legal provisions that require a married woman to obey her husband?", "Can a woman be head of household in the same way as a man?", "Is there legislation specifically addressing domestic violence?", "Can a woman obtain a judgment of divorce in the same way as a man?", "Does a woman have the same rights to remarry as a man?"))
fig.append_trace(go.Line(x=data_turkey["Report Year"], y=data_turkey["Is the law free of legal provisions that require a married woman to obey her husband?"]), row=1, col=1)
fig.append_trace(go.Line(x=data_turkey["Report Year"], y=data_turkey["Can a woman be head of household in the same way as a man?"]), row=2, col=1)
fig.append_trace(go.Line(x=data_turkey["Report Year"], y=data_turkey["Is there legislation specifically addressing domestic violence?"]), row=3, col=1)
fig.append_trace(go.Line(x=data_turkey["Report Year"], y=data_turkey["Can a woman obtain a judgment of divorce in the same way as a man?"]), row=4, col=1)
fig.append_trace(go.Line(x=data_turkey["Report Year"], y=data_turkey["Does a woman have the same rights to remarry as a man?"]), row=5, col=1)
fig.update_layout(height=800, width=800,
                  title_text="Marriage",
                  legend_tracegroupgap=500)

fig.show()

turkey_marriage=px.line(data_turkey, x = ("Report Year"), y = ("MARRIAGE"), color = "Economy", height=200, width=800)

fig = make_subplots (rows=4, cols=1,
    subplot_titles=("Can a woman choose where to live in the same way as a man?", "Can a woman travel outside her home in the same way as a man?", "Can a woman apply for a passport in the same way as a man?", "Can a woman travel outside the country in the same way as a man?"))
fig.append_trace(go.Line(x=data_turkey["Report Year"], y=data_turkey["Can a woman choose where to live in the same way as a man?"]), row=1, col=1)
fig.append_trace(go.Line(x=data_turkey["Report Year"], y=data_turkey["Can a woman travel outside her home in the same way as a man?"]), row=2, col=1)
fig.append_trace(go.Line(x=data_turkey["Report Year"], y=data_turkey["Can a woman apply for a passport in the same way as a man?"]), row=3, col=1)
fig.append_trace(go.Line(x=data_turkey["Report Year"], y=data_turkey["Can a woman travel outside the country in the same way as a man?"]), row=4, col=1)
fig.update_layout(height=800, width=800,
                  title_text="MOBILITY",
                  legend_tracegroupgap=500)

turkey_mobility=px.line(data_turkey, x = ("Report Year"), y = ("MOBILITY"), color = "Economy", height=200, width=800)

fig = make_subplots (rows=4, cols=1,
    subplot_titles=("Can a woman get a job in the same way as a man?", "Does the law prohibit discrimination in employment based on gender?", "Is there legislation on sexual harassment in employment?", "Are there criminal penalties or civil remedies for sexual harassment in employment?"))
fig.append_trace(go.Line(x=data_turkey["Report Year"], y=data_turkey["Can a woman get a job in the same way as a man?"]), row=1, col=1)
fig.append_trace(go.Line(x=data_turkey["Report Year"], y=data_turkey["Does the law prohibit discrimination in employment based on gender?"]), row=2, col=1)
fig.append_trace(go.Line(x=data_turkey["Report Year"], y=data_turkey["Is there legislation on sexual harassment in employment?"]), row=3, col=1)
fig.append_trace(go.Line(x=data_turkey["Report Year"], y=data_turkey["Are there criminal penalties or civil remedies for sexual harassment in employment?"]), row=4, col=1)
fig.update_layout(height=800, width=800,
                  title_text="WORKPLACE",
                  legend_tracegroupgap=500)

turkey_workplace=px.line(data_turkey, x = ("Report Year"), y = ("WORKPLACE"), color = "Economy", height=200, width=800)

fig = make_subplots (rows=4, cols=1,
    subplot_titles=("Does the law mandate equal remuneration for work of equal value?", "Can a woman work at night in the same way as a man?", "Can a woman work in a job deemed dangerous in the same way as a man?", "Can a woman work in an industrial job in the same way as a man?"))
fig.append_trace(go.Line(x=data_turkey["Report Year"], y=data_turkey["Does the law mandate equal remuneration for work of equal value?"]), row=1, col=1)
fig.append_trace(go.Line(x=data_turkey["Report Year"], y=data_turkey["Can a woman work at night in the same way as a man?"]), row=2, col=1)
fig.append_trace(go.Line(x=data_turkey["Report Year"], y=data_turkey["Can a woman work in a job deemed dangerous in the same way as a man?"]), row=3, col=1)
fig.append_trace(go.Line(x=data_turkey["Report Year"], y=data_turkey["Can a woman work in an industrial job in the same way as a man?"]), row=4, col=1)
fig.update_layout(height=800, width=800,
                  title_text="PAY",
                  legend_tracegroupgap=500)

turkey_pay=px.line(data_turkey, x = ("Report Year"), y = ("PAY"), color = "Economy", height=200, width=800)

data_2= data_turkey.T

fig = make_subplots (rows=10, cols=1,
    subplot_titles=("Is paid leave of at least 14 weeks available to mothers?", "Length of paid maternity leave", "Does the government administer 100% of maternity leave benefits?", "Is there paid leave available to fathers?", "Length of paid paternity leave", "Is there paid parental leave?", "Shared days", "Days for the mother", "Days for the father", "Is dismissal of pregnant workers prohibited?"))
fig.append_trace(go.Line(x=data_turkey["Report Year"], y=data_turkey["Is paid leave of at least 14 weeks available to mothers?"]), row=1, col=1)
fig.append_trace(go.Line(x=data_turkey["Report Year"], y=data_turkey["Length of paid maternity leave"]), row=2, col=1)
fig.append_trace(go.Line(x=data_turkey["Report Year"], y=data_turkey["Does the government administer 100% of maternity leave benefits?"]), row=3, col=1)
fig.append_trace(go.Line(x=data_turkey["Report Year"], y=data_turkey["Is there paid leave available to fathers?"]), row=4, col=1)
fig.append_trace(go.Line(x=data_turkey["Report Year"], y=data_turkey["Length of paid paternity leave"]), row=5, col=1)
fig.append_trace(go.Line(x=data_turkey["Report Year"], y=data_turkey["Is there paid parental leave?"]), row=6, col=1)
fig.append_trace(go.Line(x=data_turkey["Report Year"], y=data_turkey["Shared days"]), row=7, col=1)
fig.append_trace(go.Line(x=data_turkey["Report Year"], y=data_turkey["Days for the mother"]), row=8, col=1)
fig.append_trace(go.Line(x=data_turkey["Report Year"], y=data_turkey["Days for the father"]), row=9, col=1)
fig.append_trace(go.Line(x=data_turkey["Report Year"], y=data_turkey["Is dismissal of pregnant workers prohibited?"]), row=10, col=1)
fig.update_layout(height=1200, width=800,
                  title_text="PARENTHOOD",
                  legend_tracegroupgap=500)

turkey_parenthood=px.line(data_turkey, x = ("Report Year"), y = ("PARENTHOOD"), color = "Economy", height=200, width=800)

data_germany=data[data['Economy']=="Germany"]

germany_2=px.line(data_germany, x = ("Report Year"), y = ("WBL INDEX"), color = "Economy")

fig = go.Figure()
fig.add_trace(go.Bar(x=data_turkey["Report Year"], y=data_turkey["WBL INDEX"]))
fig.add_trace(go.Bar(x=data_germany["Report Year"], y=data_germany["WBL INDEX"]))
fig.update_layout(barmode='group', xaxis_tickangle=0)
fig.show()

fig1 = px.line(data_turkey, x="Report Year", y="WBL INDEX", color="Economy")
fig1.show()
fig2 = px.line(data_germany, x="Report Year", y="WBL INDEX", color="Economy")
fig2.update_layout(barmode="group")
fig2.show()
