import React, { useEffect } from "react";
import Navbar from "../components/Navbar";
import Hero from "../components/Hero";
import FAQ from "../components/FAQ";
import Features from "../components/Features";


const scrollToHash = () => {
	const hash = window.location.hash;
	if (hash) {
		const id = hash.replace("#", "");
		const element = document.getElementById(id);
		if (element) {
			const yOffset = -80; // Adjust based on your navbar height
			const y =
				element.getBoundingClientRect().top + window.pageYOffset + yOffset;
			window.scrollTo({ top: y, behavior: "smooth" });
		}
	}
};

const Home = () => {
	useEffect(() => {
		// Scroll on load
		scrollToHash();

		// Scroll on hash change
		window.addEventListener("hashchange", scrollToHash);
		return () => window.removeEventListener("hashchange", scrollToHash);
	}, []);

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
