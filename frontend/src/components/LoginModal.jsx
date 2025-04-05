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
					<div className="w-full min-h-screen flex items-center justify-center mt-[30px] -translate-y-4">
						<motion.div
							className="bg-[#1A1A1A] p-10 rounded-2xl w-[95%] sm:w-[600px] md:w-[700px] shadow-2xl border border-[#333] relative"
							initial={{ opacity: 0, scale: 0.95 }}
							animate={{ opacity: 1, scale: 1 }}
							exit={{ opacity: 0, scale: 0.95 }}
							transition={{ duration: 0.25, ease: "easeOut" }}
							onClick={(e) => e.stopPropagation()}>
							<button
								onClick={onClose}
								className="absolute top-3 right-4 text-white text-xl">
								×
							</button>

							<h2 className="text-white text-xl font-bold mb-4 text-center">
								{isSignup ? "Sign Up" : "Login"}
							</h2>

							<input
								type="email"
								placeholder="abc@example.com"
								className="w-full text-lg p-4 mb-4 bg-[#111] border border-gray-700 rounded text-white"
								value={email}
								onChange={(e) => setEmail(e.target.value)}
							/>
							<input
								type="password"
								placeholder="Password"
								className="w-full text-lg p-4 mb-5 bg-[#111] border border-gray-700 rounded text-white"
								value={password}
								onChange={(e) => setPassword(e.target.value)}
							/>

							{error && <p className="text-red-400 text-sm mb-3">{error}</p>}

							<button
								onClick={handleEmailAuth}
								className="w-full bg-[#FED34C] text-black py-3 text-lg rounded font-semibold mb-4">
								{isSignup ? "Create Account" : "Login"}
							</button>

							<p className="text-white text-center text-sm mb-3">
								{isSignup
									? "Already have an account?"
									: "Don't have an account?"}{" "}
								<span
									className="text-[#FED34C] cursor-pointer underline"
									onClick={() => setIsSignup(!isSignup)}>
									{isSignup ? "Log in here" : "Sign up here"}
								</span>
							</p>
							<p className="text-sm text-gray-400 mt-2 text-center">
								<span
									className="text-yellow-400 hover:underline cursor-pointer"
									onClick={handleForgotPassword}>
									Forgot your password?
								</span>
							</p>

							<div className="flex items-center justify-center mt-4">
								<button
									onClick={handleGoogleSignIn}
									className="flex items-center gap-3 px-6 py-3 bg-white text-black text-base rounded hover:bg-gray-200 transition">
									<img
										src="https://www.svgrepo.com/show/475656/google-color.svg"
										alt="Google"
										className="w-6 h-6"
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
