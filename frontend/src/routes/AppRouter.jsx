import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Home from "../pages/Home";
import Results from "../pages/Results";
import AboutUs from "../pages/AboutUs";


const AppRouter = () => {
	return (
		<Router>
			<Routes>
				<Route path="/" element={<Home />} />
				<Route path="/results" element={<Results />} />
				<Route path="/about" element={<AboutUs />} />
			</Routes>
		</Router>
	);
};

export default AppRouter;
