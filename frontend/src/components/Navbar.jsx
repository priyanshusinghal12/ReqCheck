import { NavLink } from "react-router-dom";

const Navbar = () => {
	return (
		<header className="fixed top-0 w-full z-50 px-6 py-5 flex justify-between items-center backdrop-blur-sm bg-transparent">
			<a
				href="/"
				className="text-xl sm:text-2xl font-extrabold text-[#FED34C] tracking-wide">
				WatCourse
			</a>
			<nav className="flex gap-6 text-sm sm:text-base font-medium text-white">
				<a href="#faq" className="hover:text-[#FED34C] transition">
					FAQ
				</a>
				<a href="/about" className="hover:text-[#FED34C] transition">
					About Us
				</a>
			</nav>
		</header>
	);
};

export default Navbar;
