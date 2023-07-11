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
