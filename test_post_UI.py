from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
import pytest

post_text = "create test post"


def test_add_post_to_fb_test_page():
    # Use options to disable notifications
    options = Options().add_argument("--disable-notifications")

    # Start the driver with disabled notifications
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.get("https://www.facebook.com/Page_for_test_user-108928174075398")

    # Login using a test user
    driver.find_element_by_id("email").send_keys("lkrsfuhxcn_1584545322@tfbnw.net")
    driver.find_element_by_id("pass").send_keys("agileengine")
    sleep(2)
    driver.find_element_by_id("loginbutton").click()

   # Click on Create post object
    create_post = driver.find_element_by_xpath("//*[@name=\"xhpc_message\"]")
    create_post.click()

    # Write post text
    create_post.send_keys(post_text)
    sleep(2)

    # Scroll the window to be able to find Post button
    driver.execute_script("window.scrollTo(0, 1080)")
    sleep(2)

    # CLick on Post button
    post_it = driver.find_element_by_css_selector("#feedx_sprouts_container [type='submit']")
    post_it.click()
    sleep(10)

    # Quit the driver
    driver.quit()
