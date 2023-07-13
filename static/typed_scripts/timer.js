var newYears = "1 Jan 2023";
console.log(newYears)
function countdown() {
    var currentDate = new Date();
    var newYearsDate = new Date(newYears);
    var tseconds = (newYearsDate - currentDate) / 1000;
    var days = Math.floor(tseconds / (3600 * 24));
    var hours = Math.floor(tseconds / 3600) % 24;
    var mins = Math.floor(tseconds / 60) % 60 % 60;
    var seconds = Math.floor(tseconds) % 60;
    document.getElementById("days").innerHTML = formatTime(Math.abs(days));
    document.getElementById("hours").innerHTML = formatTime(Math.abs(hours));
    document.getElementById("mins").innerHTML = formatTime(Math.abs(mins));
    document.getElementById("seconds").innerHTML = formatTime(Math.abs(seconds));
}
var formatTime = function (time) {
    return time < 10 ? "0".concat(time) : "".concat(time);
};
countdown();
setInterval(countdown, 1000);