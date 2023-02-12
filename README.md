# Extract Transactions from Coverflex to CSV
A python script to extract transactions data from Coverflex and save it as a CSV file. This guide is designed to help beginners who are new to Python.

## Requirements
- Python 3.6 or higher
- Google Chrome browser (Tested with version 110.0.5481.78)
- Chromedriver that matches your Google Chrome browser version
- The following Python libraries:
  - selenium
  - csv
  - datetime
  - time
  - json

## How to Download the Repository
- Click the green "Clone or download" button on the right side of the repository page.
- Choose "Download ZIP".
- Extract the contents of the downloaded .zip file.
- Open the terminal or command prompt and navigate to the directory where you extracted the files.

## How to Install Required Libraries
1. Make sure you have Python 3 installed. If you don't, you can download it from the official Python website (https://www.python.org/downloads/)
2. Open the terminal or command prompt and navigate to the directory where you extracted the files.
3. Type `pip install -r requirements.txt` and press enter.

## How to Set Up Chromedriver
1. Download the Chromedriver executable that matches your Google Chrome browser version from the Chromedriver downloads page (https://sites.google.com/chromium.org/driver/downloads).
2. Copy the downloaded chromedriver.exe file.
3. Paste the chromedriver.exe file into the C:\Windows folder.

## How to Input Your Credentials
1. Open the credentials.txt file in a text editor.
2. Replace "email": "john@gmail.com" with your Coverflex email address and "password": "1234" with your Coverflex password.
3. Save and close the credentials.txt file.

## How to Run the Script
1. Open the terminal or command prompt and navigate to the directory where you extracted the files.
2. Type `python scrapper.py` and press enter.
3. The script will open a new Chrome window, log into Coverflex, extract your transactions, and save them to a .csv file in the Downloads directory.

## Troubleshooting
1. Make sure that you are using the correct version of Chromedriver for your Google Chrome browser.
2. If the script throws an error about not being able to find the Chromedriver executable, make sure that the chromedriver.exe file is in the C:\Windows folder.
