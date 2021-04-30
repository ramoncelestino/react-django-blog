import styles from './articleCard.module.scss';

const ArticleCard = (props) => {
  return (
    <div className={styles.articleCard}>
      <h2>{props.title}</h2>
      <p>{props.content}</p>
    </div>
  );
};

export default ArticleCard;
