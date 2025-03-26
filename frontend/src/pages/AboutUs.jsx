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
			<div className="min-h-screen bg-black from-[#1a1a1a] via-[#1e1e1f] to-[#111] text-white pt-24">
				{/* About Section */}
				<motion.div
					initial={{ opacity: 0, y: 30 }}
					animate={{ opacity: 1, y: 0 }}
					transition={{ duration: 0.8 }}
					className="text-left max-w-4xl mx-auto pt-12 px-6">
					{" "}
					{/* Added mt-32 for spacing above */}
					<h1 className="text-4xl sm:text-4xl font-bold mb-6 sm:mb-8 text-center">
						About WatCourse
					</h1>
					<p className="text-gray-300 text-base sm:text-base leading-relaxed mb-8 text-justify">
						WatCourse is, first and foremost, a brainchild of intense
						desperation born out of sheer frustration at the new undergrad
						calendar, and a sincere desire to reduce students' suffering through
						a quick, convenient way to verify course progression by checking
						transcripts against major requirements. It is also the product of a
						lot of free time.
					</p>
				</motion.div>

				{/* The Team */}
				<motion.div
					initial={{ opacity: 0, y: 30 }}
					animate={{ opacity: 1, y: 0 }}
					transition={{ duration: 0.8 }}
					className="text-left max-w-4xl mx-auto mt-16 px-6">
					<h2 className="text-4xl sm:text-4xl font-bold mb-8 text-center">
						The Team
					</h2>
				</motion.div>

				{/* Team Members */}
				<div className="mt-16 sm:mt-20 max-w-5xl mx-auto px-6 space-y-20 sm:space-y-24 pb-16">
					{teamMembers.map((member, index) => (
						<motion.div
							key={index}
							initial={{ opacity: 0, y: 50 }}
							whileInView={{ opacity: 1, y: 0 }}
							transition={{ duration: 0.8, ease: "easeOut" }}
							viewport={{ once: true }}
							className={`flex flex-col md:flex-row ${
								member.imagePosition === "left" ? "" : "md:flex-row-reverse"
							} items-center gap-12 sm:gap-16`}>
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
								<h2 className="text-2xl sm:text-3xl font-bold mb-2 text-center md:text-left">
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
