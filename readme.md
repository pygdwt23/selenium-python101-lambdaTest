# LambdaTest-Certifications

## Intro
This is my Selenium Python 101 Assignment for LambdaTest Certification. 
- I am using python programming language with Selenium version 4.9 and pytest framework to solve this assignment.
- I am using 4 different browsers and platforms for parallel execution in this repository:
    1. Chrome + 88.0 + Windows 10
    2. MicrosoftEdge + 87.0 + macOS Sierra
    3. Firefox + 82.0 + Windows 7
    4. Internet Explorer + 11.0 + Windows 10
- I've ensured that network logs, video recording, screenshots, & console logs are enabled through the capability
- I am using conftest for common used command
- I created config.json to adjust the browser and platform
- I am using Select library to handle the dropdown
- I am using Actionchain to handle drag and drop, etc.
- I am using Faker library to generate random dynamic value

## Pre-requisites
- have latest version of python installed
- have latest version of pip installed
- pip install selenium==4.9.0 
- pip install pytest
- pip install faker

## How to change browser and platform
1. go to config.json
2. adjust the value of browser and platform with provided browser and platform, e.g: Chrome + 88.0 + Windows 10, MicrosoftEdge + 87.0 + macOS Sierra, Firefox + 82.0 + Windows 7, Internet Explorer + 11.0 + Windows 10
 

## How to execute the test
e.g:
```bash
pytest -v -s test_seleniumPython101.py
```
## About Me
- Name : Prayogo Dewantoro
- Nick Name: Yogo
- Current Occupation: Quality Assurance Engineer
