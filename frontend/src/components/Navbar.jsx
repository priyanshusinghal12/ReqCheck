import { HashLink } from "react-router-hash-link";
import { auth, provider } from "../firebase";
import { signInWithPopup, signOut, onAuthStateChanged } from "firebase/auth";
import { useState, useEffect } from "react";

const Navbar = () => {
	const [user, setUser] = useState(null);

	useEffect(() => {
		const unsubscribe = onAuthStateChanged(auth, (firebaseUser) => {
			setUser(firebaseUser);
		});
		return () => unsubscribe();
	}, []);

	const handleLogin = async () => {
		try {
			await signInWithPopup(auth, provider);
		} catch (err) {
			console.error("Login failed", err);
		}
	};

	const handleLogout = () => {
		signOut(auth);
	};

	return (
		<header className="fixed top-0 w-full z-50 px-6 py-5 flex justify-between items-center backdrop-blur-sm bg-transparent">
			<a
				href="/"
				className="text-xl sm:text-2xl font-medium tracking-wide text-white">
				<span style={{ color: "#FED34C" }}>Req</span>Check
			</a>

			<nav className="flex items-center gap-6 text-sm sm:text-base font-medium text-white">
				<HashLink smooth to="/#faq" className="hover:text-[#FED34C] transition">
					FAQ
				</HashLink>
				<a href="/about" className="hover:text-[#FED34C] transition">
					About
				</a>
				<a href="/feedback" className="hover:text-[#FED34C] transition">
					Feedback
				</a>

				{/* Auth Controls */}
				{user ? (
					<div className="flex items-center gap-2">
						<span className="text-sm hidden sm:inline text-gray-300 truncate max-w-[120px]">
							{user.displayName}
						</span>
						<button
							onClick={handleLogout}
							className="bg-[#FED34C] text-black text-sm px-3 py-1 rounded-md hover:bg-yellow-400 transition">
							Logout
						</button>
					</div>
				) : (
					<button
						onClick={handleLogin}
						className="bg-[#FED34C] text-black text-sm px-3 py-1 rounded-md hover:bg-yellow-400 transition">
						Login
					</button>
				)}
			</nav>
		</header>
	);
};

export default Navbar;
