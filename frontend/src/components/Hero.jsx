// Hero.jsx
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
	// const [reuseTranscript, setReuseTranscript] = useState(null);
	const [user, setUser] = useState(null);
	const navigate = useNavigate();

	useEffect(() => {
		const unsubscribe = onAuthStateChanged(auth, (firebaseUser) => {
			setUser(firebaseUser);
		});
		return () => unsubscribe();
	}, []);

	useEffect(() => {
		if (shouldType) {
			// Reset handled by key prop
		}
	}, [shouldType]);

	useEffect(() => {
		if (showModal) window.scrollTo({ top: 0, behavior: "smooth" });
	}, [showModal]);

	useEffect(() => {
		fetch(`${import.meta.env.VITE_BACKEND_URL}/`).catch(() => {});
	}, []);

	// useEffect(() => {
	// 	const fetchPreviousTranscript = async () => {
	// 		// Check localStorage
	// 		const localCourses = localStorage.getItem("parsedCourses");
	// 		const localMajor = localStorage.getItem("selectedMajor");
	// 		const localName = localStorage.getItem("transcriptFilename");

	// 		if (localCourses && localMajor && localName) {
	// 			setReuseTranscript({
	// 				completed_courses: JSON.parse(localCourses),
	// 				major: localMajor,
	// 				filename: localName,
	// 			});
	// 		}

	// 		// Check Firebase (if user is logged in)
	// 		auth.onAuthStateChanged(async (user) => {
	// 			if (user) {
	// 				const token = await user.getIdToken();
	// 				const res = await fetch(
	// 					`${import.meta.env.VITE_BACKEND_URL}/get-last-transcript/`,
	// 					{
	// 						headers: { Authorization: `Bearer ${token}` },
	// 					}
	// 				);
	// 				const data = await res.json();
	// 				if (data.status === "success") {
	// 					setReuseTranscript({
	// 						completed_courses: data.transcript.completed_courses,
	// 						major: data.transcript.major,
	// 						filename: data.transcript.filename,
	// 					});
	// 				}
	// 			}
	// 		});
	// 	};

	// 	fetchPreviousTranscript();
	// }, []);

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

	const retryFetch = async (url, options, retries = 1) => {
		try {
			const res = await fetch(url, options);
			if (!res.ok) throw new Error("Fetch failed");
			return res;
		} catch (err) {
			if (retries > 0) {
				setIsRetrying(true);
				await new Promise((res) => setTimeout(res, 2000));
				return retryFetch(url, options, retries - 1);
			}
			throw err;
		}
	};

	const handleGoClick = async (courses) => {
		setIsLoading(true);
		setIsRetrying(false);

		if (!selectedMajor || !courses?.length) {
			toast.error("Please select a major and/or provide courses.");
			setIsLoading(false);
			return;
		}

		// if (!selectedMajor && reuseTranscript?.major) {
		// 	setSelectedMajor(reuseTranscript.major);
		// }

		try {
			let response;
			try {
				response = await retryFetch(
					`${import.meta.env.VITE_BACKEND_URL}/check-requirements/`,
					{
						method: "POST",
						headers: { "Content-Type": "application/json" },
						body: JSON.stringify({
							major: selectedMajor,
							completed_courses: courses,
						}),
					},
					1 // retry once
				);
			} catch {
				setIsRetrying(false);
				throw new Error("Retry failed");
			}

			if (!response.ok) {
				toast.error("Backend not ready. Please wait and try again.");
				setIsLoading(false);
				return;
			}

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
			console.error("Request failed:", err);
			toast.error("Backend is sleeping or unreachable. Please try again.");
		} finally {
			setIsRetrying(false);
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

	return (
		<section
			className="relative z-0 min-h-[95vh] pt-20 pb-10 flex items-center justify-center text-white text-center overflow-visible bg-black px-4"
			onDragEnter={handleDragEnter}
			onDragLeave={handleDragLeave}
			onDragOver={handleDragOver}
			onDrop={handleDrop}>
			<ParticlesBackground />
			<motion.div className="relative z-10 w-full max-w-2xl flex flex-col items-center">
				{shouldType && (
					<motion.h1 className="text-5xl sm:text-6xl font-medium mb-4">
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

				<motion.p className="text-base text-gray-100 sm:text-lg font-medium mb-2">
					This is ReqCheck, the one-click tool to check your progress on your
					major's requirements and simulate how your future courses will affect
					your progress.
				</motion.p>
				<motion.p className="text-gray-400 mb-6 text-sm sm:text-base">
					To get started, upload your unofficial transcript or enter your
					completed courses manually, select your major and hit go.
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
						id="upload-enter-trigger"
						onClick={() => handleGoClick(fileContent)}
						className="hidden"
					/>
					<button
						className={`px-4 py-2 rounded-lg font-semibold ${
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
							className="border border-[#333] bg-[#1A1A1A] text-white px-4 py-2 rounded-lg font-semibold hover:border-yellow-400 transition">
							View Saved Results
						</a>
					)}
				</div>

				{!showModal && (
					<div
						className="relative flex flex-col sm:flex-row items-center justify-center gap-3 w-full sm:w-auto mt-2"
						tabIndex={0}
						onKeyDown={(e) => {
							if (e.key === "Enter") {
								e.preventDefault();
								if (selectedMajor?.trim()) {
									handleGoClick(fileContent);
								} else {
									toast.error("Please select a major.");
								}
							}
						}}>
						<motion.label className="flex items-center justify-center gap-2 bg-[#FED34C] hover:scale-105 active:scale-95 transition-transform px-4 py-3 rounded-xl text-black font-semibold cursor-pointer shadow-md sm:w-auto w-full">
							<FaUpload />
							Upload/Drop Transcript
							<input
								type="file"
								accept=".pdf"
								className="hidden"
								onChange={handleFileChange}
							/>
						</motion.label>

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

						{dragCounter > 0 && (
							<div className="absolute inset-0 flex items-center justify-center bg-black bg-opacity-60 rounded-xl pointer-events-none z-20">
								<p className="text-white text-xl font-semibold">
									Drop your file here
								</p>
							</div>
						)}
					</div>
				)}

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
			</motion.div>

			{/* FAQ Bounce Button
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
			</a> */}

			{/* Manual Entry Modal */}
			{showModal && (
				<div className="absolute inset-0 bg-black bg-opacity-70 backdrop-blur-sm flex items-center justify-center z-50">
					<div
						className="bg-[#121212] rounded-lg p-6 w-[90%] max-w-lg shadow-2xl relative"
						onKeyDown={(e) => {
							if (e.key === "Enter" && !e.shiftKey) {
								e.preventDefault();
								handleManualSubmit();
							}
						}}
						tabIndex={0} // makes it focusable for key presses
					>
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
							onKeyDown={(e) => {
								if (e.key === "Enter" && !e.shiftKey) {
									e.preventDefault();
									handleManualSubmit();
								}
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
