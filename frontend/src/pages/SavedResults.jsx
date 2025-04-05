import { useEffect, useState } from "react";
import { auth } from "../firebase";
import { useNavigate } from "react-router-dom";
import Navbar from "../components/Navbar";
import { motion } from "framer-motion";

const SavedResults = () => {
	const [savedList, setSavedList] = useState([]);
	const [loading, setLoading] = useState(true);
	const [expandedIndexes, setExpandedIndexes] = useState([]);
	const navigate = useNavigate();

	useEffect(() => {
		const unsubscribe = auth.onAuthStateChanged(async (user) => {
			if (!user) {
				console.warn("⚠️ No user logged in");
				setLoading(false);
				return;
			}

			const token = await user.getIdToken();

			const response = await fetch(
				`${import.meta.env.VITE_BACKEND_URL}/get-saved-results/`,
				{
					headers: { Authorization: `Bearer ${token}` },
				}
			);

			const data = await response.json();
			if (data?.status === "success" && Array.isArray(data.results)) {
				const sorted = [...data.results].sort(
					(a, b) => new Date(b.timestamp) - new Date(a.timestamp)
				);
				setSavedList(sorted);
			} else {
				console.error("Failed to load saved results");
			}

			setLoading(false);
		});

		return () => unsubscribe();
	}, []);

	const toggleExpand = (index) => {
		setExpandedIndexes((prev) =>
			prev.includes(index) ? prev.filter((i) => i !== index) : [...prev, index]
		);
	};

	const handleLoadToResults = (result) => {
		window.scrollTo({ top: 0, behavior: "smooth" });

		const reconstructedRequirements = {};
		if (Array.isArray(result.requirements)) {
			result.requirements.forEach((req) => {
				if (req?.name) {
					reconstructedRequirements[req.name] = [req.met, req.courses || []];
				}
			});
		}

		navigate("/results", {
			state: {
				results: {
					major: result.major,
					completed_courses: result.completed_courses,
					requirements: reconstructedRequirements,
				},
			},
		});
		window.scrollTo({ top: 0, behavior: "smooth" });
	};

	return (
		<>
			<Navbar />
			<div className="pt-20 px-6 md:px-16 bg-black text-white min-h-screen font-sans">
				<h1 className="text-3xl font-bold mb-6">Your Saved Results</h1>

				{loading ? (
					<p className="text-white">Loading...</p>
				) : savedList.length === 0 ? (
					<p className="text-white">
						No saved results found. Try saving some from the results page.
					</p>
				) : (
					<div className="space-y-6">
						{savedList.map((result, index) => {
							const isExpanded = expandedIndexes.includes(index);
							return (
								<div
									key={index}
									className="border border-gray-700 p-4 rounded-lg bg-[#1A1A1A]">
									<div className="flex justify-between items-center mb-2">
										<div>
											<p className="text-sm text-gray-400">
												{new Date(result.timestamp).toLocaleString()}
											</p>
											<h2 className="text-lg font-semibold text-[#FED34C]">
												Major:{" "}
												{result.major.charAt(0).toUpperCase() +
													result.major.slice(1)}
											</h2>
											{result.name && (
												<p className="text-sm italic text-gray-300">
													“{result.name}”
												</p>
											)}
										</div>

										<div className="flex gap-2">
											<button
												onClick={() => handleLoadToResults(result)}
												className="bg-[#FED34C] text-black font-semibold px-4 py-1 rounded hover:bg-yellow-400">
												Load Result
											</button>
											<button
												onClick={() => toggleExpand(index)}
												className="bg-gray-800 border border-gray-600 px-3 py-1 rounded text-white hover:bg-gray-700">
												{isExpanded ? "↓ Minimize" : "➡️ Expand"}
											</button>
										</div>
									</div>

									{isExpanded && (
										<motion.div
											initial={{ opacity: 0, height: 0 }}
											animate={{ opacity: 1, height: "auto" }}
											transition={{ duration: 0.4 }}
											className="space-y-4 mt-2">
											{result.requirements.map((req, i) => (
												<div
													key={i}
													className={`p-3 rounded-lg border-l-4 ${
														req.met
															? "border-[#FED34C] bg-[#121212]"
															: "border-red-500 bg-[#2A1A1A]"
													}`}>
													<h3 className="font-semibold text-white mb-1">
														{req.name}
													</h3>
													<p className="text-sm text-gray-300">
														{req.courses?.length > 0
															? req.courses.join(", ")
															: "No courses found."}
													</p>
												</div>
											))}
										</motion.div>
									)}
								</div>
							);
						})}
					</div>
				)}
			</div>
		</>
	);
};

export default SavedResults;
