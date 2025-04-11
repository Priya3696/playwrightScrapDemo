from playwright.sync_api import sync_playwright
from datetime import datetime
import json

def main():
    with open('data.json', 'r') as file:
        data = json.load(file)
    
    print(data)

    with sync_playwright() as p:
        # Launch a browser (Chromium in this case)
        browser = p.chromium.launch(headless=False)  # Set headless=True to run without UI
        context = browser.new_context()
        
        # Open a new page
        page = context.new_page()
        
        # Navigate to a website
        page.goto("https://evisa.gov.vn/e-visa/foreigners")
        
        # Wait for a few seconds to observe the page
        page.wait_for_timeout(5000)
        page.get_by_role('checkbox', name='Confirm compliance with').click()
        page.get_by_role('checkbox', name='Confirmation of reading').click()
        page.get_by_role('button', name='Next').click()
        page.wait_for_load_state("networkidle")
        page.locator('input[placeholder="Enter middle and given name"]').fill(data['givenName'])
        page.locator('input[placeholder="Enter surname"]').fill(data['surName'])  
        page.get_by_role('textbox', name= 'DD/MM/YYYY' ).click()
        page.get_by_role('textbox', name= 'DD/MM/YYYY' ).fill(data["birthDate"])
        page.wait_for_timeout(1000)
        page.get_by_role("combobox", name="Sex").click()
        page.wait_for_timeout(1000)  # Wait for dropdown to open
        # Wait for the element to be visible and interactable
        # page.locator('.ant-select-selector').first.wait_for_state("visible")
        # page.locator('.ant-select-selector').first.click()
        # Select appropriate gender/sex option
        if data['genderId'] == "05ce2334-11c8-11ef-b05b-0242ac110002":
            page.get_by_text('Male', exact=True).click()
        else:
            page.get_by_text('Female', exact=True).click()
        page.wait_for_timeout(1000)
        #Nationality
        nationality = page.get_by_role('combobox', name= 'Nationality *' )
        nationality.fill("SRI LANKA")
        page.wait_for_timeout(3000)
        page.get_by_text('SRI LANKA').click()
        page.wait_for_timeout(1000)
        #email
        page.get_by_role('textbox',name= 'Email *', exact= True ).fill("tempemail@gmail.com")
        page.wait_for_timeout(1000)
        #religion
        page.get_by_role('textbox', name= 'Religion *' ).fill(data["religionId"])
        page.wait_for_timeout(1000)

        #place of birth
        page.get_by_role('textbox', name= 'Place of birth *' ).fill(data["birthPlace"])
        page.wait_for_timeout(1000)

        #reenter email
        page.get_by_role('textbox', name= 'Re-enter Email *' ).fill("tempemail@gmail.com")
        page.wait_for_timeout(1000)

        #visa date
        page.get_by_role('textbox', name= 'Grant e-Visa valid from *' ).click()
        page.wait_for_timeout(3000)
        page.get_by_role('textbox', name= 'Grant e-Visa valid from *' ).fill("12/04/2025")
        page.wait_for_timeout(1000)
        page.get_by_role('textbox', name= 'To *' ).click()
        page.wait_for_timeout(3000)
        page.get_by_role('textbox', name= 'To *' ).fill("30/04/2025")
        page.wait_for_timeout(1000)

        #passport number
        page.get_by_role('textbox', name= 'Passport *' ).fill(data["passportNumber"])
        page.wait_for_timeout(5000)
        #passport type
        # page.get_by_role('combobox', name= 'Type *' ).fill("Ordinary passport")
        page.get_by_role('combobox', name= 'Type *' ).click()
        page.wait_for_timeout(1000)
        page.get_by_text('Ordinary passport').click()
        page.wait_for_timeout(3000)

        #date of issue
        page.get_by_role('textbox', name= 'Date of issue *').click()
        page.wait_for_timeout(1000)
        page.get_by_role('textbox', name= 'Date of issue *').fill(data["dateOfIssue"])
        page.wait_for_timeout(3000)

        #expiry date
        page.get_by_role('textbox', name= 'Expiry date *').click()
        page.wait_for_timeout(1000)
        page.get_by_role('textbox', name= 'Expiry date *').fill(data["dateOfExpiry"])
        page.wait_for_timeout(3000)

        #permament address
        page.get_by_role('textbox', name= 'Permanent residential address').fill("permanent address")
        page.wait_for_timeout(1000)

        #contact address
        page.get_by_role('textbox', name= 'Contact address *' ).fill("abcd")
        page.wait_for_timeout(3000)

        #telephone
        page.locator('#basic_ttllSdt').fill(data["contact"])
        page.wait_for_timeout(3000)

        #emergency full name
        page.get_by_role('textbox', name= 'Full name *' ).fill("test name")
        page.wait_for_timeout(3000)

        #cureent address
        page.get_by_role('textbox', name= 'Current residential address *').fill("hello")
        page.wait_for_timeout(3000)

        #current telephone
        page.locator('#basic_ttllLlSdt').fill(data["contact"])
        page.wait_for_timeout(3000)

        #relation
        page.get_by_role('textbox', name= 'Relationship *' ).fill("spouse")
        page.wait_for_timeout(3000)

        #purpose of entry
        page.get_by_role('combobox', name= 'Purpose of entry *' ).fill("Tourist")
        page.wait_for_timeout(1000)
        page.get_by_title('Tourist').click()
        page.wait_for_timeout(3000)

        #entry date
        page.get_by_role('textbox', name= 'Intended date of entry *' ).click()
        page.wait_for_timeout(1000)
        page.get_by_role('textbox', name= 'Intended date of entry *' ).fill("12/04/2025")
        page.wait_for_timeout(3000)

        #stay length
        page.get_by_role('textbox', name= 'Intended length of stay in' ).fill("10")
        page.wait_for_timeout(3000)

        #vietname address
        page.get_by_role('combobox', name= 'Residential address in Viet' ).fill("abcd")
        page.wait_for_timeout(3000)
        #city
        page.get_by_role('combobox', name= 'Province/city *' ).fill("AN GIANG")
        page.wait_for_timeout(1000)
        page.get_by_title('AN GIANG').click()
        page.wait_for_timeout(3000)
        #district
        page.get_by_role('combobox', name= 'District *' ).fill("AN PHU district")
        page.wait_for_timeout(1000)
        page.get_by_title('AN PHU District').click()
        page.wait_for_timeout(3000)
        #ward
        page.get_by_role('combobox', name= 'Ward / commune *' ).fill("AN PHU town")
        page.wait_for_timeout(1000)
        page.get_by_title('AN PHU Town').click()
        page.wait_for_timeout(3000)

        #bordergateentry
        page.get_by_role('combobox', name= 'Intended border gate of entry').fill("Bo Y Landport")
        page.wait_for_timeout(1000)
        page.get_by_title('Bo Y Landport').first.click()
        page.wait_for_timeout(3000)

        #bordergateexit
        # page.getByRole('combobox', name= 'Intended border gate of exit *').fill("Bo Y Landport")
        page.get_by_role('combobox', name= 'Intended border gate of exit *' ).click()
        page.wait_for_timeout(1000)
        # page.get_by_text('Bo Y Landport').nth(1).click()
        page.get_by_text('Cam Pha Seaport').click()
        page.wait_for_timeout(3000)

        #declare
        page.get_by_role('checkbox', name= 'Committed to declare').click()

        page.wait_for_timeout(100000)
        
        # Close the browser
        browser.close()

if __name__ == "__main__":
    main()
