import React from "react";
import { motion } from "framer-motion";

const Hero = () => {
	return (
		<div className="flex flex-col items-center justify-center text-center h-screen bg-dark text-white">
			<h1 className="text-6xl font-bold">WATCOURSE</h1>
			<p className="text-grayText mt-4">
				Check which major requirements you have met so far. We do not store your
				data.
			</p>
			<div className="flex space-x-4 mt-6">
				<motion.button
					whileHover={{ scale: 1.1 }}
					className="bg-primary text-black px-6 py-3 rounded-lg font-bold">
					Upload Transcript
				</motion.button>
				<motion.button
					whileHover={{ scale: 1.1 }}
					className="bg-gray-700 text-white px-6 py-3 rounded-lg font-bold">
					Select Major
				</motion.button>
			</div>
		</div>
	);
};

export default Hero;
