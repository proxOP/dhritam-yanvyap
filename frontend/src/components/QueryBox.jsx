import React, { useState } from 'react';

export default function QueryBox({ onSubmit, disabled }) {
    const [query, setQuery] = useState('');

    const handleSubmit = (e) => {
        e.preventDefault();
        if (query.trim()) onSubmit(query);
    };

    return (
        <form onSubmit={handleSubmit}>
            <input
                type="text"
                value={query}
                onChange={(e) => setQuery(e.target.value)}
                placeholder="Ask a financial intelligence question..."
                style={{ width: '300px', padding: '10px' }}
                disabled={disabled}
            />
            <button type="submit" style={{ padding: '10px 20px', marginLeft: '10px' }} disabled={disabled}>
                Analyze
            </button>
        </form>
    );
}
