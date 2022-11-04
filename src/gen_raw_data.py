import pandas as pd
from numpy import random
from datetime import date, timedelta

group_data = pd.DataFrame({"group": ["A", "B", "C", "D", "E"] * 5})
start_date = date(2016,1,1)
end_date = date(2017,1,1)

file_dates = [x.strftime("%Y%m%d") for x in pd.date_range(start_date, end_date)]

for file_date in file_dates:
    group_data["value"] = random.randint(0, 10, group_data.shape[0])
    group_data.to_csv(f"./data/raw/events_{file_date}.csv", index=False)
