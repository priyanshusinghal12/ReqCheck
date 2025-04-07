import { useState, useRef, useEffect } from "react";

const majors = [
	"Math Degree Requirements",
	"BMath Data Science",
	"BCS Computer Science",
	"Computational Mathematics",
	"Statistics",
	"Biostatistics",
	"Mathematical Economics",
	"Mathematical Finance",
	"Mathematical Physics",
	"Mathematical Studies",
	"Mathematical Studies Business",
	"Actuarial Science",
	"Applied Mathematics",
	"Combinatorics and Optimization",
	"Mathematical Optimization Business Specialization",
	"Mathematical Optimization Operations Research Specialization",
	"Pure Mathematics",
	"Mathematics Teaching",
	"AFM BA Specialization",
	"AFM Entrepreneurial Mindset Specialization",
	"AFM Enterprise Performance and Risk Specialization",
	"AFM Financial Markets Specialization",
	"AFM Professional Accountant Specialization",
	"AFM Sustainability Specialization",
	"Farm Professional Risk Management Specialization",
	"Farm Professional Financial Analyst Specialization"
];

export default function MajorDropdown({
	selectedMajor,
	setSelectedMajor,
	fullWidth = false,
}) {
	const [query, setQuery] = useState("");
	const [open, setOpen] = useState(false);
	const dropdownRef = useRef();

	const filteredMajors = majors.filter((major) =>
		major.toLowerCase().includes(query.toLowerCase())
	);

	useEffect(() => {
		const handleClickOutside = (e) => {
			if (dropdownRef.current && !dropdownRef.current.contains(e.target)) {
				setOpen(false);
			}
		};
		document.addEventListener("mousedown", handleClickOutside);
		return () => document.removeEventListener("mousedown", handleClickOutside);
	}, []);

	return (
		<div
			className={`relative ${fullWidth ? "w-full" : "w-full sm:w-60"}`}
			ref={dropdownRef}>
			<input
				type="text"
				value={query}
				onChange={(e) => {
					setQuery(e.target.value);
					setOpen(true);
				}}
				onClick={() => setOpen(true)}
				placeholder="Change Major"
				className="w-full px-4 py-3 bg-[#1A1A1A] text-white border border-[#333] rounded-xl cursor-pointer"
			/>
			{open && (
				<div className="absolute mt-2 w-full bg-[#1A1A1A] border border-[#333] rounded-lg shadow-lg max-h-48 overflow-y-auto z-50">
					{filteredMajors.length > 0 ? (
						filteredMajors.map((major, idx) => (
							<div
								key={idx}
								onClick={() => {
									setSelectedMajor(major);
									setQuery(major);
									setOpen(false);
								}}
								className="px-4 py-2 text-sm cursor-pointer hover:bg-[#FED34C] hover:text-black text-white">
								{major}
							</div>
						))
					) : (
						<div className="px-4 py-2 text-gray-400">No majors found</div>
					)}
				</div>
			)}
		</div>
	);
}
