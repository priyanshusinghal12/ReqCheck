import { HashLink } from "react-router-hash-link";
import { auth } from "../firebase";
import { signOut, onAuthStateChanged, GoogleAuthProvider } from "firebase/auth";
import { useState, useEffect, useRef } from "react";
import defaultUserIcon from "../assets/Sample_User_Icon.png";
import { Menu, X } from "lucide-react";
import toast from "react-hot-toast";
import {
	reauthenticateWithPopup,
	reauthenticateWithCredential,
	EmailAuthProvider,
} from "firebase/auth";

const provider = new GoogleAuthProvider();

const Navbar = ({ setName, setShouldType, openGlobalModal }) => {
	const [user, setUser] = useState(null);
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
		signOut(auth)
			.then(() => {
				localStorage.removeItem("reqcheck_name");
				sessionStorage.removeItem("transcriptFilename");
				sessionStorage.removeItem("parsedCourses");
				sessionStorage.removeItem("selectedMajor");
				sessionStorage.removeItem("manualCourses");
				toast.success("Logged out.");
				window.location.reload();
			})
			.catch(() => toast.error("Logout failed."));
		setShowDropdown(false);
		setMenuOpen(false);
	};

	const handleDeleteAccount = async () => {
		const currentUser = auth.currentUser;
		if (!currentUser) return toast.error("Not logged in.");

		try {
			if (currentUser.providerData[0]?.providerId === "google.com") {
				await reauthenticateWithPopup(currentUser, provider);
				await proceedWithDeletion(currentUser);
				return;
			}

			let email = "";
			let password = "";

			toast.custom((t) => (
				<div className="bg-[#1A1A1A] p-4 rounded-lg text-white shadow-md w-[320px] border border-[#333]">
					<h3 className="font-semibold text-lg mb-2">
						Re-authenticate to Delete
					</h3>
					<input
						type="email"
						placeholder="Email"
						className="w-full mb-2 p-2 rounded bg-[#111] text-white border border-gray-700 text-sm"
						onChange={(e) => (email = e.target.value)}
					/>
					<input
						type="password"
						placeholder="Password"
						className="w-full mb-3 p-2 rounded bg-[#111] text-white border border-gray-700 text-sm"
						onChange={(e) => (password = e.target.value)}
					/>
					<div className="flex justify-between text-sm">
						<button
							onClick={async () => {
								if (!email || !password)
									return toast.error("Both fields required");
								toast.dismiss(t.id);
								try {
									const credential = EmailAuthProvider.credential(
										email,
										password
									);
									await reauthenticateWithCredential(currentUser, credential);
									await proceedWithDeletion(currentUser);
								} catch {
									toast.error("Re-authentication failed.");
								}
							}}
							className="bg-red-500 hover:bg-red-600 text-white px-3 py-1 rounded">
							Delete
						</button>
						<button
							onClick={() => toast.dismiss(t.id)}
							className="text-gray-400 hover:text-gray-200">
							Cancel
						</button>
					</div>
				</div>
			));
		} catch {
			toast.error("Re-authentication failed.");
		}
	};

	const proceedWithDeletion = async (user) => {
		try {
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
				localStorage.removeItem("reqcheck_name");
				toast.success("Account deleted.");
				window.location.reload();
			} else {
				toast.error(data.message || "Failed to delete account.");
			}
		} catch {
			toast.error("Account deletion failed.");
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
				{/* Hamburger */}
				<div className="md:hidden">
					<button onClick={() => setMenuOpen(true)} className="text-white">
						<Menu size={28} />
					</button>
				</div>
				{/* Desktop Nav */}
				<nav className="hidden md:flex items-center gap-6 text-sm sm:text-base font-medium text-white">
					<a href="/" className="hover:text-[#FED34C]">
						Home
					</a>
					<HashLink smooth to="/#faq" className="hover:text-[#FED34C]">
						FAQ
					</HashLink>
					<a href="/about" className="hover:text-[#FED34C]">
						About
					</a>
					<a href="/feedback" className="hover:text-[#FED34C]">
						Feedback
					</a>
					<HashLink smooth to="/#demo" className="hover:text-[#FED34C]">
						Demo Video
					</HashLink>
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
									<p className="text-sm text-left px-3 py-1 text-white truncate">
										{user.displayName || user.email}
									</p>
									<hr className="border-gray-600 my-1" />
									<a
										href="/saved"
										className="block px-4 py-2 text-sm text-white hover:bg-[#333]">
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
							onClick={openGlobalModal}
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
					<a
						href="/"
						onClick={() => setMenuOpen(false)}
						className="hover:text-[#FED34C]">
						Home
					</a>
					{user && (
						<a
							href="/saved"
							onClick={() => setMenuOpen(false)}
							className="hover:text-[#FED34C]">
							My Results
						</a>
					)}
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
					<HashLink
						smooth
						to="/#demo"
						onClick={() => setMenuOpen(false)}
						className="hover:text-[#FED34C]">
						Demo Video
					</HashLink>
					{user ? (
						<>
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
					) : (
						<button
							onClick={() => {
								openGlobalModal();
								setMenuOpen(false);
							}}
							className="bg-[#FED34C] text-black font-semibold px-4 py-2 rounded-lg hover:bg-yellow-400 transition">
							Login
						</button>
					)}
				</div>
			</div>
		</>
	);
};

export default Navbar;
