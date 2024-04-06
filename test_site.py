import yaml
import time
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

with open('config.yaml', 'r', encoding='utf-8') as f:
    data = yaml.safe_load(f)


# Проверка отображения ошибка 401 при вводе неверного логина и пароля 
def test_step1(site, x_selector1, x_selector2, btn_selector, x_selector3, expected_error_text):
    # Находим поля для ввода логина и пароля и вводим в них значения
    input1 = site.find_element(By.XPATH, x_selector1)
    input1.send_keys('test')
    input2 = site.find_element(By.XPATH, x_selector2)
    input2.send_keys('test')
    # Находим кнопку входа и нажимаем на неё
    btn = site.find_element(By.CSS_SELECTOR, btn_selector)
    btn.click()
    # Проверяем, что отображается ожидаемая ошибка
    err_label = site.find_element(By.XPATH, x_selector3)
    assert err_label.text == expected_error_text


# Проверка успешности входа пользователя
def test_login_success(site, x_selector1, x_selector2, btn_selector, username, password):
    input1 = site.find_element(By.XPATH, x_selector1)
    input1.send_keys(username)
    input2 = site.find_element(By.XPATH, x_selector2)
    input2.send_keys(password)
    btn = site.find_element(By.CSS_SELECTOR, btn_selector)
    btn.click()

    time.sleep(3)


def test_add_post(site, site_add, post_title_selector, post_content_selector, save_post_selector, edit_post_selector):

    post_title = site_add.find_element(By.XPATH, post_title_selector)
    post_title.send_keys(data['title'])
    post_content = site_add.find_element(By.XPATH, post_content_selector)
    post_content.send_keys(data['content'])

    submit_post = site.find_element(By.XPATH, save_post_selector)
    submit_post.click()

    time.sleep(2)

    post_title_on_page = site.find_element(By.XPATH, edit_post_selector)
    assert post_title_on_page.text == "Печенюшка"
