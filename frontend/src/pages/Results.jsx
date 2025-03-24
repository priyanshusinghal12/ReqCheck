// src/pages/Results.jsx
import { useLocation } from "react-router-dom";
import Navbar from "../components/Navbar";
import { motion } from "framer-motion";

const Results = () => {
	const location = useLocation();
	const { results } = location.state || {};

	if (!results)
		return <div className="text-center p-10">No results found.</div>;

	return (
		<>
			<Navbar />
			<div className="pt-20 px-6 md:px-16 bg-black text-white min-h-screen font-sans">
				<h1 className="text-3xl font-bold mb-6 text-[#FED34C]">
					Requirement Checklist: {results.major}
				</h1>

				<div className="max-h-[60vh] overflow-y-auto pr-2">
					{Object.entries(results.requirements).map(
						([requirement, [met, courses]], i) => (
							<motion.div
								key={i}
								initial={{ opacity: 0, x: -30 }}
								animate={{ opacity: 1, x: 0 }}
								transition={{ duration: 0.4, delay: i * 0.05 }}
								className={`p-4 rounded-xl mb-4 border-l-4 ${
									met
										? "border-[#FED34C] bg-gray-900"
										: "border-red-500 bg-gray-800"
								}`}>
								<h2 className="font-semibold text-lg mb-1">{requirement}</h2>
								<p className="text-sm text-gray-300">
									{courses.length > 0
										? courses.join(", ")
										: "No courses found yet."}
								</p>
							</motion.div>
						)
					)}
				</div>

				<div className="mt-10">
					<h2 className="text-2xl font-bold text-[#FED34C] mb-3">
						What-If Analysis
					</h2>
					<textarea
						placeholder="Type in course codes like ECON 301, STAT 333..."
						className="w-full bg-gray-800 text-white rounded-lg p-4 border border-gray-600 placeholder:text-gray-400 focus:outline-none focus:ring-2 focus:ring-[#FED34C]"
						rows={5}
					/>
					<p className="text-sm text-gray-500 mt-2">
						Simulate your future course plan to see its impact on your progress.
					</p>
				</div>
			</div>
		</>
	);
};

export default Results;
