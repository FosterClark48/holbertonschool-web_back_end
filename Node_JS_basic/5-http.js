// Create a more complex HTTP server using Node's HTTP module

const http = require('http');
const countStudents = require('./3-read_file_async');

const app = http.createServer(async (req, res) => {
  res.writeHead(200, { 'Content-Type': 'text/plain' });

  if (req.url === '/') {
    res.end('Hello Holberton School!');
  } else if (req.url === '/students') {
    const database = process.argv[2];

    // This array is used to store all the output messages that would normally go to the console
    const output = ['This is the list of our students'];
    // store original console.log function in originalConsoleLog so it can be restored later.
    const originalConsoleLog = console.log;
    // Override console.log w/ new function that, instead of printing to console,
    // pushes message into 'output' array.
    console.log = (message) => {
      output.push(message);
    };

    try {
      await countStudents(database);
      console.log = originalConsoleLog;
      res.end(output.join('\n'));
    } catch (error) {
      console.log = originalConsoleLog;
      res.end(`This is the list of our students\n${error.message}`);
    }
  } else {
    res.end('Not found');
  }
});

app.listen(1245);

module.exports = app;
