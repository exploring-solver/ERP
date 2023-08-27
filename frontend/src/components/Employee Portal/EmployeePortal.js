// src/components/EmployeePortal.js
import React from 'react';
import { Link } from 'react-router-dom';

function EmployeePortal() {
    return (
        <div className="container mx-auto mt-8">
            <h2 className="text-xl font-semibold mb-4">Employee Portal</h2>
            <div className="grid grid-cols-3 gap-4">
                <Link to="/employee/register" className="bg-blue-500 hover:bg-blue-600 text-white p-4 rounded-lg shadow">
                    <h3 className="text-lg font-semibold mb-2">Register</h3>
                    <p>Create an employee account</p>
                </Link>
                <Link to="/employee/login" className="bg-green-500 hover:bg-green-600 text-white p-4 rounded-lg shadow">
                    <h3 className="text-lg font-semibold mb-2">Login</h3>
                    <p>Existing employee login</p>
                </Link>
                <Link to="/employee/apply" className="bg-yellow-500 hover:bg-yellow-600 text-white p-4 rounded-lg shadow">
                    <h3 className="text-lg font-semibold mb-2">Apply</h3>
                    <p>Apply for a position</p>
                </Link>
            </div>
        </div>
    );
}

export default EmployeePortal;
