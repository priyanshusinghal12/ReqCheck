import { useEffect, useState } from "react";
import { auth } from "../firebase";
import Navbar from "../components/Navbar";

const SavedResults = () => {
	const [savedData, setSavedData] = useState(null);
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
			if (data?.status === "success") setSavedData(data.results);
			else console.error("Failed to load saved results");

			setLoading(false);
		};

		fetchSaved();
	}, []);

	if (loading)
		return <p className="text-center text-white mt-10">Loading...</p>;
	if (!savedData)
		return (
			<p className="text-center text-white mt-10">No saved results found.</p>
		);

	return (
		<>
			<Navbar />
			<div className="pt-20 px-6 md:px-16 text-white">
				<h1 className="text-3xl font-bold mb-4">Your Saved Results</h1>
				<p className="text-lg mb-6">
					Major:{" "}
					<span className="text-[#FED34C] font-semibold">
						{savedData.major}
					</span>
				</p>
				{Object.entries(savedData.requirements).map(
					([req, [met, courses]], i) => (
						<div
							key={i}
							className={`p-4 rounded-xl mb-3 ${
								met
									? "bg-[#1A1A1A] border-l-4 border-[#FED34C]"
									: "bg-[#2A1A1A] border-l-4 border-red-500"
							}`}>
							<h2 className="font-semibold text-lg mb-1">{req}</h2>
							<p className="text-sm text-gray-300">{courses.join(", ")}</p>
						</div>
					)
				)}
			</div>
		</>
	);
};

export default SavedResults;
