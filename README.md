# Web App

This is the complete repository of my web app that is currently deployed to the world via Render at https://huntermitchell.net/. 
The web app contains a home page and a project page which allows you to take a picture of yourself through webcam, 
and then uses machine learning on the backend to predict both your age and gender. Both models were trained using Google Colab.
The repo for that work is available at https://github.com/huntermitchell123/Face_Prediction/tree/main.

To replicate something like this, it is highly recommended to use Docker, as that makes the distribution much easier.
I also realized that using Tensorflow Lite uses a lot less memory and disk space for the face prediction model.
I'm hosting with Render because it's the only free service which provides custom domains and SSL, which is needed for the web app.
