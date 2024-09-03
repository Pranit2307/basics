# import time
#
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.select import Select
#
# from selenium import webdriver
# driver  =  webdriver.Chrome()
# driver.get("https://automationexercise.com/")
# # driver.find_element(By.XPATH,"//button[@class='btn btn-success' and @type='button']").click()
# import requests
# list_of_requests = dir(requests)
# for  request in list_of_requests:
#     print(request)
# head_ofsite= requests.head("https://automationexercise.com/")
# print(head_ofsite)
import time

import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
#
# # Use the requests module to send a HEAD request to the site
# head_of_site = requests.head("https://automationexercise.com/")
#
# # Print the status code and headers from the HEAD request
# print(f"Status Code: {head_of_site.status_code}")
# print(f"Headers: {head_of_site.headers}")
# print(f"Headers: {head_of_site.cookies}")
#
# # If the status code is 200, proceed with Selenium
# if head_of_site.status_code == 200:
#     # Set up the Selenium WebDriver
#     driver = webdriver.Chrome()
#
#     # Open the website using Selenium
#     driver.get("https://automationexercise.com/")
#
#     # Example of interacting with the website using Selenium
#     # For example, you might want to click on a button or fill out a form
#     # driver.find_element(By.XPATH, "//button[@class='btn btn-success' and @type='button']").click()
# #
# #     # You can use requests to fetch or post data while working with Selenium
# #     response = requests.get("https://automationexercise.com/api/endpoint")  # Example API endpoint
# #     print(response.json())  # Assuming the API returns JSON data
# #
# #     # Close the browser after the operations
# #     driver.quit()
# # else:
# #     print("The site is not reachable or is down. Exiting...")
# #
# # # Example of listing all attributes in the requests module
# # list_of_requests = dir(requests)
# # for request_item in list_of_requests:
# #     print(request_item)
# # #
# from selenium.webdriver.support.ui import Select
# from selenium import webdriver
# driver = webdriver.Chrome()
# driver.get("https://www.flipkart.com/tyy/4io/~cs-6i0duusqlz/pr?sid=tyy%2C4io&collection-tab-name=Realme+P1+5g&param=6372&ctx=eyJjYXJkQ29udGV4dCI6eyJhdHRyaWJ1dGVzIjp7InZhbHVlQ2FsbG91dCI6eyJtdWx0aVZhbHVlZEF0dHJpYnV0ZSI6eyJrZXkiOiJ2YWx1ZUNhbGxvdXQiLCJpbmZlcmVuY2VUeXBlIjoiVkFMVUVfQ0FMTE9VVCIsInZhbHVlcyI6WyJGcm9tIOKCuTE0LDk5OSJdLCJ2YWx1ZVR5cGUiOiJNVUxUSV9WQUxVRUQifX0sInRpdGxlIjp7Im11bHRpVmFsdWVkQXR0cmlidXRlIjp7ImtleSI6InRpdGxlIiwiaW5mZXJlbmNlVHlwZSI6IlRJVExFIiwidmFsdWVzIjpbIlJlYWxtZSBQMSA1ZyJdLCJ2YWx1ZVR5cGUiOiJNVUxUSV9WQUxVRUQifX0sImhlcm9QaWQiOnsic2luZ2xlVmFsdWVBdHRyaWJ1dGUiOnsia2V5IjoiaGVyb1BpZCIsImluZmVyZW5jZVR5cGUiOiJQSUQiLCJ2YWx1ZSI6Ik1PQkdZUTZCRUhIUTlIN1giLCJ2YWx1ZVR5cGUiOiJTSU5HTEVfVkFMVUVEIn19fX19")
# elemrnt = '//*[@id="container"]/div/div[3]/div[1]/div[1]/div/div/div/section[3]/div[2]/div/div/div/label/div[1]'
# checkbox = driver.find_element(By.XPATH,elemrnt)
# print("Done")
# if checkbox.is_selected():
#     print("Checkbox is selected.")
# else:
#     print("Checkbox is not selected")
# checkbox.click()
# time.sleep(10)
# if checkbox.is_selected():
#     print("Checkbox is selected.")
# else:
#     print("Checkbox is not selected")
#
#
# driver.quit()
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize WebDriver
driver = webdriver.Chrome()

# Open the web page
driver.get("https://www.flipkart.com/tyy/4io/~cs-6i0duusqlz/pr?sid=tyy%2C4io&collection-tab-name=Realme+P1+5g&param=6372&ctx=eyJjYXJkQ29udGV4dCI6eyJhdHRyaWJ1dGVzIjp7InZhbHVlQ2FsbG91dCI6eyJtdWx0aVZhbHVlZEF0dHJpYnV0ZSI6eyJrZXkiOiJ2YWx1ZUNhbGxvdXQiLCJpbmZlcmVuY2VUeXBlIjoiVkFMVUVfQ0FMTE9VVCIsInZhbHVlcyI6WyJGcm9tIOKCuTE0LDk5OSJdLCJ2YWx1ZVR5cGUiOiJNVUxUSV9WQUxVRUQifX0sInRpdGxlIjp7Im11bHRpVmFsdWVkQXR0cmlidXRlIjp7ImtleSI6InRpdGxlIiwiaW5mZXJlbmNlVHlwZSI6IlRJVExFIiwidmFsdWVzIjpbIlJlYWxtZSBQMSA1ZyJdLCJ2YWx1ZVR5cGUiOiJNVUxUSV9WQUxVRUQifX0sImhlcm9QaWQiOnsic2luZ2xlVmFsdWVBdHRyaWJ1dGUiOnsia2V5IjoiaGVyb1BpZCIsImluZmVyZW5jZVR5cGUiOiJQSUQiLCJ2YWx1ZSI6Ik1PQkdZUTZCRUhIUTlIN1giLCJ2YWx1ZVR5cGUiOiJTSU5HTEVfVkFMVUVEIn19fX19")

# Define the XPath of the checkbox
elemrnt = '//*[@id="container"]/div/div[3]/div[1]/div[1]/div/div/div/section[3]/div[2]/div/div/div/label/div[1]'

# Wait until the checkbox is clickable
wait = WebDriverWait(driver, 10)
checkbox = wait.until(EC.element_to_be_clickable((By.XPATH, elemrnt)))

# Check the initial state of the checkbox
if checkbox.is_selected():
    print("Checkbox is selected.")
else:
    print("Checkbox is not selected.")

# Click the checkbox
checkbox.click()

# Wait for the state change to reflect
wait.until(lambda driver: checkbox.is_selected() != checkbox.is_selected())

# Check the state after clicking
if checkbox.is_selected():
    print("Checkbox is selected.")
else:
    print("Checkbox is not selected.")

# Close the WebDriver
driver.quit()
