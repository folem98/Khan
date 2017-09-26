from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

# example option: add 'incognito' command line arg to options
option = webdriver.ChromeOptions()
option.add_argument("--incognito")

# create new instance of chrome in incognito mode
browser = webdriver.Chrome(executable_path='/Library/Application Support/Google/chromedriver', chrome_options=option)

# go to website of interest
browser.get("https://finance.yahoo.com/quote/FB?p=FB")

# wait up to 10 seconds for page to load
timeout = 10
try:
    WebDriverWait(browser, timeout).until(EC.visibility_of_element_located((By.XPATH, "//a[@class='Va(m) C($finDarkLink) Wow(bw) Us(n)']")))
except TimeoutException:
    print("Timed out waiting for page to load")
    browser.quit()


# get all of the titles for the financial values
titles_element = browser.find_elements_by_xpath("//td[@class='D(ib)']")
titles = [x.text for x in titles_element]
'''
WRITTEN AS A NORMAL FOR LOOP:
titles = []
for x in titles_element:
    titles.append(x.text)
'''
print('titles:')
print(titles)


# get all of the financial values themselves
values_element = browser.find_elements_by_xpath("//td[@class='Ta(end) Fw(b)']")
values = [x.text for x in values_element]  # same concept as for-loop/list-comprehension above
print('values:')
print(values, '\n')


# pair each title with its corresponding value using zip function and print each pair
for title, value in zip(titles, values):
    print(title + ': ' + value)