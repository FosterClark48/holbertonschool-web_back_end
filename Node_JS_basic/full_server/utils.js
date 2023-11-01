// 8.1 Organize structure of server
// create a function named readDatabase that accepts a file path as argument
// It should read the database asynchronously
// It should return a promise
// When the file is not accessible, it should reject the promise with the error
// When the file can be read, return an object of arrays of the firstname of students per fields

const fs = require('fs').promises;

const readDatabase = async (filePath) => {
  try {
    const data = await fs.readFile(filePath, 'utf8');
    // Split the file content by lines and process further
    const lines = data.trim().split('\n');
    const students = {};
    // Skip the first line (headers)
    lines.slice(1).forEach((line) => {
      const [firstName, , , field] = line.split(',');

      // Assuming 'field' is not empty
      if (!students[field]) {
        students[field] = [];
      }
      students[field].push(firstName);
    });

    return students;
  } catch (error) {
    throw new Error('Cannot load the database');
  }
};

module.exports = readDatabase;
