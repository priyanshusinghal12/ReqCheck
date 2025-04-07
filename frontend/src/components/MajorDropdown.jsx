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
	"Combinatorics & Optimization",
	"Math Opt: Business Specialization",
	"Math Opt: Operations Research",
	"Pure Mathematics",
	"Mathematics Teaching",
	"AFM BA Specialization",
	"AFM Entrepreneurial",
	"AFM Performance & Risk",
	"AFM Fin Markets Specialization",
	"AFM Prof Acct Specialization",
	"AFM Sustainability Specialization",
	"FARM Risk Mgmt",
	"FARM Fin Analyst",
];

export default function MajorDropdown({
	selectedMajor,
	setSelectedMajor,
	fullWidth = false,
}) {
	const [query, setQuery] = useState("");
	const [open, setOpen] = useState(false);
	const [highlightedIndex, setHighlightedIndex] = useState(0);
	const dropdownRef = useRef();
	const optionRefs = useRef([]);

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

	useEffect(() => {
		// Reset highlight on new query
		setHighlightedIndex(0);
	}, [query]);

	useEffect(() => {
		// Auto scroll highlighted item into view
		if (open && optionRefs.current[highlightedIndex]) {
			optionRefs.current[highlightedIndex].scrollIntoView({
				block: "nearest",
			});
		}
	}, [highlightedIndex, open]);

	const handleKeyDown = (e) => {
		if (!open) return;

		if (e.key === "ArrowDown") {
			e.preventDefault();
			setHighlightedIndex((prev) =>
				prev + 1 < filteredMajors.length ? prev + 1 : prev
			);
		} else if (e.key === "ArrowUp") {
			e.preventDefault();
			setHighlightedIndex((prev) => (prev > 0 ? prev - 1 : prev));
		} else if (e.key === "Enter") {
			e.preventDefault();
			const selected = filteredMajors[highlightedIndex];
			if (selected) {
				setSelectedMajor(selected);
				setQuery(selected);
				setOpen(false);
			}
		} else if (e.key === "Escape") {
			setOpen(false);
		}
	};

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
				onKeyDown={handleKeyDown}
				placeholder="Select Major"
				className="w-full px-4 py-3 bg-[#1A1A1A] text-white border border-[#333] rounded-xl cursor-pointer"
			/>
			{open && (
				<div className="absolute mt-2 w-full bg-[#1A1A1A] border border-[#333] rounded-lg shadow-lg max-h-48 overflow-y-auto z-50">
					{filteredMajors.length > 0 ? (
						filteredMajors.map((major, idx) => (
							<div
								key={idx}
								ref={(el) => (optionRefs.current[idx] = el)}
								onClick={() => {
									setSelectedMajor(major);
									setQuery(major);
									setOpen(false);
								}}
								className={`px-4 py-2 text-sm cursor-pointer ${
									idx === highlightedIndex
										? "bg-[#FED34C] text-black"
										: "hover:bg-[#FED34C] hover:text-black text-white"
								}`}>
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
