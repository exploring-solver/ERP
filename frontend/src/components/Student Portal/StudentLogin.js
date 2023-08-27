// src/components/StudentLogin.js
import React, { useState } from 'react';

function StudentLogin() {
    const [studentId, setStudentId] = useState('');
    const [password, setPassword] = useState('');

    const handleLogin = () => {
        // Implement login logic here
    };

    return (
        <div className="container mx-auto mt-8">
            <h2 className="text-xl font-semibold mb-4">Student Login</h2>
            <form className="grid grid-cols-1 gap-4">
                <input
                    type="text"
                    placeholder="Student ID"
                    className="p-2 border rounded"
                    value={studentId}
                    onChange={(e) => setStudentId(e.target.value)}
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
                    className="bg-green-500 hover:bg-green-600 text-white p-2 rounded"
                    onClick={handleLogin}
                >
                    Login
                </button>
            </form>
        </div>
    );
}

export default StudentLogin;
