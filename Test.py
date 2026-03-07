from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver import Chrome,ChromeOptions
from time import sleep

from selenium.webdriver.common.keys import Keys

o = ChromeOptions()
o.add_experimental_option("detach", True)
driver = Chrome(options=o)


# driver.get("https://amazon.in")
# driver.maximize_window()
# sleep(2)
#
# a= driver.find_elements("class name","nav-a")
# for i in a:
#     print(i.text)
#
#
# driver.quit()


# driver.get("https://www.imdb.com/chart/top/")
# driver.maximize_window()
# sleep(2)
#
# a = driver.find_elements("class name","ipc-title__text")
# for i in range(10):
#     print(a[i].text)



# driver.get("https://amazon.in")
# driver.maximize_window()
# sleep(2)
# a = driver.find_elements("xpath","//img")
# print(len(a))




# driver.get("https://www.amazon.in/")
# driver.maximize_window()
# sleep(2)
# a = driver.find_elements("xpath","//a")
# for i in a:
#     print(i.get_attribute("href"))
#




# driver.get("https://www.amazon.in/")
# driver.maximize_window()
# sleep(2)
# driver.find_element("xpath","//input[@id ='twotabsearchtextbox']").send_keys("phone")
# sleep(5)
# a = driver.find_elements("class name","s-suggestion-container")
# for i in a:
#     print(i.text)



# driver.get("https://amazon.in/")
# driver.maximize_window()
# sleep(4)
# driver.get("https://amazon.in/")
# driver.maximize_window()
# a=driver.find_element("id","nav-link-accountList")
# o = ActionChains(driver)
# o.move_to_element(a).perform()
# sleep(2)
#
# driver.find_element("link text","Your Wish List").click()







# driver.get("https://www.w3schools.com/html/tryit.asp?filename=tryhtml_iframe")
# driver.maximize_window()
# a=driver.find_element("xpath","//iframe[@id='iframeResult']")
# driver.switch_to.frame(a)
#
# b = driver.find_element("xpath","//iframe[@src = 'demo_iframe.htm']")
# driver.switch_to.frame(b)
# c = driver.find_element("xpath","//h1")
# print(c.text)








driver.get("https://www.amazon.in/")
driver.maximize_window()
sleep(3)
a = driver.find_element("id","twotabsearchtextbox")
a.send_keys("Laptop")
a.send_keys(Keys.ENTER)
sleep(3)
titles = driver.find_elements("xpath","//h2//span")

for t in titles:
    print(t.text)