markdown
# Good_Reads Automation Framework

## 📘 Overview
Good_Reads is a Playwright‑based automation framework built with Python and Pytest.  
It demonstrates a modular, scalable test architecture for web applications — featuring reusable page objects, centralized configuration management, and clean reporting.

## 🧩 Tech Stack
- **Language:** Python  
- **Frameworks:** Pytest + Playwright  
- **Design Pattern:** Page Object Model (POM)  
- **Reporting:** HTML reports via Pytest plugins  
- **Version Control:** Git + GitHub  

## ⚙️ Project Structure
Good_Reads/
│
├── setup/                # Environment setup and configuration
├── pages/                # Page object classes
├── tests/                # Test cases grouped by feature
├── utils/                # Helper functions and data handlers
├── test_data/            # JSON or CSV test data files
├── conftest.py           # Pytest fixtures and hooks
├── config.dev.json       # Environment configuration
└── pytest.ini            # Pytest configuration file

Code

## 🚀 Getting Started
1. Clone the repository:
   ```bash
   git clone https://github.com/RamithaBabuSDETLead/tdd_playwright_python_pytest_goodreads_automation_framework.git
Install dependencies:

bash
pip install -r requirements.txt
Install Playwright browsers:

bash
playwright install
Run tests:

bash
pytest --headed --html=report.html
🧠 Key Features
Modular and reusable test design

Feature‑specific Pytest marks

Centralized configuration and data handling

HTML reporting for test results

Easy integration with CI/CD pipelines

👩‍💻 Author
Ramitha Babu (SDET Lead)  
Automation Engineer specializing in Playwright, Python, and Pytest frameworks.
