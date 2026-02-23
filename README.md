## UI Automation Framework — SauceDemo

- UI Automation Framework — SauceDemo
- Production-style UI automation framework built with Playwright (Python) and pytest.
- The project demonstrates engineering-level test design, business-oriented validation, and release decision strategy.
- Application under test:
https://www.saucedemo.com/

---

## What This Project Demonstrates

- Risk-based test design
- Business-oriented automation
- Clean Page Object Model (POM)
- Smoke-driven Go / No-Go release strategy
- Stable multi-browser execution
- CI-ready pipeline
- Allure reporting with artifacts
- Retry strategy for flaky tests

---

## Tech Stack

- Python 3.12+
- Playwright
- pytest
- pytest-xdist (parallel execution)
- pytest-rerunfailures
- Allure reporting
- GitHub Actions CI
- Docker-ready

---

## Architecture Overview

- The framework follows these principles:
- Page Objects encapsulate UI details
- Tests represent business flows, not UI mechanics
- Assertions are minimal and meaningful
- Test data is separated from test logic
- Smoke tests represent release-critical paths
- Login is executed once per session via storage state
- Each test runs in isolated browser context

---

## Project Structure

tests/
 └─ ui/
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

data/
 ├─ users.py
 └─ checkout_data.py

.github/workflows/
conftest.py
pytest.ini

## Testing Strategy

Feature-based grouping:
- Tests are organized by business feature, not by test type (positive/negative).
Risk-based coverage:
- Each test validates a business risk:
   - Authentication failures
   - Cart consistency
   - Order processing correctness
   - Session security
   - Access control protection
   
Minimal UI Assertions:
- The goal is to avoid fragile UI checks.
- Tests verify system behavior, not layout.

---

## Test Coverage Overview

Authentication: 
- Successful login
- Access denied after logout
- Direct URL access protection

Inventory:
- Inventory visibility after login
- Add / remove items
- Cart badge state
- Navigation to cart

Cart:
- Selected items are displayed
- Remove items from cart
- Navigation back to inventory
- Navigation to checkout

Checkout:
- Happy path checkout (end-to-end)
- Required fields validation (negative cases)
- Cancel checkout flow
- Checkout with multiple items

Session & Stability:
- Cart persistence after page refresh
- Session stability on browser back navigation
- Access restriction after logout
- Checkout access restriction after order completion

---

## Smoke Tests (Go / No-Go)

Smoke tests represent the minimum critical set required for release approval.

Smoke Checklist:

Authentication:

- User can log in successfully
- Access is denied after logout

Inventory:

- Product catalog is visible
- User can add product to cart

Cart:

- Selected product is displayed
- User can proceed to checkout

Checkout:

- User can complete checkout
- Cart is empty after successful order

## Release rule
If **any smoke test fails**, the release is considered **blocked**.

---

## How to Run

Install dependencies:

- pip install -r requirements.txt
- playwright install

Run all tests:

- pytest
- 
Run smoke tests only:

- pytest -m smoke
  
Run tests in specific browser:

- pytest --browser_name=firefox
  
## Test Reports (Allure)

Generate report:

- pytest --alluredir=allure-results
- allure serve allure-results

Reports include:

- Screenshots on failure
- Playwright trace files
- Test execution details

## Engineering Decisions

- Storage state is used to avoid repeated login and reduce test runtime.
- Each test runs in isolated browser context.
- Retry strategy is applied to reduce flaky test impact.
- Multi-browser execution increases coverage confidence.
- Smoke tests act as release quality gate.

## What This Project Demonstrates

- Understanding of UI automation architecture
- Business-focused QA thinking
- Test stability engineering
- CI-ready framework design
- Release decision modeling

##  Final Status

- This is not a demo script collection.
- This is a structured automation framework built with scalability and release control in mind.
