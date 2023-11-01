// 8.3 Write Students Controller
// create a class named StudentsController. Add two static methods:
// The first one, getAllStudents reads the database, sorts the fields alphabetically,
// and then constructs a response string with the count and names of students in each field.
// The second one, getAllStudentsByMajor checks if the provided major is valid ('CS' or 'SWE'),
// reads the database, and returns the list of students in the specified major.

const readDatabase = require('../utils');

class StudentsController {
  static async getAllStudents(req, res) {
    try {
      const students = await readDatabase('./database.csv');
      let response = 'This is the list of our students\n';
      Object.keys(students).sort().forEach((field) => {
        const names = students[field].join(', ');
        response += `Number of students in ${field}: ${students[field].length}. List: ${names}\n`;
      });
      res.status(200).send(response.trim());
    } catch (error) {
      res.status(500).send('Cannot load the database');
    }
  }

  static async getAllStudentsByMajor(req, res) {
    const { major } = req.params;
    if (major !== 'CS' && major !== 'SWE') {
      return res.status(500).send('Major parameter must be CS or SWE');
    }

    try {
      const students = await readDatabase('./database.csv');
      if (students[major]) {
        const names = students[major].join(', ');
        res.status(200).send(`List: ${names}`);
      } else {
        return res.status(200).send('List: ');
      }
    } catch (error) {
      res.status(500).send('Cannot load the database');
    }
    return null;
  }
}

module.exports = StudentsController;
