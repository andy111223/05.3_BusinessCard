# Business Card Manager

 - manages business cards by creating two types of contacts: personal and business
 - stores and handles basic contact information like name, email, and phone number, with the business contacts also including job-related details
 - includes a contact() method for simulating calls, and a feature to dynamically calculate the length of the contact's name
 - generates random business card data using the faker library
 - utilizes object-oriented principles, specifically Python class inheritance, to efficiently manage and extend contact information.

## Installation

1. Clone this repository to your local machine:

    `git clone https://github.com/andy111223/05.3_BusinessCard`

2. Navigate to the project directory:

    `cd 05.3_BusinessCard`

3. Install the required dependencies (if not already installed)

    `pip install faker`

4. Run the script:

    `python3 businessCard.py`

## Usage

1. Generate random business cards by calling the `create_contacts` function, which can create a specified number of contacts for either personal or business use.
   
2. Each contact will have a `contact()` method, allowing you to simulate calling the contact's personal or business phone number.

3. Access the `label_length` property to retrieve the combined length of the contact's first and last names (and a space between).

## Requirements

- Python 3 (tested on Python 3.12)
- `faker` library

