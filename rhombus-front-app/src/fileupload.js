//This component allows for the upload and display of .xlsx and .csv files. It also passes and receives data to/from the Django API.
import React, { useState, useRef } from 'react';
import Papa from 'papaparse';
import * as XLSX from 'xlsx';
import axios from 'axios';

function Fileupload({ onFileLoad, onUploadSuccess, onUploadError, onResetProcessedData, thresholdVar }) {
    const [file, setFile] = useState(null);
    const fileInputRef = useRef(null);

    const handleFileChange = (event) => {
        const selectedFile = event.target.files[0];
        if(onResetProcessedData){onResetProcessedData()
        } //clear processed data input

        if (selectedFile) {
            const fileExt = selectedFile.name.split('.').pop();
            if (fileExt === 'csv') {
                // Parse CSV file
                Papa.parse(selectedFile, {
                    complete: (result) => {
                        onFileLoad(result.data);
                        setFile(selectedFile);
                    },
                    header: false,
                });
            } else if (fileExt === 'xlsx') {
                // console.log("here");
                // Parse XLSX file
                const reader = new FileReader();
                reader.onload = (e) => {
                    const bstr = e.target.result;
                    const wb = XLSX.read(bstr, { type: 'binary' });
                    const wsname = wb.SheetNames[0];
                    const ws = wb.Sheets[wsname];
                    const data = XLSX.utils.sheet_to_json(ws, { header: 1 });
                    onFileLoad(data);
                    setFile(selectedFile);
                };
                reader.readAsBinaryString(selectedFile);
            } else {
                // If the file is not CSV or XLSX, just set the file
                setFile(selectedFile);
            }
        }
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        if (onResetProcessedData){onResetProcessedData(); //Reset processed data state
        }
        if (!file) {
            alert('Please select a file first.');
            return;
        }
        const formData = new FormData();
        formData.append('file', file);
        formData.append('threshold_var',thresholdVar)
        try {
            const response = await axios.post('http://localhost:8000/api/upload/', formData, {
                headers: {
                    'Content-Type': 'multipart/form-data',
                },
            });
            console.log('File uploaded successfully', response.data);
            if (onUploadSuccess) {
                onUploadSuccess(response.data); // Now passing the whole response data back
            }
            setFile(null);
            fileInputRef.current.value = ""; // Clear the file input
        } catch (error) {
            const errorMessage = error.response && error.response.data && error.response.data.error
                                 ? error.response.data.error
                                 : 'An unexpected error occurred';
            if (onUploadError) {
                onUploadError(errorMessage); // Use the onUploadError prop to pass the error message up
            } else {
                console.error('Error uploading file', error);
            }
          }
    };

    return (
        <div>
            <form onSubmit={handleSubmit}>
                <input type="file" onChange={handleFileChange} ref={fileInputRef} accept=".csv, .xlsx" />
                <button type="submit">Process Data</button>
            </form>
        </div>
    );
}

export default Fileupload;