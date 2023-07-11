
const newYears = "July 27, 2023, midnight"//"1 Jan 2023";


function countdown() {
    const currentDate = new Date();
    const newYearsDate = new Date(newYears);
    console.log(newYearsDate)

    const tseconds = (newYearsDate - currentDate) / 1000;

    const days = Math.floor(tseconds/(3600 * 24))
    const hours = Math.floor(tseconds/3600) % 24
    const mins = Math.floor(tseconds/60) % 60 % 60
    const seconds = Math.floor(tseconds) % 60

    document.getElementById("days").innerHTML = formatTime(Math.abs(days))
    document.getElementById("hours").innerHTML = formatTime(Math.abs(hours))
    document.getElementById("mins").innerHTML = formatTime(Math.abs(mins))
    document.getElementById("seconds").innerHTML = formatTime(Math.abs(seconds))
}

const formatTime = (time) => {
    return time < 10 ? `0${time}`: `${time}`;
}

countdown();
setInterval(countdown, 1000)

// -----------------||--------------------

function countTime() {
    const currentDate = new Date();
    
    // document.getElementById("day").innerHTML = currentDate.getDate()
    document.getElementById("hour").innerHTML = currentDate.getHours() 
    document.getElementById("min").innerHTML = currentDate.getMinutes()
    document.getElementById("second").innerHTML = formatTime(currentDate.getSeconds())
}

countTime();
setInterval(countTime, 1000)