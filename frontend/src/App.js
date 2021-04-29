import People from './components/People';
import Posts from './components/Posts';
import { BrowserRouter as Router, Route } from 'react-router-dom';

function App() {
  //return <PostCards posts={posts} />;
  return (
    <Router>
      <Route path="/" component={People} exact />
      <Route path="/posts" component={Posts} exact />
    </Router>
  );
}

export default App;

//{data.length !== 0 && <PostCard src="Teste" name={data} />}
