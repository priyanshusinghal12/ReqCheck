import React, { useState } from "react";

const FAQ = () => {
	const [openIndex, setOpenIndex] = useState(null);

	const faqs = [
		{
			question: "What is WatCourse?",
			answer: "It helps students track major requirements.",
		},
		{
			question: "How do I upload my transcript?",
			answer: "Click the 'Upload Transcript' button.",
		},
		{
			question: "Is my data stored?",
			answer: "No, we do not store any of your data.",
		},
	];

	return (
		<div className="p-10 bg-gray-900 text-white">
			<h2 className="text-4xl font-bold text-center mb-6">
				Frequently Asked Questions
			</h2>
			{faqs.map((faq, index) => (
				<div key={index} className="border-b border-gray-600 py-4">
					<button
						className="w-full text-left text-xl font-semibold"
						onClick={() => setOpenIndex(index === openIndex ? null : index)}>
						{faq.question} {index === openIndex ? "▲" : "▼"}
					</button>
					{index === openIndex && (
						<p className="text-grayText mt-2">{faq.answer}</p>
					)}
				</div>
			))}
		</div>
	);
};

export default FAQ;
