from selenium import webdriver
from selenium.webdriver.common.by import By
import pyautogui
from time import sleep

driver = webdriver.Firefox()
driver.install_addon('./adblock.xpi')
driver.install_addon('./xdm.xpi')
driver.maximize_window()
driver.get("https://anime-sama.fr/catalogue/oregairu/saison1/vostfr/")
sleep(5)
 
driver.switch_to.window(driver.window_handles[1])
sleep(2)
pp=driver.find_element(By.CSS_SELECTOR,"#accept")
print(pp.text)
pp.click()

# for window_handle in driver.window_handles:
#     driver.switch_to.window(window_handle)
#     sleep(2)

# print(driver.window_handles)
# print(driver.find_element(By.CSS_SELECTOR,"#selectLecteurs > option:nth-child(2)").text)
# driver.find_element(By.CSS_SELECTOR,"#selectLecteurs > option:nth-child(2)").click()
# driver.find_element(By.CSS_SELECTOR,".css-k8o10q").click()
# sleep(3)
# driver.find_element(By.CSS_SELECTOR,"#selectEpisodes > option:nth-child(10)").click()

# print(pyautogui.displayMousePosition())
# # driver = webdriver.Firefox()
# # # driver.install_addon('./adblock.xpi')
# # # driver.install_addon('./xdm.xpi')
# # driver.maximize_window()
# # # driver.get(link)
# # driver.get('https://anime-sama.fr/catalogue/classroom-of-the-elite/saison3/vostfr/')
# # sleep(1)
# # name = driver.find_element(By.CSS_SELECTOR, "#titreOeuvre").text
# # season = driver.find_element(By.CSS_SELECTOR, "#avOeuvre").text

# # print(name)
# # print(season)
# # driver.close()