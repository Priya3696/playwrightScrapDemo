import json
import logging
from playwright.sync_api import sync_playwright, TimeoutError
from actions import load_data, click_element, fill_input, wait_get_by_role, wait_get_by_text, wait_get_by_title

def main():
    logging.basicConfig(level=logging.INFO)
    try:
        data = load_data('data.json')
    except Exception as e:
        logging.error("Failed to load data.json: %s", e)
        return

    logging.info("Data loaded successfully")
    
    with sync_playwright() as p:
        try:
            browser = p.chromium.launch(headless=False)
            context = browser.new_context()
            page = context.new_page()
            try:
                page.goto("https://evisa.gov.vn/e-visa/foreigners")
                click_element(page, 'checkbox', 'Confirm compliance with')
                click_element(page, 'checkbox', 'Confirmation of reading')
                click_element(page, 'button', 'Next')
                page.wait_for_load_state("networkidle")
                page.locator('input[placeholder="Enter middle and given name"]').fill(data['givenName'])
                page.locator('input[placeholder="Enter surname"]').fill(data['surName'])
                wait_get_by_role(page, 'textbox', 'DD/MM/YYYY').click()
                wait_get_by_role(page, 'textbox', 'DD/MM/YYYY').fill(data["birthDate"])
                
                wait_get_by_role(page, "combobox", "Sex").click()
                if data['genderId'] == "05ce2334-11c8-11ef-b05b-0242ac110002":
                    wait_get_by_text(page, 'Male', exact=True).click()
                else:
                    wait_get_by_text(page, 'Female', exact=True).click()
                
                wait_get_by_role(page, 'combobox', 'Nationality *').fill("SRI LANKA")
                wait_get_by_text(page, 'SRI LANKA').click()
                fill_input(page, 'textbox', 'Email *', "tempemail@gmail.com", exact=True)
                fill_input(page, 'textbox', 'Religion *', data["religionId"])
                fill_input(page, 'textbox', 'Place of birth *', data["birthPlace"])
                fill_input(page, 'textbox', 'Re-enter Email *', "tempemail@gmail.com")
                wait_get_by_role(page, 'textbox', 'Grant e-Visa valid from *').click()
                wait_get_by_role(page, 'textbox', 'Grant e-Visa valid from *').fill("12/04/2025")
                wait_get_by_role(page, 'textbox', 'To *').click()
                wait_get_by_role(page, 'textbox', 'To *').fill("30/04/2025")
                fill_input(page, 'textbox', 'Passport *', data["passportNumber"])
                
                wait_get_by_role(page, 'combobox', 'Type *').click()
                wait_get_by_text(page, 'Ordinary passport', exact=True).click()
                
                wait_get_by_role(page, 'textbox', 'Date of issue *').click()
                wait_get_by_role(page, 'textbox', 'Date of issue *').fill(data["dateOfIssue"])
                wait_get_by_role(page, 'textbox', 'Expiry date *').click()
                wait_get_by_role(page, 'textbox', 'Expiry date *').fill(data["dateOfExpiry"])
                
                fill_input(page, 'textbox', 'Permanent residential address', "permanent address")
                fill_input(page, 'textbox', 'Contact address *', "abcd")
                page.locator('#basic_ttllSdt').fill(data["contact"])
                fill_input(page, 'textbox', 'Full name *', "test name")
                fill_input(page, 'textbox', 'Current residential address *', "hello")
                page.locator('#basic_ttllLlSdt').fill(data["contact"])
                fill_input(page, 'textbox', 'Relationship *', "spouse")
                
                wait_get_by_role(page, 'combobox', 'Purpose of entry *').fill("Tourist")
                wait_get_by_title(page, 'Tourist').click()
                wait_get_by_role(page, 'textbox', 'Intended date of entry *').click()
                wait_get_by_role(page, 'textbox', 'Intended date of entry *').fill("12/04/2025")
                fill_input(page, 'textbox', 'Intended length of stay in', "10")
                wait_get_by_role(page, 'combobox', 'Residential address in Viet').fill("abcd")
                wait_get_by_role(page, 'combobox', 'Province/city *').fill("AN GIANG")
                wait_get_by_title(page, 'AN GIANG').click()
                wait_get_by_role(page, 'combobox', 'District *').fill("AN PHU district")
                wait_get_by_title(page, 'AN PHU District').click()
                wait_get_by_role(page, 'combobox', 'Ward / commune *').fill("AN PHU town")
                wait_get_by_title(page, 'AN PHU Town').click()
                wait_get_by_role(page, 'combobox', 'Intended border gate of entry').fill("Bo Y Landport")
                wait_get_by_title(page, 'Bo Y Landport').first.click()
                wait_get_by_role(page, 'combobox', 'Intended border gate of exit *').click()
                wait_get_by_text(page, 'Cam Pha Seaport').click()
                click_element(page, 'checkbox', 'Committed to declare')
                
                # Pause to observe; in production remove or replace with proper wait conditions.
                page.wait_for_timeout(1000)
            except TimeoutError as te:
                logging.error("Timeout occurred during page interaction: %s", te)
            except Exception as ex:
                logging.error("An error occurred during page interaction: %s", ex)
            finally:
                browser.close()
        except Exception as e:
            logging.error("Failed to initialize Playwright or browser: %s", e)

if __name__ == "__main__":
    main()