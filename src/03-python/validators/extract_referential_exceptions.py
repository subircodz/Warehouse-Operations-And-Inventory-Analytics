from pandas import DataFrame


def extract_referential_exceptions(
    workbook: dict[str, DataFrame],
    referential_result
) -> DataFrame:
    """
    Extracts records that contain invalid referential
    identifiers from the workbook.

    Args:
        workbook:
            Dictionary containing worksheet names
            and their corresponding DataFrames.

        referential_result:
            Result returned by the referential integrity
            validator.

    Returns:
        DataFrame:
            DataFrame containing all invalid referential
            records.
    """

    exceptions = []

    for relationship, result in referential_result.data.items():

        if result["invalid"] == 0:
            continue

        child_worksheet, relationship_part = relationship.split(".", 1)
        child_column = relationship_part.split(" -> ")[0]

        dataframe = workbook[child_worksheet]

        for row_number in result["invalid_row_list"]:

            dataframe_index = row_number - 2

            row = dataframe.iloc[dataframe_index].copy()

            exceptions.append({
                "worksheet": child_worksheet,
                "row_number": row_number,
                "column": child_column,
                "invalid_value": row[child_column]
            })

    return DataFrame(exceptions)