# IQ Option Trading Bot

![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![Docker](https://img.shields.io/badge/Docker-Compose-brightgreen)

## Overview

This repository contains a Python application for automated trading on the IQOption platform. The application is designed to facilitate trading activities using the IQOption broker. It leverages the power of Python and can be easily deployed using Docker Compose for a seamless experience.

## Features

- **Automated Trading:** Execute trading strategies automatically on the IQOption platform.
- **Pythonic Approach:** Developed in Python, making it versatile and easy to understand.
- **Docker Compose:** Simple deployment using Docker Compose for containerized execution.

## Prerequisites

Before running the application, ensure you have the following installed:

- Python 3.9 or higher
- Docker and Docker Compose

## Getting Started

1. **Clone the repository:**

   ```bash
   git clone https://github.com/your-username/iqoption-trading-bot.git
   ```

2. **Navigate to the project directory:**
   ```bash
   cd iqoption-trading-bot
   ```
3. **Copy the example .env file:**
   ```bash
   cp example.env .env
   ```
4. **Open the .env file and configure the necessary settings.**
5. **Run the application using Docker Compose:**
   ```
   docker-compose up -d
   ```

## Configuration

Modify the config.yml file to customize the trading strategy, account credentials, and other settings.

## Disclaimer

Use this trading bot responsibly and at your own risk. The authors are not responsible for any financial losses incurred during its use.

## Contributing

Feel free to contribute by opening issues, providing feedback, or submitting pull requests.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
