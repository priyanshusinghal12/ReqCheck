import React, { useEffect } from "react";
import { motion } from "framer-motion";
import { FaCheckCircle, FaRegCircle, FaCircle } from "react-icons/fa";

const checklist = {
	"Complete all the following: ECON 101/102/290/306/391/393/472/491/496": [
		true,
		[
			"ECON 101",
			"ECON 102",
			"ECON 290",
			"ECON 306",
			"ECON 391",
			"ECON 393",
			"ECON 472",
			"ECON 491",
			"ECON 496",
		],
	],
	"Complete one of the following: ECON 406/407/408/409": [true, ["ECON 406"]],
	"Complete 4 additional ECON courses at the 300/400 level": [
		true,
		["ECON 310", "ECON 320", "ECON 330", "ECON 440"],
	],
	"Complete all the following: AMATH 350/STAT 331/STAT 443": [
		true,
		["AMATH 350", "STAT 331", "STAT 443"],
	],
	"Complete one of the following: AMATH 331/PMATH 331/PMATH 333/PMATH 351": [
		true,
		["PMATH 331"],
	],
	"Complete one of the following: CO 250/255": [true, ["CO 250"]],
	"Complete one of the following: MATH 237/247": [true, ["MATH 237"]],
	"Complete 7 additional courses from: ACTSC, AMATH, CO, CS, MATBUS, MATH, PMATH, STAT":
		[
			true,
			[
				"AMATH 101",
				"AMATH 450",
				"CO 487",
				"CS 371",
				"MATBUS 471",
				"MATH 340",
				"PMATH 450",
			],
		],
	"Complete 2 additional courses": [false, []],
};

const Results = () => {
	useEffect(() => {
		window.scrollTo(0, 0);
	}, []);

	return (
		<section className="min-h-screen bg-[#0D1117] text-white px-6 sm:px-10 py-16">
			<h1 className="text-4xl font-extrabold text-center text-[#FED34C] mb-8">
				Your Progress
			</h1>

			<div className="max-w-3xl mx-auto border-l-4 border-[#FED34C] pl-6">
				{Object.entries(checklist).map(
					([requirement, [status, courses]], index) => (
						<motion.div
							key={index}
							initial={{ opacity: 0, y: 20 }}
							whileInView={{ opacity: 1, y: 0 }}
							transition={{ duration: 0.4, delay: index * 0.1 }}
							viewport={{ once: true }}
							className="relative mb-10">
							<span
								className={`absolute -left-[32px] top-1 ${
									status ? "text-[#FED34C]" : "text-gray-600"
								}`}>
								{status ? (
									<FaCheckCircle size={20} />
								) : (
									<FaRegCircle size={20} />
								)}
							</span>

							<h2 className="text-lg font-semibold text-white">
								{requirement}
							</h2>
							{courses.length > 0 ? (
								<ul className="mt-1 ml-4 list-disc text-gray-300 text-sm">
									{courses.map((course, i) => (
										<li key={i}>{course}</li>
									))}
								</ul>
							) : (
								<p className="text-gray-500 text-sm italic ml-4">
									No courses completed yet
								</p>
							)}
						</motion.div>
					)
				)}
			</div>

			{/* What-If Analysis */}
			<div className="max-w-2xl mx-auto mt-16 bg-[#1A1A1A] p-6 rounded-lg shadow-md">
				<h2 className="text-2xl font-bold mb-4 text-[#FED34C]">
					📘 What-If Analysis
				</h2>
				<p className="text-sm text-gray-400 mb-4">
					Simulate different course selections and see how they affect your
					progress.
				</p>
				<textarea
					rows="4"
					placeholder="Type in additional courses like 'MATH 239, STAT 230'..."
					className="w-full bg-gray-800 border border-gray-600 rounded-lg p-3 text-sm text-white placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-[#FED34C]"
				/>
				<button className="mt-4 bg-[#FED34C] text-black px-5 py-2 rounded-xl font-semibold hover:scale-105 transition-transform">
					Run Simulation
				</button>
			</div>
		</section>
	);
};

export default Results;
