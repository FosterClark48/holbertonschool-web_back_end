// function countStudents that reads a file asynchronously

const fs = require('fs').promises;

function countStudents(path) {
  // Return a promise by calling readFile mehtod of fs.promises
  return fs.readFile(path, 'utf8')
    .then((data) => {
      // Split the data into lines
      const lines = data.trim().split('\n');

      // Check if there are no valid lines
      if (lines.length <= 1) {
        throw new Error('Cannot load the database');
      }

      // Extract the header
      const headers = lines.shift().split(',');

      // Initialize counters and data structures for storing students and counts
      const students = {};
      const counts = {};

      // Process each line
      lines.forEach((line) => {
        if (!line.trim()) return; // Skip empty lines

        // Split the line into values and create a student object
        const values = line.split(',');
        const student = {};
        values.forEach((value, index) => {
          student[headers[index]] = value.trim();
        });

        // Count students per field and store their first names
        if (!counts[student.field]) {
          counts[student.field] = 0;
          students[student.field] = [];
        }
        counts[student.field] += 1;
        students[student.field].push(student.firstname);
      });

      // Log the total number of students
      const totalStudents = lines.length;
      console.log(`Number of students: ${totalStudents}`);

      // Log the number of students per field and their first names
      for (const field in counts) {
        if (Object.prototype.hasOwnProperty.call(counts, field)) {
          console.log(`Number of students in ${field}: ${counts[field]}. List: ${students[field].join(', ')}`);
        }
      }
    })
    .catch(() => { // If there is an error reading the file, throw an error message
      throw new Error('Cannot load the database');
    });
}

module.exports = countStudents;
