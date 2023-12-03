import React from 'react'
import { ResultList } from "../helpers/resultList";
import ResultItem from "../components/ResultItem";
import "../styles/Result.css";

function Result() {
  return (
    <div className="result">
        <h1 className="resultTitle">results:</h1>
        <div className="resultList">
          {ResultList.map((resultItem, key) => {
            return <ResultItem 
              key={key}
              image={resultItem.image} 
              name={resultItem.name} 
            />
          })}
        </div>
    </div>
  )
}

export default Result