import React, { useEffect, useState } from 'react';
import api from '../../services/api';

import styles from './posts.module.scss';

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
    <div>
      {posts.map((post) => (
        <div className={styles.posts}>
          <h1>{post.title}</h1>
          <p>{post.content}</p>
          <img src={post.image}></img>
        </div>
      ))}
    </div>
  );
};

export default Posts;
