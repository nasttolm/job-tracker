import React, { useEffect, useState } from "react";
import { useNavigate, useParams } from "react-router-dom";
import api from "../services/api";

/**
 * Page to edit an existing vacancy using PUT /vacancies/:id
 */
export default function EditVacancy() {
  const { id } = useParams(); // Get the vacancy ID from the URL
  const [title, setTitle] = useState("");
  const [company, setCompany] = useState("");
  const [status, setStatus] = useState("applied");
  const [error, setError] = useState("");

  const navigate = useNavigate();

  // Load existing vacancy data
  useEffect(() => {
    async function fetchVacancy() {
      try {
        const res = await api.get(`/vacancies/${id}`);
        setTitle(res.data.title);
        setCompany(res.data.company);
        setStatus(res.data.status);
      } catch (err) {
        setError("Failed to load vacancy.");
      }
    }

    fetchVacancy();
  }, [id]);

  // Submit updated vacancy
  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      await api.put(`/vacancies/${id}`, { title, company, status });
      navigate("/vacancies");
    } catch (err) {
      setError("Failed to update vacancy.");
    }
  };

  return (
    <div>
      <h2>Edit Vacancy</h2>
      {error && <p style={{ color: "red" }}>{error}</p>}
      <form onSubmit={handleSubmit}>
        <div>
          <label>Job Title:</label>
          <input
            type="text"
            value={title}
            onChange={(e) => setTitle(e.target.value)}
            required
          />
        </div>
        <div>
          <label>Company:</label>
          <input
            type="text"
            value={company}
            onChange={(e) => setCompany(e.target.value)}
            required
          />
        </div>
        <div>
          <label>Status:</label>
          <select value={status} onChange={(e) => setStatus(e.target.value)}>
            <option value="applied">Applied</option>
            <option value="interview">Interview</option>
            <option value="offer">Offer</option>
            <option value="rejected">Rejected</option>
          </select>
        </div>
        <button type="submit">Update Vacancy</button>
      </form>
    </div>
  );
}
