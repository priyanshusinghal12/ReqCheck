import { useState } from "react";
import { auth, provider } from "../firebase";
import {
	signInWithEmailAndPassword,
	createUserWithEmailAndPassword,
	signInWithPopup,
	sendPasswordResetEmail,
} from "firebase/auth";
import { motion, AnimatePresence } from "framer-motion";
import toast from "react-hot-toast";

const LoginModal = ({ isOpen, onClose }) => {
	const [email, setEmail] = useState("");
	const [password, setPassword] = useState("");
	const [isSignup, setIsSignup] = useState(false);
	const [error, setError] = useState("");

	const handleEmailAuth = async () => {
		try {
			if (isSignup) {
				await createUserWithEmailAndPassword(auth, email, password);
				toast.success("Account created successfully!");
			} else {
				await signInWithEmailAndPassword(auth, email, password);
				toast.success("Logged in successfully!");
			}
			onClose();
		} catch (err) {
			setError(err.message);
			toast.error("Authentication failed. Please check your credentials.");
		}
	};

	const handleGoogleSignIn = async () => {
		try {
			await signInWithPopup(auth, provider);
			toast.success("Logged in with Google!");
			onClose();
		} catch (err) {
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
		} catch (err) {
			toast.error("Failed to send reset email.");
		}
	};

	return (
		<AnimatePresence initial={false}>
			{isOpen && (
				<div className="fixed inset-0 z-50 bg-black/50 backdrop-blur-md backdrop-saturate-150">
					<div className="w-full min-h-screen flex items-center justify-center mt-8">
						<motion.div
							className="bg-[#1A1A1A] p-8 sm:p-10 rounded-2xl w-[90%] sm:w-[500px] md:w-[600px] shadow-xl border border-[#2A2A2A] relative"
							initial={{ opacity: 0, scale: 0.95 }}
							animate={{ opacity: 1, scale: 1 }}
							exit={{ opacity: 0, scale: 0.95 }}
							transition={{ duration: 0.3, ease: "easeOut" }}
							onClick={(e) => e.stopPropagation()}>
							{/* Close button */}
							<button
								onClick={onClose}
								className="absolute top-4 right-5 text-gray-400 hover:text-white text-2xl transition">
								×
							</button>

							{/* Title */}
							<h1 className="text-white text-2xl font-extrabold mb-6 text-center tracking-tight">
								{isSignup ? "Create an Account" : "Welcome Back"}
							</h1>

							{/* Email input */}
							<input
								type="email"
								placeholder="Email"
								className="w-full p-3 text-sm sm:text-base bg-[#111] border border-gray-700 rounded-md text-white placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-yellow-400 mb-4"
								value={email}
								onChange={(e) => setEmail(e.target.value)}
							/>

							{/* Password input */}
							<input
								type="password"
								placeholder="Password"
								className="w-full p-3 text-sm sm:text-base bg-[#111] border border-gray-700 rounded-md text-white placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-yellow-400 mb-4"
								value={password}
								onChange={(e) => setPassword(e.target.value)}
							/>

							{/* Error */}
							{error && (
								<p className="text-red-400 text-sm text-center mb-3">{error}</p>
							)}

							{/* Submit button */}
							<button
								onClick={handleEmailAuth}
								className="w-full bg-[#FED34C] hover:bg-[#f7c634] text-black py-3 rounded-md font-semibold text-base transition mb-4">
								{isSignup ? "Sign Up" : "Login"}
							</button>

							{/* Conditional UW note or Forgot Password */}
							{isSignup ? (
								<p className="text-xs text-gray-500 font-medium mb-3 text-center">
									Note: UW emails may not support password reset.
								</p>
							) : (
								<p className="text-sm text-center mt-3">
									<span
										className="text-yellow-400 hover:underline cursor-pointer"
										onClick={handleForgotPassword}>
										Forgot your password?
									</span>
								</p>
							)}

							{/* Toggle Login/Signup */}
							<p className="text-gray-300 text-center text-sm mt-5">
								{isSignup
									? "Already have an account? "
									: "Don't have an account? "}
								<span
									className="text-yellow-400 hover:underline cursor-pointer"
									onClick={() => setIsSignup(!isSignup)}>
									{isSignup ? "Log in here" : "Sign up here"}
								</span>
							</p>

							{/* Google Sign In */}
							<div className="flex items-center justify-center mt-6">
								<button
									onClick={handleGoogleSignIn}
									className="flex items-center gap-3 px-6 py-3 bg-white text-black text-base rounded-md shadow hover:bg-gray-100 transition">
									<img
										src="https://www.svgrepo.com/show/475656/google-color.svg"
										alt="Google"
										className="w-5 h-5"
									/>
									Continue with Google
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
