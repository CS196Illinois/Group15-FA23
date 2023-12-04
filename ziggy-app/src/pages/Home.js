import React from 'react'
import {Link} from "react-router-dom";
import "../styles/Home.css"

function Home() {
  return (
    <div className="home">
        <div className="headerContainer">
          <h1>draw a circle</h1>
            
        </div>
        <div className="drawArea">
          <p></p>
        </div>

        <div className="buttonContainer">
          <Link to="/result">
            <button>result</button>
          </Link>
        </div>
    </div>
  )
}

export default Home