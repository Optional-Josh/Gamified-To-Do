import pandas as pd

# function that converts list of dictionary to dataframe
def convert_dataframe(data):
    df = pd.DataFrame(data)
    return df