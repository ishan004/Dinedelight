import csv
import requests
from bs4 import BeautifulSoup


# Function to search for the location of a postal code
def search_location(postal_code):
    try:
        # Define the search query
        search_query = f"Postal code {postal_code} location"

        # Send a GET request to Google
        google_url = f"https://www.google.com/search?q={search_query}"
        response = requests.get(google_url)

        # Check if the request was successful
        if response.status_code == 200:
            # Parse the HTML content of the page using BeautifulSoup
            soup = BeautifulSoup(response.text, "html.parser")

            # Extract the location information (the first search result)
            search_result = soup.find("div", class_="BNeawe iBp4i AP7Wnd")
            if search_result:
                location = search_result.text
                return location
            else:
                return "Location not found"

        else:
            return "Failed to retrieve search results"

    except Exception as e:
        return f"Error: {str(e)}"


# CSV file containing postal codes
csv_file = "chitwan.csv"  # Replace with your CSV file containing the postal codes

# Create a new CSV file to store postal codes and their corresponding locations
output_csv_file = "postal_codes_with_locations.csv"

# Open the CSV files for reading and writing
with open(csv_file, "r", newline="") as input_file, open(
    output_csv_file, "w", newline=""
) as output_file:
    reader = csv.DictReader(input_file)
    fieldnames = reader.fieldnames + ["location"]  # Add a new column for Location
    writer = csv.DictWriter(output_file, fieldnames=fieldnames)
    writer.writeheader()

    for row in reader:
        postal_code = row.get(
            "location"
        )  # Make sure this column name matches the one in your CSV
        if postal_code:
            location = search_location(postal_code)
            row["location"] = location
            writer.writerow(row)
            print(f"Processed: Postal Code {postal_code} - Location: {location}")

print("Postal code location search completed.")
