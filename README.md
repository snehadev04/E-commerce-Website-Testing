
# E-commerce Website Testing

## Project Description
This project focuses on testing the E-commerce functionalities of the Sauce Demo website. It includes both manual and automated tests to ensure the website's reliability and functionality.

## Tools and Technologies
- Selenium WebDriver
- Python
- unittest
- WebDriver Manager
- PyCharm (IDE)

## Setup Instructions

### Prerequisites
- Python 3.x
- Google Chrome browser

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/snehadev04/E-commerce_Website_Testing_P1.git
   cd E-commerce_Website_Testing_P1
   ```

2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Tests

### Automated Tests
1. Open PyCharm and load the project.
2. Run the automated tests:
   - Right-click on the test file (e.g., `test_login.py`) and select `Run 'test_login'`.

### Manual Tests
1. Navigate to the `manual_tests/test_cases.md` file.
2. Follow the test cases outlined in the `test_cases.md` file.
3. Document the results in the `test_reports/` directory.

## Directory Structure
```
E-commerce_Website_Testing_P1/
│
├── automation_tests/
│   ├── test_login.py
│   ├── test_product_search.py
│   └── test_checkout.py
│
├── manual_tests/
│   ├── test_cases/
│   │   └── test_case.md                                                                                                                   
│   ├── test_plans/
│   │   └── test_plan.md                                                                                                        
│   └── test_reports/
│       └── test_plan.md 
│
├── venv/
├── requirements.txt
├── README.md
└── main.py
```

## Test Cases
The project includes various test cases for functional, regression, and integration testing, as well as end-to-end testing scenarios.

## Contributors
- Sneha D

## Contact
For any questions or feedback, please contact me at snehadev1999@gmail.com.
