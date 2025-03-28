import React from "react";
import { FaLinkedin, FaGithub, FaEnvelope } from "react-icons/fa";
import { motion, AnimatePresence } from "framer-motion";
import Navbar from "../components/Navbar";
import ridhikaImage from "../assets/ridhika.jpeg";
import priyanshuImage from "../assets/priyanshu.jpeg";

const teamMembers = [
	{
		name: "Priyanshu Singhal",
		major: "Math Studies '27",
		bio: "As a developer, I like creating applications that create a tangible impact in other peoples’ lives. You can often catch me playing a game of chess, going on long drives, at the Warrior Basketball Courts or planning another trip to Goa.",
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
	const [selectedMember, setSelectedMember] = React.useState(null);

	return (
		<>
			<Navbar />
			<div className="min-h-screen bg-black from-[#1a1a1a] via-[#1e1e1f] to-[#111] text-white pt-24">
				{/* About Section */}
				<motion.div
					initial={{ opacity: 0, y: 30 }}
					animate={{ opacity: 1, y: 0 }}
					transition={{ duration: 0.8 }}
					className="text-left max-w-4xl mx-auto pt-12 px-6">
					<h1 className="text-4xl font-bold mb-6 text-center">
						About ReqCheck
					</h1>
					<div className="max-w-3xl mx-auto">
						<p className="text-gray-300 text-base leading-relaxed mb-8 text-center">
							ReqCheck was born out of a genuine need to simplify a frustrating
							process — navigating the new undergraduate calendar and verifying
							major requirements. What started as a personal challenge became a
							passion project aimed at reducing stress and saving time for
							students. With a focus on speed, clarity, and convenience,
							ReqCheck helps you instantly check your completed courses against
							your program’s requirements — so you can plan with confidence and
							peace of mind.
						</p>
					</div>
				</motion.div>

				{/* The Team */}
				<motion.div
					initial={{ opacity: 0, y: 30 }}
					animate={{ opacity: 1, y: 0 }}
					transition={{ duration: 0.8 }}
					className="text-left max-w-4xl mx-auto mt-16 px-6">
					<h2 className="text-4xl font-bold mb-8 text-center">The Team</h2>
				</motion.div>

				{/* Team Members */}
				<div className="mt-16 max-w-5xl mx-auto px-6 space-y-20 pb-16">
					{teamMembers.map((member, index) => (
						<motion.div
							key={index}
							initial={{ opacity: 0, y: 50 }}
							whileInView={{ opacity: 1, y: 0 }}
							transition={{ duration: 0.8, ease: "easeOut" }}
							viewport={{ once: true }}
							onClick={() => setSelectedMember(member)}
							className={`cursor-pointer flex flex-col md:flex-row ${
								member.imagePosition === "left" ? "" : "md:flex-row-reverse"
							} items-center gap-12`}>
							{/* Profile Image */}
							<div className="flex justify-center w-full md:w-1/2">
								<img
									src={member.image}
									alt={member.name}
									className="w-40 h-40 sm:w-48 sm:h-48 md:w-56 md:h-56 rounded-full object-cover"
								/>
							</div>

							{/* Info Card */}
							<div className="w-full bg-gradient-to-br from-[#1a1a1c] via-[#2a2a2d] to-[#1c1c1f] border border-gray-600 rounded-2xl shadow-xl p-8">
								<h2 className="text-2xl font-bold mb-2 text-center md:text-left">
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

				{/* Overlay Popup for Selected Member */}
				<AnimatePresence>
					{selectedMember && (
						<motion.div
							initial={{ opacity: 0 }}
							animate={{ opacity: 1 }}
							exit={{ opacity: 0 }}
							className="fixed inset-0 bg-black bg-opacity-80 backdrop-blur-sm flex items-center justify-center z-50"
							onClick={() => setSelectedMember(null)}>
							<motion.div
								initial={{ scale: 0.9, opacity: 0 }}
								animate={{ scale: 1, opacity: 1 }}
								exit={{ scale: 0.9, opacity: 0 }}
								transition={{ duration: 0.3 }}
								className="relative bg-[#1a1a1a] border border-[#2a2a2a] text-white rounded-3xl p-8 max-w-xl w-full shadow-lg"
								onClick={(e) => e.stopPropagation()}>
								<button
									className="absolute top-4 right-4 text-gray-400 hover:text-white text-3xl"
									onClick={() => setSelectedMember(null)}>
									&times;
								</button>
								<img
									src={selectedMember.image}
									alt={selectedMember.name}
									className="w-32 h-32 mx-auto rounded-full object-cover mb-6"
								/>
								<h2 className="text-2xl font-bold text-center">
									{selectedMember.name}
								</h2>
								<p className="text-center text-gray-400 mb-4">
									{selectedMember.major}
								</p>
								<p className="text-center text-gray-300">
									{selectedMember.bio}
								</p>
							</motion.div>
						</motion.div>
					)}
				</AnimatePresence>
			</div>
		</>
	);
};

export default AboutUs;
