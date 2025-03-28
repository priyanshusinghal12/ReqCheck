import {
	FaEye,
	FaLock,
	FaUserGraduate,
	FaProjectDiagram,
} from "react-icons/fa";
import { motion } from "framer-motion";

const features = [
	{
		title: "No manual comparisons",
		icon: <FaEye size={24} />,
		description: "No more digging through the undergrad calendar 👀 ",
	},
	{
		title: "What If Analysis",
		icon: <FaProjectDiagram size={24} />,
		description:
			"Simulate what requirements you could complete by adding future courses",
	},
	{
		title: "Security guaranteed",
		icon: <FaLock size={24} />,
		description:
			"We don’t store your transcript- all processing is done locally in your browser",
	},
	{
		title: "Made by UW Students",
		icon: <FaUserGraduate size={24} />,
		description: "By UW students, for UW students",
	},
];

export default function Features() {
	return (
		<section className="bg-black text-white px-4 sm:px-10 py-20">
			<motion.h2
				className="text-3xl sm:text-4xl font-bold text-center text-[#FFFFFF] mb-12"
				initial={{ opacity: 0, y: 30 }}
				whileInView={{ opacity: 1, y: 0 }}
				transition={{ duration: 0.6 }}
				viewport={{ once: true }}>
				Why Use ReqCheck?
			</motion.h2>
			<div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
				{features.map((feature, idx) => (
					<motion.div
						key={idx}
						whileHover={{ scale: 1.05 }}
						whileTap={{ scale: 0.97 }}
						className="bg-[#1A1A1A] border border-[#2A2A2A] hover:border-[#FED34C] text-white p-6 rounded-xl transition-shadow shadow-md hover:shadow-yellow-600/30">
						<div className="flex justify-between items-center mb-3">
							<h3 className="text-lg font-semibold">{feature.title}</h3>
							<span className="text-yellow-400 text-xl">{feature.icon}</span>
						</div>
						<p className="text-gray-400 text-sm">{feature.description}</p>
					</motion.div>
				))}
			</div>
		</section>
	);
}
