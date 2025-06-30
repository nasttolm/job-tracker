def authenticate_user(client, email="updateuser@example.com", password="securepassword"):
    """
    Helper function to register and authenticate a user, returning authorization headers.
    """
    # Register the user
    client.post("/users/register", json={"email": email, "password": password})
    
    # Log in and retrieve the access token
    login_response = client.post("/users/login", json={"email": email, "password": password})
    token = login_response.json()["access_token"]
    return {"Authorization": f"Bearer {token}"}


def test_update_vacancy(client):
    """
    Test updating a vacancy owned by the authenticated user.
    """
    headers = authenticate_user(client)

    # Create vacancy
    create_response = client.post(
        "/vacancies",
        json={"title": "Old Title", "company": "Old Co"},
        headers=headers
    )
    vacancy_id = create_response.json()["id"]

    # Update vacancy
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


def test_update_vacancy_unauthorized(client):
    """
    Test updating a vacancy without providing a token.
    """
    response = client.put(
        "/vacancies/1",
        json={"title": "Hacker", "company": "Hackers Inc", "status": "applied"}
    )
    assert response.status_code == 401


def test_update_nonexistent_vacancy(client):
    """
    Test updating a vacancy that does not exist.
    """
    headers = authenticate_user(client)
    response = client.put(
        "/vacancies/999",
        json={"title": "Ghost Job", "company": "None", "status": "applied"},
        headers=headers
    )
    assert response.status_code == 404
