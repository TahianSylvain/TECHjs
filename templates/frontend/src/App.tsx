import './App.css';  // https://www.youtube.com/@grafikart
import React from 'react';
import Formular from './components/Formular';
import { Great } from './components/List';
import fakeAPI from './FakeAPI.json'


const App = () => { // ES5
  const [annotation, setAnnotation]=React.useState([]);
  React.useEffect(
      () => {
        fetch('http://localhost:3333/fullstack/')
              .then((data) => data.json())
              .then((json) => { setAnnotation(json) })
      }, []                                             // c'est un objet type new Array()
  )
  const notes = annotation.length ? annotation : fakeAPI;  
  const presentation = annotation.length ? <Formular /> : <h1>Hummm!!! You've got no task:</h1>;

  return (  // type inference
    <div className="App">
      <div className="partitioning">
        {
          notes.map((item, index) => {
            return <Great product={item} key={index} />
          })
        }
      </div>
      { presentation }
    </div>
  );
};

export default App;
