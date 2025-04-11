// components/VideoTeaser.jsx
import React from "react";
import demoVideo from "../assets/demo-video.mp4";

const VideoTeaser = () => {
	return (
		<div className="relative w-full overflow-hidden bg-black pb-30">
			<video
				id="demo"
				src={demoVideo}
				autoPlay
				loop
				muted
				playsInline
				className="w-full max-w-4xl mx-auto rounded-xl opacity-80 shadow-xl h-[200px] sm:h-[300px] md:h-auto"
				style={{
					paddingTop: "1px",
				}}
			/>
		</div>
	);
};

export default VideoTeaser;
