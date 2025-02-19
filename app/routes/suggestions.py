import os
import datetime
import jwt
import unittest
from fastapi.testclient import TestClient
from app.main import app

class TestSuggestEndpoint(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.client = TestClient(app.main.app)
        cls.SECRET_KEY = os.getenv("SECRET_KEY")

    def get_test_token(self, role="questionUser"):
        token = jwt.encode(
            {
                "sub": "userQuestion",
                "idUser": "8aa1a5f6-680e-435d-9367-ef57bdaca5b8",
                "role": role,
                "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1),
            },
            self.SECRET_KEY,
            algorithm="HS256",
        )
        return token

    def test_suggest(self):
        token = self.get_test_token(role="questionUser")
        headers = {"Authorization": f"Bearer {token}"}
        payload = {"queryAsk": "¿Cómo cambio mi contraseña?"}
        response = self.client.post("/suggest", json=payload, headers=headers)
        self.assertEqual(response.status_code, 200)
        data = response.json()
        # Verificamos que la respuesta esté envuelta en "data"
        self.assertIn("data", data)
        self.assertIn("queryAsk", data["data"])
        self.assertIn("responseSuggestion", data["data"])

if __name__ == '__main__':
    unittest.main()
