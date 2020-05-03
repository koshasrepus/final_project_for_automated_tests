import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--set_os', action='store', default='windows',
                     help='Choose operation system: windows or ubuntu')
    parser.addoption('--browser_name', action='store', default='chrome',
                     help='Choose browser: chrome or firefox')
    parser.addoption('--language', action='store', default='en',
                     help='Choose language')


@pytest.fixture(scope='function')
def browser(request):
    browser_name = request.config.getoption("browser_name")
    user_language = request.config.getoption("language")
    set_os = request.config.getoption("set_os")
    if set_os == "windows":
        path_to_chromedriver = 'Drivers/Windows_10_64/chromedriver.exe'
        path_to_geckodriver = 'Drivers/Windows_10_64/geckodriver.exe'
    elif set_os == "ubuntu":
        path_to_chromedriver = './Drivers/Ubuntu/chromedriver'
        path_to_geckodriver = './Drivers/Ubuntu/geckodriver'
    else:
        pytest.UsageError("--set_os should be windows or ubuntu")
    if browser_name == 'chrome':
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        browser = webdriver.Chrome(executable_path=path_to_chromedriver, options=options)
    elif browser_name == 'firefox':
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", user_language)
        browser = webdriver.Firefox(firefox_profile=fp, executable_path=path_to_geckodriver)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    browser.quit()

