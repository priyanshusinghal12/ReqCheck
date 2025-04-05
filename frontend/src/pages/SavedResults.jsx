import { useEffect, useState } from "react";
import { auth } from "../firebase";
import Navbar from "../components/Navbar";
import { motion, AnimatePresence } from "framer-motion";

const SavedResults = () => {
	const [savedList, setSavedList] = useState([]);
	const [loading, setLoading] = useState(true);
	const [expandedIndex, setExpandedIndex] = useState(null);

	useEffect(() => {
		const fetchSaved = async () => {
			const user = auth.currentUser;
			if (!user) return;

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
		};

		fetchSaved();
	}, []);

	if (loading)
		return <p className="text-center text-white mt-10">Loading...</p>;

	if (savedList.length === 0)
		return (
			<p className="text-center text-white mt-10">No saved results found.</p>
		);

	return (
		<>
			<Navbar />
			<div className="pt-20 px-6 md:px-16 text-white">
				<h1 className="text-3xl font-bold mb-6">Your Saved Results</h1>

				{savedList.map((entry, index) => (
					<div
						key={index}
						className="border border-[#333] rounded-lg p-4 mb-4 bg-[#121212]">
						<div className="flex flex-col sm:flex-row sm:items-center sm:justify-between">
							<div>
								<h2 className="text-xl font-semibold capitalize">
									{entry.major}
								</h2>
								<p className="text-sm text-gray-400">
									{new Date(entry.timestamp).toLocaleString()}
								</p>
							</div>
							<button
								onClick={() =>
									setExpandedIndex(index === expandedIndex ? null : index)
								}
								className="mt-3 sm:mt-0 bg-[#FED34C] text-black px-4 py-2 rounded font-semibold hover:bg-yellow-400 transition">
								{expandedIndex === index ? "Hide" : "View"} Details
							</button>
						</div>

						<AnimatePresence>
							{expandedIndex === index && (
								<motion.div
									initial={{ opacity: 0, height: 0 }}
									animate={{ opacity: 1, height: "auto" }}
									exit={{ opacity: 0, height: 0 }}
									transition={{ duration: 0.3 }}
									className="mt-4">
									{entry.requirements.map((req, i) => (
										<div
											key={i}
											className={`p-4 rounded-xl mb-3 ${
												req.met
													? "bg-[#1A1A1A] border-l-4 border-[#FED34C]"
													: "bg-[#2A1A1A] border-l-4 border-red-500"
											}`}>
											<h3 className="font-semibold text-lg mb-1">{req.name}</h3>
											<p className="text-sm text-gray-300">
												{req.courses.length > 0
													? req.courses.join(", ")
													: "No courses found yet."}
											</p>
										</div>
									))}
								</motion.div>
							)}
						</AnimatePresence>
					</div>
				))}
			</div>
		</>
	);
};

export default SavedResults;
