// src/components/ParticlesBackground.jsx
import { useEffect } from "react";

const ParticlesBackground = () => {
	useEffect(() => {
		if (window.particlesJS) {
			window.particlesJS("particles-js", {
				particles: {
					number: { value: 80, density: { enable: true, value_area: 800 } },
					color: { value: "#ffffff" },
					shape: { type: "circle" },
					opacity: { value: 0.5 },
					size: { value: 3, random: true },
					line_linked: {
						enable: true,
						distance: 150,
						color: "#ffffff",
						opacity: 0.4,
						width: 1,
					},
					move: { enable: true, speed: 2 },
				},
				interactivity: {
					events: {
						onhover: { enable: true, mode: "repulse" },
						onclick: { enable: true, mode: "push" },
					},
					modes: {
						repulse: { distance: 100 },
						push: { particles_nb: 4 },
					},
				},
				retina_detect: true,
			});
		}
	}, []);

	return (
		<div
			id="particles-js"
			className="absolute inset-0 w-full h-full pointer-events-none z-[-10]"
		/>
	);
};

export default ParticlesBackground;
