import selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import ActionChains
from openpyxl import Workbook


options = Options()
options.add_argument("--window-size=1920,1080")


website = "https://www.amazon.in/"
driver = webdriver.Chrome(options=options)
driver.get(website)
driver.maximize_window()
driver.implicitly_wait(10)
searchm=driver.find_element_by_xpath("//input[@id='twotabsearchtextbox']")
searchm.clear()
searchm.send_keys("Samsung Phon")
submit_button=driver.find_element_by_xpath("//input[@id='nav-search-submit-button']")
submit_button.click()
samsung_checkbox=driver.find_element_by_xpath("//span[text()='Samsung']")
samsung_checkbox.click()
phon_names=driver.find_elements_by_xpath("//span[contains(@class,'a-color-base a-text-normal')]")
phon_prices=driver.find_elements_by_xpath("//span[contains(@class,'a-price-whole')]")

myphon=[]
myprice=[]

for phon in phon_names:
    myphon.append(phon.text)
    

for price in phon_prices:
    myprice.append(price.text)

finallist=zip(myphon,myprice)

# for data in list(finallist):
#     print(data)
wb=Workbook()
wb['Sheet'].title='Samsung data'
sh1=wb.active
sh1.append(['Name','Price'])
for x in list(finallist):
    sh1.append(x)

wb.save('finalList.xlsx')

driver.close()