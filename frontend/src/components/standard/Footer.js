import React from 'react';

function Footer() {
    return (
        <footer className="bg-gray-900 text-white py-6">
            <div className="container mx-auto text-center">
                <p className="mb-2">College ERP for MAIT</p>
                <p className="mb-2">Made by ERP group</p>
                <p>&copy; {new Date().getFullYear()} All rights reserved</p>
            </div>
        </footer>
    );
}

export default Footer;
