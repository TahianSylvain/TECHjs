var body = document.body;
var header = document.querySelector('header');
var footer = document.querySelector('footer');
var searchButton = document.getElementById('searchButton');
var darkModeToggle = document.getElementById('darkModeToggle');
searchButton.addEventListener('click', function () {
    // Perform search functionality here
    console.log('Search button clicked');
});


function toggleDarkMode() {
  var body = document.querySelector('body');
  body.classList.toggle('dark-mode');

  var side = document.querySelector('div.sidebar');
  side.classList.toggle('dark-side'); // the side bar items are now desorganized, How to arrange that?
  if (side.classList.contains('dark-side')){
    document.querySelector('.logo').style.backgroundColor="#333";
    side.style.backgroundColor="#1b1a1a";
  } else {
    document.querySelector('.logo').style.backgroundColor="#007bff";
    side.style.backgroundColor="#f1f1f1";
  }
}
// ---------LoginSignUP-----------
// Get the login and signup buttons
var loginButton = document.querySelector('a[href="https://tahiansylvain.pythonanywhere.com/auth/login/"]');
var signupButton = document.querySelector('a[href="https://tahiansylvain.pythonanywhere.com/auth/signup/"]');

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
