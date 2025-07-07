import { Link, useNavigate } from "react-router-dom"
import { useAuth } from "../context/AuthContext"
import styles from "./Navbar.module.css"

export default function Navbar() {
  const { token, logout } = useAuth()
  const navigate = useNavigate()

  const handleLogout = () => {
    logout() // Clear token and user
    navigate("/login") // Redirect to login page
  }

  return (
    <nav className={styles.navbar}>
      <div className={styles.navLinks}>
        <Link to="/vacancies" className={styles.navLink}>
          🏠 Vacancies
        </Link>
        <Link to="/vacancies/add" className={styles.navLink}>
          ➕ Add
        </Link>
        <button onClick={handleLogout} className={styles.logoutButton}>
          🚪 Logout
        </button>
      </div>
    </nav>
  )
}
