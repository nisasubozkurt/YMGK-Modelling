/* eslint-disable react/prop-types */
import chaos_maps from "./chaos_maps";
import "../styles/main.css";

const Sidebar = ({ selectedChaosMap,selectedChaos }) => {
  return (
    <div className="sidebar">
      {chaos_maps?.map((chaos, i) => (
        <div key={i}>
          <h4
            onClick={() => selectedChaosMap(chaos)}
            className={selectedChaos === chaos ? 'selected' : ''}
          >
            {chaos.name}
          </h4>
        </div>
      ))}
    </div>
  );
};

export default Sidebar;
