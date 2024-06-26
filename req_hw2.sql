SELECT * FROM tasks WHERE user_id = 25;
SELECT * FROM tasks WHERE status_id = (SELECT id FROM status WHERE name = 'new');
UPDATE tasks SET status_id = (SELECT id FROM status WHERE name = 'in progress') WHERE id = 8;
SELECT * FROM users WHERE id NOT IN (SELECT DISTINCT user_id FROM tasks);
INSERT INTO tasks (title, description, status_id, user_id) VALUES ('task_title', 'task_description', (SELECT id FROM status WHERE name = 'new'), 25);
SELECT * FROM tasks WHERE status_id <> (SELECT id FROM status WHERE name = 'completed');
DELETE FROM tasks WHERE id = 10;
SELECT * FROM users WHERE email LIKE '%@example.com';
UPDATE users SET fullname = 'Robert' WHERE id = 15;
SELECT status.name, COUNT(tasks.id) FROM status LEFT JOIN tasks ON status.id = tasks.status_id GROUP BY status.name;
SELECT tasks.* FROM tasks JOIN users ON tasks.user_id = users.id WHERE users.email LIKE '%@example.com';
SELECT * FROM tasks WHERE description IS NULL OR description = '';
SELECT users.*, tasks.* FROM users INNER JOIN tasks ON users.id = tasks.user_id INNER JOIN status ON tasks.status_id = status.id WHERE status.name = 'in progress';
SELECT users.fullname, COUNT(tasks.id) FROM users LEFT JOIN tasks ON users.id = tasks.user_id GROUP BY users.fullname;












