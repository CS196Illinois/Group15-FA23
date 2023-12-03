import React from 'react';
import {Link} from "react-router-dom";
import "../styles/Navbar.css";

function Navbar() {
  return (
    <div className="navbar">
        <div className="leftSide">
            ziggy<sub><b>FOAK</b></sub>
        </div>
        <div className="rightSide">
            <Link to="/"> Home</Link>
        </div>
    </div>
  )
}

export default Navbar;