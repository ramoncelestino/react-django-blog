import axios from 'axios';
import { useEffect, useState } from 'react';
import People from './components/People';
import Post from './components/Post';
import { BrowserRouter as Router, Route } from 'react-router-dom';

function App() {
  //return <PostCards posts={posts} />;
  return (
    <div>
      {people.length !== 0 && <h1>{people[0].name}</h1>}
      <People people={people} />
      <Post />
    </div>
  );
}

export default App;

//{data.length !== 0 && <PostCard src="Teste" name={data} />}
