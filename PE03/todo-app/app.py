from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory database (dictionary)
database = {}  # This acts as a simple key-value store for tasks

@app.route("/")
def index():
    return "Tasks Todo API!"  # A simple index route for the root endpoint

# Create a new task record (POST)
@app.route('/tasks', methods=['POST'])
def post_tasks_details():
    try:
        data = request.json  # Parse the incoming JSON request body
        # Ensure that the required keys are in the incoming JSON
        if "name" not in data or "status" not in data:
            return 'Invalid data: Missing "name" or "status"', 400  # Return 400 if required data is missing
        
        # Add or update the task in the database
        database[data["name"]] = data["status"]  # Store task in the in-memory dictionary
        return 'Task added successfully', 200  # Respond with 200 OK if successful
    except Exception as e:
        print("Error during saving task:", e)  # Log any errors
        return 'Failed to add task', 400  # Return 400 Bad Request on failure

# Update existing task record (PUT)
@app.route('/tasks', methods=['PUT'])
def put_tasks_details():
    try:
        data = request.json  # Parse the incoming JSON request body
        # Ensure that the required keys are in the incoming JSON
        if "name" not in data or "status" not in data:
            return 'Invalid data: Missing "name" or "status"', 400  # Return 400 if required data is missing
        
        # Update the task in the database
        if data["name"] in database:
            database[data["name"]] = data["status"]  # Update the task in the database
            return 'Task updated successfully', 200  # Respond with 200 OK if successful
        else:
            return 'Task not found', 404  # Return 404 if task does not exist
    except Exception as e:
        print("Error during updating task:", e)  # Log any errors
        return 'Failed to update task', 400  # Return 400 Bad Request on failure

# Retrieve all tasks (GET)
@app.route('/tasks', methods=['GET'])
def get_all_tasks():
    try:
        # Convert the database dictionary to a list of tasks
        tasks = [{"name": name, "status": status} for name, status in database.items()]
        
        # Use jsonify to return the list of tasks as JSON
        return jsonify(tasks), 200  # Return 200 OK with the list of tasks in JSON format
    except Exception as e:
        print("Error during fetching tasks:", e)  # Log any errors
        return 'Failed to fetch tasks', 400  # Return 400 Bad Request on failure

# Delete a task record (DELETE)
@app.route('/tasks/<task_name>', methods=['DELETE'])
def delete_tasks_details(task_name):
    try:
        if task_name in database:
            del database[task_name]  # Delete the task from the database
            return 'Task deleted successfully', 200  # Respond with 200 OK if deletion was successful
        else:
            return 'Task not found', 404  # Return 404 if the task does not exist
    except Exception as e:
        print("Error during deleting task:", e)  # Log any errors
        return 'Failed to delete task', 400  # Return 400 Bad Request on failure

if __name__ == "__main__":
    app.run(debug=True)  # Run the Flask app in debug mode



# The main changes from the students API to the tasks API involve adapting the functionality to manage tasks instead of student records. The route paths were updated from /students to /tasks, reflecting the shift in purpose, and the in-memory database was changed to store task names and statuses instead of student names and ages. Key names in the request data, such as "name" and "age" for students, were replaced with "name" and "status" for tasks. 
# Response messages were also modified to reflect task-related operations, such as adding, updating, or deleting tasks. Additionally, the task API introduced a new route for retrieving all tasks (GET /tasks), which lists every task along with its status, enhancing the functionality compared to the original students API, which only allowed retrieving individual student records by name. 
# Despite all these, the core structure of CRUD operations remains consistent across both APIs.