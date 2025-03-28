import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Home from "../pages/Home";
import AboutUs from "../pages/AboutUs";
import Results from "../pages/Results";
import FeedbackForm from "../pages/FeedbackForm";

export default function AppRouter() {
	return (
		<Router>
			<Routes>
				<Route path="/" element={<Home />} />
				<Route path="/about" element={<AboutUs />} />
				<Route path="/results" element={<Results />} />
				<Route path="/feedback" element={<FeedbackForm />} />
			</Routes>
		</Router>
	);
}
