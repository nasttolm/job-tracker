import React from 'react';
import { BrowserRouter, Routes, Route, Navigate } from 'react-router-dom';

import { AuthProvider, useAuth } from './context/AuthContext';
import Login from './pages/Login';
import Register from './pages/Register';
import ProtectedRoute from "./components/ProtectedRoute";
import Vacancies from "./pages/Vacancies";
import AddVacancy from "./pages/AddVacancy";
import EditVacancy from './pages/EditVacancy';
import Navbar from './components/Navbar';


function App() {
  const { token } = useAuth();
  return (
    <BrowserRouter>
      <Navbar />
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
        <Route
          path="/vacancies/edit/:id"
          element={
            <ProtectedRoute>
              <EditVacancy />
            </ProtectedRoute>
          }
        />
        {/* Redirect home to /login */}
        <Route path="/" element={<Navigate to="/login" />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
