import React, { useEffect, useState } from 'react';
import api from '../../services/api';
import RestPost from '../RestPost';
import ArticleCard from '../ArticleCard';

import styles from './articles.module.scss';

const Posts = (props) => {
  const [posts, setPosts] = useState([]);

  useEffect(() => {
    const fetchData = async () => {
      const { data } = await api.get('posts/');
      setPosts(data);
    };

    fetchData();
  });

  return (
    <div className="container">
      <RestPost />
      <div className="row">
        {posts.map((post) => (
          <div className="col-md-4">
            <ArticleCard
              title={post.title}
              content={post.content}
              img={post.image}
            />
          </div>
        ))}
      </div>
    </div>
  );
};

export default Posts;
