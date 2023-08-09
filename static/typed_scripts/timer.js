function countdown() {
    var currentDate = new Date();
    var hours = Math.floor((currentDate / 1000) / 3600) % 24;
    var mins = Math.floor((currentDate / 1000) / 60) % 60 % 60;
    var seconds = Math.floor((currentDate / 1000)) % 60;

    hours = (hours + 3) % 24;
    document.getElementById("hours").innerHTML = formatTime(Math.abs(hours));
    document.getElementById("mins").innerHTML = formatTime(Math.abs(mins));
    document.getElementById("seconds").innerHTML = formatTime(Math.abs(seconds));
}
var formatTime = function (time) {
    return time < 10 ? "0".concat(time) : "".concat(time);
};
countdown();
setInterval(countdown, 1000);