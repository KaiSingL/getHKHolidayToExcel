import requests
from bs4 import BeautifulSoup
from datetime import datetime
import pandas as pd
import sys

# Check for correct command-line argument
if len(sys.argv) != 2:
    print("Usage: python script.py <year>")
    sys.exit(1)

year = sys.argv[1]

# Validate that the year is a four-digit number
if not (year.isdigit() and len(year) == 4):
    print("Error: Year must be a four-digit number.")
    sys.exit(1)

# Construct the URL with the provided year
url = f"https://www.gov.hk/en/about/abouthk/holiday/{year}.htm"

try:
    # Fetch the webpage content
    response = requests.get(url)
    response.raise_for_status()
except requests.exceptions.RequestException as e:
    print(f"Error fetching the URL: {e}")
    sys.exit(1)

# Parse the HTML content
soup = BeautifulSoup(response.content, 'html.parser')

# Find the holiday table
table = soup.find('table')
if table is None:
    print("Error: No table found on the page.")
    sys.exit(1)

# Extract data from the table, skipping header rows
data = []
for row in table.find_all('tr'):
    cells = row.find_all('td')
    if len(cells) == 3:
        holiday_name = cells[0].text.strip()
        date_str = cells[1].text.strip()
        day_of_week = cells[2].text.strip()
        
        # Parse and format the date if present
        if date_str:
            try:
                date_obj = datetime.strptime(date_str + " " + year, "%d %B %Y")
                formatted_date = date_obj.strftime("%Y-%m-%d")
            except ValueError:
                formatted_date = date_str  # Keep original string if parsing fails
        else:
            formatted_date = ""  # Leave blank for non-specific dates like "Every Sunday"
        
        # Add the row to the data list
        data.append([holiday_name, formatted_date, day_of_week])

# Check if any data was extracted
if not data:
    print("Error: No data extracted from the table.")
    sys.exit(1)

# Create a DataFrame with the extracted data
df = pd.DataFrame(data, columns=['Holiday Name', 'Date', 'Day of the Week'])

# Define the Excel filename and save the DataFrame
excel_filename = f"HK Holiday {year}.xlsx"
df.to_excel(excel_filename, sheet_name=year, index=False)

print(f"Data saved to {excel_filename}")