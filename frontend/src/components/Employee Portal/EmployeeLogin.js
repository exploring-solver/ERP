// src/components/EmployeeLogin.js
import React, { useState } from 'react';

function EmployeeLogin() {
    const [employeeId, setEmployeeId] = useState('');
    const [password, setPassword] = useState('');

    const handleLogin = () => {
        // Implement login logic here
    };

    return (
        <div className="container mx-auto mt-8">
            <h2 className="text-xl font-semibold mb-4">Employee Login</h2>
            <form className="grid grid-cols-1 gap-4">
                <input
                    type="text"
                    placeholder="Employee ID"
                    className="p-2 border rounded"
                    value={employeeId}
                    onChange={(e) => setEmployeeId(e.target.value)}
                />
                <input
                    type="password"
                    placeholder="Password"
                    className="p-2 border rounded"
                    value={password}
                    onChange={(e) => setPassword(e.target.value)}
                />
                <button
                    type="button"
                    className="bg-blue-500 hover:bg-blue-600 text-white p-2 rounded"
                    onClick={handleLogin}
                >
                    Login
                </button>
            </form>
        </div>
    );
}

export default EmployeeLogin;
