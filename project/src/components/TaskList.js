import React, { useState, useEffect } from 'react';
import axios from 'axios';
import Task from './Task';

function TaskList() {
    const [tasks, setTasks] = useState([]);

    useEffect(() => {
        // Fetch tasks from the backend
        axios.get('/tasks')
            .then(response => {
                setTasks(response.data);
            })
            .catch(error => {
                console.error("Error fetching tasks:", error);
            });
    }, []);

    return (
        <div className="container">
            {tasks.map(task => <Task key={task.id} task={task} />)}
        </div>
    );
}

export default TaskList;
