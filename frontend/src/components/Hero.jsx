import { useState, useRef, useEffect } from "react";
import { motion } from "framer-motion";
import { FaUpload, FaArrowRight, FaTimes } from "react-icons/fa";
import ParticlesBackground from "./ParticlesBackground";
import { useNavigate } from "react-router-dom";
import MajorDropdown from "./MajorDropdown"; // <- Imported custom dropdown component
import { toast } from "react-hot-toast";

const courseRegex = /^[A-Z]{2,8} \d{3}[A-Z]?$/;

export default function Hero() {
	const [selectedFile, setSelectedFile] = useState(null);
	const [fileContent, setFileContent] = useState(null);
	const [selectedMajor, setSelectedMajor] = useState("");
	const [manualCourses, setManualCourses] = useState("");
	const [badCourses, setBadCourses] = useState([]);
	const [showModal, setShowModal] = useState(false);
	const [isLoading, setIsLoading] = useState(false);

	const navigate = useNavigate();

	const handleFileChange = async (event) => {
		const file = event.target.files[0];
		if (file && file.type === "application/pdf") {
			setSelectedFile(file);
			const reader = new FileReader();
			reader.onload = async () => {
				try {
					const base64 = reader.result.split(",")[1];
					const response = await fetch(
						`${import.meta.env.VITE_BACKEND_URL}/parse-transcript/`,
						{
							method: "POST",
							headers: { "Content-Type": "application/json" },
							body: JSON.stringify({ base64_pdf: base64 }),
						}
					);
					const data = await response.json();
					setFileContent(data.courses);
				} catch (error) {
					toast.error("Failed to parse transcript.");
				}
			};
			reader.readAsDataURL(file);
		} else {
			toast.error("Please upload a valid PDF file.");
		}
	};

	const handleGoClick = async (courses) => {
		setIsLoading(true);

		if (!selectedMajor || !courses || courses.length === 0) {
			toast.error(
				"Please select a major and/or provide courses/upload transcript."
			);
			setIsLoading(false);
			return;
		}

		try {
			const response = await fetch(
				`${import.meta.env.VITE_BACKEND_URL}/check-requirements/`,
				{
					method: "POST",
					headers: { "Content-Type": "application/json" },
					body: JSON.stringify({
						major: selectedMajor.toLowerCase(),
						completed_courses: courses,
					}),
				}
			);
			const data = await response.json();
			if (data.error) {
				toast.error("Invalid major or backend error.");
			} else {
				navigate("/results", {
					state: {
						results: {
							...data,
							major: selectedMajor.trim().toLowerCase(),
							completed_courses: courses,
						},
					},
				});
			}
		} catch (error) {
			toast.error("Failed to fetch requirements.");
			console.error(error);
		}
		setIsLoading(false);
	};

	const handleManualSubmit = () => {
		const entries = manualCourses
			.split(/[,;\n]/)
			.map((c) => c.trim().toUpperCase())
			.filter(Boolean);

		const valid = entries.filter((c) => courseRegex.test(c));
		const invalid = entries.filter((c) => !courseRegex.test(c));

		setBadCourses(invalid);

		if (valid.length === 0) {
			toast.error(
				"Please enter at least one valid course (e.g. CS 136L or ECON 201)"
			);
			return;
		}

		handleGoClick(valid);
	};

	return (
		<section className="relative min-h-[95vh] pt-24 flex items-center justify-center text-white text-center overflow-visible bg-black px-4 pb-10">
			<ParticlesBackground />
			<motion.div className="relative z-10 w-full max-w-2xl flex flex-col items-center">
				<motion.h1 className="text-5xl sm:text-6xl font-medium mb-4">
					<span className="text-[#FED34C]">Req</span>Check
				</motion.h1>
				<motion.p className="text-base text-gray-100 sm:text-lg font-medium mb-2">
					The one-click tool to check your missing and satisfied major
					requirements
				</motion.p>
				<motion.p className="text-gray-400 mb-6 text-sm sm:text-base">
					Upload your unofficial transcript or enter your completed courses
					manually
				</motion.p>

				<div className="flex items-center gap-3 mb-6">
					<button
						className={`px-4 py-2 rounded-lg font-semibold ${
							!showModal ? "border border-[#FED34C]" : "border border-[#333]"
						} bg-[#1A1A1A] text-white`}
						onClick={() => setShowModal(false)}>
						Upload Transcript
					</button>
					<button
						className={`px-4 py-2 rounded-lg font-semibold ${
							showModal ? "border border-[#FED34C]" : "border border-[#333]"
						} bg-[#1A1A1A] text-white`}
						onClick={() => setShowModal(true)}>
						Enter Courses Manually
					</button>
				</div>

				{!showModal && (
					<div className="flex flex-col sm:flex-row items-center justify-center gap-3 w-full sm:w-auto mt-2">
						<motion.label className="flex items-center justify-center gap-2 bg-[#FED34C] hover:scale-105 active:scale-95 transition-transform px-4 py-3 rounded-xl text-black font-semibold cursor-pointer shadow-md sm:w-auto w-full">
							<FaUpload />
							Upload Transcript
							<input
								type="file"
								accept=".pdf"
								className="hidden"
								onChange={handleFileChange}
							/>
						</motion.label>

						{/* 💡 MajorDropdown used here */}
						<MajorDropdown
							selectedMajor={selectedMajor}
							setSelectedMajor={setSelectedMajor}
						/>

						<motion.button
							onClick={() => handleGoClick(fileContent)}
							disabled={isLoading}
							className={`bg-[#1A1A1A] border border-[#333] px-4 py-3 rounded-xl shadow-md transition-all duration-300 ${
								isLoading
									? "opacity-50 cursor-not-allowed"
									: "hover:bg-white hover:text-black text-white"
							}`}
							whileHover={!isLoading ? { scale: 1.1 } : {}}
							whileTap={!isLoading ? { scale: 0.95 } : {}}>
							<FaArrowRight />
						</motion.button>
					</div>
				)}

				{isLoading && (
					<p className="text-sm text-gray-400 mt-3 animate-pulse">
						Checking requirements...
					</p>
				)}

				{selectedFile && !showModal && (
					<p className="mt-3 text-sm text-gray-400">
						Selected: {selectedFile.name}
					</p>
				)}
			</motion.div>

			{/* FAQ Button */}
			<a
				href="#faq"
				className="absolute bottom-6 right-6 text-white text-xl sm:text-sm flex flex-col items-center animate-bounce hover:text-[#FED34C] transition-colors duration-300">
				<svg
					xmlns="http://www.w3.org/2000/svg"
					className="w-8 h-8 mt-1"
					fill="none"
					viewBox="0 0 24 24"
					stroke="currentColor">
					<path
						strokeLinecap="round"
						strokeLinejoin="round"
						strokeWidth={2}
						d="M19 9l-7 7-7-7"
					/>
				</svg>
			</a>

			{/* Modal */}
			{showModal && (
				<div className="absolute inset-0 bg-black bg-opacity-70 backdrop-blur-sm flex items-center justify-center z-50">
					<div className="bg-[#121212] rounded-lg p-6 w-[90%] max-w-lg shadow-2xl relative">
						<button
							onClick={() => setShowModal(false)}
							className="absolute top-3 right-3 text-gray-400 hover:text-white">
							<FaTimes size={18} />
						</button>
						<h2 className="text-white text-xl font-semibold mb-3">
							Enter Courses Manually
						</h2>

						<textarea
							rows={4}
							className="w-full bg-[#1A1A1A] border border-[#333] text-sm text-white rounded-lg px-4 py-3 mb-2"
							placeholder="Enter courses like MATH 135, ECON 201, CS 136L separated by commas."
							value={manualCourses}
							onChange={(e) => {
								setManualCourses(e.target.value);
								setBadCourses([]);
							}}
						/>

						<div className="w-full mt-2">
							<MajorDropdown
								fullWidth
								selectedMajor={selectedMajor}
								setSelectedMajor={setSelectedMajor}
							/>
						</div>

						{badCourses.length > 0 && (
							<p className="text-red-400 text-sm mt-2">
								Ignored: {badCourses.join(", ")}
							</p>
						)}

						<motion.button
							onClick={handleManualSubmit}
							disabled={isLoading}
							className={`bg-[#FED34C] font-semibold w-full py-3 mt-4 rounded-lg transition ${
								isLoading
									? "opacity-60 cursor-not-allowed"
									: "hover:bg-yellow-400 text-black"
							}`}
							whileTap={!isLoading ? { scale: 0.96 } : {}}>
							{isLoading ? "Checking..." : "Continue"}
						</motion.button>
					</div>
				</div>
			)}
		</section>
	);
}
