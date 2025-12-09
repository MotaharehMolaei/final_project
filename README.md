Enrollment Management System

Features
- Add Enrollment -> Register new students with their personal and class details.
- Edit Enrollment -> Update existing student information.
- Remove Enrollment -> Delete enrollment from the database.
- View Enrollments -> Display all enrollments in a table, sorted by family and name.
- Validation -> Ensures data for names, phone numbers, enrollment dates, levels, and teacher names.

Structure and Folder
- enroll_model file -> Enroll class defines the structure of an enrollment record.
- enroll_controller file -> Handles validation and connects the GUI to the database.
- enroll_dao file -> EnrollDataAccess manages database operations (save, edit, remove, find).
- enroll_view file -> Tkinter GUI for managing enrollments (add, edit, remove, view).
