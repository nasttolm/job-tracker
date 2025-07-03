import { useAuth } from "../context/AuthContext";
import { Navigate } from "react-router-dom";

/**
 * This component protects private routes.
 * If the user is not authenticated, they are redirected to /login.
 * Otherwise, the requested page is rendered.
 */
export default function ProtectedRoute({ children }) {
  const { token } = useAuth();

  if (!token) {
    return <Navigate to="/login" />;
  }

  return children;
}
