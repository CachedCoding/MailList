# ----------------------------------------
# Created on 3rd Apr 2021
# By the Cached Coder
# ----------------------------------------
'''
This script defines the function required
to get a the email ids to send the mail to
from the GForms' responses.

Functions:
    getAllResponses():
        No Inputs
        Returns emails, names and list of whether
        they wish to recieve the mail or not
'''
# ----------------------------------------
import gspread
import json
# ----------------------------------------


# Function to open sheet and get all responses
def getAllResponses():
    # Gets secrets
    with open('secrets.json', 'r') as fh:
        secrets = json.load(fh)

    # Load spreadsheet
    gc = gspread.service_account(filename='secrets.json')
    sh = gc.open_by_key(secrets['key'])

    # Get all entries
    worksheet = sh.sheet1
    emails = worksheet.col_values(2)[1:]
    names = worksheet.col_values(3)[1:]
    sendMail = worksheet.col_values(4)[1:]

    # Turn sendMail from strings to bools
    sendMail = [True if i == 'Yes' else False for i in sendMail]

    # Return email and names
    return emails, names, sendMail


if __name__ == '__main__':
    emails, names, sendMail = getAllResponses()
    print(emails)
    print(names)
    print(sendMail)
