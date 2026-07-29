def worksheet_discovery(workbook):
    return {
    "worksheet_names": list(workbook.keys()),
    "worksheet_count": len(workbook.keys())
}