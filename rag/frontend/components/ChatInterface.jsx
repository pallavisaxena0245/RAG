import { useState, useRef, useEffect } from 'react';

export default function ChatInterface({ messages, onSendMessage }) {
  const [input, setInput] = useState('');
  const chatContainerRef = useRef(null);

  useEffect(() => {
    if (chatContainerRef.current) {
      chatContainerRef.current.scrollTop = chatContainerRef.current.scrollHeight;
    }
  }, [messages]);

  const handleSubmit = (e) => {
    e.preventDefault();
    if (input.trim()) {
      onSendMessage(input);
      setInput('');
    }
  };

  return (
    <div style={{ display: 'flex', flexDirection: 'column', height: '500px', width: '400px', border: '1px solid #ccc' }}>
      <div
        ref={chatContainerRef}
        style={{ flex: 1, overflowY: 'auto', padding: '10px' }}
      >
        {messages.map((message, index) => (
          <div
            key={index}
            style={{
              textAlign: message.sender === 'user' ? 'right' : 'left',
              marginBottom: '5px',
            }}
          >
            <span
              style={{
                backgroundColor: message.sender === 'user' ? '#DCF8C6' : '#E5E5EA',
                padding: '8px 12px',
                borderRadius: '10px',
                display: 'inline-block',
                maxWidth: '70%',
                wordWrap: 'break-word',
              }}
            >
              {message.text}
            </span>
          </div>
        ))}
      </div>
      <form onSubmit={handleSubmit} style={{ padding: '10px', borderTop: '1px solid #ccc' }}>
        <input
          type="text"
          value={input}
          onChange={(e) => setInput(e.target.value)}
          placeholder="Type your message..."
          style={{ width: 'calc(100% - 70px)', padding: '8px', borderRadius: '5px', border: '1px solid #ccc' }}
        />
        <button
          type="submit"
          style={{
            padding: '8px 12px',
            borderRadius: '5px',
            backgroundColor: '#0070f3',
            color: 'white',
            border: 'none',
            marginLeft: '10px',
            cursor: 'pointer',
          }}
        >
          Send
        </button>
      </form>
    </div>
  );
}