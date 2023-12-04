import React from 'react'

function ResultItem({ image, name}) {
  return (
    <div className="resultItem">
        <div style={{ backgroundImage: `url(${image})`}}></div>
        <h1> {name} </h1>
    </div>
  )
}

export default ResultItem