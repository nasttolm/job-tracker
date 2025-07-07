import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import api from "../services/api";
import styles from "./Pages.module.css";

/**
 * Page with a form to add a new vacancy (title, company, status).
 * Sends data to the backend via POST /vacancies.
 */
export default function AddVacancy() {
  const [title, setTitle] = useState("");
  const [company, setCompany] = useState("");
  const [status, setStatus] = useState("applied");
  const [error, setError] = useState("");

  const navigate = useNavigate();

  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      await api.post("/vacancies", {
        title,
        company,
        status,
      });

      navigate("/vacancies"); // Go back to list after adding
    } catch (err) {
      setError("Failed to add vacancy.");
    }
  };

  return (
    <div className={styles.formContainer}>
      <h2>Add New Vacancy</h2>
      {error && <p style={{ color: "red" }}>{error}</p>}
      <form onSubmit={handleSubmit}>
        <div className={styles.formGroup}>
          <label>Job Title:</label>
          <input
            type="text"
            value={title}
            onChange={(e) => setTitle(e.target.value)}
            required
          />
        </div>
        <div className={styles.formGroup}>
          <label>Company:</label>
          <input
            type="text"
            value={company}
            onChange={(e) => setCompany(e.target.value)}
            required
          />
        </div>
        <div className={styles.formGroup}>
          <label>Status:</label>
          <select value={status} onChange={(e) => setStatus(e.target.value)}>
            <option value="applied">Applied</option>
            <option value="interview">Interview</option>
            <option value="offer">Offer</option>
            <option value="rejected">Rejected</option>
          </select>
        </div>
        <button type="submit">Add Vacancy</button>
      </form>
    </div>
  );
}
