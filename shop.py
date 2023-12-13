# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get("https://practice.automationtesting.in/")
# account = driver.find_element(By.ID, "menu-item-50")
# account.click()
# username = driver.find_element(By.ID, "username")
# username.send_keys("ttd94@yandex.ru")
# password = driver.find_element(By.ID, "password")
# password.send_keys("01Qwerty!")
# login_btn = driver.find_element(By.NAME, "login")
# login_btn.click()
# shop = driver.find_element(By.CSS_SELECTOR, "#menu-item-40 > a")
# shop.click()
# html_book = driver.find_element(By.CSS_SELECTOR, ".post-181 h3")
# html_book.click()
# element = driver.find_element(By.CSS_SELECTOR, ".product_title.entry-title")
# element_get_text = element.text
# assert element_get_text == "HTML5 Forms"
# driver.quit()


# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get("https://practice.automationtesting.in/")
# account = driver.find_element(By.ID, "menu-item-50")
# account.click()
# username = driver.find_element(By.ID, "username")
# username.send_keys("ttd94@yandex.ru")
# password = driver.find_element(By.ID, "password")
# password.send_keys("01Qwerty!")
# login_btn = driver.find_element(By.NAME, "login")
# login_btn.click()
# shop = driver.find_element(By.CSS_SELECTOR, "#menu-item-40 > a")
# shop.click()
# html_cat = driver.find_element(By.CSS_SELECTOR, ".cat-item-19 > a")
# html_cat.click()
# element = driver.find_element(By.CSS_SELECTOR, ".current-cat > span")
# element_get_number = element.text
# assert element_get_number == "(3)"


# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.select import Select
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get("https://practice.automationtesting.in/")
# shop = driver.find_element(By.CSS_SELECTOR, "#menu-item-40 > a")
# shop.click()
# element = driver.find_element(By.CSS_SELECTOR, ".orderby")
# element_checked = element.get_attribute("menu_order")
# sort_desc = driver.find_element(By.CSS_SELECTOR, ".orderby")
# select = Select(sort_desc)
# select.select_by_value("price-desc")
# element = driver.find_element(By.CSS_SELECTOR, ".orderby")
# element_1_checked = element.get_attribute("price-desc")


# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.ui import WebDriverWait
# driver = webdriver.Chrome()
# driver.implicitly_wait(5)
# driver.maximize_window()
# driver.get("https://practice.automationtesting.in/")
# shop = driver.find_element(By.CSS_SELECTOR, "#menu-item-40 > a")
# shop.click()
# android_book = driver.find_element(By.CSS_SELECTOR, ".post-169 h3")
# android_book.click()
# old_price = driver.find_element(By.CSS_SELECTOR, "del > span")
# new_price = driver.find_element(By.CSS_SELECTOR, "ins > span")
# old_price_text = old_price.text
# new_price_text = new_price.text
# assert old_price_text == "₹600.00"
# assert new_price_text == "₹450.00"
# book_image = WebDriverWait(driver, 10).until(
# EC. element_to_be_clickable((By.CSS_SELECTOR, ".images")) )
# book_image.click()
# close_btn = WebDriverWait(driver, 10).until(
# EC. element_to_be_clickable((By.CSS_SELECTOR, ".pp_close")) )
# close_btn.click()
# driver.quit()


# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.ui import WebDriverWait
# driver = webdriver.Chrome()
# driver.implicitly_wait(5)
# driver.maximize_window()
# driver.get("https://practice.automationtesting.in/")
# shop = driver.find_element(By.CSS_SELECTOR, "#menu-item-40 > a")
# shop.click()
# add_btn = driver.find_element(By.CSS_SELECTOR, ".post-182 > a:nth-child(2)")
# add_btn.click()
# item = driver.find_element(By.CSS_SELECTOR, ".cartcontents")
# item_text = item.text
# assert item_text == "1 item"
# count = driver.find_element(By.CSS_SELECTOR, ".wpmenucart-contents > span:nth-child(3)")
# count_text = count.text
# assert count_text == "₹180.00"
# cart = driver.find_element(By.CSS_SELECTOR, ".wpmenucart-contents")
# cart.click()
# price_check = WebDriverWait(driver, 10).until(
# EC. text_to_be_present_in_element((By.CSS_SELECTOR, ".product-price > span"), "₹180.00") )
# total_check = WebDriverWait(driver, 10).until(
# EC. text_to_be_present_in_element((By.CSS_SELECTOR, ".product-subtotal > span"), "₹180.00") )


# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.ui import WebDriverWait
# driver = webdriver.Chrome()
# driver.implicitly_wait(5)
# driver.maximize_window()
# driver.get("https://practice.automationtesting.in/")
# shop = driver.find_element(By.CSS_SELECTOR, "#menu-item-40 > a")
# shop.click()
# add_btn = driver.find_element(By.CSS_SELECTOR, ".post-182 > a:nth-child(2)")
# add_btn.click()
# time.sleep(5)
# item = driver.find_element(By.CSS_SELECTOR, ".cartcontents")
# item_text = item.text
# assert item_text == "1 Item"
# count = driver.find_element(By.CSS_SELECTOR, ".wpmenucart-contents > span:nth-child(3)")
# count_text = count.text
# assert count_text == "₹180.00"
# cart = driver.find_element(By.CSS_SELECTOR, ".wpmenucart-contents")
# cart.click()
# price_check = WebDriverWait(driver, 10).until(
# EC. text_to_be_present_in_element((By.CSS_SELECTOR, ".product-price > span"), "₹180.00") )
# total_check = WebDriverWait(driver, 10).until(
# EC. text_to_be_present_in_element((By.CSS_SELECTOR, ".product-subtotal > span"), "₹180.00") )



# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.ui import WebDriverWait
# driver = webdriver.Chrome()
# driver.implicitly_wait(5)
# driver.maximize_window()
# driver.get("https://practice.automationtesting.in/")
# shop = driver.find_element(By.CSS_SELECTOR, "#menu-item-40 > a")
# shop.click()
# driver.execute_script("window.scrollBy(0, 300);")
# add_html = driver.find_element(By.CSS_SELECTOR, ".post-182 > a:nth-child(2)")
# add_html.click()
# time.sleep(2)
# add_js_data = driver.find_element(By.CSS_SELECTOR, ".post-180 > a:nth-child(2)")
# add_js_data.click()
# time.sleep(2)
# cart = driver.find_element(By.ID, "wpmenucartli")
# cart.click()
# delete_1 = driver.find_element(By.XPATH, "//a[@data-product_id='182']")
# delete_1.click()
# time.sleep(2)
# undo = driver.find_element(By.CSS_SELECTOR, ".woocommerce-message > a")
# undo.click()
# input = driver.find_element(By.CSS_SELECTOR, ".quantity > input")
# input.clear()
# input.send_keys("3")
# update_btn = driver.find_element(By.NAME, "update_cart")
# update_btn.click()
# time.sleep(2)
# apply_coupon_btn = driver.find_element(By.NAME, "apply_coupon")
# apply_coupon_btn.click()
# error = driver.find_element(By.CSS_SELECTOR, ".woocommerce-error")
# error_get_text = error.text
# assert error_get_text == "Please enter a coupon code."



# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support.select import Select
# driver = webdriver.Chrome()
# driver.implicitly_wait(5)
# driver.maximize_window()
# driver.get("https://practice.automationtesting.in/")
# shop = driver.find_element(By.CSS_SELECTOR, "#menu-item-40 > a")
# shop.click()
# driver.execute_script("window.scrollBy(0, 300);")
# add_html = driver.find_element(By.CSS_SELECTOR, ".post-182 > a:nth-child(2)")
# add_html.click()
# time.sleep(5)
# cart = driver.find_element(By.ID, "wpmenucartli")
# cart.click()
# checkout_btn = WebDriverWait(driver, 10).until(
# EC. element_to_be_clickable((By.CSS_SELECTOR, ".checkout-button")) )
# checkout_btn.click()
# first_name = WebDriverWait(driver, 10).until(
# EC. visibility_of_element_located((By.ID, "billing_first_name")) )
# first_name.send_keys("Elon")
# last_name = driver.find_element(By.ID, "billing_last_name")
# last_name.send_keys("Musk")
# email = driver.find_element(By.ID, "billing_email")
# email.send_keys("ttd94@yandex.ru")
# phone = driver.find_element(By.ID, "billing_phone")
# phone.send_keys("111222333")
# country = driver.find_element(By.ID, "s2id_billing_country")
# country.click()
# input_country = driver.find_element(By.ID, "s2id_autogen1_search")
# input_country.send_keys("Colombia")
# result = driver.find_element(By.ID, "select2-results-1")
# result.click()
# address = driver.find_element(By.CSS_SELECTOR, "#billing_address_1_field > input")
# address.send_keys("Lenina")
# town = driver.find_element(By.CSS_SELECTOR, "#billing_city_field > input")
# town.send_keys("York")
# state = driver.find_element(By.CSS_SELECTOR, "#billing_state_field > input")
# state.send_keys("USA")
# driver.execute_script("window.scrollBy(0, 600);")
# time.sleep(5)
# check_payments = driver.find_element(By.ID, "payment_method_cheque")
# check_payments.click()
# place_order_btn = driver.find_element(By.ID, "place_order")
# place_order_btn.click()
# state = driver.find_element(By.CSS_SELECTOR, "#billing_state_field > input")
# text_check = WebDriverWait(driver, 10).until(
# EC. text_to_be_present_in_element((By.CSS_SELECTOR, ".woocommerce-thankyou-order-received"), "Thank you. Your order has been received.") )
# text_check_1 = WebDriverWait(driver, 10).until(
# EC. text_to_be_present_in_element((By.CSS_SELECTOR, ".method"), "Check Payments") )
