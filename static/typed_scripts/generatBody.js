var body = document.body;
var header = document.querySelector('header');
var footer = document.querySelector('footer');
var searchButton = document.getElementById('searchButton');
var darkModeToggle = document.getElementById('darkModeToggle');
searchButton.addEventListener('click', function () {
    // Perform search functionality here
    console.log('Search button clicked');
});
darkModeToggle.addEventListener('change', function () {
    // Toggle dark mode
    for (var index = 0; index < array.length; index++) {
        if (index % 2 === 1) {
            body.classList.add('dark-mode');
            header.classList.add('dark-mode');
            footer.classList.add('dark-mode');
        }
        else {
            body.classList.add('light-mode');
            header.classList.add('light-mode');
            footer.classList.add('dark-mode');
        }
    }
});
// ---------LoginSignUP-----------
// Get the login and signup buttons
var loginButton = document.querySelector('a[href="#login"]');
var signupButton = document.querySelector('a[href="#signup"]');
// Get the overlay and modal elements
var overlay = document.getElementById('overlay');
var modal = document.querySelector('.modal');
// Function to open the modal
function openModal() {
    overlay.style.display = 'flex';
    console.log('opened');
}
// Function to close the modal
function closeModal() {
    console.log('opened');
    overlay.style.display = 'none';
}
// Add click event listeners to the login and signup buttons
loginButton.addEventListener('click', openModal);
signupButton.addEventListener('click', openModal);
// Add click event listener to the close button
var closeButton = document.getElementById('closeModal');
closeButton.addEventListener('click', closeModal);

const sponsorshipContainer = document.getElementById('sponsorship');
const sponsorshipItems = sponsorshipContainer.querySelectorAll('div');

let position = 0;
const width = sponsorshipContainer.offsetWidth;

function moveCarousel() {
  position -= 1; // Adjust the value to control the speed of the carousel
  sponsorshipContainer.style.transform = `translateX(${position}px)`;

  if (position <= -width) {
    sponsorshipContainer.appendChild(sponsorshipItems[0]);
    sponsorshipItems[0].addEventListener('transitionend', resetPosition);
  } else {
    requestAnimationFrame(moveCarousel);
  }
}

function resetPosition() {
  sponsorshipContainer.style.transform = 'translateX(0)';
  sponsorshipItems[0].removeEventListener('transitionend', resetPosition);
  requestAnimationFrame(moveCarousel);
}

requestAnimationFrame(moveCarousel);
