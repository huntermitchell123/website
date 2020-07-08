# webApp

Hunter Mitchell - 07/08/20

This is the complete repository for my first web app that is currently deployed to the world via AWS. 
The web app contains a home page and a project page which allows you to take a picture of yourself, 
and then uses machine learning models to predict both your age and gender. Both models are pre-trained on Kaggle notebooks, 
so I am including the code for that as well. 

To replicate this, you will need to have Docker installed, as that made the Elastic Beanstalk transition much smoother.
Also, the images and javascript/CSS files will need to be in a static folder, since Flask looks for them there. 
Lastly, the HTML files will need to be in a folder labeled 'templates'.
