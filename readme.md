# Playwright Automation Script

This project automates the process of filling out an e-visa application form using Playwright.

## Prerequisites

1. **Python**: Ensure Python 3.7 or higher is installed on your system. You can download it from [python.org](https://www.python.org/).
2. **Node.js**: Playwright requires Node.js. Install it from [nodejs.org](https://nodejs.org/).
3. **Playwright**: Install Playwright Python bindings using pip.
4. **Dependencies**: Install other required Python libraries.

## Setup Instructions

1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd auto
   ```

2. **Install Dependencies**:
   Install the required Python libraries:
   ```bash
   pip install playwright
   pip install -r requirements.txt
   ```

3. **Install Playwright Browsers**:
   After installing Playwright, run the following command to download the necessary browser binaries:
   ```bash
   playwright install
   ```

4. **Prepare the Input Data**:
   Create a `data.json` file in the project directory with the following structure:
   ```json
   {
       "givenName": "John",
       "surName": "Doe",
       "birthDate": "01/01/1990",
       "genderId": "05ce2334-11c8-11ef-b05b-0242ac110002",
       "religionId": "Christianity",
       "birthPlace": "New York",
       "passportNumber": "A12345678",
       "dateOfIssue": "01/01/2020",
       "dateOfExpiry": "01/01/2030",
       "contact": "1234567890"
   }
   ```

5. **Run the Script**:
   Execute the automation script using the following command:
   ```bash
   python auto_optimized_reusable.py
   ```
   By default, the script launches the browser in non-headless mode (with UI). To run it in headless mode, modify the following line in the [auto_optimized_reusable.py](auto_optimized_reusable.py) file:
   ```python
   browser = p.chromium.launch(headless=True)
   ```

## Notes

- Ensure you have a stable internet connection while running the script.
- The script uses hardcoded values for some fields (e.g., email, address). Update these values in the source code as needed.
- The current input JSON is a sample. If your application requires additional fields, update the `data.json` accordingly.
- For troubleshooting issues, double-check that all dependencies are correctly installed and that the JSON file is properly formatted.

## License

This project is licensed under the MIT License.