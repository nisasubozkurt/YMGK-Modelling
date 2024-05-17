/* eslint-disable react/prop-types */
import chaos_maps from "./chaos_maps";
import "../styles/main.css";

const NavBar = ({ selectedChaosMap,selectedChaos }) => {
  return (
    <div className="navbar">
      <div className="navbar-header">
        <img className="logo" src="/public/logo.png" />
        <h1> Chaos Map Analizleri </h1>
      </div>
      <ul className="navbar-items">
        {chaos_maps?.map((chaos, i) => (
          <li key={i} className="navbar-item">
            <h4
              onClick={() => selectedChaosMap(chaos)}
              className={selectedChaos === chaos ? 'selected' : ''}
            >
              {chaos.name}
            </h4>
          </li>
        ))}

      </ul>
    </div>
  );
};

export default NavBar;
