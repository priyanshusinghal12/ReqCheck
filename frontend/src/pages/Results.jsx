import { useLocation } from "react-router-dom";
import Navbar from "../components/Navbar";
import MajorDropdown from "../components/MajorDropdown";
import { motion } from "framer-motion";
import { useEffect, useRef, useState } from "react";
import { FaArrowRight } from "react-icons/fa";
import { toast } from "react-hot-toast";

const Results = () => {
	const location = useLocation();
	const { results: initialResults } = location.state || {};
	const [results, setResults] = useState(initialResults);
	const [isLoading, setIsLoading] = useState(false);
	const [whatIfText, setWhatIfText] = useState("");
	const [whatIfResults, setWhatIfResults] = useState(null);
	const [showWhatIf, setShowWhatIf] = useState(false);
	const [newlyFulfilledKeys, setNewlyFulfilledKeys] = useState([]);
	const [updatedKeys, setUpdatedKeys] = useState([]);
	const [newMajor, setNewMajor] = useState(initialResults?.major || "");
	const [errorMessage, setErrorMessage] = useState("");

	const whatIfRef = useRef(null);

	useEffect(() => {
		if (showWhatIf && whatIfRef.current) {
			whatIfRef.current.scrollIntoView({ behavior: "smooth" });
		}
	}, [showWhatIf]);

	if (!results)
		return <div className="text-center p-10 text-white">No results found.</div>;

	const capitalizedMajor = results.major
		.split(" ")
		.map((word) => word.charAt(0).toUpperCase() + word.slice(1))
		.join(" ");

	const areAllRequirementsFulfilled = (requirements) =>
		Object.values(requirements).every(([met]) => met);

	const allRequirementsFulfilled = areAllRequirementsFulfilled(
		results.requirements
	);

	const handleMajorChange = async () => {
		const trimmedMajor = newMajor.trim().toLowerCase();
		if (!trimmedMajor || !results?.completed_courses) {
			toast.error("Please select a valid major.");
			return;
		}

		setIsLoading(true);

		try {
			const response = await fetch(
				`${import.meta.env.VITE_BACKEND_URL}/check-requirements/`,
				{
					method: "POST",
					headers: { "Content-Type": "application/json" },
					body: JSON.stringify({
						major: trimmedMajor,
						completed_courses: results.completed_courses,
					}),
				}
			);

			const text = await response.text();
			const data = JSON.parse(text);

			if (data.error) {
				toast.error("Error updating major requirements.");
			} else {
				setResults({
					...data,
					completed_courses: results.completed_courses,
					major: trimmedMajor,
				});
				setShowWhatIf(false);
				const formattedMajor = newMajor
					.trim()
					.split(" ")
					.map((word) => word.charAt(0).toUpperCase() + word.slice(1))
					.join(" ");

				toast.success(`Switched to ${formattedMajor}!`);
			}
		} catch (error) {
			console.error("Major change failed", error);
			toast.error("Something went wrong. Please try again.");
		}

		setIsLoading(false);
	};

	const handleWhatIf = async () => {
		if (!whatIfText.trim()) return;

		const validCourseRegex = /^[A-Z]{2,8} \d{3}[A-Z]?$/;
		const futureCourses = whatIfText
			.split(",")
			.map((course) => course.trim().toUpperCase())
			.filter((course) => validCourseRegex.test(course));

		if (futureCourses.length === 0) {
			toast.error(
				"Please type valid course codes like 'CS 136L', 'STAT 230' etc."
			);
			return;
		}

		const allCourses = [
			...Object.values(results.requirements).flatMap(([_, courses]) => courses),
			...futureCourses,
		];

		const response = await fetch(
			`${import.meta.env.VITE_BACKEND_URL}/check-requirements/`,
			{
				method: "POST",
				headers: { "Content-Type": "application/json" },
				body: JSON.stringify({
					major: results.major,
					completed_courses: allCourses,
				}),
			}
		);

		const data = await response.json();

		const original = results.requirements;
		const updated = data.requirements;

		const newMetKeys = [];
		const changedKeys = [];

		for (const key of Object.keys(updated)) {
			const [originalMet, originalCourses = []] = original[key] || [];
			const [updatedMet, updatedCourses = []] = updated[key] || [];

			if (updatedMet && !originalMet) {
				newMetKeys.push(key);
			} else if (
				originalCourses.length < updatedCourses.length &&
				updatedCourses.some((c) => !originalCourses.includes(c))
			) {
				changedKeys.push(key);
			}
		}

		setNewlyFulfilledKeys(newMetKeys);
		setUpdatedKeys(changedKeys);
		setWhatIfResults(updated);
		setShowWhatIf(true);
	};

	const handleKeyDown = (e) => {
		if (e.key === "Enter") {
			e.preventDefault();
			handleWhatIf();
		}
	};

	const renderRequirements = (reqs, fulfilled = [], updated = []) =>
		Object.entries(reqs).map(([requirement, [met, courses]], i) => {
			const isNew = fulfilled.includes(requirement);
			const isUpdated = updated.includes(requirement);

			return (
				<motion.div
					key={i}
					initial={{ opacity: 0, x: -30 }}
					animate={{ opacity: 1, x: 0 }}
					transition={{ duration: 0.4, delay: i * 0.04 }}
					className={`p-4 rounded-xl mb-4 border-l-4 relative ${
						met
							? "border-[#FED34C] bg-[#1A1A1A]"
							: "border-red-500 bg-[#2A1A1A]"
					}`}>
					<h2 className="font-semibold text-white text-lg mb-1 flex items-center gap-2">
						{requirement}
						{isNew && (
							<span className="bg-[#FED34C] text-black text-xs font-semibold px-2 py-0.5 rounded-full">
								Newly Fulfilled
							</span>
						)}
						{!isNew && isUpdated && (
							<span className="bg-[#FED34C] text-black text-xs font-semibold px-2 py-0.5 rounded-full">
								Updated
							</span>
						)}
					</h2>
					<p className="text-sm text-gray-300">
						{courses.length > 0 ? courses.join(", ") : "No courses found yet."}
					</p>
				</motion.div>
			);
		});

	return (
		<>
			<Navbar />
			<div className="pt-20 px-6 md:px-16 bg-black text-white min-h-screen font-sans">
				{/* Header */}
				<div className="flex flex-col sm:flex-row sm:items-center sm:justify-between mb-6 gap-4">
					<h1 className="text-3xl font-bold">
						Requirement Checklist:{" "}
						<span className="text-white">{capitalizedMajor}</span>
					</h1>

					{/* Custom Styled Dropdown + Button */}
					<div className="flex flex-row gap-2 items-center w-full sm:w-auto">
						<MajorDropdown
							selectedMajor={newMajor}
							setSelectedMajor={setNewMajor}
							fullWidth={false}
						/>
						<button
							onClick={handleMajorChange}
							disabled={isLoading}
							className={`bg-white text-black p-3 rounded-xl transition flex items-center justify-center hover:bg-gray-200 ${
								isLoading ? "opacity-60 cursor-not-allowed" : ""
							}`}>
							{isLoading ? (
								<div className="animate-spin rounded-full h-5 w-5 border-2 border-t-black border-white" />
							) : (
								<FaArrowRight size={16} />
							)}
						</button>
					</div>
				</div>

				{allRequirementsFulfilled && (
					<div className="mb-6 text-[#FED34C] text-lg font-semibold">
						All Requirements Fulfilled!
					</div>
				)}

				<div className="max-h-[60vh] overflow-y-auto pr-2">
					{showWhatIf
						? renderRequirements(whatIfResults, newlyFulfilledKeys, updatedKeys)
						: renderRequirements(results.requirements)}
				</div>

				{/* What-If */}
				<div className="mt-10">
					<h2 className="text-2xl font-bold mb-3">What-If Analysis</h2>
					<textarea
						placeholder="Type in courses like ECON 301, STAT 333..."
						className="w-full bg-[#1A1A1A] text-white rounded-lg p-4 border-2 border-[#333] placeholder:text-gray-400 focus:outline-none focus:ring-2 focus:ring-[#2a2a2a]"
						rows={5}
						value={whatIfText}
						onChange={(e) => setWhatIfText(e.target.value)}
						onKeyDown={handleKeyDown}
					/>
					<div className="flex items-center mt-3 gap-3">
						<button
							onClick={handleWhatIf}
							className="px-6 py-2 border border-[#333] bg-[#1A1A1A] text-white font-semibold rounded-lg hover:scale-105 active:scale-95 transition-transform shadow-md">
							Check What-If
						</button>
						{showWhatIf && (
							<button
								onClick={() => {
									setShowWhatIf(false);
									setWhatIfResults(null);
									setNewlyFulfilledKeys([]);
									setUpdatedKeys([]);
								}}
								className="px-6 py-2 border border-[#333] bg-[#1A1A1A] text-white font-semibold rounded-lg hover:scale-105 active:scale-95 transition-transform shadow-md">
								Reset to Original
							</button>
						)}
					</div>
				</div>

				{/* Feedback Message */}
				<div ref={whatIfRef} className="mt-6 text-sm text-white font-medium">
					{showWhatIf && (
						<>
							{newlyFulfilledKeys.length === 0 && updatedKeys.length === 0 ? (
								<p>No additional requirement completed.</p>
							) : (
								<>
									{newlyFulfilledKeys.length > 0 && (
										<p>
											You would fulfill{" "}
											<span className="text-[#FED34C] font-semibold">
												{newlyFulfilledKeys.length}
											</span>{" "}
											new requirement
											{newlyFulfilledKeys.length > 1 ? "s" : ""}!
										</p>
									)}
									{updatedKeys.length > 0 && (
										<p>
											<span className="text-[#FED34C] font-semibold">
												{updatedKeys.length}
											</span>{" "}
											requirement
											{updatedKeys.length > 1 ? "s" : ""} updated above.
										</p>
									)}
								</>
							)}
						</>
					)}
				</div>
			</div>
		</>
	);
};

export default Results;
