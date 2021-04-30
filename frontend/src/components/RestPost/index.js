import api from '../../services/api';
import React, { useEffect, useState } from 'react';
import styles from './restpost.module.scss';

const RestPost = (props) => {
  const [enteredTitle, setEnteredTitle] = useState('');
  const [enteredDescription, setEnteredDescription] = useState('');

  const titleChangeHandler = (event) => {
    setEnteredTitle(event.target.value);
  };

  const descriptionChangeHandler = (event) => {
    setEnteredDescription(event.target.value);
  };

  const submitHandler = (event) => {
    event.preventDefault();

    const article = {
      title: enteredTitle,
      user: '1',
      description: enteredDescription,
      content: 'Here is the content',
    };

    api
      .post('posts/', article)
      .then(function (response) {
        console.log(response.data);
      })
      .catch(function (error) {
        console.log(error);
      });
  };

  /*useEffect(() => {
    // POST request using axios inside useEffect React hook
    const article = {
      user: '1',
      title: 'React Hooks POST Request Example',
      description: props.description,
      content: 'Here is the content',
    };

    const fetchData = async () => {
      const { data } = await api.post('posts/', article);
      setPosts(data);
    };

    fetchData();
  });*/

  return (
    <div className={styles.cont}>
      <form onSubmit={submitHandler}>
        <div className="form-group">
          <label>Title</label>
          <input
            className="form-control"
            type="text"
            value={enteredTitle}
            onChange={titleChangeHandler}
          />
        </div>
        <div className="form-group">
          <label>Description</label>

          <input
            className="form-control"
            type="text"
            value={enteredDescription}
            onChange={descriptionChangeHandler}
          />
        </div>
        <div className="form-group">
          <button className="btn btn-primary form-control" type="submit">
            Send Data
          </button>
        </div>
      </form>
    </div>
  );
};

export default RestPost;
