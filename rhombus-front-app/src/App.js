// This javascipt represents the front end display which interacts with the backend via the Django API. It comprises several components.
// It was developed by Christian Daish on the 26-MAR-2024 for Rhombus AI.
// This is version 1.0.260324

import React, { useState } from 'react';
import FileUpload from './fileupload'; // Adjusted FileUpload component that includes upload functionality
import DataTable from './processeddatatable'; // Component for displaying the data
import Processeddatacard from "./processeddatacard";

function App() {
  const [tableData, setTableData] = useState([]);
  const [uploadStatus, setUploadStatus] = useState(''); // New state to track upload status
  const [processedData, setProcessedData] = useState(null); //New state for storing processed data
  const [errorMessage, setErrorMessage] = useState('')
  const [thresholdVar, setThresholdVar] = useState('');

  // Function to process file data (e.g., displaying it in DataTable)
  const handleFileData = (parsedData) => {
    setTableData(parsedData);
  };

  //Function to handle changing value in table
  const handleTypeChange = (key, newValue) => {
      // Assume processedData is an object where you can directly modify the value by key
      const updatedData = { ...processedData, [key]: newValue };
      setProcessedData(updatedData);
    };

  // Function to handle threshold selection
  const handleThresholdChange = (event) => {
    setThresholdVar(event.target.value);
  };


  const resetProcessedData = () => {
    setProcessedData(null); // Resetting processedData to its initial state
    setErrorMessage(''); // Clearing any error messages
  };
  // Add a function to handle upload errors
  const handleUploadError = (errorMessage) => {
    alert(errorMessage); // Display the error message in an alert box
  };

  // Function to handle upload success
  const handleUploadSuccess = (data) => {
    console.log('Upload successful:', data);
    setUploadStatus('Upload successful!'); // Update upload status message
    setProcessedData(data); //Assuming 'data' is the processed data you want to display
  };

  return (
      <div className="App">
        <h1>File Infer and Convert</h1>
        <h2>by Christian Daish 28-MAR-2024</h2>
          <h3>Step 1. Choose file <br/> Step 2. Choose desired category threshold (i.e., proportion of unique
              values) <br/> Step 3. Press 'Process Data' button to infer and convert data <br/> Step 4. Press 'Change Type' button next to value field, select the desired type.</h3>
          <select onChange={handleThresholdChange} value={thresholdVar}>
              <option value="">Categorical threshold</option>
              <option value="0.5">0.5</option>
              <option value="0.6">0.6</option>
              <option value="0.7">0.7</option>
              <option value="0.8">0.8</option>
              <option value="0.9">0.9</option>
              <option value="1.0">1.0</option>
              {/* Add more options as needed */}
          </select>

          <FileUpload onFileLoad={handleFileData} onUploadSuccess={handleUploadSuccess}
                    onResetProcessedData={resetProcessedData} onUploadError={handleUploadError} thresholdVar={thresholdVar}/>
        {uploadStatus && <p>{uploadStatus}</p>} {/* Display upload status */}
        <DataTable data={tableData}/>
        {processedData && <Processeddatacard data={processedData} onTypeChange={handleTypeChange}/>} {/* Conditionally render Processeddatacard */}
      </div>
  );
}

export default App;