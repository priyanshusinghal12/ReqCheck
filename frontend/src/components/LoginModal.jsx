import { useState } from "react";
import { auth, provider } from "../firebase";
import {
	signInWithEmailAndPassword,
	createUserWithEmailAndPassword,
	signInWithPopup,
	sendPasswordResetEmail,
	updateProfile,
} from "firebase/auth";
import { motion, AnimatePresence } from "framer-motion";
import toast from "react-hot-toast";

const LoginModal = ({ isOpen, onClose, setName, setShouldType }) => {
	const [email, setEmail] = useState("");
	const [password, setPassword] = useState("");
	const [nameInput, setNameInput] = useState("");
	const [isSignup, setIsSignup] = useState(false);
	const [error, setError] = useState("");

	const triggerWelcomeAnimation = (name) => {
		setName(name);
		setShouldType(false);
		setTimeout(() => setShouldType(true), 10);
	};

	const handleEmailAuth = async () => {
		try {
			let finalName = "";

			if (isSignup) {
				const userCredential = await createUserWithEmailAndPassword(
					auth,
					email,
					password
				);
				await updateProfile(userCredential.user, { displayName: nameInput });
				finalName = nameInput.trim().split(" ")[0];
			} else {
				const userCredential = await signInWithEmailAndPassword(
					auth,
					email,
					password
				);
				const firebaseName = userCredential.user?.displayName || "";
				finalName = firebaseName.trim().split(" ")[0];
			}

			localStorage.setItem("reqcheck_name", finalName);
			triggerWelcomeAnimation(finalName);
			toast.success(
				isSignup ? "Account created successfully!" : "Logged in successfully!"
			);
			onClose();
		} catch (err) {
			setError(err.message);
			toast.error("Authentication failed. Please check your credentials.");
		}
	};

	const handleGoogleSignIn = async () => {
		try {
			const result = await signInWithPopup(auth, provider);
			const displayName = result.user.displayName || "";
			const firstName = displayName.trim().split(" ")[0];

			localStorage.setItem("reqcheck_name", firstName);
			triggerWelcomeAnimation(firstName);
			toast.success("Logged in with Google!");
			onClose();
		} catch {
			toast.error("Google login failed.");
		}
	};

	const handleForgotPassword = async () => {
		if (!email) {
			toast.error("Enter your email to reset your password.");
			return;
		}
		try {
			await sendPasswordResetEmail(auth, email);
			toast.success("Password reset email sent.");
		} catch {
			toast.error("Failed to send reset email.");
		}
	};

	const continueAsGuest = () => {
		localStorage.removeItem("reqcheck_name");
		triggerWelcomeAnimation("");
		onClose();
	};

	return (
		<AnimatePresence>
			{isOpen && (
				<div className="fixed inset-0 z-50 bg-black/50 backdrop-blur-md">
					<div className="w-full min-h-screen flex items-center justify-center mt-8">
						<motion.div
							className="bg-[#1A1A1A] p-8 sm:p-10 rounded-2xl w-[90%] sm:w-[500px] shadow-xl border border-[#2A2A2A] relative"
							initial={{ opacity: 0, scale: 0.95 }}
							animate={{ opacity: 1, scale: 1 }}
							exit={{ opacity: 0, scale: 0.95 }}
							transition={{ duration: 0.3 }}>
							<button
								onClick={onClose}
								className="absolute top-4 right-5 text-gray-400 hover:text-white text-2xl">
								×
							</button>

							<h1 className="text-white text-2xl font-extrabold mb-6 text-center">
								{isSignup ? "Create an Account" : "Welcome Back"}
							</h1>

							{isSignup && (
								<input
									type="text"
									placeholder="Full Name"
									className="w-full p-3 bg-[#111] border border-gray-700 rounded-md text-white placeholder-gray-400 mb-4"
									value={nameInput}
									onChange={(e) => setNameInput(e.target.value)}
								/>
							)}

							<input
								type="email"
								placeholder="Email"
								className="w-full p-3 bg-[#111] border border-gray-700 rounded-md text-white placeholder-gray-400 mb-4"
								value={email}
								onChange={(e) => setEmail(e.target.value)}
							/>

							<input
								type="password"
								placeholder="Password"
								className="w-full p-3 bg-[#111] border border-gray-700 rounded-md text-white placeholder-gray-400 mb-4"
								value={password}
								onChange={(e) => setPassword(e.target.value)}
							/>

							{error && (
								<p className="text-red-400 text-sm text-center mb-3">{error}</p>
							)}

							<button
								onClick={handleEmailAuth}
								className="w-full bg-[#FED34C] text-black py-3 rounded-md font-semibold mb-4">
								{isSignup ? "Sign Up" : "Login"}
							</button>

							{!isSignup && (
								<p className="text-sm text-center mb-3">
									<span
										className="text-yellow-400 hover:underline cursor-pointer"
										onClick={handleForgotPassword}>
										Forgot your password?
									</span>
								</p>
							)}

							<p className="text-gray-300 text-center text-sm">
								{isSignup
									? "Already have an account? "
									: "Don't have an account? "}
								<span
									className="text-yellow-400 hover:underline cursor-pointer"
									onClick={() => setIsSignup(!isSignup)}>
									{isSignup ? "Log in here" : "Sign up here"}
								</span>
							</p>

							<div className="flex items-center justify-center mt-6">
								<button
									onClick={handleGoogleSignIn}
									className="flex items-center gap-3 px-6 py-3 bg-white text-black rounded-md shadow">
									<img
										src="https://www.svgrepo.com/show/475656/google-color.svg"
										alt="Google"
										className="w-5 h-5"
									/>
									Continue with Google
								</button>
							</div>

							<div className="text-center mt-5">
								<button
									onClick={continueAsGuest}
									className="text-sm text-gray-400 hover:underline">
									Continue as Guest
								</button>
							</div>
						</motion.div>
					</div>
				</div>
			)}
		</AnimatePresence>
	);
};

export default LoginModal;
