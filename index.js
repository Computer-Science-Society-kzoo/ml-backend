const express = require("express");
const https = require("https");

const app = express();
const PORT = 9000;

app.get("/", (req, res) => {
  res.send("Hello World");
});

app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});

app.get("/aleksandr", (req, res) => {
  input = req.query.input; 
  if (!input || input == "" ) {
    res.send("Hello Aleksandr. Please add parameter to the end of the url: /aleksandr?input=DATA");
  } else {
    res.send("Coming soon");
  }
});

app.get("/duure_mall/", (req, res) => {
  input = req.query.input
  if (!input || input == "" ) {
    res.send("Hello Duurenbayar and Mallory. Please add parameter to the end of the url: /duure_mall?input=DATA");
  } else {
    res.send("Coming soon");
  }
});

app.get("/derik", (req, res) => {
  input = req.query.input; 
  if (!input || input == "" ) {
    res.send("Hello Luke. Please add parameter to the end of the url: /derik?input=DATA");
  } else {
    res.send("Coming soon");
  }
});
