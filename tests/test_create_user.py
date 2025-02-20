import os
import jwt
import datetime
from fastapi.testclient import TestClient
from app.main import app
from app.auth import users_db  

class TestRegisterEndpoint:
    @classmethod
    def setup_class(cls):
        cls.client = TestClient(app)
        cls.secret_key = os.getenv("SECRET_KEY") 

    def get_test_token(self, role="admin"):
        token = jwt.encode(
            {
                "sub": "admin",
                "idUser": "admin_id",
                "role": role,
                "exp": datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(hours=1),
            },
            self.secret_key,
            algorithm= os.getenv("ALGORITHM"),
        )
        return token

    def test_register_success(self):
        
        new_username = "testUserRegister"
        if new_username in users_db:
            del users_db[new_username]

        new_user_payload = {
            "username": new_username,
            "password": "TestPassword123!",
            "role": "questionUser"
        }
        token = self.get_test_token("admin")
        headers = {"Authorization": f"Bearer {token}"}
        response = self.client.post("api/v1/users/register", json=new_user_payload, headers=headers)
        assert response.status_code == 200, f"Error: {response.text}"
        json_data = response.json()
        
        assert "data" in json_data
        data = json_data["data"]
        assert data["username"] == new_username

    def test_register_forbidden(self):
       
        new_user_payload = {
            "username": "forbiddenUser",
            "password": "TestPassword123!",
            "role": "questionUser"
        }
        token = self.get_test_token("questionUser")  
        headers = {"Authorization": f"Bearer {token}"}
        response = self.client.post("api/v1/users/register", json=new_user_payload, headers=headers)
        assert response.status_code == 403

    def test_register_existing_user(self):
        
        new_username = "existingUser"
        new_user_payload = {
            "username": new_username,
            "password": "TestPassword123!",
            "role": "questionUser"
        }
        token = self.get_test_token("admin")
        headers = {"Authorization": f"Bearer {token}"} 

        response1 = self.client.post("api/v1/users/register", json=new_user_payload, headers=headers)
        assert response1.status_code == 200    

        response2 = self.client.post("api/v1/users/register", json=new_user_payload, headers=headers)
        assert response2.status_code == 400
