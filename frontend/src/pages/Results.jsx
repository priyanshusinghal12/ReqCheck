// src/pages/Results.jsx
import { useLocation } from "react-router-dom";
import Navbar from "../components/Navbar";
import { motion } from "framer-motion";
import { useState } from "react";

const Results = () => {
	const location = useLocation();
	const { results } = location.state || {};
	const [whatIfText, setWhatIfText] = useState("");
	const [whatIfResults, setWhatIfResults] = useState(null);

	if (!results)
		return <div className="text-center p-10 text-white">No results found.</div>;

	// Capitalize first letter of each word
	const capitalizedMajor = results.major
		.split(" ")
		.map((word) => word.charAt(0).toUpperCase() + word.slice(1))
		.join(" ");

	const handleWhatIf = async () => {
		if (!whatIfText.trim()) return;

		const futureCourses = whatIfText
			.split(",")
			.map((course) => course.trim().toUpperCase())
			.filter(Boolean);

		const allCourses = [
			...results.requirements.flatMap((r) => r[1]),
			...futureCourses,
		];

		const response = await fetch("http://127.0.0.1:8000/check-requirements/", {
			method: "POST",
			headers: { "Content-Type": "application/json" },
			body: JSON.stringify({
				major: results.major,
				completed_courses: allCourses,
			}),
		});

		const data = await response.json();
		setWhatIfResults(data.requirements);
	};

	const handleKeyDown = (e) => {
		if (e.key === "Enter") {
			e.preventDefault();
			handleWhatIf();
		}
	};

	const renderRequirements = (reqs) =>
		Object.entries(reqs).map(([requirement, [met, courses]], i) => (
			<motion.div
				key={i}
				initial={{ opacity: 0, x: -30 }}
				animate={{ opacity: 1, x: 0 }}
				transition={{ duration: 0.4, delay: i * 0.05 }}
				className={`p-4 rounded-xl mb-4 border-l-4 ${
					met ? "border-[#FED34C] bg-[#1A1A1A]" : "border-red-500 bg-[#2A1A1A]"
				}`}>
				<h2 className="font-semibold text-white text-lg mb-1">{requirement}</h2>
				<p className="text-sm text-gray-300">
					{courses.length > 0 ? courses.join(", ") : "No courses found yet."}
				</p>
			</motion.div>
		));

	return (
		<>
			<Navbar />
			<div className="pt-20 px-6 md:px-16 bg-black text-white min-h-screen font-sans">
				<h1 className="text-3xl font-bold mb-6 text-white">
					Requirement Checklist:{" "}
					<span className="text-white">{capitalizedMajor}</span>
				</h1>

				<div className="max-h-[60vh] overflow-y-auto pr-2">
					{renderRequirements(results.requirements)}
				</div>

				<div className="mt-10">
					<h2 className="text-2xl font-bold text-white mb-3">
						What-If Analysis
					</h2>
					<textarea
						placeholder="Type in courses like ECON 301, STAT 333 and check what additional requirements get completed!!"
						className="w-full bg-[#1A1A1A] text-white rounded-lg p-4 border-2 border-[#333] placeholder:text-gray-400 focus:outline-none focus:ring-2 focus:ring-[#2a2a2a]"
						rows={5}
						value={whatIfText}
						onChange={(e) => setWhatIfText(e.target.value)}
						onKeyDown={handleKeyDown}
					/>
					<button
						onClick={handleWhatIf}
						className="mt-3 px-6 py-2 bg-[#FED34C] text-black font-semibold rounded-lg hover:scale-105 active:scale-95 transition-transform shadow-md">
						Check What-If
					</button>
					<p className="text-sm text-gray-500 mt-2">
						Simulate your future course plan to see its impact on your progress.
					</p>
				</div>

				{whatIfResults && (
					<div className="mt-10">
						<h2 className="text-2xl font-bold text-white mb-3">
							What-If Results
						</h2>
						<div className="max-h-[50vh] overflow-y-auto pr-2">
							{renderRequirements(whatIfResults)}
						</div>
					</div>
				)}
			</div>
		</>
	);
};

export default Results;
