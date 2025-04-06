import React, { useEffect, useState } from "react";
import AppRouter from "./routes/AppRouter";
import { Toaster } from "react-hot-toast";
import LoginModal from "./components/LoginModal";
import { onAuthStateChanged } from "firebase/auth";
import { auth } from "./firebase";

function App() {
	const [showLoginModal, setShowLoginModal] = useState(false);
	const [shouldType, setShouldType] = useState(false);
	const [name, setName] = useState("");

	useEffect(() => {
		const unsubscribe = onAuthStateChanged(auth, (user) => {
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
		});
		return () => unsubscribe();
	}, []);

	const handleLoginModalClose = () => {
		const stored = localStorage.getItem("reqcheck_name");
		if (stored) {
			const first = stored.trim().split(" ")[0];
			setName(first);
		} else {
			setName("");
		}
		setShouldType(false); // reset animation
		setTimeout(() => {
			setShouldType(true);
		}, 10); // trigger animation restart
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
