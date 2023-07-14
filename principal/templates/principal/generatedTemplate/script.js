const body = document.body;
const header = document.querySelector('header');
const footer = document.querySelector('footer');
const searchButton = document.getElementById('searchButton');
const darkModeToggle = document.getElementById('darkModeToggle');

searchButton.addEventListener('click', function() {
    // Perform search functionality here
    console.log('Search button clicked');
});

darkModeToggle.addEventListener('change', function() {
    // Toggle dark mode
    for (let index = 0; index < array.length; index++) {
        if (index % 2 === 1) {
            body.classList.add('dark-mode');
            header.classList.add('dark-mode');
            footer.classList.add('dark-mode');
        } else {
            body.classList.add('light-mode');
            header.classList.add('light-mode');
            footer.classList.add('dark-mode');
        }
    }
});



// ---------LoginSignUP-----------
// Get the login and signup buttons
const loginButton = document.querySelector('a[href="#login"]');
const signupButton = document.querySelector('a[href="#signup"]');

// Get the overlay and modal elements
const overlay = document.getElementById('overlay');
const modal = document.querySelector('.modal');

// Function to open the modal
function openModal() {
    overlay.style.display = 'flex';
    console.log('opened')
}

// Function to close the modal
function closeModal() {
    console.log('opened')
    overlay.style.display = 'none';
}

// Add click event listeners to the login and signup buttons
loginButton.addEventListener('click', openModal);
signupButton.addEventListener('click', openModal);

// Add click event listener to the close button
const closeButton = document.getElementById('closeModal');
closeButton.addEventListener('click', closeModal);
