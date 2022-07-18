import unittest
import os
os.environ['TESTING'] = 'true'

from app import app

class AppTestCase(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_home(self):
        response = self.client.get("/")
        assert response.status_code == 200
        html = response.get_data(as_text=True)
        assert "<title>ABOUT ME</title>" in html
        assert '<meta charset="utf-8">' in html
        # assert '<meta property="og:url" content="localhost:5000">' in html
        

    def test_timeline(self):
        self.client.delete("/api/timeline_post_clear")
        response = self.client.get("/api/timeline_post")
        assert response.status_code == 200
        assert response.is_json
        json = response.get_json()
        assert "timeline_posts" in json
        assert len(json['timeline_posts']) == 0
        post_test = self.client.post('/api/timeline_post', 
        data = {'name':'ronald', 'email':'ronald@mail.com', 'content': 'content' })
        assert post_test.status_code == 200
        assert post_test.is_json
        post_test_json = post_test.get_json()
        assert post_test_json['name'] == 'ronald'
        assert post_test_json['email'] == 'ronald@mail.com'
        get_test = self.client.get('/api/timeline_post')
        get_test_json = get_test.get_json()
        assert get_test_json['timeline_posts'][0]['name'] ==  'ronald'

    def test_malformed_timeline_post(self):
        #POST request missing name
        response = self.client.post("/api/timeline_post", data=
        {"name":'',"email": "John@example.com", "content": "Hello World, I'm John"})
        assert response.status_code == 400
        response_text = response.get_data(as_text=True)
        assert "Invalid name" in response_text

        #POST request with empty content
        response = self.client.post("/api/timeline_post", data=
        {"name": "John Doe", "email": "john@example.com", "content": ""})
        assert response.status_code == 400
        response_text = response.get_data(as_text=True)
        assert "Invalid content" in response_text

        #POST request with malformed email 
        response = self.client.post('/api/timeline_post', data=
        {'name': "John Doe", "email": "not-an-email", "content": "Hello world, I'm John!"})
        assert response.status_code == 400
        response_text = response.get_data(as_text=True)
        assert "Invalid email" in response_text