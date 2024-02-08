import requests
from bs4 import BeautifulSoup
import re
import json

from fastapi import FastAPI
from fastapi.responses import JSONResponse

def get_pnr_status(pnr):
    # Specify the URL of the website
    url = f"https://www.confirmtkt.com/pnr-status/{pnr}"

    # Send an HTTP request to the URL
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find all script tags with type="text/javascript"
        script_tags = soup.find_all('script', {'type': 'text/javascript'})

        # Iterate through script tags
        for script_tag in script_tags:
            # Extract the text inside the script tag
            script_text = script_tag.text

            # Define a regular expression pattern to match the desired data structure
            pattern = r'data\s*=\s*({.*?;)'

            # Search for the pattern in the script text
            match = re.search(pattern, script_text, re.DOTALL)

            # Check if a match is found
            if match:
                # Extract the JSON data
                json_data = match.group(1)
                json_data=json_data.replace(';', '')

                
                try:
                    # Load the JSON string to get a Python object
                    parsed_data = json.loads(json_data)

                    return parsed_data
                except json.JSONDecodeError as e:
                    print("JSON decoding error:", e)
                    return None
        else:
            print("No JSON data found on the webpage.")
    else:
        print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
        return None
log = get_pnr_status(4361365838)
print(log)
app = FastAPI()
@app.get("/status")
async def prn_status(pnr: str):
    prn_json = get_pnr_status(pnr)
    return prn_json
