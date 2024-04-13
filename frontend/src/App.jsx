import { useState } from "react";
import Sidebar from "./components/Sidebar";
import ChaosMap from "./components/ChaosMap";

function App() {
  const [selectedChaosMap, setSelectedChaosMap] = useState("");
  return (
    <>
      <div style={{marginTop:'2rem',display:'flex', justifyContent:'center', alignItems:'center'}}>
        <h1> Chaos Map Analizleri </h1>
      </div>
      <div style={{ display: "flex", marginTop: "4rem",gap:'8rem' }}>
        <div style={{marginLeft:'4rem'}}>
          <Sidebar selectedChaos={selectedChaosMap} selectedChaosMap={setSelectedChaosMap} />
        </div>
        <div style={{ flexGrow: 1 }}>
          {selectedChaosMap ? (
            <ChaosMap chaosMap={selectedChaosMap} />
          ) : (
            <div>
              <p>Lütfen bir Chaos Map seçin.</p>
            </div>
          )}
        </div>
      </div>
    </>
  );
}

export default App;
