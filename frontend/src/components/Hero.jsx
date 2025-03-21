import React, { useState } from "react";
import { motion } from "framer-motion";
import { FaUpload } from "react-icons/fa";
import { Combobox } from "@headlessui/react";
import Logo from "../assets/Logo-watcourse.png"; // Import logo

const majors = [
	"Actuarial Science",
	"Applied Mathematics",
	"Biostatistics",
	"Combinatorics and Optimization",
	"Computational Mathematics",
	"Data Science",
	"Mathematical Economics",
	"Mathematical Finance",
	"Mathematical Optimization",
	"Mathematical Physics",
	"Mathematical Studies",
	"Pure Mathematics",
	"Statistics",
	"Mathematics/Teaching",
];

const Hero = () => {
	const [selectedFile, setSelectedFile] = useState(null);
	const [selectedMajor, setSelectedMajor] = useState("");
	const [query, setQuery] = useState("");
	const [isDropdownOpen, setDropdownOpen] = useState(false);

	const handleFileChange = (event) => {
		const file = event.target.files[0];
		if (file && file.type === "application/pdf") {
			setSelectedFile(file.name);
		} else {
			alert("Please upload a valid PDF file.");
		}
	};

	const filteredMajors =
		query === ""
			? majors
			: majors.filter((major) =>
					major.toLowerCase().includes(query.toLowerCase())
			  );

	return (
		<section className="relative flex flex-col items-center justify-center text-center px-6 py-16 bg-[#0D1117] text-white min-h-screen">
			{/* Subtle Background Gradient */}
			<div className="absolute inset-0 bg-gradient-to-br from-black via-[#0D1117] to-gray-900 opacity-40"></div>

			{/* Animated Logo */}
			<motion.img
				src={Logo}
				alt="WatCourse Logo"
				className="w-72 md:w-80 lg:w-96 h-auto mb-6 relative"
				initial={{ opacity: 0, scale: 0.85 }}
				animate={{ opacity: 1, scale: 1 }}
				transition={{ duration: 0.8 }}
			/>

			{/* Tagline (Softer gold, Smaller text) */}
			<motion.p
				className="text-[#C49A3A] text-lg font-medium max-w-2xl mb-2 relative"
				initial={{ opacity: 0 }}
				animate={{ opacity: 1 }}
				transition={{ delay: 0.5, duration: 0.8 }}>
				"Your Personalized Requirement Tracker"
			</motion.p>

			{/* Subtitle */}
			<motion.p
				className="text-gray-400 max-w-2xl mb-8 text-base relative"
				initial={{ opacity: 0 }}
				animate={{ opacity: 1 }}
				transition={{ delay: 0.3, duration: 0.8 }}>
				Check which major requirements you have met so far—simply upload your
				unofficial transcript PDF downloaded from Quest. None of your
				information is stored.
			</motion.p>

			{/* Upload & Major Selection */}
			<div className="flex flex-col md:flex-row gap-4 relative">
				{/* Upload Button with Softer Glow */}
				<motion.label
					className="flex items-center gap-2 bg-[#C49A3A] hover:bg-[#B38A2E] hover:scale-105 active:scale-95 transition-transform px-6 py-3 rounded-xl text-black font-semibold cursor-pointer shadow-md shadow-[#C49A3A]/40"
					whileHover={{ scale: 1.05 }}
					whileTap={{ scale: 0.95 }}>
					<FaUpload />
					Upload Transcript
					<input
						type="file"
						accept=".pdf"
						className="hidden"
						onChange={handleFileChange}
					/>
				</motion.label>

				{/* Fancy Dropdown */}
				<Combobox
					value={selectedMajor}
					onChange={setSelectedMajor}
					open={isDropdownOpen}
					onOpenChange={setDropdownOpen}>
					<div className="relative w-64">
						<Combobox.Input
							className="bg-gray-800 border border-gray-600 px-4 py-3 rounded-xl text-white w-full cursor-pointer"
							placeholder="Select Major"
							onClick={() => setDropdownOpen(!isDropdownOpen)}
							onChange={(event) => setQuery(event.target.value)}
						/>
						{isDropdownOpen && (
							<Combobox.Options className="absolute mt-2 w-full bg-gray-900 border border-gray-700 rounded-lg shadow-lg overflow-hidden max-h-48 overflow-y-auto">
								{filteredMajors.length === 0 ? (
									<Combobox.Option
										className="p-2 text-gray-400"
										value=""
										disabled>
										No majors found
									</Combobox.Option>
								) : (
									filteredMajors.map((major, index) => (
										<Combobox.Option
											key={index}
											value={major}
											className={({ active }) =>
												`p-3 cursor-pointer ${
													active ? "bg-[#C49A3A] text-black" : "text-gray-300"
												}`
											}>
											{major}
										</Combobox.Option>
									))
								)}
							</Combobox.Options>
						)}
					</div>
				</Combobox>
			</div>

			{/* Display Selected File Name */}
			{selectedFile && (
				<motion.p
					className="mt-4 text-sm text-gray-400 relative"
					initial={{ opacity: 0 }}
					animate={{ opacity: 1 }}
					transition={{ duration: 0.5 }}>
					Selected: {selectedFile}
				</motion.p>
			)}
		</section>
	);
};

export default Hero;
