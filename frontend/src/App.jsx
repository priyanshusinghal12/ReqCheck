import React, { useEffect, useState } from "react";
import AppRouter from "./routes/AppRouter";
import { Toaster } from "react-hot-toast";
import LoginModal from "./components/LoginModal";
import { onAuthStateChanged } from "firebase/auth";
import { auth, db } from "./firebase";
import {
	collection,
	addDoc,
	serverTimestamp,
	getCountFromServer,
} from "firebase/firestore";

function App() {
	const [showLoginModal, setShowLoginModal] = useState(false);
	const [shouldType, setShouldType] = useState(false);
	const [name, setName] = useState("");

	const EXEMPT_UIDS = [
		"PqirRr6CzkRpFQ24oQq9qcoA4Hg1",
		"jJ83UnrzQCeZfAjmBDyZt7hHOMA3",
	];

	const setNameFromLocalStorage = () => {
		const stored = localStorage.getItem("reqcheck_name");
		if (stored) {
			const first = stored.trim().split(" ")[0];
			setName(first);
		} else {
			setName("");
		}
	};

	useEffect(() => {
		const alreadyVisited = localStorage.getItem("reqcheck_has_visited");
		const isGuestSession = sessionStorage.getItem("reqcheck_guest_session");

		if (!alreadyVisited && !isGuestSession) {
			setShowLoginModal(true);
		} else {
			setNameFromLocalStorage();
			setShouldType(true);
		}
	}, []);

	// Log visit ONCE per session — exclude specific UIDs
	useEffect(() => {
		const logVisit = async () => {
			const alreadyLogged = sessionStorage.getItem("reqcheck_logged_visit");
			const user = auth.currentUser;

			const isExemptUser = user && EXEMPT_UIDS.includes(user.uid);

			if (!alreadyLogged && !isExemptUser) {
				try {
					await addDoc(collection(db, "visits"), {
						timestamp: serverTimestamp(),
						userAgent: navigator.userAgent,
						path: window.location.pathname,
					});
					sessionStorage.setItem("reqcheck_logged_visit", "true");
				} catch (err) {
					console.error("Visit logging failed:", err);
				}
			}
		};

		logVisit();
	}, []);

	useEffect(() => {
		const unsubscribe = onAuthStateChanged(auth, async (user) => {
			const isGuestSession = sessionStorage.getItem("reqcheck_guest_session");

			if (!user && !isGuestSession) {
				setShowLoginModal(true);
			} else if (user) {
				const display =
					user.displayName || localStorage.getItem("reqcheck_name");
				if (display) {
					const first = display.trim().split(" ")[0];
					setName(first);
				}
				setShouldType(true);

				if (EXEMPT_UIDS.includes(user.uid)) {
					try {
						const snapshot = await getCountFromServer(collection(db, "visits"));
						console.log("Total Visits:", snapshot.data().count);
					} catch (err) {
						console.error("Failed to fetch visit count:", err);
					}
				}
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
			sessionStorage.setItem("reqcheck_guest_session", "true");
		}

		setShouldType(false); // reset animation
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
				openGlobalModal={() => setShowLoginModal(true)}
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
