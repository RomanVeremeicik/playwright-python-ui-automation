# UI Automation Project — SauceDemo

This project demonstrates a production-like UI automation framework
built with Playwright (Python) and pytest.

The goal of the project is to showcase:
- Critical QA thinking
- business-oriented test design
- clean test architecture
- go / no-go decision making using smoke tests

The application under test: https://www.saucedemo.com/

---

 Tech Stack

- Python 3.14
- Playwright
- pytest
- Page Object Model (POM)

---

##  Project Structure

tests/ui/
├─ test_login.py 
├─ test_inventory.py 
├─ test_cart.py 
├─ test_checkout.py 
├─ test_session.py 
└─ test_smoke.py 

pages/
├─ login_page.py
├─ inventory_page.py
├─ cart_page.py
└─ checkout_page.py

##  Testing Approach

This project follows several key principles:

- **Tests are grouped by feature**, not by test type (positive/negative)
- **Each test covers a business risk**, not a UI detail
- **UI assertions are minimal** to avoid flaky tests
- **Page Objects encapsulate UI details**
- Smoke tests represent **release-critical flows**

---

## Test Coverage Overview

###  Authentication
- Successful login
- Access denied after logout
- Direct URL access protection

###  Inventory
- Inventory visibility after login
- Add / remove items
- Cart badge state
- Navigation to cart

###  Cart
- Selected items are displayed
- Remove items from cart
- Navigation back to inventory
- Navigation to checkout

### Checkout
- Happy path checkout (end-to-end)
- Required fields validation (negative cases)
- Cancel checkout flow
- Checkout with multiple items

### Session & Stability
- Cart persistence after page refresh
- Session stability on browser back navigation
- Access restriction after logout
- Checkout access restriction after order completion

---

## Smoke Tests (Go / No-Go)

Smoke tests represent the **minimal critical set**
that must pass to allow a release.

### Smoke checklist

#### Authentication
- [x] User can successfully log in
- [x] Access is denied after logout

#### Inventory
- [x] Product catalog is visible after login
- [x] User can add product to cart

#### Cart
- [x] Selected product is displayed in cart
- [x] User can proceed from cart to checkout

#### Checkout
- [x] User can complete checkout (happy path)
- [x] Cart is empty after successful order

 **Release rule:**  
If **any smoke test fails**, the release is considered **blocked**.

---

##  How to Run Tests

### Install dependencies

# bash
pip install -r requirements.txt
playwright install

# Run all tests

pytest

# Run smoke tests only

pytest tests/ui/test_smoke.py

## Test Reports (Allure)

Generate report:
# bash
pytest --alluredir=allure-results
allure serve allure-results
