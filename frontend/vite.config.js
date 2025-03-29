import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";
import tailwindcss from "@tailwindcss/vite";

export default defineConfig({
	plugins: [react(), tailwindcss()],
	server: {
		proxy: {
			"/check-requirements": "http://127.0.0.1:8000",
			"/parse-transcript": "http://127.0.0.1:8000",
		},
	},
	build: {
		outDir: "dist",
	},
});
