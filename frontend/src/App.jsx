import React, { useEffect, useState } from "react";
import AppRouter from "./routes/AppRouter";
import { Toaster } from "react-hot-toast";
import LoginModal from "./components/LoginModal";
import { onAuthStateChanged } from "firebase/auth";
import { auth, db } from "./firebase";
import { collection, addDoc, serverTimestamp } from "firebase/firestore";
import { collection, getCountFromServer } from "firebase/firestore";

function App() {
	const [showLoginModal, setShowLoginModal] = useState(false);
	const [shouldType, setShouldType] = useState(false);
	const [name, setName] = useState("");

	// Track page load to Firestore (visits)
	useEffect(() => {
		const logVisit = async () => {
			try {
				await addDoc(collection(db, "visits"), {
					timestamp: serverTimestamp(),
					userAgent: navigator.userAgent,
					path: window.location.pathname,
				});
			} catch (err) {
				console.error("Visit logging failed:", err);
			}
		};
		logVisit();
	}, []);

	// Listen for user authentication
	useEffect(() => {
		const unsubscribe = onAuthStateChanged(auth, async (user) => {
			if (!user) {
				setShowLoginModal(true);
			} else {
				const display =
					user.displayName || localStorage.getItem("reqcheck_name");
				if (display) {
					const first = display.trim().split(" ")[0];
					setName(first);
				}
				setShouldType(true);
			}

			// ✅ Add this block to get visitor count
			try {
				const coll = collection(db, "visits");
				const snapshot = await getCountFromServer(coll);
				console.log("🔥 Total Visits:", snapshot.data().count);
			} catch (err) {
				console.error("Failed to fetch visit count:", err);
			}
		});

		return () => unsubscribe();
	}, []);

	// Called when modal is closed (login/signup/guest)
	const handleLoginModalClose = () => {
		const stored = localStorage.getItem("reqcheck_name");
		if (stored) {
			const first = stored.trim().split(" ")[0];
			setName(first);
		} else {
			setName("");
		}
		setShouldType(false);
		setTimeout(() => setShouldType(true), 10);
		setShowLoginModal(false);
	};

	return (
		<div className="min-h-screen bg-[#1c1c1e] text-white">
			<Toaster position="top-center" reverseOrder={false} />
			<AppRouter
				shouldType={shouldType}
				name={name}
				setName={setName}
				setShouldType={setShouldType}
			/>
			<LoginModal
				isOpen={showLoginModal}
				onClose={handleLoginModalClose}
				setName={setName}
				setShouldType={setShouldType}
			/>
		</div>
	);
}

export default App;
