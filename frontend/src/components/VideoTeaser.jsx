// components/VideoTeaser.jsx
import React from "react";
import demoVideo from "../assets/demo-video.mp4";

const VideoTeaser = () => {
	return (
		<div className="relative w-full overflow-hidden bg-black">
			<video
				src={demoVideo}
				autoPlay
				loop
				muted
				playsInline
				className="w-full max-w-4xl mx-auto rounded-xl opacity-80 shadow-xl"
				style={{
					paddingTop: "1px", // gentle nudge down instead of marginTop
				}}
			/>
		</div>
	);
};

export default VideoTeaser;
