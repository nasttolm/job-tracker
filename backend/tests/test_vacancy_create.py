def authenticate_user(client, email="creator@example.com", password="securepassword"):
    """
    Helper function to register and authenticate a user, returning authorization headers.
    """
    # Register the user
    client.post("/users/register", json={"email": email, "password": password})

    # Log in and retrieve the access token
    login_response = client.post(
        "/users/login",
        json={"email": email, "password": password}
    )
    token = login_response.json()["access_token"]
    return {"Authorization": f"Bearer {token}"}


def test_create_vacancy(client):
    """
    Test creating a vacancy with required fields.
    """
    headers = authenticate_user(client)

    # Vacancy data with required fields only
    vacancy_data = {
        "title": "Software Engineer",
        "company": "Acme Corp"
    }

    # Send POST request to create the vacancy
    response = client.post("/vacancies", json=vacancy_data, headers=headers)

    # Check if the response is successful
    assert response.status_code == 201

    # Validate the response content
    data = response.json()
    assert data["title"] == "Software Engineer"
    assert data["company"] == "Acme Corp"
    assert data["status"] == "applied"  # Default value


def test_create_vacancy_unauthenticated(client):
    """
    Test that unauthenticated users cannot create a vacancy.
    """
    vacancy_data = {
        "title": "Backend Developer",
        "company": "Initech"
    }

    # No authorization header provided
    response = client.post("/vacancies", json=vacancy_data)

    # Expecting 401 Unauthorized
    assert response.status_code == 401


def test_create_vacancy_missing_fields(client):
    """
    Test that creating a vacancy without required fields returns a validation error.
    """
    headers = authenticate_user(client)

    # Missing 'company' field
    incomplete_data = {
        "title": "Frontend Developer"
    }

    # Send request with missing field
    response = client.post("/vacancies", json=incomplete_data, headers=headers)

    # Expecting 422 Unprocessable Entity (validation error)
    assert response.status_code == 422
