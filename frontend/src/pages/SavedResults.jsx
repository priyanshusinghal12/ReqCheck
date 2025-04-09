import { useEffect, useState } from "react";
import { auth } from "../firebase";
import { useNavigate } from "react-router-dom";
import Navbar from "../components/Navbar";
import { FaTrash, FaPen } from "react-icons/fa";
import { motion } from "framer-motion";
import toast from "react-hot-toast";
import ParticlesBackground from "../components/ParticlesBackground";

const SavedResults = ({ openGlobalModal }) => {
	const [savedList, setSavedList] = useState([]);
	const [loading, setLoading] = useState(true);
	const [expandedIndexes, setExpandedIndexes] = useState([]);
	const [editIndex, setEditIndex] = useState(null);
	const [tempEditName, setTempEditName] = useState("");
	const [showDeleteModal, setShowDeleteModal] = useState(null);

	const navigate = useNavigate();

	useEffect(() => {
		const unsubscribe = auth.onAuthStateChanged(async (user) => {
			if (!user) {
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
				toast.error("Failed to load saved results.");
			}

			setLoading(false);
		});

		return () => unsubscribe();
	}, []);

	useEffect(() => {
		document.title = "ReqCheck | Saved Results";
	}, []);

	const handleEditName = (index) => {
		setTempEditName(savedList[index]?.name || "");
		setEditIndex(index);
	};

	const submitEditName = async () => {
		try {
			const user = auth.currentUser;
			if (!user) return toast.error("You must be logged in.");
			const token = await user.getIdToken();

			const res = await fetch(
				`${import.meta.env.VITE_BACKEND_URL}/edit-result-name/`,
				{
					method: "PATCH",
					headers: { "Content-Type": "application/json" },
					body: JSON.stringify({
						id_token: token,
						index: editIndex,
						new_name: tempEditName,
					}),
				}
			);

			const data = await res.json();
			if (data.status === "success") {
				toast.success("Name updated.");
				setSavedList((prev) => {
					const updated = [...prev];
					updated[editIndex].name = tempEditName;
					return updated;
				});
				setEditIndex(null);
			} else {
				toast.error("Update failed.");
			}
		} catch (e) {
			toast.error("Something went wrong.");
		}
	};

	const handleDelete = async (index) => {
		setShowDeleteModal(null);
		try {
			const user = auth.currentUser;
			if (!user) return toast.error("You must be logged in.");
			const token = await user.getIdToken();

			const res = await fetch(
				`${import.meta.env.VITE_BACKEND_URL}/delete-result/`,
				{
					method: "DELETE",
					headers: { "Content-Type": "application/json" },
					body: JSON.stringify({ id_token: token, index }),
				}
			);

			const data = await res.json();
			if (data.status === "success") {
				toast.success("Result deleted.");
				setSavedList((prev) => prev.filter((_, i) => i !== index));
			} else {
				toast.error("Failed to delete.");
			}
		} catch (e) {
			toast.error("Error deleting result.");
		}
	};

	const handleLoadToResults = (result) => {
		window.scrollTo({ top: 0, behavior: "smooth" });
		const reconstructedRequirements = {};
		result.requirements?.forEach((req) => {
			if (req?.name) {
				reconstructedRequirements[req.name] = [req.met, req.courses || []];
			}
		});
		navigate("/results", {
			state: {
				results: {
					major: result.major,
					completed_courses: result.completed_courses,
					requirements: reconstructedRequirements,
				},
			},
		});
	};

	const capitalizeWords = (str) =>
		str
			.split(" ")
			.map((w) => w.charAt(0).toUpperCase() + w.slice(1))
			.join(" ");

	return (
		<>
			<Navbar openGlobalModal={openGlobalModal} />
			<ParticlesBackground />

			{editIndex !== null && (
				<div className="fixed inset-0 bg-black bg-opacity-60 z-50 flex justify-center items-center">
					<div className="bg-[#1a1a1a] p-6 rounded-xl shadow-lg border border-gray-600 max-w-sm w-full">
						<h2 className="text-lg font-semibold mb-3 text-white">Edit Name</h2>
						<input
							type="text"
							placeholder="Enter a new name"
							className="w-full p-2 rounded border border-gray-600 bg-black text-white placeholder-gray-400"
							value={tempEditName}
							onChange={(e) => setTempEditName(e.target.value)}
						/>
						<div className="mt-4 flex justify-end gap-2">
							<button
								onClick={() => setEditIndex(null)}
								className="text-gray-300 hover:text-white">
								Cancel
							</button>
							<button
								onClick={submitEditName}
								className="bg-[#FED34C] text-black px-4 py-1 rounded hover:bg-yellow-400">
								Save
							</button>
						</div>
					</div>
				</div>
			)}

			{showDeleteModal !== null && (
				<div className="fixed inset-0 bg-black bg-opacity-60 z-50 flex justify-center items-center">
					<div className="bg-[#1a1a1a] p-6 rounded-xl shadow-lg border border-gray-600 max-w-sm w-full">
						<h2 className="text-lg font-semibold mb-3 text-white">
							Delete Result
						</h2>
						<p className="text-sm text-gray-300 mb-4">
							Are you sure you want to permanently delete this saved result?
						</p>
						<div className="mt-4 flex justify-end gap-3">
							<button
								onClick={() => setShowDeleteModal(null)}
								className="text-gray-300 hover:text-white">
								Cancel
							</button>
							<button
								onClick={() => handleDelete(showDeleteModal)}
								className="bg-red-600 text-white px-4 py-1 rounded hover:bg-red-700">
								Delete
							</button>
						</div>
					</div>
				</div>
			)}

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
								<motion.div
									key={index}
									initial={{ opacity: 0, y: 40 }}
									animate={{ opacity: 1, y: 0 }}
									transition={{ duration: 0.4, delay: index * 0.05 }}
									className="border border-gray-700 p-4 rounded-lg bg-[#1A1A1A]">
									<div className="flex justify-between items-center mb-2">
										<div>
											<h2 className="text-xl font-bold text-white mb-1">
												{result.name || (
													<span className="italic text-gray-400">Unnamed</span>
												)}
											</h2>
											<p className="text-white font-medium mb-0.5">
												{capitalizeWords(result.major)}
											</p>
											<p className="text-sm text-gray-400">
												{new Date(result.timestamp).toLocaleString()}
											</p>
										</div>

										<div className="flex gap-2">
											<button
												onClick={() => handleLoadToResults(result)}
												className="bg-[#FED34C] text-black font-semibold px-4 py-1 rounded hover:bg-yellow-400">
												Load Result
											</button>
											<button
												onClick={() => handleEditName(index)}
												className="bg-gray-800 border border-gray-600 px-3 py-1 rounded text-white hover:bg-gray-700">
												<FaPen />
											</button>
											<button
												onClick={() => setShowDeleteModal(index)}
												className="bg-gray-800 border border-gray-600 px-3 py-1 rounded text-white hover:bg-gray-700">
												<FaTrash />
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
								</motion.div>
							);
						})}
					</div>
				)}
			</div>
		</>
	);
};

export default SavedResults;
