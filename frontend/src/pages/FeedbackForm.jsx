import React, { useState } from "react";
import { FaStar, FaStarHalfAlt, FaRegStar } from "react-icons/fa";
import emailjs from "emailjs-com";
import { Filter } from "bad-words";
import Navbar from "../components/Navbar";
import ParticlesBackground from "../components/ParticlesBackground";

const SERVICE_ID = import.meta.env.VITE_EMAILJS_SERVICE_ID;
const TEMPLATE_ID = import.meta.env.VITE_EMAILJS_TEMPLATE_ID;
const PUBLIC_KEY = import.meta.env.VITE_EMAILJS_PUBLIC_KEY;

const FeedbackForm = () => {
	const [rating, setRating] = useState(0);
	const [hover, setHover] = useState(null);
	const [message, setMessage] = useState("");
	const [submitted, setSubmitted] = useState(false);
	const [error, setError] = useState("");

	const handleRating = (value) => {
		if (value === rating) {
			setRating(value - 0.5); // toggle half star
		} else {
			setRating(value);
		}
	};

	const handleSubmit = (e) => {
		e.preventDefault();
		const filter = new Filter();

		if (filter.isProfane(message)) {
			setError("Your text contains foul language! Please rephrase!");
			return;
		}

		const templateParams = {
			title: "User Feedback",
			rating,
			message,
		};

		emailjs
			.send(SERVICE_ID, TEMPLATE_ID, templateParams, PUBLIC_KEY)
			.then(() => {
				setSubmitted(true);
				setMessage("");
				setRating(0);
				setError("");
			})
			.catch((error) => {
				console.error("EmailJS Error:", error);
				setError("Oops! Something went wrong. Try again later.");
			});
	};

	return (
		<>
			<Navbar />
			<ParticlesBackground />
			<div className="flex flex-col items-center justify-center min-h-screen px-6 text-white bg-black">
				{!submitted ? (
					<form
						onSubmit={handleSubmit}
						className="bg-[#111] p-8 rounded-xl shadow-lg border border-gray-800 w-full max-w-xl">
						<h1 className="text-3xl font-bold mb-6 text-center">
							We’d love your feedback!
						</h1>

						<label className="block text-lg font-medium mb-2">
							How would you rate your experience?
						</label>
						<div className="flex items-center mb-6">
							{[1, 2, 3, 4, 5].map((value) => {
								const full = value <= Math.floor(hover ?? rating);
								const half = value - 0.5 === rating;
								return (
									<span
										key={value}
										className="text-3xl cursor-pointer transition-transform duration-200 transform hover:scale-110"
										onClick={() => handleRating(value)}
										onMouseEnter={() => setHover(value)}
										onMouseLeave={() => setHover(null)}>
										{full ? (
											<FaStar className="text-yellow-400" />
										) : half ? (
											<FaStarHalfAlt className="text-yellow-400" />
										) : (
											<FaRegStar className="text-gray-500" />
										)}
									</span>
								);
							})}
						</div>

						<label className="block text-lg font-medium mb-2">
							Your feedback
						</label>
						<textarea
							className="w-full p-4 rounded-lg bg-black border border-gray-700 text-gray-100 placeholder-gray-400 resize-none min-h-[160px]"
							placeholder="Tell us what you liked or what we can improve..."
							value={message}
							onChange={(e) => setMessage(e.target.value)}
							required
						/>

						{error && <p className="text-red-500 mt-4 font-medium">{error}</p>}

						<button
							type="submit"
							className="w-full mt-6 py-3 bg-[#FED34C] text-black border border-[#333] font-semibold rounded-lg transition duration-200 hover:bg-white hover:text-black">
							Submit Feedback
						</button>
					</form>
				) : (
					<div className="text-center max-w-xl px-4">
						<h2 className="text-3xl font-bold mb-4 text-yellow-400">
							Thank you so much! 💛
						</h2>
						<p className="text-lg text-gray-300">
							We truly appreciate your feedback and are always looking for ways
							to improve. Your thoughts help shape the future of ReqCheck!
						</p>
					</div>
				)}
			</div>
		</>
	);
};

export default FeedbackForm;
