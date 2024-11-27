import React, { useState } from 'react';
import './App.css';

function App() {
  const [task, setTask] = useState('');  // To capture input 
  const [tasks, setTasks] = useState([]); // List of tasks

  // Add new task to the list
  const addTask = () => {
    if (task) {
      setTasks([...tasks, task]);
      setTask(''); // Reset 
    }
  };

  // Delete 
  const deleteTask = (taskToDelete) => {
    setTasks(tasks.filter((task) => task !== taskToDelete));
  };

  return (
    <div className="App">
      <h1>To-Do List</h1>
      <div className="input-container">
        <input
          type="text"
          value={task}
          onChange={(e) => setTask(e.target.value)}
          placeholder="Add a new task"
        />
        <button onClick={addTask}>Add Task</button>
      </div>
      
      <ul>
        {tasks.map((task, index) => (
          <li key={index}>
            {task} 
            <button onClick={() => deleteTask(task)}>Delete</button>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default App;
