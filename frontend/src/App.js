import Articles from './components/Articles';
import RestPost from './components/RestPost';
import Article from './components/Article';
import { BrowserRouter as Router, Route } from 'react-router-dom';

function App() {
  //return <PostCards posts={posts} />;
  return (
    <Router>
      <Route path="/" component={Articles} exact />
      <Route path="/createpost" component={RestPost} exact />
      <Route path="/posts/:id" component={Article} />
    </Router>
  );
}

export default App;

//{data.length !== 0 && <PostCard src="Teste" name={data} />}
