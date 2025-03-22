import React, { useState } from "react";
import { motion, AnimatePresence } from "framer-motion";
import { FiPlus, FiX } from "react-icons/fi";

const faqs = [
	{
		question: "How does it work?",
		answer:
			"Upload your unofficial transcript PDF from Quest and select your intended major. Our system checks your completed courses against the academic calendar to show what requirements you've fulfilled and what's left.",
	},
	{
		question: "Is any personal info stored?",
		answer:
			"No. We do not store any transcripts, names, or email addresses. Everything happens locally in your browser — your data is never saved.",
	},
	{
		question: "Which undergrad calendar do we use?",
		answer:
			"We currently use the 2024–2025 Undergraduate Calendar for all major requirement checks.",
	},
	{
		question: "What is WatCourse?",
		answer:
			"WatCourse is a course requirement tracker for University of Waterloo students. It helps you figure out which major requirements you’ve completed — instantly and privately.",
	},
];

const FAQ = () => {
	const [activeIndex, setActiveIndex] = useState(null);

	const toggleFAQ = (index) => {
		setActiveIndex(activeIndex === index ? null : index);
	};

	return (
		<section className="bg-black text-white py-16 px-4 sm:px-8 md:px-16">
			<h2 className="text-3xl sm:text-4xl font-bold mb-10 text-center">
				Frequently Asked Questions
			</h2>

			<div className="max-w-3xl mx-auto space-y-4">
				{faqs.map((faq, index) => (
					<div
						key={index}
						className="bg-[#1C1C1C] rounded-xl p-4 sm:p-6 shadow-md cursor-pointer"
						onClick={() => toggleFAQ(index)}>
						{/* Header */}
						<div className="flex justify-between items-center">
							<h3 className="text-lg sm:text-xl font-semibold">
								{faq.question}
							</h3>
							<span className="text-xl sm:text-2xl">
								{activeIndex === index ? <FiX /> : <FiPlus />}
							</span>
						</div>

						{/* Answer */}
						<AnimatePresence>
							{activeIndex === index && (
								<motion.div
									initial={{ opacity: 0, height: 0 }}
									animate={{ opacity: 1, height: "auto" }}
									exit={{ opacity: 0, height: 0 }}
									transition={{ duration: 0.3 }}
									className="overflow-hidden text-sm sm:text-base text-gray-300 mt-4">
									{faq.answer}
								</motion.div>
							)}
						</AnimatePresence>
					</div>
				))}
			</div>
		</section>
	);
};

export default FAQ;
