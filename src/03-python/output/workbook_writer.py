import pandas as pd

# Save cleaned workbook

def save_workbook(workbook, filename):
    with pd.ExcelWriter(filename) as writer:
        for worksheet, dataframe in workbook.items():
            dataframe.to_excel(writer, sheet_name=worksheet, index=False)