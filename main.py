# ----------------------------------------
# Created on 4th Apr 2021
# By the Cached Coder
# ----------------------------------------
'''
This script handles all the integrations
between all libraries
'''
# ----------------------------------------
import getPosts as reddit
import readSheet as gs
import sendMails as email
# ----------------------------------------


if __name__ == '__main__':
    # Reddit Stuff
    print("Reddit Login and body generation")
    bot = reddit.redditLogin()
    data = reddit.getPosts(bot)
    body = reddit.generateEmail(data)

    # Spreadsheets stuff
    print("Body generated, reading spreadsheet")
    emails, names, sendMail = gs.getAllResponses()

    # Email Stuff
    print("Spreadsheet read, sending emails")
    email.parseData(names, emails, sendMail, body)

    print('fin')
