# Secret Santa Assignment

## Overview

This project is a Python-based solution for managing and assigning Secret Santa participants. The program allows you to upload employee data and previous Secret Santa assignments, then generates new assignments ensuring that participants don't get the same person they had in previous years.

## Features

- **Employee Management:** Add and manage employee data.
- **Previous Assignment Handling:** Load and consider previous Secret Santa pairings.
- **Random Assignment:** Generates new Secret Santa assignments randomly while avoiding repeats.
- **File Upload:** Supports `.xls`, `.xlsx`, and `.csv` file formats.
- **Output:** Generates a new Secret Santa assignment list and provides it as a downloadable file.

## Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

### Steps

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/Anandha001/Secret-Santa.git
   cd SECRET-SANTA
   ```

### Set Up a Virtual Environment

To isolate your project and manage dependencies, it is recommended to set up a virtual environment.

1. **Create the Virtual Environment:**

   Use the following command to create a virtual environment named `env`:

   ```bash
   python3 -m venv env
   ```

2. **Activate the Virtual Environment:**

   - On **macOS/Linux**:

     ```bash
     source env/bin/activate
     ```

     - On **Windows**:

     ```bash
     .\env\Scripts\activate
     ```

3. **Install Dependencies:**

   Once the virtual environment is activated, install the required dependencies using the following command:

   ```bash
   pip install -r requirements.txt
   ```

### Running the Application

To run the Secret Santa assignment tool, follow these steps:

1. **Start the FastAPI Server:**

   Use the following command to start the FastAPI application locally:

   ```bash
   uvicorn main:app --reload
   ```
