// components/VideoTeaser.jsx
import React from "react";
import demoVideo from "../assets/demo-video.mp4";

const VideoTeaser = () => {
	return (
		<div className="relative w-full overflow-hidden bg-black pb-20 pt-10 sm:pt-16">
			<video
				id="demo"
				src={demoVideo}
				autoPlay
				loop
				muted
				playsInline
				className="w-full max-w-4xl mx-auto rounded-xl opacity-80 shadow-xl block"
				style={{
					display: "block",
					objectFit: "cover",
					minHeight: "200px", // 👈 forces some height on mobile
				}}
			/>
		</div>
	);
};

export default VideoTeaser;
