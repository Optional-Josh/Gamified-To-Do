import pandas as pd

# function that converts list of dictionary to dataframe
def convert_dataframe(data):
    df = pd.DataFrame(data)
    return df

# function that formats dataframe content and inserted into a txt file
# separates header row from value row
# also takes into account the formatting with the use of different functions in python
def dataframe_txt_styled(dataframe, profile):

    column_widths = {col: max(len(str(val)) for val in [col] + dataframe[col].tolist()) for col in dataframe.columns}

    border = "+" + "+".join("-" * (column_widths[col] + 2) for col in dataframe.columns) + "+"

    header = "| " + " | ".join(col.ljust(column_widths[col]) for col in dataframe.columns) + " |"

    rows = []
    for _, row in dataframe.iterrows():
        row_line = "| " + " | ".join(str(row[col]).ljust(column_widths[col]) for col in dataframe.columns) + " |"
        rows.append(row_line)

    table = border + "\n" + header + "\n" + border + "\n" + "\n".join(rows) + "\n" + border

    with open(f"{profile}.txt", "w") as file:
        file.write(table)

    return table