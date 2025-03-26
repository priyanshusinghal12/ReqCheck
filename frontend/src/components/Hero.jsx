import { useState, useRef, useEffect } from "react";
import { motion } from "framer-motion";
import { FaUpload, FaArrowRight, FaExchangeAlt } from "react-icons/fa";
import { Combobox } from "@headlessui/react";
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
	const [manualCourses, setManualCourses] = useState("");
	const [isManual, setIsManual] = useState(false);
	const [badCourses, setBadCourses] = useState([]);
	const [isDropdownOpen, setDropdownOpen] = useState(false);

	const dropdownRef = useRef();
	const navigate = useNavigate();

	const courseRegex = /^[A-Z]{2,8} \d{3}[A-Z]?$/;

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
			setSelectedFile(file);
			const reader = new FileReader();
			reader.onload = async () => {
				try {
					const base64 = reader.result.split(",")[1];
					const response = await fetch("/parse-transcript/", {
						method: "POST",
						headers: { "Content-Type": "application/json" },
						body: JSON.stringify({ base64_pdf: base64 }),
					});
					const data = await response.json();
					setFileContent(data.courses);
				} catch (error) {
					alert("Failed to parse transcript.");
					console.error(error);
				}
			};
			reader.readAsDataURL(file);
		} else {
			alert("Please upload a valid PDF file.");
		}
	};

	const handleGoClick = async () => {
		let majorToUse = selectedMajor;

		if (!majorToUse && query) {
			const matched = majors.find(
				(m) => m.toLowerCase() === query.toLowerCase()
			);
			if (matched) {
				setSelectedMajor(matched);
				majorToUse = matched;
			} else {
				alert("Please select a valid major from the dropdown.");
				return;
			}
		}

		if (!majorToUse) {
			alert("Please select a major.");
			return;
		}

		let allCourses = [];

		if (isManual) {
			const entries = manualCourses
				.split(/[,;\n]/)
				.map((c) => c.trim().toUpperCase())
				.filter(Boolean);

			const valid = entries.filter((c) => courseRegex.test(c));
			const invalid = entries.filter((c) => !courseRegex.test(c));

			if (valid.length === 0) {
				alert(
					"Please enter at least one valid course like CS 136L or ECON 201."
				);
				return;
			}

			setBadCourses(invalid);
			allCourses = valid;
		} else {
			if (!fileContent || fileContent.length === 0) {
				alert("Please upload a transcript first.");
				return;
			}
			allCourses = fileContent;
		}

		try {
			const response = await fetch("/check-requirements/", {
				method: "POST",
				headers: { "Content-Type": "application/json" },
				body: JSON.stringify({
					major: majorToUse.toLowerCase(),
					completed_courses: allCourses,
				}),
			});
			const data = await response.json();
			if (data.error) {
				alert("Invalid major selected or backend error.");
				return;
			}
			navigate("/results", { state: { results: data } });
		} catch (error) {
			alert("Failed to fetch requirements.");
			console.error(error);
		}
	};

	const filteredMajors =
		query === ""
			? majors
			: majors.filter((major) =>
					major.toLowerCase().includes(query.toLowerCase())
			  );

	return (
		<section className="relative min-h-[95vh] flex items-center justify-center text-white text-center overflow-hidden bg-black px-4 pb-10">
			<ParticlesBackground />
			<motion.div
				className="relative z-10 w-full max-w-2xl flex flex-col items-center"
				initial={{ opacity: 0, y: 30 }}
				whileInView={{ opacity: 1, y: 0 }}
				transition={{ duration: 0.6 }}
				viewport={{ once: true }}>
				<motion.h1 className="text-5xl sm:text-6xl font-medium mb-4">
					<span className="text-[#FED34C]">Req</span>Check
				</motion.h1>

				<motion.p className="text-base text-gray-100 sm:text-lg font-medium mb-2">
					The one-click tool to check your missing and satisfied major
					requirements.
				</motion.p>
				<motion.p className="text-gray-400 mb-6 text-sm sm:text-base whitespace-nowrap overflow-auto">
					Select between: uploading your unofficial transcript or entering your
					completed courses manually!
				</motion.p>

				<div className="flex items-center gap-3 mb-6 shadow-md">
					<button
						className={`px-4 py-2 rounded-lg font-semibold ${
							isManual
								? "bg-[#1A1A1A] text-white border border-[#333]"
								: "bg-[#1A1A1A] text-white border border-[#FED34C]"
						}`}
						onClick={() => setIsManual(false)}>
						Uploading your transcript
					</button>
					<button
						className={`px-4 py-2 rounded-lg font-semibold ${
							isManual
								? "bg-[#1A1A1A] text-white border border-[#FED34C]"
								: "bg-[#1A1A1A] text-white border border-[#333]"
						}`}
						onClick={() => setIsManual(true)}>
						Enter Courses Manually
					</button>
				</div>

				{!isManual ? (
					<motion.label className="flex items-center justify-center gap-2 bg-[#FED34C] hover:scale-105 active:scale-95 transition-transform px-5 py-3 rounded-xl text-black font-semibold cursor-pointer shadow-md w-full sm:w-56">
						<FaUpload />
						Upload Transcript
						<input
							type="file"
							accept=".pdf"
							className="hidden"
							onChange={handleFileChange}
						/>
					</motion.label>
				) : (
					<textarea
						rows={4}
						className="w-full bg-[#1A1A1A] border border-[#333] text-sm text-white rounded-lg px-4 py-3 mb-2 focus:outline-none focus:ring-2 focus:ring-[#FED34C]"
						placeholder="Enter courses like MATH 135, ECON 201, CS 136L separated by commas, semicolons or new lines"
						value={manualCourses}
						onChange={(e) => {
							setManualCourses(e.target.value);
							setBadCourses([]); // clear on edit
						}}
					/>
				)}

				{badCourses.length > 0 && (
					<p className="text-red-400 text-sm mt-1">
						Ignored invalid entries: {badCourses.join(", ")}
					</p>
				)}

				<Combobox value={selectedMajor} onChange={setSelectedMajor}>
					<div className="relative w-full sm:w-56 mt-4" ref={dropdownRef}>
						<Combobox.Input
							className="border border-[#333] bg-[#1A1A1A] px-4 py-3 rounded-xl text-white w-full cursor-pointer"
							placeholder="Select Major"
							onClick={() => setDropdownOpen(true)}
							onChange={(e) => {
								setQuery(e.target.value);
								setSelectedMajor(e.target.value);
								setDropdownOpen(true);
							}}
							onFocus={() => setDropdownOpen(true)}
						/>
						{isDropdownOpen && (
							<Combobox.Options className="absolute mt-2 w-full bg-[#1A1A1A] border border-[#333] rounded-lg shadow-lg max-h-48 overflow-y-auto z-50">
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

				<motion.button
					onClick={handleGoClick}
					className="bg-[#1A1A1A] border border-[#333] hover:bg-white hover:text-black text-white px-4 py-3 rounded-xl shadow-md transition-all duration-300 mt-6"
					whileHover={{ scale: 1.1 }}
					whileTap={{ scale: 0.95 }}>
					<FaArrowRight />
				</motion.button>

				{selectedFile && !isManual && (
					<p className="mt-3 text-sm text-gray-400">
						Selected: {selectedFile.name}
					</p>
				)}
			</motion.div>

			{/* Scroll Arrow */}
			<a
				href="#faq"
				className="absolute bottom-6 right-6 text-white text-xl sm:text-sm flex flex-col items-center animate-bounce hover:text-[#FED34C] transition-colors duration-300">
				<svg
					xmlns="http://www.w3.org/2000/svg"
					fill="none"
					viewBox="0 0 24 24"
					strokeWidth={2}
					stroke="currentColor"
					className="w-8 h-8 mt-1">
					<path
						strokeLinecap="round"
						strokeLinejoin="round"
						d="M19 9l-7 7-7-7"
					/>
				</svg>
			</a>
		</section>
	);
}
