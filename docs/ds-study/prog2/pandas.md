# Pandas

!!! info

    Pandas is a Python library for data analysis and manipulation. It provides data structures and functions to work with structured data like CSV files, Excel sheets or SQL tables.

## Load & Save Data

```python
import pandas as pd

# Load data
df = pd.read_csv("data.csv", sep=";", encoding="utf-8")
df = pd.read_excel("data.xlsx", sheet_name="Sheet1", engine="openpyxl")

# Save data
df.to_csv("data.csv", sep=";", encoding="utf-8", index=False)
```

**Note:**

-   `sep` is the separator used in the CSV file (default is `,`)
-   `encoding` is the encoding used in the CSV file (default is `utf-8`)
    -   `utf-8`
    -   `latin-1`
    -   see [here](https://docs.python.org/3/library/codecs.html#standard-encodings) for a list of all encodings

Web

```python
import pandas as pd

url = "https://example.com/data.csv"
df = pd.read_csv(url, sep=";", encoding="utf-8")
```

SQL

```python
import pandas as pd
import sqlite3

conn = sqlite3.connect("data.db")
df = pd.read_sql_query("SELECT * FROM data", conn)
```

## Column Operations

Select Columns

```python
df2 = df[["column1", "column2"]]
```

Drop Columns

```python
df = df.drop(columns=["column1", "column2"])
```

Rename Column

```python
df = df.rename(columns={"old": "new"})
```

Apply to Column

```python
df["column"] = df["column"].apply(lambda x: x + 1)
```

Add Columns

```python
df["new"] = df["column1"] + df["column2"]
```

Remove Duplicates

```python
df = df.drop_duplicates(subset="column")
```

## Row Operations

Filter Rows

```python
df = df[df["column"] > 10]
```

Group Rows

```python
df = df.groupby("column").sum()
```

Sort Rows

```python
df = df.sort_values("column", ascending=False)
```

Select Rows and Columns

```python
df = df.loc[df["column"] > 10, ["column1", "column2"]]
```

Iterate over Rows

```python
for index, row in df.iterrows():
    print(index, row["column1"], row["column2"])
```
