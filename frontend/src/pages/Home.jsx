import React from "react";
import Navbar from "../components/Navbar";
import Hero from "../components/Hero";
import FAQ from "../components/FAQ";
import Features from "../components/Features";

const Home = () => {
	return (
		<>
			<Navbar />
			<Hero />
			<Features />
			<FAQ />
		</>
	);
};

export default Home;
