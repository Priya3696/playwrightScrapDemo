import json
import logging
from playwright.sync_api import sync_playwright, TimeoutError

def wait_get_by_role(page, role: str, name: str, exact: bool = False):
    element = page.get_by_role(role, name=name, exact=exact)
    element.wait_for(timeout=7000)
    return element

def wait_get_by_text(page, text: str, exact: bool = False):
    element = page.get_by_text(text, exact=exact)
    element.wait_for(timeout=7000)
    return element

def wait_get_by_title(page, title: str, exact: bool = False):
    element = page.get_by_title(title, exact=exact)
    element.wait_for(timeout=7000)
    return element

def load_data(filepath: str) -> dict:
    try:
        with open(filepath, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        logging.error("File not found: %s", filepath)
        raise
    except json.JSONDecodeError:
        logging.error("Invalid JSON format in file: %s", filepath)
        raise

def fill_input(page, role: str, name: str, value: str, exact: bool = False):
    try:
        element = wait_get_by_role(page, role, name, exact)
        element.fill(value)
    except TimeoutError:
        logging.error("Timeout while waiting for input element: role=%s, name=%s", role, name)
        raise
    except Exception as e:
        logging.error("Error filling input: %s", e)
        raise

def click_element(page, role: str, name: str):
    try:
        element = wait_get_by_role(page, role, name)
        element.click()
    except TimeoutError:
        logging.error("Timeout while waiting for clickable element: role=%s, name=%s", role, name)
        raise
    except Exception as e:
        logging.error("Error clicking element: %s", e)
        raise

def select_option(page, combobox_name: str, option_text: str):
    try:
        combo = wait_get_by_role(page, 'combobox', combobox_name)
        combo.click()
        wait_get_by_text(page, option_text, exact=True).click()
    except TimeoutError:
        logging.error("Timeout while selecting option: combobox_name=%s, option_text=%s", combobox_name, option_text)
        raise
    except Exception as e:
        logging.error("Error selecting option: %s", e)
        raise

def click_element_by_locator(page, locator_type: str, locator: str):
    try:
        if locator_type == 'id':
            selector = f"#{locator}"
        elif locator_type == 'class':
            selector = f".{locator}"
        elif locator_type == 'xpath':
            selector = f"xpath={locator}"
        else:
            raise ValueError(f"Unsupported locator type: {locator_type}")
            
        element = page.locator(selector)
        element.wait_for(timeout=7000)
        element.click()
    except TimeoutError:
        logging.error("Timeout while waiting for element with %s: %s", locator_type, locator)
        raise
    except Exception as e:
        logging.error("Error clicking element by %s with selector %s: %s", locator_type, locator, e)
        raise

def click_combobox(page, name: str, exact: bool = False):
    try:
        element = wait_get_by_role(page, 'combobox', name, exact)
        element.click()
    except TimeoutError:
        logging.error("Timeout while waiting for combobox with name: %s", name)
        raise
    except Exception as e:
        logging.error("Error clicking combobox with name %s: %s", name, e)
        raise

def click_text(page, text: str, exact: bool = True):
    try:
        element = wait_get_by_text(page, text, exact)
        element.click()
    except TimeoutError:
        logging.error("Timeout while waiting for element with text: %s", text)
        raise
    except Exception as e:
        logging.error("Error clicking element with text %s: %s", text, e)
        raise

def click_title(page, title: str, exact: bool = True):
    try:
        element = wait_get_by_title(page, title, exact)
        element.click()
    except TimeoutError:
        logging.error("Timeout while waiting for element with title: %s", title)
        raise
    except Exception as e:
        logging.error("Error clicking element with title %s: %s", title, e)
        raise