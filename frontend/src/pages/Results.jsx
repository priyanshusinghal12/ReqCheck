import { HashLink } from "react-router-hash-link";
import { auth, provider } from "../firebase";
import { signInWithPopup, signOut } from "firebase/auth";
import { useState, useEffect, useRef } from "react";

const Navbar = () => {
	const [user, setUser] = useState(null);
	const [dropdownOpen, setDropdownOpen] = useState(false);
	const dropdownRef = useRef();

	useEffect(() => {
		const unsubscribe = auth.onAuthStateChanged((user) => {
			setUser(user);
		});

		// Close dropdown if clicked outside
		const handleClickOutside = (e) => {
			if (dropdownRef.current && !dropdownRef.current.contains(e.target)) {
				setDropdownOpen(false);
			}
		};

		document.addEventListener("mousedown", handleClickOutside);
		return () => {
			unsubscribe();
			document.removeEventListener("mousedown", handleClickOutside);
		};
	}, []);

	const handleLogin = async () => {
		try {
			await signInWithPopup(auth, provider);
		} catch (error) {
			console.error("Login failed", error);
		}
	};

	const handleLogout = async () => {
		try {
			await signOut(auth);
		} catch (error) {
			console.error("Logout failed", error);
		}
	};

	return (
		<header className="fixed top-0 w-full z-50 px-6 py-5 flex justify-between items-center backdrop-blur-sm bg-transparent">
			<a href="/" className="text-xl sm:text-2xl font-medium tracking-wide">
				<span style={{ color: "#FED34C" }}>Req</span>Check
			</a>

			<nav className="flex gap-6 text-sm sm:text-base font-medium text-white items-center">
				<HashLink smooth to="/#faq" className="hover:text-[#FED34C] transition">
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
							src={user.photoURL}
							alt="Profile"
							onClick={() => setDropdownOpen(!dropdownOpen)}
							className="w-8 h-8 rounded-full cursor-pointer border border-white"
						/>
						{dropdownOpen && (
							<div className="absolute right-0 mt-2 w-32 bg-[#1A1A1A] border border-[#333] rounded-lg shadow-md">
								<button
									onClick={handleLogout}
									className="block w-full text-left px-4 py-2 text-sm text-white hover:bg-[#333] rounded-lg">
									Logout
								</button>
							</div>
						)}
					</div>
				) : (
					<button
						onClick={handleLogin}
						className="bg-[#FED34C] text-black font-semibold px-4 py-2 rounded-lg hover:bg-yellow-400 transition">
						Login
					</button>
				)}
			</nav>
		</header>
	);
};

export default Navbar;
