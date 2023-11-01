// Create a small HTTP server using http module

const http = require('http');

// Create an HTTP server
const app = http.createServer((req, res) => {
  // Set the response header
  res.writeHead(200, {'Content-Type': "text/plain"});

  // Send the response body
  res.end('Hello Holberton School!');
});

// The server should listen on port 1245
app.listen(1245, () => {
  console.log('Server running on http://localhost:1245/');
});

module.exports = app;
