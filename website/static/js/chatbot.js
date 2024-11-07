document.addEventListener('DOMContentLoaded', function () {
    const chatbotIcon = document.querySelector('.chatbot');
    const chatWindow = document.querySelector('.chat-window');
    const closeChat = document.querySelector('.close-chat');
    const sendButton = document.querySelector('.chat-send');
    const chatInput = document.querySelector('.chat-input');
    const chatMessages = document.querySelector('.chat-messages');

    // Function to append messages to the chat window
    function appendMessage(sender, message) {
        const messageDiv = document.createElement('div');
        messageDiv.classList.add(sender === 'user' ? 'user-message' : 'bot-message');
        messageDiv.textContent = message;
        chatMessages.appendChild(messageDiv);
        chatMessages.scrollTop = chatMessages.scrollHeight;  
    }

    // Function to handle user input
    function handleUserInput() {
        const userMessage = chatInput.value.trim().toLowerCase();

        if (userMessage) {
            appendMessage('user', userMessage);

            if (userMessage.includes('hello') || userMessage.includes('hi')) {
                appendMessage('bot', 'Hello! I am Copilot, your virtual assistant. How can I help you today?');
            } else if (userMessage.includes('properties')) {
                appendMessage('bot', 'Redirecting you to the properties...');
                setTimeout(() => {
                    window.location.href = '/properties';  
                }, 2000);  
            } else if (userMessage.includes('pune')) {
                appendMessage('bot', 'Redirecting you to the Pune properties...');
                setTimeout(() => {
                    window.location.href = '/pune_etc';  
                }, 2000);  
            } else if (userMessage.includes('mumbai')) {
                appendMessage('bot', 'Redirecting you to the Mumbai properties...');
                setTimeout(() => {
                    window.location.href = '/mumbai';  
                }, 2000);
            } else if (userMessage.includes('delhi')) {
                appendMessage('bot', 'Redirecting you to the Delhi properties...');
                setTimeout(() => {
                    window.location.href = '/delhi';  
                }, 2000);
            } else if (userMessage.includes('villa')) {
                appendMessage('bot', 'Redirecting you to villa properties...');
                setTimeout(() => {
                    window.location.href = '/villa';  
                }, 2000);
            } else if (userMessage.includes('vizag')) {
                appendMessage('bot', 'Redirecting you to vizag properties...');
                setTimeout(() => {
                    window.location.href = '/prop_vizag';  
                }, 2000);
            } else if (userMessage.includes('help')) {
                appendMessage('bot', 'I can help you with property searches, navigating to specific locations, and more. Just type "properties" or ask about specific locations.');
            } else {
                appendMessage('bot', 'Sorry, I don’t understand that. Please enter a valid location (e.g., Pune, Mumbai, Delhi) or type "help" for assistance.');
            }

            chatInput.value = '';  // Clear input field
        }
    }

    // Open chat window and send initial greeting
    chatbotIcon.addEventListener('click', () => {
        chatWindow.style.display = 'flex';
        // Send a greeting message when the chat window opens
        setTimeout(() => {
            appendMessage('bot', 'Hello! I am Copilot, your virtual assistant. How can I help you today?');
        }, 500);
    });

    // Close chat window
    closeChat.addEventListener('click', () => {
        chatWindow.style.display = 'none';
    });

    // Event listener for send button
    sendButton.addEventListener('click', handleUserInput);

    // Event listener for pressing Enter key
    chatInput.addEventListener('keydown', function (e) {
        if (e.key === 'Enter') {
            handleUserInput();
        }
    });
});



// const properties = [
//     {name: "Luxury Apartment", location: "Pune", price: "₹1.5 Crore", url: "{{ url_for('views.pune') }}"},
//     {name: "Penthouse Suite", location: "Mumbai", price: "₹5.5 Crore", url: "{{ url_for('views.mumbai') }}"},
//     {name: "Modern Villa", location: "Hyderabad", price: "₹3 Crore", url: "{{ url_for('views.vizag') }}"},
//     // Add more properties with the correct URL mappings here...
// ];

// document.getElementById("search-form").addEventListener("submit", function(event) {
//     event.preventDefault();  // Prevent form submission
//     searchProperties();
// });

// function searchProperties() {
//     let input = document.getElementById("search-input").value.trim().toLowerCase();

//     // Check if input is empty
//     if (!input) {
//         alert("Please enter a search term.");
//         return;  // Exit the function if input is empty
//     }

//     let matchedProperty = properties.find(property => 
//         property.name.toLowerCase().includes(input) || 
//         property.location.toLowerCase().includes(input)
//     );

//     if (matchedProperty) {
//         // Redirect to the property's page if a match is found
//         window.location.href = matchedProperty.url;
//     } else {
//         alert("No properties found");  // Show an alert if no matches found
//     }
// }

    