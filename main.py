import requests
from bs4 import BeautifulSoup
import pandas as pd



def scrape_flu_vaccination_data(url):
    try:
        # Send a GET request to the URL
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses

        # Parse the HTML content of the page
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find the first table - adjust this as needed for the specific data table
        table = soup.find('table')

        if table:
            # Convert the HTML table to a DataFrame
            df = pd.read_html(str(table))[0]
            return df
        else:
            print("No table found on the webpage.")
            return pd.DataFrame()
    except requests.RequestException as e:
        print(f"Request failed: {e}")
        return pd.DataFrame()


def clean_data(df):
    # Example cleaning function - adjust based on the structure of your data
    if not df.empty:
        # Perform data cleaning steps here, such as renaming columns, handling missing data, etc.
        cleaned_df = df.rename(columns=lambda x: x.strip()).dropna()
        return cleaned_df
    else:
        return df


if __name__ == "__main__":
    # Placeholder URL - replace with the actual URL you intend to scrape
    url = 'https://www.cdc.gov/flu/fluvaxview/coverage-2021estimates.htm'
    flu_data = scrape_flu_vaccination_data(url)

    if not flu_data.empty:
        cleaned_flu_data = clean_data(flu_data)
        print("Flu vaccination data scraped and cleaned successfully.")
        print(cleaned_flu_data.head())
    else:
        print("No data scraped.")
