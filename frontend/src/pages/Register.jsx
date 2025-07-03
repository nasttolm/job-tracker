import { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import api from '../services/api'; // axios instance

export default function Register() {
  // Local state for form inputs and error message
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState('');
  const navigate = useNavigate(); // to redirect the user

  const handleRegister = async (e) => {
    e.preventDefault(); // prevent default form behavior
    setError('');

    try {
      // Send POST request to backend
      await api.post('/users/register', {
        email,
        password,
      });

      // Redirect to login page on success
      navigate('/login');
    } catch (err) {
      // Show error if registration fails
      setError('Registration failed');
    }
  };

  return (
    <div>
      <h2>Register</h2>

      <form onSubmit={handleRegister}>
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
        <button type="submit">Register</button>
      </form>

      {/* Show error message if needed */}
      {error && <p style={{ color: 'red' }}>{error}</p>}
    </div>
  );
}
