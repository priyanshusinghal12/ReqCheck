import React from "react";
import { FaLinkedin, FaGithub, FaEnvelope } from "react-icons/fa";
import { motion } from "framer-motion";
import Navbar from "../components/Navbar";
import ridhikaImage from "../assets/ridhika.jpeg";
import priyanshuImage from "../assets/priyanshu.jpeg";

const teamMembers = [
	{
		name: "Priyanshu Singhal",
		major: "Math Studies '27",
		bio: "Priyanshu is a fullstack developer who is passionate about creating an impact through his projects, and watching the tears of his opponents as he defeats them on chess.com.",
		image: priyanshuImage,
		imagePosition: "right",
		linkedin: "https://www.linkedin.com/in/priysinghal/",
		github: "https://github.com/priyanshusinghal12",
		email: "mailto:priyanshusinghal14@gmail.com",
	},
	{
		name: "Ridhika Madan",
		major: "Statistics '27",
		bio: "Ridhika is... not very interesting to write a bio for.",
		image: ridhikaImage,
		imagePosition: "left",
		linkedin: "https://www.linkedin.com/in/ridhikamadan/",
		github: "https://github.com/yourgithub",
		email: "mailto:ridhikamadan22@gmail.com",
	},
];

const AboutUs = () => {
	return (
		<>
			<Navbar />
			<div className="min-h-screen bg-gradient-to-b from-[#1a1a1a] via-[#1e1e1f] to-[#111] text-white">
				<motion.div
					initial={{ opacity: 0, y: 30 }}
					animate={{ opacity: 1, y: 0 }}
					transition={{ duration: 0.8 }}
					className="text-center max-w-4xl mx-auto mt-24 px-6">
					<h1 className="text-5xl font-bold mb-4">About</h1>
					<p className="text-gray-300 text-lg leading-relaxed">
						WatCourse is your academic sidekick, built to make your life easier.
						Our goal is simple: help you understand what you’ve completed,
						what’s left, and how you can plan ahead smarter. With a quick PDF
						upload, we analyze your transcript, break down your major’s
						requirements, and even let you test out future course plans with our
						What-If simulator. Whether you’re grinding for grad school or
						winging your last electives, WatCourse is here for you.
					</p>
				</motion.div>

				{/* Team Members */}
				<div className="mt-24 max-w-5xl mx-auto px-6 space-y-24 pb-24">
					{teamMembers.map((member, index) => (
						<motion.div
							key={index}
							initial={{ opacity: 0, y: 50 }}
							whileInView={{ opacity: 1, y: 0 }}
							transition={{ duration: 0.8, ease: "easeOut" }}
							viewport={{ once: true }}
							className={`flex flex-col md:flex-row ${
								member.imagePosition === "left" ? "" : "md:flex-row-reverse"
							} items-center gap-10`}>
							{/* Profile Image */}
							<div className="flex justify-center w-full md:w-1/2">
								<img
									src={member.image}
									alt={member.name}
									className="w-40 h-40 sm:w-48 sm:h-48 md:w-56 md:h-56 rounded-full object-cover"
								/>
							</div>

							{/* Info Card */}
							<div className="w-full bg-gradient-to-br from-[#1a1a1c] via-[#2a2a2d] to-[#1c1c1f] border border-[#FED34C] rounded-2xl shadow-xl p-8">
								<h2 className="text-3xl font-bold mb-1 text-center md:text-left">
									{member.name}
								</h2>
								<h3 className="text-gray-400 text-lg mb-4 text-center md:text-left">
									{member.major}
								</h3>
								<p className="text-gray-300 text-base mb-6 leading-relaxed text-center md:text-left">
									{member.bio}
								</p>
								<div className="flex justify-center md:justify-start gap-6 text-2xl">
									<motion.a
										href={member.linkedin}
										target="_blank"
										rel="noopener noreferrer"
										whileHover={{ scale: 1.15 }}>
										<FaLinkedin className="hover:text-blue-400 transition duration-200" />
									</motion.a>
									<motion.a
										href={member.github}
										target="_blank"
										rel="noopener noreferrer"
										whileHover={{ scale: 1.15 }}>
										<FaGithub className="hover:text-gray-300 transition duration-200" />
									</motion.a>
									<motion.a href={member.email} whileHover={{ scale: 1.15 }}>
										<FaEnvelope className="hover:text-red-400 transition duration-200" />
									</motion.a>
								</div>
							</div>
						</motion.div>
					))}
				</div>
			</div>
		</>
	);
};

export default AboutUs;
