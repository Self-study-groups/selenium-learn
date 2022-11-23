from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://id.carousell.com/categories/mobile-phones-338/iphones-1235/?addRecent=true&canChangeKeyword=true&includeSuggestions=true&sc=0a0208301a0408cca464220a0a066950686f6e6578012a170a0b636f6c6c656374696f6e7312060a043132333578013204080578013a02180742060801100118004a0620012801400150015a020801&search=iPhone&searchId=2eAFPm&sort_by=5")

# #main > div.D_aZm > div > div.D_aZy > main > div > div > div:nth-child(1) > div:nth-child > div > div.D_jG > a:nth-child(2) > p.D_jm.D_gQ.D_jn.D_jq.D_jt.D_jw.D_jy.D_ju.D_jj

judul = driver.find_element(By.CSS_SELECTOR,'#main > div.D_aZm > div > div.D_aZy > main > div > div > div:nth-child(1) > div:nth-child > div > div.D_jG > a:nth-child(2) > p.D_jm.D_gQ.D_jn.D_jq.D_jt.D_jw.D_jy.D_ju.D_jj').text
print(judul)

driver.quit()

# judul 1
# #main > div.D_aZm > div > div.D_aZy > main > div > div > div:nth-child(1) > div:nth-child > div > div.D_jG > a:nth-child(2) > p.D_jm.D_gQ.D_jn.D_jq.D_jt.D_jw.D_jy.D_ju.D_jj
# judul 2
# #main > div.D_aZm > div > div.D_aZy > main > div > div > div:nth-child(1) > div:nth-child(2) > div > div.D_jG > a:nth-child(2) > p.D_jm.D_gQ.D_jn.D_jq.D_jt.D_jw.D_jy.D_ju.D_jj