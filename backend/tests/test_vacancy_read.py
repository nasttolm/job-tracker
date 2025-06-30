def authenticate_user(client, email="getuser@example.com", password="securepassword"):
    """
    Helper function to register and authenticate a user, returning authorization headers.
    """
    # Register the user
    client.post("/users/register", json={"email": email, "password": password})
    
    # Log in and retrieve the access token
    login_response = client.post("/users/login", json={"email": email, "password": password})
    token = login_response.json()["access_token"]
    return {"Authorization": f"Bearer {token}"}


def test_get_user_vacancies(client):
    """
    Test retrieving all vacancies for the authenticated user.
    """
    headers = authenticate_user(client)

    # Create two vacancies
    client.post("/vacancies", json={"title": "Dev", "company": "A"}, headers=headers)
    client.post("/vacancies", json={"title": "Tester", "company": "B"}, headers=headers)

    # Get all vacancies
    response = client.get("/vacancies", headers=headers)

    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) == 2

    titles = [v["title"] for v in data]
    assert "Dev" in titles and "Tester" in titles


def test_get_vacancies_unauthenticated(client):
    """
    Test retrieving vacancies without authentication.
    """
    response = client.get("/vacancies")
    assert response.status_code == 401
