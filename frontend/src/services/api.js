import axios from 'axios';

// Create an axios instance with a base URL from .env
const api = axios.create({
  baseURL: import.meta.env.VITE_API_URL,
});

// Add a request interceptor to attach the token to every request
api.interceptors.request.use((config) => {
  const token = localStorage.getItem('token');
  if (token) {
    // Set the Authorization header
    config.headers.Authorization = `Bearer ${token}`;
  }
  return config;
});

// Export the configured axios instance
export default api;
