import requests
import yaml
from module import Site

with open("testdata.yaml") as f:
    testdata = yaml.safe_load(f)
site = Site(testdata["address"])


def test_post_existence_by_description(create_post):
    post_id = create_post
    # Проверка наличия созданного поста по его описанию
    description = "Тестовое описание нового поста"
    response = requests.get("post_path", params={"description": description})
    assert response.status_code == 200
    posts = response.json()
    assert any(post["id"] == post_id for post in posts)

# Добавленный тестовый блок для проверки создания поста после входа
with open("testdata.yaml") as f:
    testdata = yaml.safe_load(f)
site = Site(testdata["address"])

def test_step1(x_selector1, x_selector2, x_selector3, btn_selector, er1, x_selector4, er2):
    input1 = site.find_element("xpath", x_selector1)
    input1.clear()
    input1.send_keys("test")
    input2 = site.find_element("xpath", x_selector2)
    input2.clear()
    input2.send_keys("test")
    btn = site.find_element("xpath", btn_selector)
    btn.click()
    user_label = site.find_element("xpath", x_selector4)
    text = user_label.text
    site.quit()
    assert text == er2