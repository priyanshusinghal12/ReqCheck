import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Home from "../pages/Home";
import AboutUs from "../pages/AboutUs";
import Results from "../pages/Results";
import FeedbackForm from "../pages/FeedbackForm";
import SavedResults from "../pages/SavedResults";

export default function AppRouter({
	shouldType,
	name,
	setName,
	setShouldType,
	openGlobalModal, // <- add this
}) {
	return (
		<Router>
			<Routes>
				<Route
					path="/"
					element={
						<Home
							name={name}
							shouldType={shouldType}
							setName={setName}
							setShouldType={setShouldType}
							openGlobalModal={openGlobalModal} // <- pass it here
						/>
					}
				/>
				<Route
					path="/about"
					element={<AboutUs openGlobalModal={openGlobalModal} />}
				/>
				<Route
					path="/results"
					element={<Results openGlobalModal={openGlobalModal} />}
				/>
				<Route
					path="/feedback"
					element={<FeedbackForm openGlobalModal={openGlobalModal} />}
				/>
				<Route
					path="/saved"
					element={<SavedResults openGlobalModal={openGlobalModal} />}
				/>
			</Routes>
		</Router>
	);
}
