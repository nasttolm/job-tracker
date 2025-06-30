def test_register_user(client):
    """
    Test the user registration endpoint.
    """
    response = client.post(
        "/users/register",
        json={"email": "testuser111@example.com", "password": "securepassword"}
    )
    assert response.status_code == 201
    assert response.json()["email"] == "testuser111@example.com"


def test_register_existing_user(client):
    """
    Test registering a user that already exists.
    """
    client.post(
        "/users/register",
        json={"email": "duplicate@example.com", "password": "securepassword"}
    )
    response = client.post(
        "/users/register",
        json={"email": "duplicate@example.com", "password": "securepassword"}
    )
    assert response.status_code == 400


def test_login(client):
    """
    Test the user login endpoint.
    """
    client.post(
        "/users/register",
        json={"email": "loginuser@example.com", "password": "securepassword"}
    )
    response = client.post(
        "/users/login",
        json={"email": "loginuser@example.com", "password": "securepassword"}
    )
    assert response.status_code == 200
    assert "access_token" in response.json()


def test_login_invalid_credentials(client):
    """
    Test login with incorrect password.
    """
    client.post(
        "/users/register",
        json={"email": "wrongpass@example.com", "password": "securepassword"}
    )
    response = client.post(
        "/users/login",
        json={"email": "wrongpass@example.com", "password": "wrongpassword"}
    )
    assert response.status_code == 400
