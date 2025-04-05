import sys
import os
import pytest
from dao.user_dao import UserDAO
from utils.validators import Validator

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def test_create_user():
    # Verifica que se lance una excepción con datos inválidos
    with pytest.raises(ValueError, match="El correo electrónico no es válido."):
        UserDAO.create_user("Juan", "password123", "invalid_email")

    with pytest.raises(ValueError, match="Los campos no pueden estar vacíos."):
        UserDAO.create_user("", "", "")

def test_email_validator():
    assert Validator.is_valid_email("example@gmail.com") is True
    assert Validator.is_valid_email("invalid_email") is False