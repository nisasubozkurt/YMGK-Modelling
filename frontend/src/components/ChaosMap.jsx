/* eslint-disable react/prop-types */
import { useEffect, useState } from "react";
import "../styles/main.css";
import getChaosMapAnalysis from "../../api/api";

const ChaosMap = ({ chaosMap }) => {
  const [formData, setFormData] = useState({});
  const [image, setImage] = useState(null);
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    const initialState = {};
    chaosMap.inputs?.forEach((input) => {
      initialState[input] = "";
    });
    setFormData(initialState);
    setImage(null);
  }, [chaosMap]);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    setImage(null); 
    const response = await getChaosMapAnalysis(chaosMap.id, formData);
    const processedImagePath = response.data.plot_url?.replace(/\\/g, "/");
    setImage(`${processedImagePath}?${Date.now()}`);
    setLoading(false);
  };

  const handleInputChange = (e, input) => {
    setFormData({
      ...formData,
      [input]: e.target.value,
    });
  };

  if (loading) {
    return <div>Loading...</div>;
  }

  return (
    <div className="map-item">
      <h1>{chaosMap.name}</h1>
      <p style={{ maxWidth: "40rem", textAlign: "justify" }}>
        {" "}
        {chaosMap.description}{" "}
      </p>
      <form onSubmit={handleSubmit}>
        {chaosMap?.inputs?.map((input, i) => (
          <div key={i} className="inputs">
            <label style={{ textTransform: "capitalize" }}>{input}</label>
            <input
              placeholder={input}
              value={formData[input]}
              onChange={(e) => handleInputChange(e, input)}
            />
          </div>
        ))}
        <div style={{ marginTop: "1rem" }}>
          <button className="btn" type="submit">
            Gönder
          </button>
        </div>
      </form>

      {image && (
        <div>
          <img src={`http://127.0.0.1:8000/${image}`} alt={"sdfsd"} />
        </div>
      )}
    </div>
  );
};
export default ChaosMap;
