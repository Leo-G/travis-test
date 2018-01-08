from selenium import webdriver
driver=webdriver.Chrome('chromedriver_win32/chromedriver.exe')


driver.get("https://techarena51.com")
assert "Techarena51.com Tech Tutorials" in driver.title
