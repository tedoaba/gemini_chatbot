document.addEventListener('DOMContentLoaded', function() {
    const messageInput = document.getElementById('message-input');
    const chatMessages = document.querySelector('.chat-messages');
    const chatForm = document.getElementById('chat-form');


    chatForm.addEventListener('submit', function(event) {
        event.preventDefault(); // prevent default form submission
        const message = messageInput.value.trim();
        if (message) {
            sendMessage(message);
            messageInput.value = '';
        }
    });

    function sendMessage(message) {
        appendMessage(message, 'user');
        fetch('/chat', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ message: message }),
        })
        .then(response => response.json())
        .then(data => {
            appendMessage(data.response, 'bot');
        })
        .catch(error => {
            console.error('Error:', error);
            appendMessage("Error processing your message", 'bot');
        });
    }

    function appendMessage(message, sender) {
      const messageDiv = document.createElement('div');
        messageDiv.classList.add('message', `${sender}-message`);
        messageDiv.textContent = message;
        chatMessages.appendChild(messageDiv);
        chatMessages.scrollTop = chatMessages.scrollHeight; // Scroll to bottom
    }
    const clearButton = document.getElementById('clear-button');
        clearButton.addEventListener('click', function() {
            fetch('/clear', {
                method: 'POST',
            })
            .then(response => {
                if (response.ok) {
                  chatMessages.innerHTML = ''; // Clear the chat UI
                }
            })
            .catch(error => {
                console.error('Error clearing chat:', error);
            });
        });
});