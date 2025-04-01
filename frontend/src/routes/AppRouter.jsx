import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Home from "../pages/Home";
import AboutUs from "../pages/AboutUs";
import Results from "../pages/Results";
import FeedbackForm from "../pages/FeedbackForm";
import SavedResults from "../pages/SavedResults";

export default function AppRouter() {
	return (
		<Router>
			<Routes>
				<Route path="/" element={<Home />} />
				<Route path="/about" element={<AboutUs />} />
				<Route path="/results" element={<Results />} />
				<Route path="/feedback" element={<FeedbackForm />} />
				<Route path="/saved" element={<SavedResults />} />
			</Routes>
		</Router>
	);
}
