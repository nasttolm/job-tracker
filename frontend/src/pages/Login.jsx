import { useState } from 'react';
import { useNavigate } from 'react-router-dom'; // to redirect after login
import { useAuth } from '../context/AuthContext'; // custom hook to access login()
import api from '../services/api'; // our axios instance

export default function Login() {
  // Local state for form inputs and error message
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState('');

  const { login } = useAuth(); // get login() function from context
  const navigate = useNavigate(); // to redirect the user

  const handleSubmit = async (e) => {
    e.preventDefault(); // prevent default form behavior
    setError('');

    try {
      // Send POST request to backend
      const response = await api.post('/users/login', {
        email,
        password,
      });

      // Extract token from response
      const token = response.data.access_token;

      // Save token to context + localStorage
      login(token);

      // Redirect to vacancies
      navigate('/vacancies');
    } catch (err) {
      // Show error if login fails
      setError('Invalid credentials');
    }
  };

  return (
    <div>
      <h2>Login</h2>

      <form onSubmit={handleSubmit}>
        {/* Username input */}
        <input
          type="text"
          placeholder="Email"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
        /><br />

        {/* Password input */}
        <input
          type="password"
          placeholder="Password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
        /><br />

        {/* Submit button */}
        <button type="submit">Login</button>
      </form>

      {/* Show error message if needed */}
      {error && <p style={{ color: 'red' }}>{error}</p>}
    </div>
  );
}
