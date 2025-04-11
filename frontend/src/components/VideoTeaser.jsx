import React from "react";
import demoVideo from "../assets/demo-video.mp4";

const VideoTeaser = () => {
	return (
		<div className="relative w-full overflow-hidden bg-black pt-2 sm:pt-4 pb-6 sm:pb-10">
			<video
				id="demo"
				src={demoVideo}
				autoPlay
				loop
				muted
				playsInline
				className="w-full max-w-4xl mx-auto rounded-xl opacity-80 shadow-xl h-[200px] sm:h-[300px] md:h-auto"
			/>
		</div>
	);
};

export default VideoTeaser;
