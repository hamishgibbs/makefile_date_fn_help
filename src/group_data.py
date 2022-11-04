import sys
import pandas as pd

in_data = pd.read_csv(sys.argv[1])

grouped = in_data.groupby('group').agg(mean = ("value", "mean"))

grouped.reset_index().to_csv(sys.argv[-1], index=False)
