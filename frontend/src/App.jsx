import React, { useState, useEffect } from 'react';
import QueryBox from './components/QueryBox';
import ResultView from './components/ResultView';
import ReasoningView from './components/ReasoningView';
import { sendQuery, getGraphState } from './api';

function App() {
    const [traceId, setTraceId] = useState(null);
    const [status, setStatus] = useState('idle');
    const [result, setResult] = useState(null);
    const [reasoning, setReasoning] = useState(null);

    const handleQuery = async (query) => {
        setStatus('submitting');
        setResult(null);
        setReasoning(null);
        try {
            const data = await sendQuery(query);
            setTraceId(data.reasoning_trace_id);
            setStatus('polling');
        } catch (e) {
            console.error(e);
            setStatus('error');
        }
    };

    useEffect(() => {
        if (status === 'polling' && traceId) {
            const interval = setInterval(async () => {
                const data = await getGraphState(traceId);
                if (data.status === 'completed') {
                    setResult(data.result);
                    setReasoning(data.full_state);
                    setStatus('completed');
                    clearInterval(interval);
                }
            }, 2000);
            return () => clearInterval(interval);
        }
    }, [status, traceId]);

    return (
        <div style={{ padding: '20px', fontFamily: 'Arial, sans-serif' }}>
            <h1>Dritam AI Intelligence</h1>
            <QueryBox onSubmit={handleQuery} disabled={status === 'polling' || status === 'submitting'} />
            {status === 'polling' && <p>Thinking...</p>}
            {status === 'completed' && (
                <div style={{ display: 'flex', gap: '20px', marginTop: '20px' }}>
                    <div style={{ flex: 1 }}>
                        <ResultView data={result} />
                    </div>
                    <div style={{ flex: 1 }}>
                        <ReasoningView data={reasoning} />
                    </div>
                </div>
            )}
        </div>
    );
}

export default App;
