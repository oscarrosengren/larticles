def sort_csv_by_article_number(file, article_numbers):
    # Ensure the uploaded file is read as a file-like object
    try:
        df = pd.read_csv(file, encoding="utf-16", delimiter="\t", dtype={"Article number": str})
    except Exception as e:
        st.error(f"Error reading CSV file: {e}")
        return pd.DataFrame()  # Return an empty dataframe in case of error

    # Ensure 'Article number' exists
    if "Article number" not in df.columns:
        st.error("The CSV file does not contain the 'Article number' column.")
        return pd.DataFrame()

    # Process input article numbers as strings
    article_numbers = [num.strip() for num in article_numbers.split(",")]

    # Filter and sort data
    df_filtered = df[df["Article number"].isin(article_numbers)].copy()
    df_sorted = df_filtered.sort_values(by="Article number")

    # Reorder columns if 'Stock' is present
    if "Stock" in df_sorted.columns:
        columns = ["Article number", "Stock"] + [col for col in df_sorted.columns if col not in ["Article number", "Stock"]]
        df_sorted = df_sorted[columns]

    return df_sorted
