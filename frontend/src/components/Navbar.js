import React from "react";

const Navbar = () => {
	return (
		<nav className="flex justify-between items-center p-6 bg-dark text-white">
			<h1 className="text-2xl font-bold">WatCourse</h1>
			<div className="flex space-x-6">
				<a href="/" className="hover:text-primary">
					Home
				</a>
				<a href="/about" className="hover:text-primary">
					About Us
				</a>
			</div>
		</nav>
	);
};

export default Navbar;
