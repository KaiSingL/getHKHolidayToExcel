import requests
from bs4 import BeautifulSoup
from datetime import datetime
import pandas as pd

# URL of the webpage containing the holiday table
url = "https://www.gov.hk/en/about/abouthk/holiday/2025.htm"

# Fetch the HTML content
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Find the table containing the holiday data
table = soup.find('table')

# Initialize a list to store the extracted data
data = []

# Extract each row from the table
for row in table.find_all('tr'):
    cells = row.find_all(['td', 'th'])
    if len(cells) == 3:
        holiday_name = cells[0].text.strip()
        date_str = cells[1].text.strip()
        day_of_week = cells[2].text.strip()
        
        # Process the date: convert to yyyy-MM-dd if it's a specific date
        if date_str:
            try:
                date_obj = datetime.strptime(date_str + " 2025", "%d %B %Y")
                formatted_date = date_obj.strftime("%Y-%m-%d")
            except ValueError:
                formatted_date = date_str  # Keep original if parsing fails
        else:
            formatted_date = ""  # Leave blank if no specific date
        
        # Append the row data
        data.append([holiday_name, formatted_date, day_of_week])

# Create a DataFrame
df = pd.DataFrame(data, columns=['Holiday Name', 'Date', 'Day of the Week'])

# Save to Excel file
df.to_excel('HK holiday.xlsx', index=False)