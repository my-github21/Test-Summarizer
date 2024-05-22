<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Student Grade Management System</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            background-color: #f4f4f4;
        }
        .container {
            width: 80%;
            margin: 0 auto;
            padding: 20px;
            background-color: #fff;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }
        h1, h2, h3 {
            color: #333;
        }
        pre {
            background-color: #eee;
            padding: 10px;
            overflow-x: auto;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Student Grade Management System</h1>
        <h2>Overview</h2>
        <p>The Student Grade Management System is a Python-based program that allows users to manage student records, calculate scores, and generate batch-wise topper lists. This system is designed to store student information in a MySQL database and perform various operations such as adding, removing, updating, and displaying student records.</p>
        
        <h2>Features</h2>
        <ul>
            <li><strong>Add Student:</strong> Add a new student record, including name, course, assessments, and assignments.</li>
            <li><strong>Remove Student:</strong> Remove a student record by providing the student ID.</li>
            <li><strong>Update Student:</strong> Update the information for a specific student by providing the student ID.</li>
            <li><strong>Show All Students:</strong> Display all student records in the system.</li>
            <li><strong>Batch-wise Topper List:</strong> Display the batch-wise topper list for each course.</li>
        </ul>
        
        <h2>Requirements</h2>
        <ul>
            <li>Python 3.x</li>
            <li>MySQL Database</li>
        </ul>
        
        <h2>Setup</h2>
        <h3>Install the required Python packages:</h3>
        <pre><code>pip install mysql-connector-python</code></pre>
        
        <h3>Set up a MySQL database named <em>pythonprojectsdb</em> with the necessary table. You can use the following SQL query to create the table:</h3>
        <pre><code>CREATE TABLE tblStudent (
    Id INT AUTO_INCREMENT PRIMARY KEY,
    stud_name VARCHAR(255),
    course VARCHAR(255),
    assessment INT,
    assignment INT
);</code></pre>
        
        <h3>Update the MySQL database connection details in the <em>student.py</em> file:</h3>
        <pre><code>mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="pythonprojectsdb"
)</code></pre>
        
        <h2>Usage</h2>
        <p>Run the <em>main.py</em> file to start the Student Grade Management System. Follow the on-screen instructions to perform various operations.</p>
    </div>
</body>
</html>
