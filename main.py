import streamlit as st
import pandas as pd


def sort_csv_by_article_number(file, article_numbers):
    # Load the CSV file with UTF-16 encoding and tab delimiter
    df = pd.read_csv(file, encoding="UTF-16", delimiter="\t")

    # Convert 'Article number' to numeric for proper sorting
    df["Article number"] = pd.to_numeric(df["Article number"], errors="coerce")

    # Filter the dataframe by the provided article numbers
    article_numbers = [int(num.strip()) for num in article_numbers.split(
        ",") if num.strip().isdigit()]
    df_filtered = df[df["Article number"].isin(article_numbers)]

    # Sort the dataframe by 'Article number'
    df_sorted = df_filtered.sort_values(by="Article number")

    return df_sorted


def main():
    st.title("Article Number Sorter")

    uploaded_file = st.file_uploader("Upload CSV file", type=["csv"])
    article_numbers = st.text_area("Enter article numbers (comma-separated)")

    if uploaded_file and article_numbers:
        sorted_df = sort_csv_by_article_number(uploaded_file, article_numbers)
        st.write("### Sorted Articles Table")
        st.dataframe(sorted_df)


if __name__ == "__main__":
    main()
