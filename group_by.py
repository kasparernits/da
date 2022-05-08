import pandas as pd

print("hello")

dtypes = {
    "first_name": "category",
    "gender": "category",
    "type": "category",
    "state": "category",
    "party": "category",
}
df = pd.read_csv(
    "/Users/kasparernits/datasets/groupby-data/legislators-historical.csv",
    dtype=dtypes,
    usecols=list(dtypes) + ["birthday", "last_name"],
    parse_dates=["birthday"]
)

n_by_state = df.groupby("state")["last_name"].count()

print(n_by_state.head(10))



