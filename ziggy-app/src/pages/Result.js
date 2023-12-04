import React from 'react'
import { ResultList } from "../helpers/resultList";
import { Link } from "react-router-dom";
import ResultItem from "../components/ResultItem";
import "../styles/Result.css";

function Result() {
  return (
    <div className="result">
        <h1 className="resultTitle">Results:</h1>
        <div className="resultList">
          {ResultList.map((resultItem, key) => {
            return <ResultItem 
              key={key}
              image={resultItem.image} 
              name={resultItem.name} 
            />
          })}
        </div>
        <div id="returnToHomeButton" className="buttonContainer">
          <Link to="/">
            <button>Try again</button>
          </Link>
        </div>
    </div>
  )
}

export default Result