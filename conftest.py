import pytest
import requests
import yaml
from ddt import data

with open("./testdata.yaml") as f:
    testdata = yaml.safe_load(f)
name = testdata["username"]
@pytest.fixture()
def x_selector1():
    return """//*[@id="login"]/div[1]/label/input"""
@pytest.fixture()
def x_selector2():
    return """//*[@id="login"]/div[2]/label/input"""
@pytest.fixture()
def x_selector3():
    return """//*[@id="app"]/main/div/div/div[2]/h2"""
@pytest.fixture()
def btn_selector():
    return """button"""
@pytest.fixture()
def x_selector4():
    return """//*[@id="app"]/main/nav/ul/li[3]/a"""
@pytest.fixture()
def er2():
    return "Hello, {}".format(name)
@pytest.fixture()
def login():
    res1 = requests.post(data["address"] + "getway/login",
                         data={"username": data["username"], "password": data["password"]})
    print(res1.content)
    return res1.json()["token"]
@pytest.fixture()
def create_post(login):
    # Создание нового поста
    post_data = {
        "title": "Новый пост",
        "description": "Тестовое описание нового поста",
        "content": "Содержание нового поста"
    }
    # Добавляем токен авторизации в заголовок
    headers = {"Authorization": login}
    response = requests.post("post_path", json=post_data, headers=headers)
    assert response.status_code == 200
    post_id = response.json()["id"]
    yield post_id  # Передача ID созданного поста в качестве значения фикстуры
    # После завершения теста удаление созданного поста
    delete_response = requests.delete(f"post_path/{post_id}", headers=headers)
    assert delete_response.status_code == 200