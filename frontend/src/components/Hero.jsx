import { useState, useEffect } from "react";
import { motion } from "framer-motion";
import { Typewriter } from "react-simple-typewriter";
import ParticlesBackground from "./ParticlesBackground";
import MajorDropdown from "./MajorDropdown";
import { useNavigate } from "react-router-dom";
import { FaUpload, FaArrowRight, FaTimes } from "react-icons/fa";
import { toast } from "react-hot-toast";
import { auth } from "../firebase";
import { onAuthStateChanged } from "firebase/auth";

const courseRegex = /^[A-Z]{2,8} \d{3}[A-Z]?$/;

export default function Hero({ shouldType, name }) {
	const [selectedFile, setSelectedFile] = useState(null);
	const [fileContent, setFileContent] = useState(null);
	const [selectedMajor, setSelectedMajor] = useState("");
	const [manualCourses, setManualCourses] = useState("");
	const [badCourses, setBadCourses] = useState([]);
	const [showModal, setShowModal] = useState(false);
	const [isLoading, setIsLoading] = useState(false);
	const [dragCounter, setDragCounter] = useState(0);
	const [isRetrying, setIsRetrying] = useState(false);
	const [user, setUser] = useState(null);
	const navigate = useNavigate();

	useEffect(() => {
		const unsubscribe = onAuthStateChanged(auth, (firebaseUser) => {
			setUser(firebaseUser);
		});
		return () => unsubscribe();
	}, []);

	useEffect(() => {
		if (!showModal && window.innerWidth < 640) {
			setTimeout(() => {
				window.scrollTo({ top: 120, behavior: "smooth" });
			}, 300);
		}
	}, [showModal]);

	useEffect(() => {
		if (showModal) window.scrollTo({ top: 0, behavior: "smooth" });
	}, [showModal]);

	useEffect(() => {
		fetch(`${import.meta.env.VITE_BACKEND_URL}/`).catch(() => {});
	}, []);

	useEffect(() => {
		const savedMajor = sessionStorage.getItem("selectedMajor");
		const savedCourses = sessionStorage.getItem("manualCourses");
		const savedParsedCourses = sessionStorage.getItem("parsedCourses");
		const savedFilename = sessionStorage.getItem("transcriptFilename");

		if (savedMajor) setSelectedMajor(savedMajor);
		if (savedCourses) setManualCourses(savedCourses);
		if (savedParsedCourses) setFileContent(JSON.parse(savedParsedCourses));
		if (savedFilename) setSelectedFile({ name: savedFilename });
	}, []);

	useEffect(() => {
		sessionStorage.setItem("selectedMajor", selectedMajor);
	}, [selectedMajor]);

	useEffect(() => {
		sessionStorage.setItem("manualCourses", manualCourses);
	}, [manualCourses]);

	const processFile = (file) => {
		if (file?.type === "application/pdf") {
			setSelectedFile(file);
			sessionStorage.setItem("transcriptFilename", file.name);

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
					sessionStorage.setItem("parsedCourses", JSON.stringify(data.courses));
				} catch {
					toast.error("Failed to parse transcript.");
				}
			};
			reader.readAsDataURL(file);
		} else {
			toast.error("Please upload a valid PDF file.");
		}
	};

	const handleFileChange = async (event) => {
		const file = event.target.files[0];
		processFile(file);
	};

	const handleGoClick = async (courses) => {
		setIsLoading(true);
		setIsRetrying(false);

		if (!selectedMajor || !courses?.length) {
			toast.error("Please select a major and/or provide courses.");
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
						major: selectedMajor,
						completed_courses: courses,
					}),
				}
			);

			if (!response.ok) throw new Error();

			const data = await response.json();
			if (data.error) {
				toast.error("Invalid major or backend error.");
			} else {
				navigate("/results", {
					state: {
						results: {
							...data,
							major: selectedMajor.trim(),
							completed_courses: courses,
						},
					},
				});
			}
		} catch (err) {
			toast.error("Backend is sleeping or unreachable. Please try again.");
		} finally {
			setIsLoading(false);
		}
	};

	const handleManualSubmit = () => {
		const entries = manualCourses
			.split(/[,;\n]/)
			.map((c) => c.trim().toUpperCase())
			.filter(Boolean);

		const valid = entries.filter((c) => courseRegex.test(c));
		const invalid = entries.filter((c) => !courseRegex.test(c));

		setBadCourses(invalid);

		if (!valid.length) {
			toast.error("Please enter at least one valid course (e.g. CS 136L)");
			return;
		}

		handleGoClick(valid);
	};

	const handleDragEnter = (e) => {
		e.preventDefault();
		e.stopPropagation();
		setDragCounter((prev) => prev + 1);
	};

	const handleDragLeave = (e) => {
		e.preventDefault();
		e.stopPropagation();
		setDragCounter((prev) => Math.max(prev - 1, 0));
	};

	const handleDragOver = (e) => {
		e.preventDefault();
		e.stopPropagation();
	};

	const handleDrop = (e) => {
		e.preventDefault();
		e.stopPropagation();
		setDragCounter(0);
		const file = e.dataTransfer.files[0];
		processFile(file);
	};

	const handleClearTranscript = () => {
		setSelectedFile(null);
		setFileContent(null);
		sessionStorage.removeItem("parsedCourses");
		sessionStorage.removeItem("transcriptFilename");
	};

	return (
		<section
			className="relative z-0 min-h-[95vh] pt-20 pb-10 flex items-center justify-center text-white text-center overflow-visible bg-black px-4"
			onDragEnter={handleDragEnter}
			onDragLeave={handleDragLeave}
			onDragOver={handleDragOver}
			onDrop={handleDrop}>
			<ParticlesBackground />
			<motion.div className="relative z-10 w-full max-w-2xl flex flex-col items-center">
				{/* Welcome */}
				{shouldType && (
					<motion.h1 className="text-2xl sm:text-4xl md:text-5xl font-medium mb-4 leading-tight">
						<span className="text-[#FED34C]">Wel</span>
						<span className="text-white">
							<Typewriter
								key={name + shouldType}
								words={[`come${name ? ` ${name}` : ""}`]}
								cursor
								typeSpeed={100}
								deleteSpeed={0}
								loop={1}
							/>
						</span>
					</motion.h1>
				)}

				{/* Tagline */}
				<motion.p className="text-base text-gray-100 sm:text-lg font-medium mb-2">
					This is ReqCheck, the one-click tool to check your progress on your
					major's requirements and simulate how your future courses will affect
					your progress.
				</motion.p>
				<motion.p className="text-gray-400 mb-6 text-sm sm:text-base">
					To get started, upload your unofficial transcript or enter your
					completed courses manually, select your major and hit go.
				</motion.p>

				{/* Top Buttons */}
				<div className="flex flex-wrap justify-center items-center gap-2 sm:gap-3 mb-4 sm:mb-6">
					<button
						className={`px-3 py-1.5 sm:px-4 sm:py-2 text-sm sm:text-base rounded-lg font-semibold ${
							!showModal ? "border border-[#FED34C]" : "border border-[#333]"
						} bg-[#1A1A1A] text-white`}
						onClick={() => setShowModal(false)}>
						Upload Transcript
					</button>

					<button
						className={`px-3 py-1.5 sm:px-4 sm:py-2 text-sm sm:text-base rounded-lg font-semibold ${
							showModal ? "border border-[#FED34C]" : "border border-[#333]"
						} bg-[#1A1A1A] text-white hover:border-yellow-400 transition`}
						onClick={() => {
							setShowModal(true);
							sessionStorage.setItem("selectedMajor", selectedMajor);
						}}>
						Enter Courses Manually
					</button>

					{user && (
						<a
							href="/saved"
							className="border border-[#333] bg-[#1A1A1A] text-white px-3 py-1.5 sm:px-4 sm:py-2 text-sm sm:text-base rounded-lg font-semibold hover:border-yellow-400 transition">
							View Saved Results
						</a>
					)}
				</div>

				{/* Upload / Major / Go Row */}
				{!showModal && (
					<div className="flex flex-row items-center justify-center gap-2 sm:gap-3 w-full mt-2 flex-wrap sm:flex-nowrap">
						{/* Upload Icon Button */}
						<motion.label
							className="bg-[#FED34C] hover:scale-105 active:scale-95 transition-transform w-10 h-10 rounded-xl text-black font-semibold cursor-pointer shadow-md flex items-center justify-center"
							title="Upload Transcript">
							<FaUpload className="text-sm" />
							<input
								type="file"
								accept=".pdf"
								className="hidden"
								onChange={handleFileChange}
							/>
						</motion.label>

						{/* Major Dropdown */}
						<div className="flex-1 min-w-[140px] max-w-xs">
							<MajorDropdown
								selectedMajor={selectedMajor}
								setSelectedMajor={setSelectedMajor}
							/>
						</div>

						{/* Go Button same height/width as dropdown */}
						<motion.button
							onClick={() => handleGoClick(fileContent)}
							disabled={isLoading}
							className={`bg-[#1A1A1A] border border-[#333] text-white rounded-xl shadow-md transition-all duration-300 flex items-center justify-center px-4 py-3 w-full max-w-[3rem] h-[2.875rem] sm:h-[3rem] ${
								isLoading
									? "opacity-50 cursor-not-allowed"
									: "hover:bg-white hover:text-black"
							}`}
							whileHover={!isLoading ? { scale: 1.1 } : {}}
							whileTap={!isLoading ? { scale: 0.95 } : {}}>
							<FaArrowRight />
						</motion.button>
					</div>
				)}

				{/* Selected file display */}
				{selectedFile && !showModal && (
					<div className="mt-3 text-sm text-gray-400 flex items-center gap-2">
						<p>Selected: {selectedFile.name}</p>
						<button
							onClick={handleClearTranscript}
							className="text-red-400 hover:text-red-600 focus:outline-none"
							title="Remove file">
							<FaTimes />
						</button>
					</div>
				)}

				{/* Loader */}
				{isLoading && (
					<div className="flex items-center gap-2 text-sm text-gray-400 mt-3 animate-pulse">
						<svg
							className="w-4 h-4 animate-spin text-[#FED34C]"
							fill="none"
							viewBox="0 0 24 24"
							xmlns="http://www.w3.org/2000/svg">
							<circle
								className="opacity-25"
								cx="12"
								cy="12"
								r="10"
								stroke="currentColor"
								strokeWidth="4"
							/>
							<path
								className="opacity-75"
								fill="currentColor"
								d="M4 12a8 8 0 018-8v4a4 4 0 00-4 4H4z"
							/>
						</svg>
						<span>
							{isRetrying
								? "Backend waking up... Retrying shortly."
								: "Checking requirements..."}
						</span>
					</div>
				)}
			</motion.div>
		</section>
	);
}
