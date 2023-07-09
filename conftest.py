import pytest
import os
import sys
import json
import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.edge.options import Options
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.ie.options import Options

username = "pygdwt"
accessKey = "YkgRYdljv0S3A2Ai7Q3crv1YvREzhvY07MMy1NrLZ1ivam6n2F"
gridUrl = "hub.lambdatest.com/wd/hub"
url = "https://"+(username)+":"+accessKey+"@"+gridUrl
baseurl = "https://www.lambdatest.com/selenium-playground"
CONFIG_PATH = 'config.json'


@pytest.fixture(scope='session')
def config():
    # open the config file and read json data to return it as dict
    with open(CONFIG_PATH) as config_file:
        if os.path.isfile(CONFIG_PATH):
            data = json.load(config_file)
            return data
        else:
            raise Exception('File does not exists in the path')

@pytest.fixture(scope='session')
def browser(config):
    return config['browser']

@pytest.fixture(scope='session')
def platform(config):
    return config['platform']

@pytest.fixture()
def conftest(browser, platform):
    if browser == "Chrome" and platform == "Windows 10":
        capability = {
	            "browserName": "Chrome",
	            "browserVersion": "88.0",
	            "LT:Options": {
		            "username": "pygdwt",
		            "accessKey": "YkgRYdljv0S3A2Ai7Q3crv1YvREzhvY07MMy1NrLZ1ivam6n2F",
		            "visual": True,
		            "video": True,
                    "network": True,
                    "console": True,
		            "platformName": "Windows 10",
		            "build": "chrome_Windows10",
		            "project": "chrome_Windows10",
		            "name": "test_seleniumPython101"
	            }
            }
        # driver = webdriver.Remote(command_executor=url,desired_capabilities=capability)
        
    elif browser == "Edge" and platform == "MacOS Sierra":
        capability = {
	            "browserName": "Edge",
	            "browserVersion": "87.0",
	            "LT:Options": {
		            "username": "pygdwt",
		            "accessKey": "YkgRYdljv0S3A2Ai7Q3crv1YvREzhvY07MMy1NrLZ1ivam6n2F",
		            "visual": True,
		            "video": True,
                    "network": True,
                    "console": True,
		            "platformName": "MacOS Sierra",
		            "build": "edge_MacOSSierra",
		            "project": "edge_MacOSSierra",
		            "name": "test_seleniumPython101"
	            }
            }
        # driver = webdriver.Remote(command_executor=url,desired_capabilities=capability)

    elif browser == "Firefox" and platform == "Windows 7":
        capability = {
	            "browserName": "Firefox",
	            "browserVersion": "82.0",
	            "LT:Options": {
		            "username": "pygdwt",
		            "accessKey": "YkgRYdljv0S3A2Ai7Q3crv1YvREzhvY07MMy1NrLZ1ivam6n2F",
		            "visual": True,
		            "video": True,
                    "network": True,
                    "console": True,
		            "platformName": "Windows 7",
		            "build": "firefox_Windows7",
		            "project": "firefox_Windows7",
		            "name": "test_seleniumPython101"
	            }
            }
        # driver = webdriver.Remote(command_executor=url,desired_capabilities=capability)
    
    elif browser == "Internet Explorer" and platform == "Windows 10" :
        capability = {
	            "browserName": "IE",
	            "browserVersion": "11.0",
	            "LT:Options": {
		            "username": "pygdwt",
		            "accessKey": "YkgRYdljv0S3A2Ai7Q3crv1YvREzhvY07MMy1NrLZ1ivam6n2F",
		            "visual": True,
		            "video": True,
                    "network": True,
                    "console": True,
		            "platformName": "Windows 10",
		            "build": "explorer_Windows10",
		            "project": "explorer_Windows10",
		            "name": "test_seleniumPython101"
	            }
            }
    	# driver = webdriver.Remote(command_executor=url,desired_capabilities=capability)
    else:
        raise Exception("Browser is not recommended")
    
    driver = webdriver.Remote(command_executor=url,desired_capabilities=capability)
    print("Run started at:" + str(datetime.datetime.now()))
    print("Browser: %s" %browser)
    print("Platform: %s" %platform)
    driver.implicitly_wait(20)
    driver.maximize_window()
    driver.delete_all_cookies
    driver.get(baseurl)

    yield driver
    driver.quit
