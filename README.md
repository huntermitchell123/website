# Web App

This is the complete repository of my web app that is currently deployed to the world via Render at https://huntermitchell.net/. 
The web app contains a home page and a project page which allows you to take a picture of yourself through webcam, 
and then uses machine learning on the backend to predict both your age and gender. Both models were trained using Google Colab.
The repo for that work is available at https://github.com/huntermitchell123/Face_Prediction/tree/main.

To replicate something like this, it is highly recommended to use Docker, as that makes the distribution much easier.
I also realized that using Tensorflow Lite uses a lot less memory and disk space for the face prediction model.
I'm hosting with Render because it's the only free service which provides custom domains and SSL, which is needed for the web app.
Since it's being hosted for free, the only downside is that the app will autoscale down after a certain time period when no one is actively using it. If this is the case, it should spin up in 10-15 seconds.

For the routing to work correctly, I have Render using the domain huntermitchell.net instead of www.huntermitchell.net. Render will
automatically add a redirect from the www domain. I also have all the routing in the code use huntermitchell.net. And in my domain provider (NameCheap),
I have an extra redirect from www.huntermitchell.net to huntermitchell.net. If I don't have all of this, the main bug that I've encountered
is a CORS error like "Access to XMLHttpRequest at 'https://huntermitchell.net/project' from origin 'https://www.huntermitchell.net' has been blocked by CORS policy: No 'Access-Control-Allow-Origin' header is present on the requested resource." when trying to predict age or gender, which leads you to believe the error is more complicated than simple DNS routing.
