import React from "react";
import './App.css';
class App extends React.Component{

  render(){
    const items = [
      {name: "Masha"},
      {name: "Bear"},
    ];
    return(
      <div>
        {items.map(item => <button>{item.name}</button>)}
      </div>    
    );
  }
}

export default App;
