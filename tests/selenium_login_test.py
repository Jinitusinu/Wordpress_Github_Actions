import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os

@pytest.fixture
def browser():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()

def test_wordpress_login(browser):
    browser.get("http://localhost:8080/wp-login.php")
    assert "Log In" in browser.title

    username = browser.find_element(By.ID, "user_login")
    password = browser.find_element(By.ID, "user_pass")
    login_btn = browser.find_element(By.ID, "wp-submit")

    username.send_keys("admin")
    password.send_keys("adminpassword")  # Update with your test creds
    login_btn.click()

    time.sleep(3)  # Wait for redirect
    assert "Dashboard" in browser.page_source
