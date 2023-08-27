// src/components/EmployeeRegistration.js
import React, { useState } from 'react';

function EmployeeRegistration() {
    const [employeeId, setEmployeeId] = useState('');
    const [name, setName] = useState('');
    const [email, setEmail] = useState('');
    const [contactNo, setContactNo] = useState('');
    const [password, setPassword] = useState('');

    const handleRegister = () => {
        // Implement registration logic here
    };

    return (
        <div className="container mx-auto mt-8">
            <h2 className="text-xl font-semibold mb-4">Employee Registration</h2>
            <form className="grid grid-cols-1 gap-4">
                <input
                    type="text"
                    placeholder="Employee ID"
                    className="p-2 border rounded"
                    value={employeeId}
                    onChange={(e) => setEmployeeId(e.target.value)}
                />
                <input
                    type="text"
                    placeholder="Name"
                    className="p-2 border rounded"
                    value={name}
                    onChange={(e) => setName(e.target.value)}
                />
                <input
                    type="email"
                    placeholder="Email"
                    className="p-2 border rounded"
                    value={email}
                    onChange={(e) => setEmail(e.target.value)}
                />
                <input
                    type="text"
                    placeholder="Contact Number"
                    className="p-2 border rounded"
                    value={contactNo}
                    onChange={(e) => setContactNo(e.target.value)}
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
                    onClick={handleRegister}
                >
                    Register
                </button>
            </form>
        </div>
    );
}

export default EmployeeRegistration;
