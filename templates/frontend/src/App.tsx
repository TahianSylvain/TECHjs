import './App.css';  //https://www.youtube.com/@grafikart
import React, { useState, useEffect } from 'react';
import { Great } from './components/List';


function App() { // ES5
  const [annotation, setAnnotation]=React.useState([]);
  React.useEffect(
      () => {
          fetch('http://192.168.43.98:3333/api/annotation/')
              .then((data) => data.json())
              .then((json) => { setAnnotation(json) })
      }, []
  )

  const presentation = annotation.length ? <h1>Here are your tasks:</h1> : <h1>No task since now!</h1>
  return (  // type inference
    <div className="App">
      { presentation }
      <div className="partitioning">
        {
          annotation.map((item, index) => {
            return <Great product={item} key={index}/>
          })
        }
      </div>
    </div>
  );
}

export default App;
