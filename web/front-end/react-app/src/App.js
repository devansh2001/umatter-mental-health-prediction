import React from 'react';
import logo from './logo.svg';
import './App.css';
import NavBarComponent from './components/NavBarComponent';
import SearchByUsernameComponent from './components/SearchByUsernameComponent';
import TweetCard from './components/TweetCard'
import TweetContainer from './components/TweetContainer'
import {Container} from 'react-bootstrap';

function App() {
  return (
    <div className="App">
      {/*<Container>*/}
        <NavBarComponent/>
        <SearchByUsernameComponent/>
        <TweetContainer/>
      {/*</Container>*/}
    </div>
  );
}

export default App;
