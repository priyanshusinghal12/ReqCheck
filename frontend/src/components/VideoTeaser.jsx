import { useEffect } from "react";
import demoVideo from "../assets/demo-video.mp4";

const VideoTeaser = () => {
	useEffect(() => {
		const video = document.getElementById("demo");
		if (video) {
			video.play().catch((err) => {
				console.warn("Autoplay failed:", err);
			});
		}
	}, []);

	return (
		<div className="relative w-full overflow-hidden bg-black pb-30">
			<video
				id="demo"
				src={demoVideo}
				autoPlay
				loop
				muted
				playsInline
				className="w-full max-w-4xl mx-auto rounded-xl opacity-80 shadow-xl"
				style={{ paddingTop: "1px" }}>
				Sorry, your browser doesn't support embedded videos.
			</video>
		</div>
	);
};

export default VideoTeaser;
