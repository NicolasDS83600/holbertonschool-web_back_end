import readDatabase from '../utils';

class StudentsController {
  static async getAllStudents(req, res) {
    const dbPath = process.argv[2];

    try {
      const students = await readDatabase(dbPath);

      let response = 'This is the list of our students';

      const fields = Object.keys(students).sort((a, b) => (
        a.localeCompare(b, undefined, { sensitivity: 'base' })
      ));

      fields.forEach((field) => {
        response += `\nNumber of students in ${field}: ${students[field].length}. List: ${students[field].join(', ')}`;
      });

      res.status(200).send(response);
    } catch (err) {
      res.status(500).send('Cannot load the database');
    }
  }

  static async getAllStudentsByMajor(req, res) {
    const dbPath = process.argv[2];
    const { major } = req.params;

    if (major !== 'CS' && major !== 'SWE') {
      res.status(500).send('Major parameter must be CS or SWE');
      return;
    }

    try {
      const students = await readDatabase(dbPath);

      res.status(200).send(`List: ${students[major].join(', ')}`);
    } catch (err) {
      res.status(500).send('Cannot load the database');
    }
  }
}

export default StudentsController;
