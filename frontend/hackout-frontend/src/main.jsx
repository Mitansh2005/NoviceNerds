import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import Form from './Form.jsx'
import Navigation from './Navbar.jsx'
import './index.css'

createRoot(document.getElementById('root')).render(
  <StrictMode>
    <Navigation/>
    <Form/>
  </StrictMode>,
)
