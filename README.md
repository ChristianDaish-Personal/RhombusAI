# RhombusAI
## Project Name:
Rhombus Ai Data Test
## Project Description: 
This full-stack application was created by Christian Daish 26-MAR-2024. It comprises Python/Django for the backend and React for the frontend. It performs the task of uploading .csv or .xlsx data, inferring and converting datatypes, and displaying the information. More module/component-specific details are provided in the headers of each script. 

## Prerequisites:
Before you begin, ensure you have met the following requirements:
- Python 3.8 or higher installed on your machine
- Node.js 14 or higher and npm (Node Package Manager)
- Pip (python package installer)
- A virtual environment tool (venv or virtualenv)
- Git for version control

This project uses Django 3.2 LTS. 

## Installation Steps
To set up and and run the application, from GitHub, involves several steps. These steps include cloning the repository, setting up the environments for both backend and frontend, installing dependencies, and finally running the application. Below is a step-by-step guide to get everything up and running.

### Step 1: Clone the Repository
First, clone the GitHub repository to your local machine. Open a terminal and run:

git clone https://github.com/ChristianDaish-Personal/RhombusAI.git
cd RhombusAI

### Step 2: Set Up the Backend (Django)

**2.1. Create a Virtual Environment:**
Navigate to the backend directory if your project is structured that way, then create a Python virtual environment:

python3 -m venv venv

**2.2. Activate the Virtual Environment:**
- On macOS/Linux:
  source venv/bin/activate
  
- On Windows (Command Prompt):
  venv\Scripts\activate.bat
  
**2.3. Install Dependencies:**
Ensure you have a `requirements.txt` file in your backend directory and install the required packages:

pip install -r requirements.txt

**2.4. Run Migrations:**
python manage.py migrate

**2.5. Start the Django Development Server:**
python manage.py runserver

This command starts the backend server, typically accessible at `http://localhost:8000`.

### Step 3: Set Up the Frontend (React)

**3.1. Navigate to the Frontend Directory:**
If your project structure separates the frontend, navigate into the frontend directory:

cd path/to/rhombus-front-app

**3.2. Install Node.js Dependencies:**
Make sure you have `Node.js` and `npm` (Node Package Manager) installed, then run:

npm install

This command installs all the dependencies defined in your `package.json` file.

**3.3. Start the React Development Server:**
npm start

This command starts the frontend development server, typically accessible at `http://localhost:3000`.

### Step 4: Environment Variables
To run this project, you will need to add the following environment variables to your `.env` file:

`DJANGO_SECRET_KEY` - A secret key for Django's settings. [Generate a Django secret key](https://djecrety.ir/).

`DEBUG` - Set to `True` for development to enable debug mode in Django.

`DATABASE_URL` - The URL for your database connection.

`REACT_APP_API_URL` - The base URL for your Django backend API.

Make sure to replace placeholder values with actual data relevant to your project.

## Usage

### Step 5: Access the Application
With both servers running, you can now access the frontend of your application in a web browser at the URL indicated by the React development server (`http://localhost:3000` typically). If the frontend needs to communicate with the backend, ensure that the React application is correctly configured to reach your Django API at `http://localhost:8000`.

### Step 6: Basic Usage
Step 6.1 Choose file from your system by pressing the 'Choose file' button
Step 6.2 Choose desired category threshold (i.e., proportion of unique values). The default is 0.5
Step 6.3 Press 'Process Data' button to infer and convert data 
Step 6.4 Press 'Change Type' button next to value field, select the desired type

## Features
Below are some key features of the app:

### Intelligent Data Processing and Visualization
The application allows for the uploading, processing, and visual display of data from .xlsx and .csv files, catering to a wide range of data formats commonly used in data analysis and business intelligence.
### Dynamic Data Type Inference and Conversion
A standout feature is the app's capability to infer data types from the uploaded files and present an option for users to manually adjust these inferred types via a dropdown selection. This feature, powered by the DictionaryTable component, adds flexibility and user control over how data is interpreted and displayed.
### Interactive Data Exploration
The DataTable and Processeddatacard components work together to showcase processed data in a structured and easily digestible format. Users can interact with the data, particularly changing data types on the fly, which is critical for exploratory data analysis and ensuring the data is in the correct format for subsequent operations or analysis.
### Seamless Backend Integration
With the use of the Django REST framework on the backend, the app emphasizes seamless integration between the frontend React application and the Django API. This backend integration facilitates real-time data processing and enriches the app with powerful server-side capabilities like data validation, authentication, and more.
### User-centric Design and Workflow
The application guides users through a clearly defined workflow: uploading data, selecting a category threshold for unique values, processing data, and optionally modifying data types. This structured approach ensures a smooth user experience and makes complex data processing tasks more approachable.
### Threshold-based Data Categorization
Users have the flexibility to choose a categorical threshold for data processing, an innovative feature that allows for customization based on the uniqueness of values within the dataset. This threshold adjustment capability can significantly impact the processing logic and outcomes, making the app versatile for different data analysis scenarios.
### Error Handling and Feedback
The app provides immediate feedback on the status of data uploads and processing, including success messages and alerts for errors. This instant communication helps users troubleshoot issues quickly and enhances the overall usability of the application.
### Modern Web Technologies
Built with React for the frontend and Django for the backend, the app leverages modern web development frameworks and libraries, ensuring a responsive, efficient, and scalable application. The use of libraries like Papa Parse for parsing CSV files and XLSX for handling Excel files underscores the app's robustness in dealing with diverse data sources.
These features together make "Rhombus AI Data Test" a comprehensive tool for data processing and analysis, emphasizing user interaction, flexibility, and a seamless integration between frontend and backend technologies.

## Technologies Used
This project is created with:

- **Backend**
  - [Django](https://www.djangoproject.com/): A high-level Python Web framework.
  - [Django REST Framework](https://www.django-rest-framework.org/): A powerful toolkit for building Web APIs in Django.

- **Frontend**
  - [React](https://reactjs.org/): A JavaScript library for building user interfaces.
  - [Axios](https://axios-http.com/): A promise-based HTTP client for the browser and Node.js.

- **Deployment/Other Tools**
  - [Git](https://git-scm.com/): A distributed version-control system for tracking changes in source code during software development.

## Contributing

I am not open to contributions. 
### Code of Conduct:


## Screenshots / Demo


## Documentation

## Tests

## Deployment

## Authors and Acknowledgment

## License

## Contact Information

## Contact Information
