# Task Management Application

A dynamic task management web application built with Flask and React.

## Features

- Hierarchical todo list (up to sub-sub-task level).
- Multi-user support with individual task visibility.
- Dynamic frontend allowing tasks to expand and show sub-tasks.
- RESTful backend API built with Flask.

## Installation Instructions

### Backend (Flask)

1. **Clone the Repository**:
```
git clone [your-repository-link]
cd [your-repository-directory]

```

2. **Set Up a Virtual Environment**:
```
python -m venv venv
```


3. **Activate the Virtual Environment**:
- On Windows: 
  ```
  venv\Scripts\activate
  ```
- On macOS and Linux: 
  ```
  source venv/bin/activate
  ```

4. **Install the Required Packages**:

```
pip install -r requirements.txt

```

5. **Run the Flask App**:
```
export FLASK_APP=project
export FLASK_ENV=development
flask run

```

### Frontend (React)

1. **Navigate to the React App Directory**:

```
cd task-management

```
2. **Install the Required npm Packages**:
```
npm install

```

3. **Run the React App**:

```
npm start

```

The React app will now run on `http://localhost:3000` and will proxy backend requests to Flask which runs on `http://localhost:5000`.

## Usage

1. Navigate to the React app in your browser.
2. Register or log in.
3. Start creating and managing tasks!
