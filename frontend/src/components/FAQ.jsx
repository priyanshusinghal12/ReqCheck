import { Disclosure } from "@headlessui/react";
import { FaPlus, FaTimes } from "react-icons/fa";
import { motion } from "framer-motion";

const faqs = [
	{
		question: "What is ReqCheck?",
		answer:
			"ReqCheck is a tool for Waterloo students to check their missing major requirements quickly, using their unofficial transcript or entering courses taken so far. It’s fast, private, and easy to use.",
	},
	{
		question: "How does it work?",
		answer:
			"You upload your unofficial transcript PDF or enter your completed courses, then select your major. ReqCheck compares your completed courses to your major’s requirements to show what you’ve completed and what’s still needed.",
	},
	{
		question: "How does What-If Analysis work?",
		answer:
			"What-If Analysis lets you test how future courses might impact your degree progress. Just add planned courses and instantly see which new requirements they could fulfill.",
	},
	{
		question: "Is any personal info stored?",
		answer:
			"No. All processing is done locally in your browser. Transcript data is never uploaded, stored, or sent to any server—your data stays completely on your device.",
	},
	{
		question: "Which undergrad calendar do we use?",
		answer:
			"We use the 2025-2026 (latest) University of Waterloo Undergraduate Academic Calendar. The tool will be updated yearly to reflect the latest requirements.",
	},
	{
		question: "How does saving my results work?",
		answer:
			"Once you log in with your custom account you can create or your google account, you can save your current or even other requirement results—including What-If simulations. To keep your original transcript results, click 'Reset to Original' before saving again. Your results are securely stored and tied to your account for future access.",
	},
	{
		question: "Can I change my major or edit my courses later?",
		answer:
			"Yes! You can use the change major and edit courses buttons on the results page or you can just come back and change your major!",
	},
	{
		question: "Which majors can I check?",
		answer:
			"Currently, you can check majors under the Math Faculty, AFM and FARM; we're working to integrate more options.",
	},
];

export default function FAQ() {
	return (
		<section
			id="faq"
			className="bg-black text-white px-4 sm:px-10 py-20 scroll-mt-[100px]">
			<motion.h2
				className="text-3xl sm:text-4xl font-bold text-center text-[#FFFFFF] mb-12"
				initial={{ opacity: 0, y: 30 }}
				whileInView={{ opacity: 1, y: 0 }}
				transition={{ duration: 0.6 }}
				viewport={{ once: true }}>
				Frequently Asked Questions
			</motion.h2>
			{/* test comment */}
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
