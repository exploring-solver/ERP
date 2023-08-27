import React from 'react';
import { Link } from 'react-router-dom';

function StudentPortal() {
    return (
        <div className="container mx-auto mt-8">
            <h2 className="text-xl font-semibold mb-4">Student Portal</h2>
            <div className="grid grid-cols-3 gap-4">
                <Link to="/student/login" className="bg-blue-500 hover:bg-blue-600 text-white p-4 rounded-lg shadow">
                    <h3 className="text-lg font-semibold mb-2">Login</h3>
                    <p>Existing student login</p>
                </Link>
                <Link to="/student/register" className="bg-green-500 hover:bg-green-600 text-white p-4 rounded-lg shadow">
                    <h3 className="text-lg font-semibold mb-2">Register</h3>
                    <p>Create a student account</p>
                </Link>
                <Link to="/student/admission" className="bg-yellow-500 hover:bg-yellow-600 text-white p-4 rounded-lg shadow">
                    <h3 className="text-lg font-semibold mb-2">Admission</h3>
                    <p>Apply for admission</p>
                </Link>
            </div>
        </div>
    );
}

export default StudentPortal;