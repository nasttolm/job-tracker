

def test_register_user(client):
    """
    Test the user registration endpoint.
    """
    # Send a POST request to the /users/register endpoint with a test email and password
    response = client.post(
        "/users/register",
        json={
            "email": "testuser111@example.com",
            "password": "securepassword"
        }
    )

    # Assert that the response status code is 201 Created
    assert response.status_code == 201

    # Assert that the returned email matches the one we sent
    assert response.json()["email"] == "testuser111@example.com"


def test_login(client):
    """
    Test the user login endpoint.
    """
    # Register the user first
    client.post(
        "/users/register",
        json={
            "email": "loginuser@example.com",
            "password": "securepassword"
        }
    )

    # Attempt login with correct credentials
    response = client.post(
        "/users/login",
        json={
            "email": "loginuser@example.com",
            "password": "securepassword"
        }
    )

    assert response.status_code == 200
    assert "access_token" in response.json()


def test_create_vacancy(client):
    """
    Test creating a vacancy for an authenticated user.
    """
    # Register and log in a user
    client.post(
        "/users/register",
        json={
            "email": "creator@example.com",
            "password": "securepassword"
        }
    )

    login_response = client.post(
        "/users/login",
        json={
            "email": "creator@example.com",
            "password": "securepassword"
        }
    )
    token = login_response.json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}
    
    # Create a new vacancy (only required fields)
    vacancy_data = {
        "title": "Software Engineer",
        "company": "Acme Corp"
    }

    response = client.post("/vacancies", json=vacancy_data, headers=headers)

    # Check response
    assert response.status_code == 201
    data = response.json()
    assert data["title"] == "Software Engineer"
    assert data["company"] == "Acme Corp"
    assert data["status"] == "applied"

def test_get_user_vacancies(client):
    """
    Test retrieving all vacancies for the authenticated user.
    """
    # Register and log in a user
    client.post(
        "/users/register",
        json={
            "email": "getuser@example.com",
            "password": "securepassword"
        }
    )

    login_response = client.post(
        "/users/login",
        json={
            "email": "getuser@example.com",
            "password": "securepassword"
        }
    )
    token = login_response.json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}

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

def test_update_vacancy(client):
    # Register and log in user
    client.post(
        "/users/register",
        json={
            "email": "updateuser@example.com",
            "password": "securepassword"
        }
    )
    login_response = client.post(
        "/users/login",
        json={
            "email": "updateuser@example.com",
            "password": "securepassword"
        },
    )
    token = login_response.json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}

    # Create a vacancy
    create_response = client.post(
        "/vacancies",
        json={"title": "Old Title", "company": "Old Co"},
        headers=headers
    )
    vacancy_id = create_response.json()["id"]

    # Update the vacancy
    update_response = client.put(
        f"/vacancies/{vacancy_id}",
        json={"title": "New Title", "company": "New Co", "status": "interview"},
        headers=headers
    )

    assert update_response.status_code == 200
    updated = update_response.json()
    assert updated["title"] == "New Title"
    assert updated["company"] == "New Co"
    assert updated["status"] == "interview"
