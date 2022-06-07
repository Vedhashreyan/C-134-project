import pandas as pd
import csv

rows = []

with open("data.csv", "r") as f:
  csvreader = csv.reader(f)
  for row in csvreader: 
    rows.append(row)

headers = rows[0]
star_data_rows = rows[1:]
print(headers)
print(star_data_rows[0])

names = []
dist = []
radius = []
mass = []
gravity = []
final_list = []

for star_data in star_data_rows:
    if float(star_data[2])<100:
        if float(star_data[5])>150 and float(star_data[5])<300:
            final_list.append(star_data)

for i in final_list:
    names.append(i[1])
    dist.append(i[2])
    mass.append(i[3])
    radius.append(i[4])
    gravity.append(i[5])
df = pd.DataFrame(
    list(zip(names, dist, mass, radius, gravity)),
    columns=["Star Name", "Distance", "Mass", "Radius", "Gravity"],
)
print(df)

df.to_csv('Final.csv')