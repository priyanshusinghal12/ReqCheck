import React, { useEffect } from "react";
import Navbar from "../components/Navbar";
import Hero from "../components/Hero";
import FAQ from "../components/FAQ";
import Features from "../components/Features";
import VideoTeaser from "../components/VideoTeaser";

const scrollToHash = () => {
	const hash = window.location.hash;
	if (hash) {
		const id = hash.replace("#", "");
		const element = document.getElementById(id);
		if (element) {
			const yOffset = -80;
			const y =
				element.getBoundingClientRect().top + window.pageYOffset + yOffset;
			window.scrollTo({ top: y, behavior: "smooth" });
		}
	}
};

const Home = ({
	shouldType,
	name,
	setName,
	setShouldType,
	openGlobalModal,
}) => {
	useEffect(() => {
		scrollToHash();
		window.addEventListener("hashchange", scrollToHash);
		return () => window.removeEventListener("hashchange", scrollToHash);
	}, []);

	return (
		<>
			<Navbar
				setName={setName}
				setShouldType={setShouldType}
				openGlobalModal={openGlobalModal}
			/>
			<Hero shouldType={shouldType} name={name} />
			<VideoTeaser />
			<Features />
			<FAQ />
		</>
	);
};

export default Home;
