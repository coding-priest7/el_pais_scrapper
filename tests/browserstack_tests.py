# test/browserstack_driver.py

from selenium import webdriver

def initialize_browserstack_driver(username, access_key):
    capabilities = {
        'browser': 'Chrome',
        'browser_version': 'latest',
        'os': 'Windows',
        'os_version': '10',
        'name': 'El Pais Opinion Scraping', 
        'build': 'build-1' 
    }

    # Initialize the WebDriver for BrowserStack
    driver = webdriver.Remote(
        command_executor=f'https://{username}:{access_key}@hub-cloud.browserstack.com/wd/hub',
        desired_capabilities=capabilities
    )
    return driver
