import { useEffect, useState } from 'react';
import api from '../../services/api';

const Article = (props) => {
  const [article, setArticle] = useState('');

  useEffect(() => {
    const fetchData = async () => {
      const { data } = await api.get(`posts/${props.match.params.id}`);
      setArticle(data);
      console.log('ENtrei');
    };

    fetchData();
  }, []);

  return (
    <div>
      <h1>{article.title}</h1>
    </div>
  );
};

export default Article;
