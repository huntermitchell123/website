// Javascript for Face Prediction part of website - partially from https://github.com/mdn/samples-server/blob/master/s/webrtc-capturestill/capture.js

var width = 320;    // We will scale the photo width to this
var height = 320;     // This will be computed based on the input stream

var streaming = false;

var video = null;
var canvas = null;
var photo = null;
var startbutton = null;

var male_prob = null;
var female_prob = null;


function startup() {
    //console.log('starting up!');

    video = document.getElementById('video');
    canvas = document.getElementById('canvas');
    photo = document.getElementById('photo');
    startbutton = document.getElementById('startbutton');

    navigator.mediaDevices.getUserMedia({ video: { width: { exact: width }, height: { exact: height } }, audio: false })
        .then(function (stream) {
            video.srcObject = stream;
            video.play();
        })
        .catch(function (err) {
            console.log("An error occurred: " + err);
        });

    video.addEventListener('canplay', function (ev) {
        if (!streaming) {
            video.setAttribute('width', width);
            video.setAttribute('height', height);
            canvas.setAttribute('width', width);
            canvas.setAttribute('height', height);
            streaming = true;
        }
    }, false);

    startbutton.addEventListener('click', function (ev) {
        takepicture();
        ev.preventDefault();
    }, false);

    clearphoto();
}

function clearphoto() {
    var context = canvas.getContext('2d');
    context.fillStyle = "#AAA";
    context.fillRect(0, 0, canvas.width, canvas.height);

    var data = canvas.toDataURL('image/png');
}

function takepicture() {
    var context = canvas.getContext('2d');
    if (width && height) {
        canvas.width = width;
        canvas.height = height;
        context.drawImage(video, 0, 0, width, height);

        var data = canvas.toDataURL('image/png');
    } else {
        clearphoto();
    } 
} 
window.addEventListener('load', startup, false);



var script = document.createElement('script');
script.src = 'https://code.jquery.com/jquery-3.4.1.min.js';
script.type = 'text/javascript';
document.getElementsByTagName('head')[0].appendChild(script);

predictGenderButton.addEventListener('click', function (ev) {
    predictGender();
    ev.preventDefault();
}, false);

function predictGender() {

    var dataURL = canvas.toDataURL('image/png');

    //communicate to server  ~~~ https://stackoverflow.com/questions/41957490/send-canvas-image-data-uint8clampedarray-to-flask-server-via-ajax

    $.ajax({
        type: "POST",
        //url: "http://127.0.0.1:8080/project",
        //url: "https://face-prediction-temp.onrender.com/project",
        url: "https://www.huntermitchell.net/project",
        data:{imageBase64: dataURL, predType: 'gender'},
        success:function(response){ 
            //console.log(response)
            $('<h5>'+response+'</h5>').replaceAll('h5'); 
        }
    }).done(function () {
        console.log('sent');
    });
}

predictAgeButton.addEventListener('click', function (ev) {
    predictAge();
    ev.preventDefault();
}, false);

function predictAge() {

    var dataURL = canvas.toDataURL('image/png');

    //communicate to server  ~~~ https://stackoverflow.com/questions/41957490/send-canvas-image-data-uint8clampedarray-to-flask-server-via-ajax

    $.ajax({
        type: "POST",
        //url: "http://127.0.0.1:8080/project",
        //url: "https://face-prediction-temp.onrender.com/project",
        url: "https://www.huntermitchell.net/project",
        data:{imageBase64: dataURL, predType: 'age'},
        success:function(response){ 
            //console.log(response)
            $('<h4>'+response+'</h4>').replaceAll('h4'); 
        }
    }).done(function () {
        console.log('sent');
    });
}

document.getElementById("go_to_home").onclick = function () {
    //location.href = "http://127.0.0.1:8080/";
    //location.href = "https://face-prediction-temp.onrender.com/";
    location.href = "https://www.huntermitchell.net/";
};