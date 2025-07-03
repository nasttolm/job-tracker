import { createContext, useContext, useState } from 'react';

// Create a context for authentication
const AuthContext = createContext();

// AuthProvider wraps the app and provides login state
export const AuthProvider = ({ children }) => {
  const [token, setToken] = useState(() => localStorage.getItem('token'));

  // Save token in localStorage and context
  const login = (newToken) => {
    setToken(newToken);
    localStorage.setItem('token', newToken);
  };

  // Clear token from context and storage
  const logout = () => {
    setToken(null);
    localStorage.removeItem('token');
  };

  return (
    <AuthContext.Provider value={{ token, login, logout }}>
      {children}
    </AuthContext.Provider>
  );
};

// Custom hook to use the context
export const useAuth = () => {
  return useContext(AuthContext);
};
