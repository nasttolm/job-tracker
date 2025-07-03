import React from "react";
import { Link, useNavigate } from "react-router-dom";
import { useAuth } from "../context/AuthContext";

export default function Navbar() {
  const { token, logout } = useAuth();
  const navigate = useNavigate();

  const handleLogout = () => {
    logout(); // Clear token and user
    navigate("/login"); // Redirect to login page
  };

  if (!token) return null;

  return (
    <nav style={{ padding: "1rem", borderBottom: "1px solid #ccc" }}>
      {/* Always visible */}
      <Link to="/vacancies" style={{ marginRight: "1rem" }}>
        🏠 Vacancies
      </Link>
      <Link to="/vacancies/add" style={{ marginRight: "1rem" }}>
        ➕ Add
      </Link>

      {/* Show logout only if logged in */}
      {token && (
        <button onClick={handleLogout} style={{ float: "right" }}>
          🚪 Logout
        </button>
      )}
    </nav>
  );
}
