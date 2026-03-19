// Fetch data from Python API and show in console
fetch('/api/todo')
  .then((response) => response.json())
  .then((data) => console.log('Todo item:', data))
  .catch((err) => console.error('Error:', err));
