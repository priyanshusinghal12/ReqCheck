import { useEffect, useState } from "react";
import { auth } from "../firebase";
import Navbar from "../components/Navbar";

const SavedResults = () => {
	const [savedResults, setSavedResults] = useState([]);
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
			if (data?.status === "success") {
				setSavedResults(data.results.reverse()); // Show most recent first
			}
			setLoading(false);
		};

		fetchSaved();
	}, []);

	if (loading)
		return <p className="text-white text-center mt-10">Loading...</p>;

	return (
		<>
			<Navbar />
			<div className="pt-20 px-6 md:px-16 text-white">
				<h1 className="text-3xl font-bold mb-6">Saved Results</h1>
				{savedResults.length === 0 ? (
					<p>No saved results yet.</p>
				) : (
					savedResults.map((item, index) => (
						<div
							key={index}
							className="mb-6 p-4 border-l-4 border-[#FED34C] bg-[#1A1A1A] rounded-xl">
							<p className="text-[#FED34C] font-semibold">
								{item.major.toUpperCase()} —{" "}
								{new Date(item.timestamp).toLocaleString()}
							</p>
							{Object.entries(item.requirements).map(
								([req, [met, courses]], i) => (
									<div key={i} className="mt-3">
										<h2 className="font-semibold">{req}</h2>
										<p className="text-sm text-gray-300">
											{courses.join(", ")}
										</p>
									</div>
								)
							)}
						</div>
					))
				)}
			</div>
		</>
	);
};

export default SavedResults;
