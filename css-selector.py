import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "index.html")

driver.get("file:///" + file_path.replace("\\", "/"))

print("========================================")
print("             CSS SELECTOR               ")
print("========================================")

student = driver.find_element(By.CSS_SELECTOR, ".student")
print("1. Class Selector :", student.text)

student2 = driver.find_element(
    By.CSS_SELECTOR,
    'div.student[data-role="student"]'
)
print("2. Multiple Attribute :", student2.text)

child = driver.find_element(By.CSS_SELECTOR, "#parent > p")
print("3. Direct Child :", child.text)

sub_child = driver.find_element(
    By.CSS_SELECTOR,
    "#parent .sub-child"
)
print("4. Sub-Child :", sub_child.text)

sibling = driver.find_element(
    By.CSS_SELECTOR,
    "#next-heading + p"
)
print("5. Next Sibling :", sibling.text)

first = driver.find_element(
    By.CSS_SELECTOR,
    "#student-list li:first-child"
)
print("6. First Child :", first.text)

last = driver.find_element(
    By.CSS_SELECTOR,
    "#student-list li:last-child"
)
print("7. Last Child :", last.text)

nth = driver.find_element(
    By.CSS_SELECTOR,
    "#student-list li:nth-child(5)"
)
print("8. nth Child :", nth.text)

last_nth = driver.find_element(
    By.CSS_SELECTOR,
    "#student-list li:nth-last-child(2)"
)
print("9. nth-last Child :", last_nth.text)

print("========================================")
print("PRACTICAL COMPLETED SUCCESSFULLY!")
print("========================================")

time.sleep(5)
driver.quit()