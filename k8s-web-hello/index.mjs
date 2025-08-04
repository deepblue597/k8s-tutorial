import express from "express";
import os from "os";

const app = express();
const port = 3000;

app.get("/", (req, res) => {
  const hostname = os.hostname();
  res.send(`Hello from ${hostname}!`);
});

app.get("/health", (req, res) => {
  res.status(200).send("OK"); // Health check endpoint
  res.send("Server is healthy");
});

app.listen(port, () => {
  console.log(`Server running at http://localhost:${port}/`);
});
// Export the app for testing purposes
