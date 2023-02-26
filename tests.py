import requests


def test_hello_world():
    res = requests.get("http://127.0.0.1:8001/")
    assert 200 == res.status_code
    assert "Hello, world!" == res.text


def test_tasks_list():
    res = requests.get("http://127.0.0.1:8001/tasks")
    assert 200 == res.status_code
    assert "tasks" in res.json()
    assert 2 == len(res.json()["tasks"])
    assert "One Take" == res.json()["tasks"][0]["title"]


def test_tasks_detail():
    res = requests.get("http://127.0.0.1:8001/tasks/123")
    assert 200 == res.status_code
    assert 123 == res.json()["id"]
    assert "One Take" == res.json()["title"]


def test_not_found():
    res = requests.get("http://127.0.0.1:8001/lost")
    assert 404 == res.status_code
    res = requests.get("http://127.0.0.1:8001/tasks/678")
    assert 404 == res.status_code
