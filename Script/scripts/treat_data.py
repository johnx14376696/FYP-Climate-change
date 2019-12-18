import pandas as pd
import csv

global_data = pd.read_csv("../data_raw/GlobalTemperatures.csv")

global_data = global_data.values
global_data_squashed = []

running_total = 0

for i in range(0, global_data.shape[0]):
    running_total = running_total + global_data[i][1]
    if i % 12 == 0:
        global_data_squashed.append((global_data[i][0], running_total / 12))
        running_total = 0

print(global_data_squashed)

with open('global_temperate_treated.csv', mode='w') as f:
    writer = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for row in global_data_squashed:
        writer.writerow(row)