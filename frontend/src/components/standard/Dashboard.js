// src/components/Dashboard.js
import React from 'react';
import { Link } from 'react-router-dom';

function Dashboard() {
    return (
        <div className="container mx-auto mt-8">
            <h1 className="text-2xl font-semibold mb-4">Welcome to College ERP</h1>
            <div className="grid grid-cols-2 gap-4">
                <Link to="/student" className="bg-blue-500 hover:bg-blue-600 text-white p-4 rounded-lg shadow">
                    <h2 className="text-lg font-semibold mb-2">Student Portal</h2>
                    <p>Login, Register, and more</p>
                </Link>
                <Link to="/employee" className="bg-green-500 hover:bg-green-600 text-white p-4 rounded-lg shadow">
                    <h2 className="text-lg font-semibold mb-2">Employee Portal</h2>
                    <p>Login, Register, and apply</p>
                </Link>
            </div>
        </div>
    );
}

export default Dashboard;
