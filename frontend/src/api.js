// api.js

export const sendQuery = async (query) => {
    const response = await fetch('/v1/query', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ query }),
    });
    return response.json();
};

export const getGraphState = async (traceId) => {
    const response = await fetch(`/v1/graph/${traceId}`);
    return response.json();
};
