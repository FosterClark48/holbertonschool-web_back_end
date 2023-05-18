export default function updateStudentGradeByCity(students, city, newGrades) {
  return students.filter((student) => student.location === city)
    .map((student) => {
      const dupe = student;
      dupe.grade = 'N/A';
      for (const field of newGrades) {
        if (dupe.id === field.studentId) {
          dupe.grade = field.grade;
        }
      }
      return dupe;
    });
}
