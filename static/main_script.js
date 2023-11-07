// Hunter Mitchell - 6/30/20

// javascript for main page of website  :)


document.getElementById("go_to_project").onclick = function () {
    location.href = "http://127.0.0.1:8080/project";
    //location.href = "https://huntermitchell.net/project";
};

document.getElementById("go_to_linkedin").onclick = function () {
    //location.href = "https://www.linkedin.com/in/huntermitchell1/";
    window.open(
        'https://www.linkedin.com/in/huntermitchell1/',
        '_blank' // <- This is what makes it open in a new window.
      );
};

document.getElementById("go_to_github").onclick = function () {
    //location.href = "https://github.com/huntermitchell123/";
    window.open(
        'https://github.com/huntermitchell123/',
        '_blank' // <- This is what makes it open in a new window.
      );
};

document.getElementById("go_to_apps").onclick = function () {
    //location.href = "https://apps.apple.com/us/developer/hunter-mitchell/id1450700638";
    window.open(
        'https://apps.apple.com/us/developer/hunter-mitchell/id1450700638',
        '_blank' // <- This is what makes it open in a new window.
      );
};
