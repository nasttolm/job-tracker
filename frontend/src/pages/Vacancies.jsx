import React, { useEffect, useState } from "react";
import api from "../services/api";
import { useNavigate } from "react-router-dom";
import VacancyCard from "../components/VacancyCard";
import styles from "./Pages.module.css";

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

  // Handle deleting a vacancy
  const handleDelete = async (id) => {
    const confirmDelete = window.confirm("Are you sure you want to delete this vacancy?");
    if (!confirmDelete) return;

    try {
      await api.delete(`/vacancies/${id}`);
      // Remove deleted vacancy from the list
      setVacancies((prev) => prev.filter((vacancy) => vacancy.id !== id));
    } catch (err) {
      setError("Failed to delete vacancy.");
    }
  };

  if (loading) return <p>Loading...</p>;
  if (error) return <p style={{ color: "red" }}>{error}</p>;

  return (
    <div className={styles.container}> 
      <div className={styles.header}> 
          <h2>My Vacancies</h2>
          <button className={styles.addButton} onClick={() => navigate("/vacancies/add")}> {/* ← ДОБАВИТЬ класс */}
          ➕ Add Vacancy
          </button>
      </div>
      {vacancies.length === 0 ? (
          <p>No vacancies found.</p>
      ) : (
        <ul className={styles.list}>
          {vacancies.map((vacancy) => (
              <VacancyCard
                  key={vacancy.id}
                  vacancy={vacancy}
                  onDelete={handleDelete}
              />
          ))}
        </ul>
      )}
    </div>
  );
}
