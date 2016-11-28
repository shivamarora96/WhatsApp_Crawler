# Shivam Arora
# Date : 28/11/16


# import requests
from bs4 import BeautifulSoup


# This function  would concatenate the contacts

def Joincontacts(contact):
    finalContact = ''
    refactoredContact = contact.split()
    for r in refactoredContact:
        finalContact = finalContact + r

    return finalContact


# Main Crawler Function

def Whatsapp_crawler(code):
    no_of_contacts = 0
    contact_file = open('Contacts_WhatsApp.txt', 'w')

    # response = requests.get(url)
    # code = response.text
    soup = BeautifulSoup(code, 'html.parser')

    for span in soup.find_all('span', {'class': 'emojitext ellipsify'}):
        title = span.get('title')

        if title is not None:
            no_of_contacts += 1

            if title[0] is '+':
                title = Joincontacts(title)

            print(title)
            contact_file.write(str(title))
            contact_file.write('\n\n')

    contact_file.write('\n\n\n\n\n TOTAL CONTACTS FOUND :: ' + str(no_of_contacts))
    contact_file.close()
    return no_of_contacts


# Copy the div element from (WhatsApp_Web -- > Inspect_Element) having class infinite-list around line_number "10"

x = ''' '''

NoContacts = Whatsapp_crawler(x)
print('\n\n Total Contacts :: ', NoContacts)
