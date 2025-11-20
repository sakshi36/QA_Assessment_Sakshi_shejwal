# QA_Assessment_Sakshi_shejwal

## SauceDemo UI Automation with Playwright & Python

This project is a UI automation framework built using Playwright with Python for testing the SauceDemo application:  
https://www.saucedemo.com/

It includes both Happy Path and Negative Path test scenarios.

---

## Project Structure
```text
project-root/
├── pytest.ini
├── requirements.txt
├── .gitignore
├── data/
│   ├── credentials.example.json
├── tests/
│   ├── conftest.py
│   └── test_framework.py
├── videos1/   (ignored)
└── videos2/   (ignored)
```
---

## Test Scenarios

### Happy Path
- Login with all valid users (except locked_out_user)
- Add items from inventory
- Proceed to checkout
- Enter user details
- Verify order success page

### Negative Path
- Attempt login with locked_out_user
- Validate correct error message

---

## Test Data

Sample file in repo: `data/credentials.example.json`  
Local file required: `data/credentials.json`
```text
{
  "user_credentials": [
    {
      "username": "standard_user",
      "password": "secret_sauce"
    },
    {
      "username": "locked_out_user",
      "password": "secret_sauce"
    }
  ]
}
```
---

## How to Run

### 1. Clone Repository
git clone https://github.com/sakshi36/QA_Assessment_Sakshi_shejwal.git  
cd QA_Assessment_Sakshi_shejwal

### 2. Create Virtual Environment (optional)
python -m venv venv  
venv\Scripts\activate

### 3. Install Dependencies
pip install -r requirements.txt

### 4. Install Playwright Browsers
playwright install, pip install pytest-playwright, pip install pytest-html


### 5. Add Local Credentials File
copy data\credentials.example.json data\credentials.json

---

## Running Tests

### Run all tests
pytest

### Run specific test
pytest tests/test_framework.py

### Run with HTML report
pytest tests/test_framework.py --html=report.html

---

## Videos

Playwright recordings are saved in:
- videos1/
- videos2/

(These folders are ignored in Git, which are useful while debugging.)

---

## Tools and Technology

- Python  
- Playwright  
- Pytest  
- JSON (data driven testing)
