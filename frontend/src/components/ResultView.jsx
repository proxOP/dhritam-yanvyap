import React from 'react';

export default function ResultView({ data }) {
    return (
        <div style={{ border: '1px solid #ccc', padding: '15px', borderRadius: '5px' }}>
            <h2>Intelligence Result</h2>
            <pre style={{ whiteSpace: 'pre-wrap', background: '#f5f5f5', padding: '10px' }}>
                {JSON.stringify(data, null, 2)}
            </pre>
        </div>
    );
}
