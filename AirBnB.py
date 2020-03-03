import time	
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


#open page
driver = webdriver.Firefox()
driver.get("https://www.airbnb.co.in")

navigationStart = driver.execute_script("return window.performance.timing.navigationStart")
responseStart = driver.execute_script("return window.performance.timing.responseStart")
domComplete = driver.execute_script("return window.performance.timing.domComplete")

backendPerformance = responseStart - navigationStart
frontendPerformance = domComplete - responseStart
 
print("Back End: %s" % backendPerformance)
print("Front End: %s" % frontendPerformance )

driver.maximize_window();

elem_cookieok = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[4]/div[2]/div/button')
elem_where = driver.find_element_by_name("query")
elem_checkin = driver.find_element_by_name("checkin")
elem_checkout = driver.find_element_by_name("checkout")
elem_guests = driver.find_element_by_id("lp-guestpicker")
elem_search = driver.find_element_by_xpath('//*[@id="FMP-target"]/div/div[1]/div/div/div/div/div/div[2]/div/form/div[4]/div/button/span')

#click ok for cookie
elem_cookieok.click()

#Enter Destination
elem_where.clear()
elem_where.send_keys("munnar")
elem_where.send_keys(Keys.ESCAPE)

#Enter checkin dat
elem_checkin.click()
elem_checkinNextMonth = driver.find_element_by_xpath('/html/body/div[5]/div/div/div[1]/main/section/div/div/div[1]/div/div/div/div/div/div[2]/div/form/div[2]/div/div/div/div[2]/div/div/div/div/div/div[2]/div[1]/div[2]')
elem_checkinNextMonth.click()
elem_checkindate = driver.find_element_by_xpath('//*[@id="FMP-target"]/div/div[1]/div/div/div/div/div/div[2]/div/form/div[2]/div/div/div/div[2]/div/div/div/div/div/div[2]/div[2]/div/div[2]/div/table/tbody/tr[2]/td[1]')
elem_checkindate.click()


#Enter Checkout date
elem_checkoutdate = driver.find_element_by_xpath('//*[@id="FMP-target"]/div/div[1]/div/div/div/div/div/div[2]/div/form/div[2]/div/div/div/div[3]/div/div/div/div/div/div[2]/div[2]/div/div[2]/div/table/tbody/tr[2]/td[2]')
elem_checkoutdate.click()
elem_guests.click()

#Enter guests
elem_guestadd = driver.find_element_by_xpath('//*[@id="FMP-target"]/div/div[1]/div/div/div/div/div/div[2]/div/form/div[3]/div/div[2]/div/div/div[1]/div[1]/div/div/div/div[2]/div/div[3]/button')
elem_guestadd.click()
elem_guestadd.click()
elem_guests.click()
elem_search.click()
time.sleep(10)


driver.close()


