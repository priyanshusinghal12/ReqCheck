import { useEffect, useState } from "react";
import { auth } from "../firebase";
import Navbar from "../components/Navbar";

const SavedResults = () => {
	const [savedList, setSavedList] = useState([]);
	const [loading, setLoading] = useState(true);

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
			<p className="text-center text-white mt-10">
				No saved results found. Try saving some from the results page.
			</p>
		);

	return (
		<>
			<Navbar />
			<div className="pt-20 px-6 md:px-16 text-white">
				<h1 className="text-3xl font-bold mb-6">Your Saved Results</h1>

				{savedList.map((entry, i) => (
					<div key={i} className="mb-6 border border-gray-700 p-5 rounded-lg">
						<p className="text-sm text-gray-400 mb-2">
							{new Date(entry.timestamp).toLocaleString()}
						</p>
						<p className="mb-3 text-lg font-semibold text-[#FED34C]">
							Major: {entry.major}
						</p>

						{Array.isArray(entry.requirements) &&
							entry.requirements.map((req, idx) => (
								<div
									key={idx}
									className={`p-4 rounded-xl mb-3 ${
										req.met
											? "bg-[#1A1A1A] border-l-4 border-[#FED34C]"
											: "bg-[#2A1A1A] border-l-4 border-red-500"
									}`}>
									<h2 className="font-semibold text-lg mb-1">{req.name}</h2>
									<p className="text-sm text-gray-300">
										{req.courses?.length
											? req.courses.join(", ")
											: "No courses found"}
									</p>
								</div>
							))}
					</div>
				))}
			</div>
		</>
	);
};

export default SavedResults;
