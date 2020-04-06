import time


def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    #login_link = browser.find_element_by_css_selector("#login_link")
    #login_link.click()
    time.sleep(5)