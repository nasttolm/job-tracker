import React from "react";
import { useNavigate } from "react-router-dom";
import styles from "./VacancyCard.module.css";

// Reusable card component for displaying a single vacancy
export default function VacancyCard({ vacancy, onDelete }) {
  const navigate = useNavigate();

  const handleEdit = () => {
    navigate(`/vacancies/edit/${vacancy.id}`); // Navigate to edit page
  };

  const handleDelete = () => {
    if (window.confirm("Are you sure you want to delete this vacancy?")) {
      onDelete(vacancy.id); // Trigger delete in parent
    }
  };

  return (
    <div className={styles.card}>
      <h3>{vacancy.title}</h3>
      <p><strong>Company:</strong> {vacancy.company}</p>
      <p><strong>Status:</strong> {vacancy.status}</p>

      <div className={styles.buttons}>
        <button onClick={handleEdit}>✏️ Edit</button>
        <button onClick={handleDelete}>🗑️ Delete</button>
      </div>
    </div>
  );
}
