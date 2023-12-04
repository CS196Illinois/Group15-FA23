import React from 'react';
import {Link} from "react-router-dom";
import "../styles/Navbar.css";

function Navbar() {
  return (
    <div className="navbar">
        <div className="leftSide">
            <b>ziggy</b><sub><sub><sub>FOAK</sub></sub></sub>
        </div>
        <div className="rightSide">
            <Link to="/"> Home</Link>
        </div>
    </div>
  )
}

export default Navbar;