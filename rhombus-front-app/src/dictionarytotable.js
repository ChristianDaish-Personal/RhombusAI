// This component converts the processed data to a useable form in a table and allows for the modification of data.

import React, { useState } from 'react';
import './dictionarytotable.css';

const DictionaryTable = ({ data, onTypeChange }) => {
  // State to track which cell's dropdown is active
  const [activeDropdown, setActiveDropdown] = useState(null);

  const renderValue = (value) => {
      // Check if the value is 'object' and change it to 'Text'
      if (value === 'object') {
          return 'Text';
      }
      if (value === 'datetime64[ns]') {
          return 'Date/Time';
      }
      if (value === 'float64') {
          return 'Decimal Number';
      }
      if (value === 'float32') {
          return 'Decimal Number (Single Precision)';
      }
      if (value === 'int64') {
          return 'Whole Number';
      }
      if (value === 'int32') {
          return 'Whole Number (Standard)';
      }
      if (value === 'bool') {
          return 'True/False';
      }
      if (value === 'category') {
          return 'Category';
      }
      if (value === 'complex') {
          return 'Complex Number';
      }
      return value.toString();
  }


  return (
    <table className="table">
      <thead>
        <tr>
          {Object.keys(data).map((key) => (
            <th key={key}>{key}</th>
          ))}
        </tr>
      </thead>
      <tbody>
        <tr>
          {Object.entries(data).map(([key, value], index) => (
            <td key={index}>
              {/* Use renderValue function to display the value */}
              {renderValue(value)}
              <button onClick={() => setActiveDropdown(key)}>Change Type</button>
              {activeDropdown === key && (
                  <select onChange={(e) => onTypeChange(key, e.target.value)} value={value}>
                      <option value="Object">Object</option>
                      <option value="Text">Text</option>
                      <option value="Whole Number">Whole Number</option>
                      <option value="Whole Number (Standard)">Whole Number (Standard)</option>
                      <option value="Decimal Number">Decimal Number</option>
                      <option value="Decimal Number (Single Precision)">Decimal Number (Single Precision)</option>
                      <option value="True/False">True/False</option>
                      <option value="Date/Time">Date/Time</option>
                      <option value="Time Difference">Time Diff</option>
                      <option value="Category">Category</option>
                      <option value="Complex Number">Complex NUmber</option>
                      {/* Add more types as needed */}
                  </select>
              )}
            </td>
          ))}
        </tr>
      </tbody>
    </table>
  );
};

export default DictionaryTable;
