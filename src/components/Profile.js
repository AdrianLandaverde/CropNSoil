import { useNavigate } from 'react-router-dom';
import { useLocation } from "react-router-dom";

export default function Profile(props){

    const { state } = useLocation();
    const navigate = useNavigate()
    console.log(state)

    return(
        <div>
            <h1 className="text-5xl font-semibold text-center">Profile</h1>
            <ul className="list-none">
                <li className="text-lg font-semibold">Name: {state.name}</li>
                <li className="text-lg font-semibold">Email: {state.email}</li>
            </ul>
        </div>
    )
}
