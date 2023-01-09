from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time
import os

website_url = "https://www.linkedin.com/jobs/search/?currentJobId=3209721540&f_AL=true&f_E=1%2C2&f_WT=2&keywords=python%20developer&refresh=true"

EMAIL = "Your email here"
PASSWORD = os.environ["PASSWORD"]
PHONE_NUMBER = os.environ["PHONE_NUMBER"]

chrome_driver_path = "C:/Software/Development/chromedriver.exe"
service = Service(chrome_driver_path)

driver = webdriver.Chrome(service=service)
driver.get(website_url)


def sign_in():
    # sign in to linked in, enter login details
    sign_in_button = driver.find_element(By.XPATH, "/html/body/div[1]/header/nav/div/a[2]")
    sign_in_button.click()
    time.sleep(2)
    login = driver.find_element(By.XPATH, "//*[@id='username']")
    login.send_keys(EMAIL)
    password = driver.find_element(By.XPATH, "//*[@id='password']")
    password.send_keys(PASSWORD)
    submit_button = driver.find_element(By.XPATH, "//*[@id='organic-div']/form/div[3]/button")
    submit_button.click()


def apply_for_first_job():
    time.sleep(3.5)
    listing = driver.find_element(By.XPATH, "//*[@id='ember176']")
    listing.click()
    time.sleep(1.5)
    easy_apply = driver.find_element(By.XPATH, "//*[@id='ember222']")
    easy_apply.click()
    time.sleep(1.5)
    phone_number_input = driver.find_element(By.XPATH, "//*[@id='urn:li:fs_easyApplyFormElement:(urn:li:fs_normalized_jobPosting:3179324602,9,phoneNumber~nationalNumber)']")
    phone_number_input.send_keys(PHONE_NUMBER)
    time.sleep(1.5)
    submit_application = driver.find_element(By.XPATH, "//*[@id='ember244']")
    submit_application.click()


def apply_for_all_jobs():
    time.sleep(5)
    clickable_listings = driver.find_elements(By.CSS_SELECTOR, ".job-card-container--clickable")
    for listing in clickable_listings:
        print("called")
        listing.click()
        time.sleep(2)
        try:
            easy_apply = driver.find_element(By.CSS_SELECTOR, ".jobs-apply-button")
            easy_apply.click()
            time.sleep(2)

            phone_input = driver.find_element(By.CLASS_NAME, "fb-single-line-text__input")
            if phone_input.text == "":
                phone_input.send_keys(PHONE_NUMBER)

            submit_button = driver.find_element(By.CSS_SELECTOR, "footer button span")

            if submit_button.text == "Next":
                dismiss_button = driver.find_element(By.CSS_SELECTOR, ".artdeco-modal__dismiss")
                dismiss_button.click()
                time.sleep(2)
                discard_button = driver.find_elements(By.CSS_SELECTOR, ".artdeco-modal__confirm-dialog-btn")[0]
                discard_button.click()
                print("Too many steps, skipped")
                continue
            else:
                submit_button.click()
                print("application submitted")

            time.sleep(2)
            dismiss_button = driver.find_element(By.CSS_SELECTOR, ".artdeco-modal__dismiss")
            dismiss_button.click()
        except NoSuchElementException:
            print("No Button available")
            continue


sign_in()
apply_for_all_jobs()
# apply_for_first_job()
