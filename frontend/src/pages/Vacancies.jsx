import React, { useEffect, useState } from "react";
import api from "../services/api";
import { useNavigate } from "react-router-dom";

/**
 * This page fetches and displays the list of vacancies
 * for the currently logged-in user.
 */
export default function Vacancies() {
  const [vacancies, setVacancies] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");

  const navigate = useNavigate();

  // Fetch vacancies when component mounts
  useEffect(() => {
    async function fetchVacancies() {
      try {
        const response = await api.get("/vacancies");
        setVacancies(response.data);
      } catch (err) {
        setError("Failed to load vacancies.");
      } finally {
        setLoading(false);
      }
    }

    fetchVacancies();
  }, []);

  if (loading) return <p>Loading...</p>;
  if (error) return <p style={{ color: "red" }}>{error}</p>;

  return (
    <div>
      <h2>My Vacancies</h2>
      <button onClick={() => navigate("/vacancies/add")}>
        ➕ Add Vacancy
      </button>
      {vacancies.length === 0 ? (
        <p>No vacancies found.</p>
      ) : (
        <ul>
          {vacancies.map((vacancy) => (
            <li key={vacancy.id}>
              <strong>{vacancy.title}</strong> at {vacancy.company} — {vacancy.status}
              <button onClick={() => navigate(`/vacancies/edit/${vacancy.id}`)}>
                ✏️ Edit
              </button>
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}
