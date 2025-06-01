# BANK-CHECK-EXTRACTOR

Transforming checks into insights, effortlessly and accurately.

Built with the tools and technologies:

![Python](https://img.shields.io/badge/Python-white?style=flat&logo=python&logoColor=blue) ![Tesseract OCR](https://img.shields.io/badge/Tesseract_OCR-grey?style=flat&logo=tesseract&logoColor=white) ![Pandas](https://img.shields.io/badge/pandas-white?style=flat&logo=pandas&logoColor=black) ![cSpell](https://img.shields.io/badge/cSpell-blue?style=flat&logo=retext&logoColor=white)

## Core Technologies

This project leverages the following key technologies for data extraction and processing:

* **Python**: The primary programming language used for the entire application logic.

* **Tesseract OCR**: An open-source optical character recognition engine used for accurately extracting text from scanned bank checks (PDFs and images).

* **Pandas**: A powerful Python library used for data manipulation and analysis, particularly for handling extracted data and generating structured CSV output.

* **cSpell**: Integrated for spell-checking within the codebase to maintain high quality and reduce errors.

## Table of Contents

* [Overview](#overview)

* [Why bank-check-extractor?](#why-bank-check-extractor)

* [Getting Started](#getting-started)

    * [Prerequisites](#prerequisites)

    * [Installation](#installation)

    * [Usage](#usage)

    * [Testing](#testing)

## Overview

`bank-check-extractor` is a powerful Python tool designed to automate the extraction of data from scanned bank checks using advanced OCR technology.

## Why bank-check-extractor?

This project streamlines the process of digitizing and analyzing bank check information. The core features include:

* ✅ **OCR Technology**: Leverages Tesseract OCR to accurately extract text from scanned checks, eliminating manual data entry.

* 📊 **CSV Output**: Converts extracted data into structured CSV format for easy analysis and integration with other tools.

* 🖼️ **Image Processing**: Supports various image formats and PDFs, enhancing versatility for developers.

* 🔍 **Custom Spell-Checking**: Integrates cSpell to improve code quality, reducing errors and enhancing readability.

* ⚙️ **Easy Setup**: Simple directory structure for input files, streamlining the workflow for developers.

## Getting Started

### Prerequisites

This project relies on Tesseract OCR. Please ensure you have Tesseract OCR installed on your system and its executable is in your system's PATH. You can find installation instructions for various operating systems on the [Tesseract GitHub page](https://tesseract-ocr.github.io/tessdoc/Installation.html).

### Installation

Build `bank-check-extractor` from the source and install dependencies:

1.  **Clone the repository:**

    ```bash
    git clone [https://github.com/javvajibhuvi24/bank-check-extractor.git](https://github.com/javvajibhuvi24/bank-check-extractor.git)
    ```

2.  **Navigate to the project directory:**

    ```bash
    cd bank-check-extractor
    ```

3.  **Install the dependencies:**

    Using pip:

    ```bash
    pip install -r requirements.txt
    ```

### Usage

Run the project with:

Using pip:

```bash
python extractor.py
```
Note: Ensure your check images/PDFs are placed in the data/checks/ directory before running.
The extracted data will be saved as a CSV file in the data/output/ directory.

### Testing
bank-check-extractor uses the pytest test framework. Run the test suite with:

Using pip:

Bash
```
pytest
```
### Contributing
Contributions are welcome! If you'd like to contribute to this project, please follow these guidelines:

1.Fork the repository.

2.Create a new branch (git checkout -b feature/your-feature-name).

3.Make your changes.

4.Commit your changes (git commit -m 'Add new feature').

5.Push to the branch (git push origin feature/your-feature-name).

6.Open a pull request.

### License
This project is licensed under the MIT License.


### Contact
For any questions or inquiries, please contact:

Javvaji Bhuvi - javvajibhuvi01@gmail.com

Project Link: https://github.com/javvajibhuvi24/bank-check-extractor
