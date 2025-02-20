import os
import jwt
import datetime
from fastapi.testclient import TestClient
from app.main import app

class TestSuggest:
    @classmethod
    def setup_class(cls):
        cls.client = TestClient(app)       
        cls.secret_key = os.getenv("SECRET_KEY") 

    def get_test_token(self, role="questionUser"):
        token = jwt.encode(
            {
                "sub": "userQuestion",
                "idUser": "8aa1a5f6-680e-435d-9367-ef57bdaca5b8",
                "role": role,
                "exp":  datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(hours=1),
            },
            self.secret_key,
            algorithm= os.getenv("ALGORITHM"),
        )
        return token

    def test_suggest(self):
        token = self.get_test_token(role="questionUser")
        headers = {"Authorization": f"Bearer {token}"}
        payload = {"queryAsk": "¿Cómo cambio mi contraseña?"}
        response = self.client.post("api/v1/suggest", json=payload, headers=headers)
        assert response.status_code == 200
        data = response.json()       
        assert "data" in data       
        assert "queryAsk" in data["data"]
        assert "responseSuggestion" in data["data"]
