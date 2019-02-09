from selenium import webdriver
browser="ie"
if browser=="chrome":
    driver=webdriver.Chrome(executable_path="C:/Users/Heggade/PycharmProjects/s_class/drivers/chromedriver.exe")
elif browser=="firefox":
    driver=webdriver.Firefox(executable_path="C:/Users/Heggade/PycharmProjects/s_class/drivers/geckodriver.exe")
elif browser=="ie":
    driver=webdriver.Ie(executable_path="C:/Users/Heggade/PycharmProjects/s_class/drivers/IEDriverServer.exe")
else:
    print("provide appropriate browser name")
driver.get("http://facebook.com")
driver.maximize_window()
driver.find_element_by_id("email").send_keys("test")
driver.find_element_by_id("pass").send_keys("pass")
driver.find_element_by_id("u_0_2").click()

driver.get 