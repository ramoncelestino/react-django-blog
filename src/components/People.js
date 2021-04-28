import PersonCard from './PersonCard';
import api from '../../services/api';

const People = () => {
  const [people, setPeople] = useState([]);

  useEffect(() => {
    const fetchData = async () => {
      const { data } = await api.get('products/');
      setPeople(data);
    };

    fetchData();
  }, []);

  return (
    <div className="post-cards">
      <div className="row">
        {people.map((person) => (
          <div className="col-md-4">
            <PersonCard person={person} />
          </div>
        ))}
      </div>
    </div>
  );
};

export default People;
