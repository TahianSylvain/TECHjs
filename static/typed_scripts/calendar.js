var daysTag = document.querySelector(".days"), currentDate = document.querySelector(".current-date"), prevNextIcon = document.querySelectorAll(".icons span");
// getting new date, current year and month
var date = new Date(), currDay = date.getDay();
currYear = date.getFullYear();
currMonth = date.getMonth();
// storing full name of all months in array
var months = ["January", "February", "March", "April", "May", "June", "July",
    "August", "September", "October", "November", "December"];
var renderCalendar = function () {
    var firstDayofMonth = new Date(currYear, currMonth, 1).getDay(), // getting first day of month
    lastDateofMonth = new Date(currYear, currMonth + 1, 0).getDate(), // getting last date of month
    lastDayofMonth = new Date(currYear, currMonth, lastDateofMonth).getDay(), // getting last day of month
    lastDateofLastMonth = new Date(currYear, currMonth, 0).getDate(); // getting last date of previous month
    var liTag = "";
    for (var i = firstDayofMonth; i > 0; i--) { // creating li of previous month last days
        liTag += "\n                <li class=\"inactive\">\n                        ".concat(lastDateofLastMonth - i + 1, "\n                </li>");
    }
    for (var i = 1; i <= lastDateofMonth; i++) { // creating li of all days of current month
        // adding active class to li if the current day, month, and year matched
        var isToday = i === date.getDate() && currMonth === new Date().getMonth()
            && currYear === new Date().getFullYear() ? "active" : "";
        liTag += "\n        <li class=\"".concat(isToday, "\">\n            <a style=\"none\" href=\"http://localhost:3333/journey/on").concat(currYear, "-").concat(currMonth + 1, "-").concat(i, "\">\n                ").concat(i, "\n            </a>\n        </li>");
    }
    for (var i = lastDayofMonth; i < 6; i++) { // creating li of next month first days
        liTag += "\n            <li class=\"inactive\">\n                    ".concat(i - lastDayofMonth + 1, "\n            </li>");
    }
    currentDate.innerText = "".concat(months[currMonth], ", ").concat(currDay, " ").concat(currYear); // passing current mon and yr as currentDate text
    daysTag.innerHTML = liTag;
};
renderCalendar();
prevNextIcon.forEach(function (icon) {
    icon.addEventListener("click", function () {
        // if clicked icon is previous icon then decrement current month by 1 else increment it by 1
        currMonth = icon.id === "prev" ? currMonth - 1 : currMonth + 1;
        if (currMonth < 0 || currMonth > 11) { // if current month is less than 0 or greater than 11
            // creating a new date of current year & month and pass it as date value
            date = new Date(currYear, currMonth, new Date().getDate());
            currYear = date.getFullYear(); // updating current year with new date year
            currMonth = date.getMonth(); // updating current month with new date month
        }
        else {
            date = new Date(); // pass the current date as date value
        }
        renderCalendar(); // calling renderCalendar function
    });
});
