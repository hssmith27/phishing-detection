import { useState } from 'react'

interface PredictionResponse {
    probability: number;
}

const EmailForm = () => {
    const [subject, setSubject] = useState('')
    const [body, setBody] = useState('')
    const [probability, setProbability] = useState(0)

    const handleSubmit = async (e: React.FormEvent<HTMLFormElement>) => {
        e.preventDefault();
        
        const response = await fetch('http://127.0.0.1:5000/predict', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json'},
            body: JSON.stringify({subject, body})
        });
        const data = await response.json();
        setProbability(data['probability'])
    }

    return (
        <div>
            <form onSubmit = {handleSubmit}>
                <label>Email Subject:</label>
                <input
                    type = 'text'
                    required
                    value = {subject}
                    onChange={(e) => setSubject(e.target.value)}
                />
                <label>Email Body:</label>
                <input
                    type = 'text'
                    required
                    value = {body}
                    onChange={(e) => setBody(e.target.value)}
                />
                <button type='submit'>Submit</button>
            </form>
            <h2>{probability}</h2>
        </div>
    )
}

export default EmailForm;