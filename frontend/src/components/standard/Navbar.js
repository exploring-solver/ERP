// src/components/Navbar.js
import React from 'react';
import { Link } from 'react-router-dom';

function Navbar() {
    return (
        <nav className="bg-gray-900 text-white p-4">
            <div className="container mx-auto flex items-center justify-between">
                <div className="text-xl font-semibold">
                    <Link to="/">College ERP</Link>
                </div>
                <ul className="flex space-x-4">
                    <li>
                        <Link to="/" className="hover:text-gray-400">Home</Link>
                    </li>
                    <li>
                        <Link to="/employee" className="hover:text-gray-400">Employee</Link>
                    </li>
                    <li>
                        <Link to="/student" className="hover:text-gray-400">Student</Link>
                    </li>
                    <li>
                        <Link to="/about" className="hover:text-gray-400">About</Link>
                    </li>
                </ul>
            </div>
        </nav>
    );
}

export default Navbar;
