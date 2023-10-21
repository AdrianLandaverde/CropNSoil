import { useNavigate } from 'react-router-dom';
import { useState } from 'react';
export default function Form(){

    const [email, setEmail] = useState("")
    const [name, setName] = useState("Fred")
    const [password, setPassword] = useState("")

    const navigate = useNavigate()
    function handleClick(){
        console.log(email, password)
        navigate("/home", {
            state: {
              email: email,
              name: name,
            }
        })
    }
    return(
        <div className="bg-white px-40 py-20 rounded-3xl border-2 border">
            <h1 className="text-5xl font-semibold text-center">CropsNSoil</h1>
            <p className="font-medium text-lg text-gray-500 mt-4">Welcome back! Please enter your details </p>
            <div className="mt-8">
                <div>
                    <label className="text-lg font-medium">Email</label>
                    <input
                        className="w-full border-2 border-gray-100 rounded-xl p-4 mt-1 bg-transparent"
                        placeholder="Enter your email"
                        value={email}
                        onChange={(e) => setEmail(e.target.value)}
                    />
                </div>
                <div>
                    <label className="text-lg font-medium">Password</label>
                    <input
                        className="w-full border-2 border-gray-100 rounded-xl p-4 mt-1 bg-transparent"
                        placeholder="Enter your Password"
                        value={password}
                        onChange={(e) => setPassword(e.target.value)}
                    />
                </div>

                    <div className="mt-8 flex flex-col gap-y-4">
                        <button className="active:scale-[.98] active:duration-75 hover:scale-[1.01] ease-in-out transition-all bg-green-500 text-white text-lg font-bold py-3 rounded-xl"
                                 onClick={() => handleClick()}>
                        Sign In
                        </button>
                    </div>
                    <div className="mt-8 flex justify-center items-center">
                        <p className="text-base font-medium">Don't have an account?</p>
                        <button className="text-green-500 text-base font-medium ml-2">Sign Up</button>
                    </div>
            </div>
        </div>
    )
}