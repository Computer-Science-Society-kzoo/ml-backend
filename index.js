const express = require("express");
const https = require("https");
const { spawn } = require("child_process");
const os = require("os");
const app = express();
const PORT = 9000;
const pythonVersion = "python";

app.get("/", (req, res) => {
  res.send("Hello World");
});

app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});

function runPythonScript(pythonV, file, input) {
  return new Promise((resolve, reject) => {
    let dataToSend = "";

    python = spawn(pythonV, [file, input]);
    
    python.stdout.on("data", function (data) {
      console.log("Python Child Process Data: ", data.toString());
      dataToSend += data.toString();
    });

    python.on("exit", (code, signal) => {
      if (code) {
        console.error("Child exited with code: ", code);
        reject(new Error(`Child exited with code ${code}`));
      } else if (signal) {
        console.error("Child was killed with signal: ", signal);
        reject(new Error(`Child was killed with signal ${signal}`));
      } else {
        console.log("Child exited okay");
        resolve(dataToSend);
      }
    });

    python.on("close", (code) => {
      // stream from child process is closed
    });
  });
}

async function GPT3_5(input) {
  return await runPythonScript(pythonVersion, "aleksandr.py", input);
}

app.get("/aleksandr", async (req, res) => {
  input = req.query.input;
  if (!input || input == "") {
    res.send(
      "Hello Aleksandr. Please add parameter to the end of the url: /aleksandr?input=DATA"
    );
  } else {
    response = await GPT3_5(input);
    res.send(response);
  }
});

app.get("/duure_mall/", (req, res) => {
  input = req.query.input;
  if (!input || input == "") {
    res.send(
      "Hello Duurenbayar and Mallory. Please add parameter to the end of the url: /duure_mall?input=DATA"
    );
  } else {
    res.send("Coming soon");
  }
});

app.get("/derik", (req, res) => {
  input = req.query.input;
  if (!input || input == "") {
    res.send(
      "Hello Derik. Please add parameter to the end of the url: /derik?input=DATA"
    );
  } else {
    res.send("Coming soon");
  }
});
