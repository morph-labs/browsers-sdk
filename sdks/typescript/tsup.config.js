import { defineConfig } from "tsup";

export default defineConfig({
  entry: ["browsers_sdk/main.ts"],
  format: ["cjs", "esm"],
  dts: true,
  clean: true,
  splitting: false,
  sourcemap: true,
  outExtension({ format }) {
    return {
      js: format === "esm" ? ".mjs" : ".cjs",
    };
  },
  platform: "node",
  target: "node14",
  external: ["morphcloud"],
  bundle: true,
  minify: false,
});