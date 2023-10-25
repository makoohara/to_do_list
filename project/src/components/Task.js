import React, { useState } from 'react';
import axios from 'axios';

function Task({ task }) {
    const [isExpanded, setIsExpanded] = useState(false);
    const [subTasks, setSubTasks] = useState([]);

    const handleExpandClick = () => {
        if (!isExpanded) {
            // Fetch sub-tasks from the backend when the task is expanded
            axios.get(`/tasks/${task.id}/subtasks`)
                .then(response => {
                    setSubTasks(response.data);
                })
                .catch(error => {
                    console.error("Error fetching sub-tasks:", error);
                });
        }
        setIsExpanded(!isExpanded);
    };

    return (
        <div>
            <h2 className="title">{task.title}</h2>
            <button onClick={handleExpandClick}>
                {isExpanded ? "Collapse" : "Expand"}
            </button>
            {isExpanded && subTasks.map(subTask => (
                // Render SubTask component here
            ))}
        </div>
    );
}

export default Task;
