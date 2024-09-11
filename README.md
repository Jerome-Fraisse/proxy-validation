# Proxy Validation Tool

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)](https://www.python.org/downloads/release/python-380/)
[![License](https://img.shields.io/badge/license-MIT-green)](https://opensource.org/licenses/MIT)

## Description

**Proxy Validation Tool** is a simple and efficient Python script for testing the functionality of a list of proxies. It tests if the provided proxies are working by checking their ability to make HTTP requests, and categorizes them into functional and non-functional proxies. Results are saved into separate files for further use.

## Features

- **Proxy Authentication**: Supports proxies with `IP:PORT:USERNAME:PASSWORD` format.
- **Timeout Handling**: Handles connection timeouts gracefully.
- **Result Logging**: Saves functional and non-functional proxies in separate text files for easy retrieval.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Contributing](#contributing)
- [License](#license)

## Installation

### Requirements

- Python 3.8+
- `requests` library

### Install Dependencies

First, make sure you have Python 3.8 or higher installed. Then, install the required packages:

```bash
pip install -r requirements.txt
Or manually install the required package:

<strong>Usage</strong>
Usage

    Prepare your proxy list:
        Create a file called liste_proxies.txt with one proxy per line in the format IP:PORT:USERNAME:PASSWORD.

    Run the script: To run the proxy tester, use the following command:

    

    python main-proxy-testing.py

    Results:
        Functional proxies will be saved in proxies_fonctionnels.txt.
        Non-functional proxies will be saved in proxies_echoues.txt.

Configuration

The proxy list file (liste_proxies.txt) should contain one proxy per line in the following format:



IP:PORT:USERNAME:PASSWORD

Example:

64.137.104.243:5853:ejyhouxi:tv90c5w28qxj
64.137.124.56:6268:ejyhouxi:tv90c5w28qxj

Make sure that the proxies in your list follow this structure. The script will test each proxy, and output the results accordingly.
Contributing

Contributions are welcome! If you want to contribute to this project, please follow these steps:

    Fork the repository.
    Create a new feature branch (git checkout -b feature/my-new-feature).
    Commit your changes (git commit -am 'Add new feature').
    Push to the branch (git push origin feature/my-new-feature).
    Create a new Pull Request.

Feel free to open an issue if you encounter any problems or have suggestions for improvement.
License

This project is licensed under the MIT License - see the LICENSE file for details.
