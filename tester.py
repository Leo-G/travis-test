from selenium import webdriver
driver=webdriver.Chrome('/usr/local/share/chromedriver')


driver.get("https://techarena51.com")
assert "Techarena51.com Tech Tutorials" in driver.title
