import { HashLink } from "react-router-hash-link";

const Navbar = () => {
	return (
		<header className="fixed top-0 w-full z-50 px-6 py-5 flex justify-between items-center backdrop-blur-sm bg-transparent">
			<a href="/" className="text-xl sm:text-2xl font-medium tracking-wide">
				<span style={{ color: "#FED34C" }}>Req</span>Check
			</a>

			<nav className="flex gap-6 text-sm sm:text-base font-medium text-white">
				<HashLink smooth to="/#faq" className="hover:text-[#FED34C] transition">
					FAQ
				</HashLink>
				<a href="/about" className="hover:text-[#FED34C] transition">
					About
				</a>
				<a href="/feedback" className="hover:text-[#FED34C] transition">
					Feedback
				</a>
			</nav>
		</header>
	);
};

export default Navbar;
