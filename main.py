from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import os, time

urls = ["https://louis-dresbach.de", "https://dunstkunst.de", "https://bananofaucet.online"]
sizes = [[1024, 768], [390, 844]]
dir = "results/";

def main():
	global dir
	t = time.strftime("%H_%M", time.localtime())
	dir += t + "/"
	if not os.path.exists(dir):
		os.makedirs(dir)
	
	
	driver = webdriver.Chrome(ChromeDriverManager().install())
	driver.set_window_position(0, 0)
	i=0
	for u in urls:
		driver.get(u)
		for s in sizes:
			print("Getting screenshot in " + str(s[0]) + "x" + str(s[1]) + " of " + u);
			driver.set_window_size(s[0], s[1])
			time.sleep(5)
			cookieButton = driver.find_elements(By.XPATH, "//button[text()='I understand']")
			for b in cookieButton:
				b.click()
			time.sleep(1)
			screenshot = driver.save_screenshot("tmp.png")
			os.rename("tmp.png", dir + str(i) + "__" + str(s[0]) + "x" + str(s[1]) + ".png")
		
		i+=1	
		
	driver.quit()
	
	
main()