
const newYears = document.getElementById('invisible').innerHTML //"27 July 2023"//"1 Jan 2023";
console.log(newYears)

function countdown() {
    const currentDate = new Date();
    const newYearsDate = new Date(newYears, );

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
// -----------------||--------------------
function countTime() {
    var currentDate = new Date();
    // document.getElementById("day").innerHTML = currentDate.getDate()
    document.getElementById("hour").innerHTML = currentDate.getHours();
    document.getElementById("min").innerHTML = currentDate.getMinutes();
    document.getElementById("second").innerHTML = formatTime(currentDate.getSeconds());
}
countTime();
setInterval(countTime, 1000);
