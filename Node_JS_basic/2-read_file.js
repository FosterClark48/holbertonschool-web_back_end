// function countStudents that reads a file synchronously

const fs = require('fs');

function countStudents(path) {
  try {
    // Read the file synchronously
    const data = fs.readFileSync(path, 'utf8');

    // Split the data into lines
    const lines = data.trim().split('\n');

    // Check of there are no valid lines
    if (lines.length <= 1) {
      throw new Error('Cannot load the database');
    }

    // Extract the header
    const headers = lines.shift().split(',');

    // Initialize counters and data structures
    const students = {};
    const counts = {};

    // Process each line
    lines.forEach((line) => {
      // Skip empty lines
      if (!line.trim()) return;

      const values = line.split(',');
      const student = {};
      values.forEach((value, index) => {
        student[headers[index]] = value.trim();
      });

      // Count students per field
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

    // Log the number of students per field
    for (const field in counts) {
      if (Object.prototype.hasOwnProperty.call(counts, field)) {
        console.log(`Number of students in ${field}: #{counts[field]}. List: ${students[field].join(', ')}`);
      }
    }
  } catch (err) {
    throw new Error('Cannot load the database');
  }
}

module.exports = countStudents;
