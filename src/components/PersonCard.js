const PersonCard = (props) => {
  return (
    <>
      <h1>Teste</h1>
      <h1>{props.person.name}</h1>
      <h5>{props.person.email}</h5>
    </>
  );
};

export default PersonCard;
