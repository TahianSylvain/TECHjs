import './App.css';  //https://www.youtube.com/@grafikart
import React, { useState, useEffect } from 'react';
import Formular from './components/Formular';
import { Great } from './components/List';


function App() { // ES5
  const [annotation, setAnnotation]=React.useState([]);
  React.useEffect(
      () => {
        fetch('http://localhost:3333/api/annotation/')
        //fetch('http://192.168.42.249:3333/api/annotation/')
              .then((data) => data.json())
              .then((json) => { setAnnotation(json) })
      }, []
  )

  const presentation = annotation.length ? <h1>Here are your tasks:</h1> : <Formular/>;
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
