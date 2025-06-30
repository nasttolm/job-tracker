def authenticate_user(client, email="deleteuser@example.com", password="securepassword"):
    """
    Helper function to register and authenticate a user, returning authorization headers.
    """
    # Register the user
    client.post("/users/register", json={"email": email, "password": password})
    
    # Log in and retrieve the access token
    login_response = client.post("/users/login", json={"email": email, "password": password})
    token = login_response.json()["access_token"]
    return {"Authorization": f"Bearer {token}"}


def test_delete_vacancy(client):
    """
    Test deleting a vacancy owned by the authenticated user.
    """
    headers = authenticate_user(client)

    # Create a vacancy
    response = client.post(
        "/vacancies",
        json={"title": "Temp", "company": "Temp Inc"},
        headers=headers
    )
    vacancy_id = response.json()["id"]

    # Delete the vacancy
    delete_response = client.delete(f"/vacancies/{vacancy_id}", headers=headers)
    assert delete_response.status_code == 204

    # Try to get the deleted vacancy (should not exist anymore if implemented)
    get_response = client.get("/vacancies", headers=headers)
    titles = [v["title"] for v in get_response.json()]
    assert "Temp" not in titles


def test_delete_vacancy_unauthorized(client):
    """
    Test deleting a vacancy without authorization.
    """
    response = client.delete("/vacancies/1")
    assert response.status_code == 401


def test_delete_nonexistent_vacancy(client):
    """
    Test deleting a vacancy that does not exist.
    """
    headers = authenticate_user(client)
    response = client.delete("/vacancies/999", headers=headers)
    assert response.status_code == 404
