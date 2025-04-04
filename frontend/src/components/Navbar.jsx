import { HashLink } from "react-router-hash-link";
import { auth } from "../firebase";
import { signInWithPopup, signOut, onAuthStateChanged } from "firebase/auth";
import { useState, useEffect, useRef } from "react";
import LoginModal from "./LoginModal";
import defaultUserIcon from "../assets/Sample_User_Icon.png";
import { Menu, X } from "lucide-react";

const Navbar = () => {
	const [user, setUser] = useState(null);
	const [isModalOpen, setIsModalOpen] = useState(false);
	const [showDropdown, setShowDropdown] = useState(false);
	const [menuOpen, setMenuOpen] = useState(false);
	const dropdownRef = useRef(null);

	useEffect(() => {
		const unsubscribe = onAuthStateChanged(auth, (firebaseUser) => {
			setUser(firebaseUser);
		});
		return () => unsubscribe();
	}, []);

	useEffect(() => {
		const handleClickOutside = (event) => {
			if (dropdownRef.current && !dropdownRef.current.contains(event.target)) {
				setShowDropdown(false);
			}
		};
		document.addEventListener("mousedown", handleClickOutside);
		return () => document.removeEventListener("mousedown", handleClickOutside);
	}, []);

	useEffect(() => {
		document.body.style.overflow = menuOpen ? "hidden" : "auto";
	}, [menuOpen]);

	const handleLogout = () => {
		signOut(auth);
		setShowDropdown(false);
		setMenuOpen(false);
	};

	return (
		<header className="fixed top-0 left-0 w-full z-[9999] bg-black/60 backdrop-blur-md px-6 py-5">
			<div className="flex justify-between items-center">
				<a
					href="/"
					className="text-xl sm:text-2xl font-medium tracking-wide text-white">
					<span style={{ color: "#FED34C" }}>Req</span>Check
				</a>

				{/* Desktop Nav */}
				<nav className="hidden md:flex items-center gap-6 text-sm sm:text-base font-medium text-white">
					<HashLink
						smooth
						to="/#faq"
						className="hover:text-[#FED34C] transition">
						FAQ
					</HashLink>
					<a href="/about" className="hover:text-[#FED34C] transition">
						About
					</a>
					<a href="/feedback" className="hover:text-[#FED34C] transition">
						Feedback
					</a>
					{user ? (
						<div className="relative" ref={dropdownRef}>
							<img
								src={user.photoURL || defaultUserIcon}
								alt="profile"
								className="w-9 h-9 rounded-full cursor-pointer border-2 border-white"
								onClick={() => setShowDropdown((prev) => !prev)}
							/>
							{showDropdown && (
								<div className="absolute right-0 mt-2 w-32 bg-[#1A1A1A] border border-gray-700 rounded-md shadow-lg py-2 z-50">
									<p className="text-sm text-center px-3 py-1 text-white truncate">
										{user.displayName || user.email}
									</p>
									<hr className="border-gray-600 my-1" />
									<button
										onClick={handleLogout}
										className="block w-full text-left px-4 py-2 text-sm text-white hover:bg-[#333] transition">
										Logout
									</button>
								</div>
							)}
						</div>
					) : (
						<button
							onClick={() => setIsModalOpen(true)}
							className="bg-[#FED34C] text-black font-semibold px-4 py-2 rounded-lg hover:bg-yellow-400 transition">
							Login
						</button>
					)}
				</nav>

				{/* Hamburger Menu Icon (mobile only) */}
				<div className="md:hidden">
					<button onClick={() => setMenuOpen(true)} className="text-white">
						<Menu size={28} />
					</button>
				</div>
			</div>

			{/* Full-Screen Overlay Mobile Menu */}
			<div
				className={`fixed inset-0 bg-black text-white z-[9999] transition-transform duration-300 ease-in-out ${
					menuOpen ? "translate-x-0" : "translate-x-full"
				} flex flex-col items-center justify-center`}>
				{/* Close Button */}
				<button
					onClick={() => setMenuOpen(false)}
					className="absolute top-6 right-6 text-white">
					<X size={32} />
				</button>

				{/* Menu Links */}
				<div className="flex flex-col gap-8 text-2xl font-medium">
					<HashLink
						smooth
						to="/#faq"
						onClick={() => setMenuOpen(false)}
						className="hover:text-[#FED34C]">
						FAQ
					</HashLink>
					<a
						href="/about"
						onClick={() => setMenuOpen(false)}
						className="hover:text-[#FED34C]">
						About
					</a>
					<a
						href="/feedback"
						onClick={() => setMenuOpen(false)}
						className="hover:text-[#FED34C]">
						Feedback
					</a>
					{user ? (
						<button
							onClick={handleLogout}
							className="hover:text-[#FED34C] text-xl">
							Logout
						</button>
					) : (
						<button
							onClick={() => {
								setIsModalOpen(true);
								setMenuOpen(false);
							}}
							className="bg-[#FED34C] text-black font-semibold px-6 py-2 rounded-lg hover:bg-yellow-400 transition">
							Login
						</button>
					)}
				</div>
			</div>

			<LoginModal isOpen={isModalOpen} onClose={() => setIsModalOpen(false)} />
		</header>
	);
};

export default Navbar;
