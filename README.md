# Hong Kong Holiday Scraper

This Python script scrapes holiday data for a specified year from the Hong Kong government website and saves it into an Excel file.

## Description

The script fetches holiday information from the URL `https://www.gov.hk/en/about/abouthk/holiday/{year}.htm`, where `{year}` is the year provided as a command-line argument. It extracts the holiday names, dates, and days of the week from the table on the webpage and saves this data into an Excel file named `HK Holiday {year}.xlsx`.

## Usage

To run the script, use the following command:

```bash
python main.py <year>
```

Replace `<year>` with the four-digit year for which you want to retrieve the holiday data (e.g., `2025`).

### Example

```bash
python main.py 2025
```

This will generate an Excel file named `HK Holiday 2025.xlsx` containing the holiday data for the year 2025.

## Requirements

The script requires the following Python libraries:

- `requests`: To fetch the webpage content.
- `beautifulsoup4`: To parse the HTML content.
- `pandas`: To handle and save the data in Excel format.

You can install these libraries using pip:

```bash
pip install requests beautifulsoup4 pandas
```

Additionally, the script uses the standard libraries `datetime` and `sys`, which are included with Python.

## Output

The script generates an Excel file named `HK Holiday {year}.xlsx`, where `{year}` is the provided year. The Excel file contains a single sheet named after the year, with the following columns:

- **Holiday Name**: The name of the holiday.
- **Date**: The date of the holiday in `YYYY-MM-DD` format, if available. For holidays without a specific date (e.g., "Every Sunday"), this field may be blank or contain the original text.
- **Day of the Week**: The day of the week for the holiday.

## Notes

- The script expects the year to be a four-digit number. If an invalid year is provided, it will print an error message and exit.
- The script relies on the structure of the webpage. If the website changes its layout or the table structure, the script may fail to extract the data correctly.
- The date parsing assumes the date format on the website is "d %B" (e.g., "1 January"). If the format changes, the parsing may fail, and the original date string will be kept.
