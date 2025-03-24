// src/components/Hero.jsx
import { useState, useRef, useEffect } from "react";
import { motion } from "framer-motion";
import { FaUpload } from "react-icons/fa";
import { Combobox } from "@headlessui/react";
import Logo from "../assets/Logo-watcourse.png";
import ParticlesBackground from "./ParticlesBackground";
import { useNavigate } from "react-router-dom";

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

export default function Hero() {
	const [selectedFile, setSelectedFile] = useState(null);
	const [fileContent, setFileContent] = useState(null);
	const [selectedMajor, setSelectedMajor] = useState("");
	const [query, setQuery] = useState("");
	const [isDropdownOpen, setDropdownOpen] = useState(false);
	const dropdownRef = useRef();
	const navigate = useNavigate();

	useEffect(() => {
		const handleClickOutside = (event) => {
			if (dropdownRef.current && !dropdownRef.current.contains(event.target)) {
				setDropdownOpen(false);
			}
		};
		document.addEventListener("mousedown", handleClickOutside);
		return () => document.removeEventListener("mousedown", handleClickOutside);
	}, []);

	const handleFileChange = async (event) => {
		const file = event.target.files[0];
		if (file && file.type === "application/pdf") {
			setSelectedFile(file.name);
			const reader = new FileReader();
			reader.onload = async () => {
				const base64 = reader.result.split(",")[1];
				const response = await fetch(
					"http://127.0.0.1:8000/parse-transcript/",
					{
						method: "POST",
						headers: { "Content-Type": "application/json" },
						body: JSON.stringify({ base64_pdf: base64 }),
					}
				);
				const data = await response.json();
				setFileContent(data.courses);
			};
			reader.readAsDataURL(file);
		} else {
			alert("Please upload a valid PDF file.");
		}
	};

	const handleGoClick = async () => {
		if (!fileContent || !selectedMajor) {
			alert("Please select a major and upload a transcript.");
			return;
		}
		const response = await fetch("http://127.0.0.1:8000/check-requirements/", {
			method: "POST",
			headers: { "Content-Type": "application/json" },
			body: JSON.stringify({
				major: selectedMajor.toLowerCase(),
				completed_courses: fileContent,
			}),
		});

		const data = await response.json();
		if (data.error) {
			alert("Invalid major selected or backend error.");
			return;
		}

		navigate("/results", { state: { results: data } });
	};

	const filteredMajors =
		query === ""
			? majors
			: majors.filter((major) =>
					major.toLowerCase().includes(query.toLowerCase())
			  );

	return (
		<section className="relative h-screen flex items-center justify-center text-white text-center overflow-hidden bg-black px-4">
			<ParticlesBackground />
			<motion.div
				className="relative z-10 w-full max-w-2xl flex flex-col items-center"
				initial={{ opacity: 0, y: 30 }}
				whileInView={{ opacity: 1, y: 0 }}
				transition={{ duration: 0.6 }}
				viewport={{ once: true }}>
				<motion.img
					src={Logo}
					alt="WatCourse Logo"
					className="w-96 md:w-[28rem] h-auto mb-6"
					initial={{ opacity: 0, scale: 0.85 }}
					animate={{ opacity: 1, scale: 1 }}
					transition={{ duration: 0.8 }}
				/>

				<motion.p className="text-base sm:text-lg font-medium mb-2">
					Your Personalized Requirement Tracker
				</motion.p>
				<motion.p className="text-gray-400 mb-6 text-sm sm:text-base">
					Check which major requirements you have met so far—simply upload your
					unofficial transcript PDF downloaded from Quest.
				</motion.p>

				<div className="flex flex-col sm:flex-row sm:items-center sm:gap-4 items-center justify-center w-full">
					<motion.label
						className="flex items-center justify-center gap-2 bg-[#FED34C] hover:scale-105 active:scale-95 transition-transform px-5 py-3 rounded-xl text-black font-semibold cursor-pointer shadow-md shadow-[#FED34C]/40 w-full sm:w-56"
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

					<Combobox value={selectedMajor} onChange={setSelectedMajor}>
						<div className="relative w-full sm:w-56" ref={dropdownRef}>
							<Combobox.Input
								className="bg-gray-800 border border-gray-600 px-4 py-3 rounded-xl text-white w-full cursor-pointer"
								placeholder="Select Major"
								onClick={() => setDropdownOpen(true)}
								onChange={(e) => {
									setQuery(e.target.value);
									setDropdownOpen(true);
								}}
								onFocus={() => setDropdownOpen(true)}
							/>
							{isDropdownOpen && (
								<Combobox.Options className="absolute mt-2 w-full bg-gray-900 border border-gray-700 rounded-lg shadow-lg max-h-48 overflow-y-auto z-50">
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
														active ? "bg-[#FED34C] text-black" : "text-gray-300"
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

				{selectedFile && (
					<motion.p className="mt-4 text-sm text-gray-400">
						Selected: {selectedFile}
					</motion.p>
				)}

				<motion.button
					onClick={handleGoClick}
					className="mt-4 bg-[#1E2633] text-white font-medium px-6 py-2 rounded-xl hover:scale-105 active:scale-95 transition-transform shadow-md"
					whileHover={{ scale: 1.05 }}
					whileTap={{ scale: 0.95 }}>
					Go
				</motion.button>
			</motion.div>
		</section>
	);
}
