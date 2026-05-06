# AI-Powered API Automation Framework

This project demonstrates API automation using Python along with AI-assisted test case generation using Ollama.

## Overview

The framework validates APIs by checking:
- HTTP status codes
- Expected response fields
- Success and failure scenarios
- Invalid API handling
- AI-generated test data validation

This project is part of my learning journey toward AI-enabled QA automation and SDET skills.

## Tech Stack

- Python
- Requests
- JSON
- Logging
- Ollama
- Local LLM integration

## Features

- Validate multiple APIs dynamically
- Check response fields based on expected field list
- Handle success and failure API responses
- Generate logs in console and log file
- Generate API test cases using local AI model through Ollama
- Clean AI output and convert JSON into Python test data
- Add basic validation for inconsistent AI-generated output

## Project Structure

```text
api-automation-framework/
│
├── test_api.py          # Main API test runner
├── api_utils.py         # Reusable API validation functions
├── ai_test.py           # Ollama AI integration for test case generation
├── test_log.log         # Execution log file
├── requirements.txt     # Project dependencies
└── README.md            # Project documentation
