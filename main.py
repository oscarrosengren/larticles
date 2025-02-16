import pandas as pd
import streamlit as st


def sort_and_filter_articles(input_file, article_numbers):
    # Load the CSV file with UTF-16 encoding and tab delimiter
    df = pd.read_csv(input_file, encoding="UTF-16", delimiter="\t")

    # Convert 'Article number' to numeric for proper sorting
    df["Article number"] = pd.to_numeric(df["Article number"], errors="coerce")

    # Filter the dataframe by the given article numbers
    filtered_df = df[df["Article number"].isin(article_numbers)]

    # Sort the filtered dataframe by 'Article number'
    df_sorted = filtered_df.sort_values(by="Article number")

    return df_sorted


def main():
    st.title("Article Number Filter & Sort")

    input_csv = "export-articles.csv"  # Replace with actual file path

    # User input for article numbers
    user_input = st.text_input("Enter article numbers (comma-separated):")

    if user_input:
        try:
            article_numbers = list(map(int, user_input.split(',')))
            sorted_df = sort_and_filter_articles(input_csv, article_numbers)
            st.write("### Sorted Articles:")
            st.dataframe(sorted_df)
        except ValueError:
            st.error(
                "Invalid input! Please enter a valid list of numeric article numbers.")


if __name__ == "__main__":
    main()
