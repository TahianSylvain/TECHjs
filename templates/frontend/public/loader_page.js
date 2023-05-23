document.onreadystatechange = function () {

    if (document.readyState !== "complete") {
        document.querySelector("#root").style.visibility = "hidden";
        document.querySelector(".ring").style.display = "fixed";
    }
    //ifelse (api.fetching){}
    else {
        var i = 0;
        while (i < 2000000000){
            if (i == 1999999999) {
                this.documentElement.querySelector("body").style.background = "#eeeeeb";
                document.querySelector(".ring").style.visibility = "hidden";
                document.querySelector(".ring").style.display = "none";
                document.querySelector("#root").style.visibility = "visible";
                break
            } else {
                i++
            }
        };
    }
};
/* window.addEventListener("load", () => {}*/
