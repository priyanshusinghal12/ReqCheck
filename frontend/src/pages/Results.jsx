import { useEffect, useState } from "react";

const Results = () => {
	const [courses, setCourses] = useState(["STAT 330", "STAT 331"]);
	const [requirements, setRequirements] = useState(["STAT 332", "STAT 333"]);

	return (
		<div className="p-10 text-white">
			<h2 className="text-4xl font-bold text-center mb-6">Results</h2>
			<div className="grid grid-cols-2 gap-4">
				<div>
					<h3 className="text-2xl font-semibold">Completed Courses</h3>
					<ul className="list-disc pl-6">
						{courses.map((course, index) => (
							<li key={index}>{course}</li>
						))}
					</ul>
				</div>
				<div>
					<h3 className="text-2xl font-semibold">Remaining Requirements</h3>
					<ul className="list-disc pl-6">
						{requirements.map((req, index) => (
							<li key={index}>{req}</li>
						))}
					</ul>
				</div>
			</div>
		</div>
	);
};

export default Results;
