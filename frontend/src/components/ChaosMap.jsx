/* eslint-disable react/prop-types */
import { useEffect, useState } from 'react';
import '../styles/main.css';

const ChaosMap = ({ chaosMap }) => {
  const [formData, setFormData] = useState({});

  useEffect(() => {
    const initialState = {};
    chaosMap.inputs?.forEach(input => {
      initialState[input] = '';
    });
    setFormData(initialState);
  }, [chaosMap]);

  const handleInputChange = (e, input) => {
    setFormData({
      ...formData,
      [input]: e.target.value
    });
  };

  const handleSubmit = (e) => {
    e.preventDefault();

    console.log('Form submitted with data:', formData);
  };

  return (
    <div>
      <h1>{chaosMap.name}</h1>
      <p style={{maxWidth:'40rem', textAlign:'justify'}}> {chaosMap.description} </p>
      <form onSubmit={handleSubmit}>
        {chaosMap?.inputs?.map((input, i) => (
          <div key={i} className="inputs">
            <label style={{ textTransform: 'capitalize' }}>{input}</label>
            <input
              type="text"
              placeholder={input}
              value={formData[input]}
              onChange={(e) => handleInputChange(e, input)}
            />
          </div>
        ))}
        <div style={{ marginTop: '1rem' }}>
          <button className='btn' type="submit">Gönder</button>
        </div>
      </form>
    </div>
  );
};
export default ChaosMap;
