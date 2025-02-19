import os
import jwt
import datetime
from fastapi.testclient import TestClient
from app.main import app

class TestSuggest:
    @classmethod
    def setup_class(cls):
        cls.client = TestClient(app)
        # Si no está definido en el entorno, usa un valor por defecto
        cls.secret_key = os.getenv("SECRET_KEY") or "mysecret"

    def get_test_token(self, role="questionUser"):
        token = jwt.encode(
            {
                "sub": "userQuestion",
                "idUser": "8aa1a5f6-680e-435d-9367-ef57bdaca5b8",
                "role": role,
                "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1),
            },
            self.secret_key,
            algorithm="HS256",
        )
        return token

    def test_suggest(self):
        token = self.get_test_token(role="questionUser")
        headers = {"Authorization": f"Bearer {token}"}
        payload = {"queryAsk": "¿Cómo cambio mi contraseña?"}
        response = self.client.post("/suggest", json=payload, headers=headers)
        assert response.status_code == 200
        data = response.json()
        # Suponiendo que la respuesta se envuelve en "data"
        assert "data" in data
        # Verifica que dentro de data se encuentren los campos requeridos
        assert "queryAsk" in data["data"]
        assert "responseSuggestion" in data["data"]
