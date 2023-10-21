import Banner from "./banner";
import Dashboard from "./Dashboard";
import { useNavigate } from 'react-router-dom';
import { useLocation } from "react-router-dom";
export default function Homepage(props) {

    const { state } = useLocation();
    const navigate = useNavigate()
    console.log(state)

    console.log(state.email)
    
  function handleClick(){
    navigate("/profile", {
        state: {
          email: state.email,
          name: state.name,
        }
    })

  }

  return (
    <div className="relative">
      <button 
        className="bg-blue-500 text-white px-4 py-2 rounded absolute top-4 right-4"
        onClick={() => handleClick()}>
        Profile
       </button>
      <Banner />
      <Dashboard />
    </div>
  );
}
