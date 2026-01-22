import React from 'react';

export default function ReasoningView({ data }) {
    return (
        <div style={{ border: '1px solid #eee', padding: '15px', borderRadius: '5px' }}>
            <h3>Reasoning Trace</h3>
            <div style={{ maxHeight: '400px', overflowY: 'auto', fontSize: '0.9em' }}>
                {data && Object.keys(data).map(key => (
                    <div key={key} style={{ marginBottom: '10px' }}>
                        <strong>{key}:</strong>
                        <div style={{ marginLeft: '10px', color: '#555' }}>
                            {typeof data[key] === 'object' ? JSON.stringify(data[key]).substring(0, 100) + '...' : String(data[key])}
                        </div>
                    </div>
                ))}
            </div>
        </div>
    );
}
