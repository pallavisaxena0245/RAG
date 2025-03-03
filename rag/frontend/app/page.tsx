import { useState } from 'react';
import ChatInterface from '@/components/ChatInterface';

export default function Home() {
  const [messages, setMessages] = useState([]);

  const handleSendMessage = async (message) => {
    setMessages([...messages, { text: message, sender: 'user' }]);
    try {
      const response = await fetch('/api/query', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ query: message }),
      });
      const data = await response.json();
      setMessages((prevMessages) => [
        ...prevMessages,
        { text: data.response, sender: 'bot' },
      ]);
    } catch (error) {
      console.error('Error querying:', error);
      setMessages((prevMessages) => [
        ...prevMessages,
        { text: 'Error processing your query.', sender: 'bot' },
      ]);
    }
  };

  return (
    <div>
      <h1>Chat with Documents</h1>
      <ChatInterface messages={messages} onSendMessage={handleSendMessage} />
    </div>
  );
}