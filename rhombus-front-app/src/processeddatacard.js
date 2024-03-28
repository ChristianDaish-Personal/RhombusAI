//This component is used for displaying the processed information
import React from 'react';
import { Card, CardContent, Typography } from '@mui/material';
import DictionaryTable from './dictionarytotable';

function Processeddatacard({ data, onTypeChange }) {
    return (
        <Card style={{ margin: '20px' }}>
            <CardContent>
                <Typography color="textSecondary" gutterBottom>
                    Processed Data
                </Typography>
                {/* Use DictionaryTable component to display data */}
                <DictionaryTable data={data} onTypeChange={onTypeChange} />
            </CardContent>
        </Card>
    );
}
export default Processeddatacard;