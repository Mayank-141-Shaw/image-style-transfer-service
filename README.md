# Style-Transfer-GAN-microservice

## Table of Contents

1. [Introduction](#introduction)
2. [Running](#running)

## Introduction

Neural style transfer is an optimization technique used to take two images - a content image and a style reference image (such as an artwork by a famous painter) - and blend them together so the output image looks like the content image, but “painted” in the style of the style reference image.

This is implemented by optimizing the output image to match the content statistics of the content image and the style statistics of the style reference image. These statistics are extracted from the images using a convolutional network.

This is our attempt to utilize the Style Transfer GAN model built by Google and implement it in a microservice to create a service for end users, to be able to access it like a feature

## Running:

To run the service, please clone this repository, and then go inside the project directory

For running it locally, one must have python pre-installed in their system

Then follow the steps to effectively run this service

1.  Must start a virtual environment, for that first do:
    ## pip install pipenv
2.  Then create a virtual env:
    ## python -m venv env-name
3.  After the env is created write a command to activate the environment
    ## env-name\Scripts\activate.bat ### for other than windows
        OR
    ## env-name\Scripts\Activate.ps1 ### for windows
4.  Install the requirements using
    ## pip install -r requirements.txt
5.  After the setup, use the following to start the service
    ## python -m uvicorn main:app --reload

Now the service should be running at localhost:8000

## Endpoints:

1. ( path="/",
   type="POST",
   parameters = {
   content_image : Any (image file), // the image you want to convert
   style_image : Any (image_file) // the image style you wouls like to use
   },
   return={ image oject in jpg format } ) ==> Use this endpoint for accesing the service. It requires you to pass two image files as query parameters (one the sty) and returns the generated image.
