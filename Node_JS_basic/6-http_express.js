// Creating a small HTTP server using Express module

const express = require('express');

const app = express();

// Define root endpoint and send response
app.get('/', (req, res) => {
  res.send('Hello Holberton School!');
});

// Start server on port 1245
app.listen(1245);

module.exports = app;
