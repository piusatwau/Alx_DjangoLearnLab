/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./templates/**/*.html", "./**/templates/**/*.html",
    "./node_modules/flyonui/dist/js/*.js"
  ],
  theme: {
    extend: {},
  },
  plugins: [
    require("flyonui"),
    require("flyonui/plugin") // Require only if you want to use FlyonUI JS component
  ],
}

