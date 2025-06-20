// Javascript for main page of website

document.getElementById("go_to_project").onclick = function () {
    //location.href = "http://127.0.0.1:8080/project";
    //location.href = "https://face-prediction-temp.onrender.com/project";
    location.href = "https://huntermitchell.net/project";
};

document.getElementById("go_to_linkedin").onclick = function () {
    window.open(
        'https://www.linkedin.com/in/huntermitchell1/',
        '_blank' // <- This is what makes it open in a new window.
      );
};

document.getElementById("go_to_github").onclick = function () {
    window.open(
        'https://github.com/huntermitchell123/',
        '_blank' // <- This is what makes it open in a new window.
      );
};

document.getElementById("go_to_resume").onclick = function () {
    window.open(
        'https://drive.google.com/file/d/1D0lfGSfUZcxY0g6DRhxzA1_iynyq_Y2Z/view?usp=sharing',
        '_blank' // <- This is what makes it open in a new window.
      );
};
