// recreate the small HTTP server using Express, but more complex, using countStudents file

const express = require('express');
const countStudents = require('./3-read_file_async');

const app = express();
const database = process.argv[2];

app.get('/', (req, res) => {
  res.send('Hello Holberton School!');
});

app.get('/students', async (req, res) => {
  const output = ['This is the list of our students'];

  try {
    const originalConsoleLog = console.log;
    console.log = (message) => {
      output.push(message);
    };

    await countStudents(database);

    console.log = originalConsoleLog;
    res.send(output.join('\n'));
  } catch (error) {
    console.log = originalConsoleLog;
    res.send(`This is the list of our students\n${error.message}`);
  }
});

app.listen(1245);

module.exports = app;
