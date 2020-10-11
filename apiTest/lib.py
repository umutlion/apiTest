import requests


class UmutApi:
    def __init__(self, address):
        self.address = address

        self.headers = {
            "Content-Type": "application/json"
        }

        self.posts_url = f"http://{self.address}/apiTest/posts/"

    def create_post(self, title, content, author, email, category=None):
        data = {
            "title": title,
            "content": content,
            "author": author,
            "email": email,
            "category": category
        }

        response = requests.post(url=self.posts_url, json=data, headers=self.headers)
        return response.json()

    def update_post(self, post_id, title, content, author, email, category=None):
        data = {
            "title": title,
            "content": content,
            "author": author,
            "email": email,
            "category": category
        }

        update_url = f"{self.posts_url}{post_id}/"
        response = requests.put(url=update_url, json=data, headers=self.headers)
        return response.json()


umut = UmutApi(address="localhost:8000")

# response_json = umut.create_post("json1", "content json 1", "json author", "emailjson@gmail.com", 1)
response_json = umut.update_post(10, "json1", "modified json 1", "json author", "emailjson@gmail.com", 1)
print(response_json)
