// Get the input box and chat area elements
const inputBox = document.getElementById('user-input');
const chatWindow = document.getElementById('chat-window');

// Event listener for form submission
document.getElementById('send-btn').addEventListener('click', submitQuery);

// Event listener for Enter key press
inputBox.addEventListener('keydown', (e) => {
  if (e.key === 'Enter' && !e.shiftKey) {
    e.preventDefault(); // Prevent the default behavior of submitting the form
    submitQuery();
  }
});

// Function to submit the user's query
function submitQuery() {
  // Get the user query from the input box
  const query = inputBox.value.trim();

  if (query !== '') {
    // Create a JSON object with the query
    const data = {
      query: query
    };

    // Update the chat window with the user query
    updateChat(query, 'You');

    // Send a POST request to the Flask route
    axios.post('/query', data)
      .then(response => {
        // Process the response and update the chat window with the bot's answer
        const answer = response.data.answer;

        // Simulate typing effect for the bot's response
        simulateTyping(answer);
      })
      .catch(error => console.error('Error:', error));

    // Clear the input box
    inputBox.value = '';
  }
}

// Function to simulate typing effect
function simulateTyping(message) {
  // Delay before starting the typing effect
  const delayBeforeTyping = 800;

  // Delay between typing each character
  const typingDelay = 5;

  // Update the chat window with the bot typing message
  updateChat('', 'ChatBot');

  // Simulate typing effect for the bot's response
  setTimeout(() => {
    let currentCharacter = 0;
    const typingInterval = setInterval(() => {
      if (currentCharacter < message.length) {
        // Append the next character to the bot's response
        const nextCharacter = message.charAt(currentCharacter);
        const typingMessage = document.querySelector('.bot-message.typing');
        typingMessage.textContent += nextCharacter;
        currentCharacter++;
      } else {
        // Stop the typing effect
        clearInterval(typingInterval);

        // Remove the "typing" class from the bot's response
        const typingMessage = document.querySelector('.bot-message.typing');
        typingMessage.classList.remove('typing');
      }
    }, typingDelay);
  }, delayBeforeTyping);
}

// Function to update the chat window
function updateChat(message, sender) {
  let messageClass = '';

  if (sender === 'You') {
    messageClass = 'user-message';
  } else if (sender === 'ChatBot') {
    messageClass = 'bot-message typing'; // Add the "typing" class for bot's typing effect
  }

  const chatMessage = `<div class="${messageClass}"><strong>${sender.charAt(0).toUpperCase() + sender.slice(1)}:</strong> ${message}</div>`;

  // Append the user message or bot's answer to the chat window
  chatWindow.innerHTML += chatMessage;

  // Scroll to the bottom of the chat window
  chatWindow.scrollTop = chatWindow.scrollHeight;
}
