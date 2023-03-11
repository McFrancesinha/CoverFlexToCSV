import selenium
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import datetime
import time
import csv
import json
import os
import tkinter as tk

# Load email and password from json file
with open('credentials.txt', 'r') as file:
    credentials = json.load(file)
    email = credentials['email']
    password = credentials['password']

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://my.coverflex.com/signin")
WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="email"]')))

# Write Email
driver.find_element(
    By.XPATH, '//*[@id="email"]').send_keys(email)

# Write Pass
driver.find_element(
    By.XPATH, '//*[@id="password"]').send_keys(password)

# click signin
input_element = driver.find_element(
    By.XPATH, '//*[@id="root"]/div/div[1]/div[2]/div/form/button')
input_element.click()

# click continue
def continue_clicked():
    popup.destroy()

popup = tk.Tk()

popup.title("Popup")
popup.geometry("500x100")

label = tk.Label(popup, text="Insert authentication code and then click continue to proceed")
label.pack(pady=10)

continue_button = tk.Button(popup, text="Continue", command=continue_clicked)
continue_button.pack(pady=10)

popup.mainloop()

WebDriverWait(driver, 5).until(
    EC.visibility_of_element_located((By.XPATH, '//*[@id="root"]/div/div/div/div[2]/div/div[3]/div/a[2]')))

# click Meal
input_element = driver.find_element(
    By.XPATH, '//*[@id="root"]/div/div/div/div[2]/div/div[3]/div/a[2]')
input_element.click()

WebDriverWait(driver, 5).until(
    EC.visibility_of_element_located((By.XPATH, '//*[@id="root"]/div/div/div/div[5]/div/div[3]/div[2]/div[1]/div[2]')))

# gather lists of restaurants, dates and amounts
restaurants = driver.find_elements(By.XPATH,
                                   "//div[@class='text-module_large__gh5AX text-module_host__SrxSM text-module_grey-1__QMqNa _description_ok44e_36']/span")
dates = driver.find_elements(By.XPATH,
                             "//div[@class='text-module_medium__U0QfA text-module_host__SrxSM text-module_grey-2__bXlI8 _date_ok44e_32']")
amount = driver.find_elements(By.XPATH,
                              "//div[@class='text-module_large__gh5AX text-module_host__SrxSM text-module_grey-1__QMqNa text-module_bold__G51FJ _amount_ok44e_40']")
amount_topup = driver.find_elements(By.XPATH,
                                    "//div[@class='text-module_large__gh5AX text-module_host__SrxSM text-module_grey-1__QMqNa text-module_bold__G51FJ _amount_ok44e_40 _green_ok44e_107']")

rows = []

for restaurant in restaurants:
    if restaurant.text == 'meal top-up':
        if len(amount_topup) > 0:
            rows.append([restaurant.text, dates[0].text, amount_topup[0].text.replace(",", ".")])
            amount_topup.pop(0)
            dates.pop(0)
    else:
        if len(amount) > 0:
            rows.append([restaurant.text, dates[0].text, amount[0].text.replace(",", ".")])
            amount.pop(0)
            dates.pop(0)

# insert into csv
timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
filename = "meal_" + timestamp + ".csv"
download_folder = os.path.expanduser("~/Downloads")
file_path = os.path.join(download_folder, filename)

with open(file_path, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Restaurant', 'Date', 'Amount'])
    writer.writerows(rows)

# click Benefits
input_element = driver.find_element(
    By.XPATH, "/html/body/div[1]/div/div/div/div[2]/div/div[3]/div/a[3]")
input_element.click()

WebDriverWait(driver, 5).until(
    EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div/div[5]/div/div[5]/h3')))

# gather lists of benefits, dates and amounts
benefits = driver.find_elements(By.XPATH,
                                "//div[@class='text-module_large__gh5AX text-module_host__SrxSM text-module_grey-1__QMqNa _description_ok44e_36']/span")
b_dates = driver.find_elements(By.XPATH,
                               "//div[@class='text-module_medium__U0QfA text-module_host__SrxSM text-module_grey-2__bXlI8 _date_ok44e_32']")
b_amount = driver.find_elements(By.XPATH,
                                "//div[@class='text-module_large__gh5AX text-module_host__SrxSM text-module_grey-1__QMqNa text-module_bold__G51FJ _amount_ok44e_40']")
b_amount_topup = driver.find_elements(By.XPATH,
                                      "//div[@class='text-module_large__gh5AX text-module_host__SrxSM text-module_grey-1__QMqNa text-module_bold__G51FJ _amount_ok44e_40 _green_ok44e_107']")

rows = []

for benefit in benefits:
    if benefit.text == 'benefits top-up':
        if len(b_amount_topup) > 0:
            rows.append([benefit.text, b_dates[0].text, b_amount_topup[0].text.replace(",", ".")])
            b_amount_topup.pop(0)
            b_dates.pop(0)
    else:
        if len(b_amount) > 0:
            rows.append([benefit.text, b_dates[0].text, b_amount[0].text.replace(",", ".")])
            b_amount.pop(0)
            b_dates.pop(0)

# insert into csv
timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
filename = "benefits_" + timestamp + ".csv"
download_folder = os.path.expanduser("~/Downloads")
file_path = os.path.join(download_folder, filename)

with open(file_path, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Benefits', 'Date', 'Amount'])
    writer.writerows(rows)

driver.quit()

print("Meals and Benefits extraction finished.")
