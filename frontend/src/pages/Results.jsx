// src/pages/Results.jsx
import { useLocation } from "react-router-dom";
import Navbar from "../components/Navbar";
import { motion } from "framer-motion";
import { useEffect, useRef, useState } from "react";

const Results = () => {
	const location = useLocation();
	const { results } = location.state || {};
	const [whatIfText, setWhatIfText] = useState("");
	const [whatIfResults, setWhatIfResults] = useState(null);
	const [showWhatIf, setShowWhatIf] = useState(false);
	const [newlyFulfilledKeys, setNewlyFulfilledKeys] = useState([]);
	const [updatedKeys, setUpdatedKeys] = useState([]);
	const [showMajorChange, setShowMajorChange] = useState(false);
	const [newMajor, setNewMajor] = useState("");

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

	// Function to check if all requirements are fulfilled
	const areAllRequirementsFulfilled = (requirements) => {
		return Object.values(requirements).every(([met]) => met);
	};

	// Check if all requirements are fulfilled
	const allRequirementsFulfilled = areAllRequirementsFulfilled(
		results.requirements
	);

	const handleWhatIf = async () => {
		if (!whatIfText.trim()) return;

		const validCourseRegex = /^[A-Z]{2,8} \d{3}[A-Z]?$/;
		const futureCourses = whatIfText
			.split(",")
			.map((course) => course.trim().toUpperCase())
			.filter((course) => validCourseRegex.test(course));

		if (futureCourses.length === 0) {
			alert("Please type valid course codes like 'CS 136L', 'STAT 230' etc.");
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

		const text = await response.text();
		console.log("Raw response:", text);

		let data;
		try {
			data = JSON.parse(text);
		} catch (err) {
			console.error("Failed to parse JSON:", err);
			alert("Something went wrong.");
			return;
		}

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
				<h1 className="text-3xl font-bold mb-6">
					Requirement Checklist:{" "}
					<span className="text-white">{capitalizedMajor}</span>
				</h1>

				{allRequirementsFulfilled && (
					<div className="mb-6 text-[#FED34C] text-lg font-semibold">
						All Requirements Fulfilled!
					</div>
				)}
				{/* Change Major Feature */}
				<div className="flex flex-col sm:flex-row items-start sm:items-center gap-3 mb-6">
					<button
						className="bg-[#FED34C] text-black font-semibold px-4 py-2 rounded-md hover:bg-yellow-300 transition"
						onClick={() => setShowMajorChange((prev) => !prev)}>
						Change Major
					</button>

					{showMajorChange && (
						<div className="w-full sm:w-64">
							<select
								className="mt-2 sm:mt-0 w-full bg-[#1A1A1A] text-white border border-[#333] rounded-md px-4 py-2"
								value={newMajor}
								onChange={(e) => setNewMajor(e.target.value)}>
								<option value="">Select a new major</option>
								{[
									"Actuarial Science",
									"Applied Mathematics",
									"Biostatistics",
									"Combinatorics and Optimization",
									"Computational Mathematics",
									"Mathematical Economics",
									"Mathematical Finance",
									"Mathematical Optimization",
									"Mathematical Physics",
									"Mathematical Studies",
									"Pure Mathematics",
									"Statistics",
									"Mathematics/Teaching",
									"BMath Data Science",
									"BCS Computer Science",
									"Math Degree Requirements",
								].map((major, index) => (
									<option key={index} value={major}>
										{major}
									</option>
								))}
							</select>

							<button
								onClick={async () => {
									if (!newMajor || !results?.completed_courses) {
										alert("Please select a valid major.");
										return;
									}
									try {
										console.log("Changing to major:", newMajor);
										console.log(
											"Completed courses:",
											results.completed_courses
										);

										const response = await fetch(
											`${import.meta.env.VITE_BACKEND_URL}/check-requirements/`,
											{
												method: "POST",
												headers: { "Content-Type": "application/json" },
												body: JSON.stringify({
													major: newMajor.toLowerCase(),
													completed_courses: results.completed_courses,
												}),
											}
										);
										const text = await response.text();
										console.log("Raw response:", text);

										let data;
										try {
											data = JSON.parse(text);
										} catch (err) {
											console.error("Failed to parse JSON:", err);
											alert("Something went wrong.");
											return;
										}

										if (data.error) {
											alert("Error updating major requirements.");
										} else {
											window.location.reload(); // simplest way to rerun logic with new state
											// OR you can set new state here if you have a setResults() handler
										}
									} catch (error) {
										console.error("Major change failed", error);
										alert("Something went wrong.");
									}
								}}
								className="mt-2 w-full bg-white text-black py-2 rounded-md font-semibold hover:bg-gray-200 transition">
								Update Requirements
							</button>
						</div>
					)}
				</div>

				<div className="max-h-[60vh] overflow-y-auto pr-2">
					{showWhatIf
						? renderRequirements(whatIfResults, newlyFulfilledKeys, updatedKeys)
						: renderRequirements(results.requirements)}
				</div>

				<div className="mt-10">
					<h2 className="text-2xl font-bold mb-3">What-If Analysis</h2>
					<textarea
						placeholder="Type in courses like ECON 301, STAT 333 and check what additional requirements get completed!!"
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

				{/* What-If Feedback Message */}
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
