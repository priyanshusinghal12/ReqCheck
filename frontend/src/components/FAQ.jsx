import { Disclosure } from "@headlessui/react";
import { FaPlus, FaTimes } from "react-icons/fa";
import { motion } from "framer-motion";

const faqs = [
	{
		question: "How does it work?",
		answer:
			"You upload your unofficial transcript PDF and select your major. WatCourse reads your completed courses and matches them against your major's requirements.",
	},
	{
		question: "Is any personal info stored?",
		answer:
			"No. All processing happens on the client-side. No transcript data or personal info is stored or sent anywhere.",
	},
	{
		question: "Which undergrad calendar do we use?",
		answer:
			"We are currently using the 2024–2025 Undergraduate Calendar. We'll update accordingly each year.",
	},
	{
		question: "What is WatCourse?",
		answer:
			"WatCourse is a tool built for Waterloo students to quickly check what major requirements they’ve completed based on their transcript.",
	},
];

export default function FAQ() {
	return (
		<section id="faq" className="bg-black text-white px-4 sm:px-10 py-20">
			<motion.h2
				className="text-3xl sm:text-4xl font-bold text-center text-[#FED34C] mb-12"
				initial={{ opacity: 0, y: 30 }}
				whileInView={{ opacity: 1, y: 0 }}
				transition={{ duration: 0.6 }}
				viewport={{ once: true }}>
				Frequently Asked Questions
			</motion.h2>

			<div className="max-w-5xl mx-auto flex flex-col gap-6">
				{faqs.map((faq, idx) => (
					<Disclosure key={idx}>
						{({ open }) => (
							<motion.div
								initial={{ opacity: 0, y: 20 }}
								whileInView={{ opacity: 1, y: 0 }}
								transition={{ delay: idx * 0.1, duration: 0.5 }}
								viewport={{ once: true }}>
								<Disclosure.Button className="w-full flex justify-between items-center px-6 py-5 bg-[#1A1A1A] hover:border-[#FED34C] hover:bg-[#232323] transition-colors rounded-xl text-left border border-[#333] text-white text-lg font-semibold">
									{faq.question}
									{open ? <FaTimes /> : <FaPlus />}
								</Disclosure.Button>
								<Disclosure.Panel className="px-6 pt-3 pb-4 text-gray-300 bg-[#121212] rounded-b-xl border-l-2 border-yellow-500">
									{faq.answer}
								</Disclosure.Panel>
							</motion.div>
						)}
					</Disclosure>
				))}
			</div>
		</section>
	);
}
