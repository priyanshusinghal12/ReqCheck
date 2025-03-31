import React from "react";
import AppRouter from "./routes/AppRouter";
import { Toaster } from "react-hot-toast";

function App() {
	return (
		<div className="min-h-screen bg-[#1c1c1e] text-white">
			<Toaster position="top-center" reverseOrder={false} />
			<AppRouter />
		</div>
	);
}

export default App;
