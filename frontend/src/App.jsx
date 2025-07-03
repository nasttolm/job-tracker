import React from 'react';
import { BrowserRouter, Routes, Route, Navigate } from 'react-router-dom';

import { AuthProvider } from './context/AuthContext';
import Login from './pages/Login';
import Register from './pages/Register';
import ProtectedRoute from "./components/ProtectedRoute";
import Vacancies from "./pages/Vacancies";
import AddVacancy from "./pages/AddVacancy";

function App() {
  return (
    <AuthProvider>
      <BrowserRouter>
        <Routes>
          {/* Public routes */}
          <Route path="/login" element={<Login />} />
          <Route path="/register" element={<Register />} />
          <Route
            path="/vacancies"
            element={
              <ProtectedRoute>
                <Vacancies />
              </ProtectedRoute>
            }
          />
          <Route
            path="/vacancies/add"
            element={
              <ProtectedRoute>
                <AddVacancy />
              </ProtectedRoute>
            }
          />
          {/* Redirect home to /login */}
          <Route path="/" element={<Navigate to="/login" />} />
        </Routes>
      </BrowserRouter>
    </AuthProvider>
  );
}

export default App;
