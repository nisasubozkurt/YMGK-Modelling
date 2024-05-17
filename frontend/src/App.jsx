import { useState } from "react";
import Sidebar from "./components/Sidebar";
import ChaosMap from "./components/ChaosMap";
import NavBar from "./components/Navbar";
import Footer from "./components/Footer";

function App() {
  const [selectedChaosMap, setSelectedChaosMap] = useState("");
  return (
    <>

<NavBar selectedChaos={selectedChaosMap} selectedChaosMap={setSelectedChaosMap} />
      <div style={{ display: "flex", marginTop: "4rem",gap:'8rem', marginLeft:"5rem"}}>
        <div style={{ flexGrow: 1 }}>
          {selectedChaosMap ? (
            <ChaosMap chaosMap={selectedChaosMap} />
          ) : (
            <div className="main-item">
              <img src="/public/vişne.png" alt="" />
            </div>
          )}
        </div>
      </div>
      <Footer/>
    </>
  );
}

export default App;
