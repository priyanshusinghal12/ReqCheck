import { HashLink } from "react-router-hash-link";
import { auth } from "../firebase";
import { signInWithPopup, signOut, onAuthStateChanged } from "firebase/auth";
import { useState, useEffect, useRef } from "react";
import LoginModal from "./LoginModal";
import defaultUserIcon from "../assets/Sample_User_Icon.png";
import { Menu, X } from "lucide-react";
import toast from "react-hot-toast";

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

	const handleLogout = () => {
		signOut(auth);
		setShowDropdown(false);
		setMenuOpen(false);
		toast.success("Logged out.");
	};

	const handleDeleteAccount = async () => {
		try {
			const user = auth.currentUser;
			if (!user) return toast.error("Not logged in.");
			const idToken = await user.getIdToken();

			const res = await fetch(
				`${import.meta.env.VITE_BACKEND_URL}/delete-account/`,
				{
					method: "DELETE",
					headers: { "Content-Type": "application/json" },
					body: JSON.stringify({ id_token: idToken }),
				}
			);

			const data = await res.json();
			if (data.status === "success") {
				await user.delete();
				toast.success("Account deleted.");
				setUser(null);
			} else {
				toast.error(data.message || "Failed to delete account.");
			}
		} catch (err) {
			toast.error("Error deleting account.");
		}
	};

	return (
		<>
			<header className="fixed top-0 w-full z-50 px-6 py-5 flex justify-between items-center backdrop-blur-sm bg-transparent">
				<a
					href="/"
					className="text-xl sm:text-2xl font-medium tracking-wide text-white">
					<span style={{ color: "#FED34C" }}>Req</span>Check
				</a>

				{/* Hamburger Icon */}
				<div className="md:hidden">
					<button onClick={() => setMenuOpen(true)} className="text-white">
						<Menu size={28} />
					</button>
				</div>

				{/* Desktop Nav */}
				<nav className="hidden md:flex items-center gap-6 text-sm sm:text-base font-medium text-white">
					<HashLink
						smooth
						to="/#faq"
						className="hover:text-[#FED34C] transition">
						FAQ
					</HashLink>
					<a href="/about" className="hover:text-[#FED34C]">
						About
					</a>
					<a href="/feedback" className="hover:text-[#FED34C]">
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
								<div className="absolute right-0 mt-2 w-40 bg-[#1A1A1A] border border-gray-700 rounded-md shadow-lg py-2 z-50">
									<p className="text-sm text-center px-3 py-1 text-white truncate">
										{user.displayName || user.email}
									</p>
									<hr className="border-gray-600 my-1" />
									<a
										href="/saved"
										className="block w-full text-left px-4 py-2 text-sm text-white hover:bg-[#333] transition">
										My Results
									</a>
									<hr className="border-gray-600 my-1" />
									<button
										onClick={handleLogout}
										className="block w-full text-left px-4 py-2 text-sm text-white hover:bg-[#333]">
										Logout
									</button>
									<button
										onClick={handleDeleteAccount}
										className="block w-full text-left px-4 py-2 text-sm text-red-500 hover:text-red-600">
										Delete Account
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
			</header>

			{/* Mobile Menu Overlay */}
			<div
				className={`fixed inset-0 bg-black/50 z-40 transition-opacity duration-300 ${
					menuOpen ? "opacity-100" : "opacity-0 pointer-events-none"
				}`}
				onClick={() => setMenuOpen(false)}
			/>

			{/* Mobile Menu Panel */}
			<div
				className={`fixed top-0 right-0 h-full w-64 bg-black text-white z-50 transform transition-transform duration-300 ease-in-out ${
					menuOpen ? "translate-x-0" : "translate-x-full"
				}`}>
				<div className="flex justify-between items-center p-4 border-b border-gray-700">
					<span className="text-lg font-semibold">Menu</span>
					<button onClick={() => setMenuOpen(false)}>
						<X size={24} />
					</button>
				</div>
				<div className="flex flex-col space-y-4 p-6 text-base">
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
					{user && (
						<>
							<a
								href="/saved"
								onClick={() => setMenuOpen(false)}
								className="hover:text-[#FED34C]">
								See Your Results
							</a>
							<button
								onClick={handleLogout}
								className="text-left hover:text-[#FED34C]">
								Logout
							</button>
							<button
								onClick={handleDeleteAccount}
								className="text-left text-red-500 hover:text-red-600">
								Delete Account
							</button>
						</>
					)}
					{!user && (
						<button
							onClick={() => {
								setIsModalOpen(true);
								setMenuOpen(false);
							}}
							className="bg-[#FED34C] text-black font-semibold px-4 py-2 rounded-lg hover:bg-yellow-400 transition">
							Login
						</button>
					)}
				</div>
			</div>

			<LoginModal isOpen={isModalOpen} onClose={() => setIsModalOpen(false)} />
		</>
	);
};

export default Navbar;
