import { Link } from "react-router-dom";

const Navbar = () => {
	return (
		<nav className="flex justify-between items-center px-10 py-6 bg-dark text-white">
			<h1 className="text-2xl font-bold text-primary">WatCourse</h1>
			<div className="flex space-x-6">
				<Link to="/" className="hover:text-primary transition">
					Home
				</Link>
				<Link to="/about" className="hover:text-primary transition">
					About Us
				</Link>
			</div>
		</nav>
	);
};

export default Navbar;
