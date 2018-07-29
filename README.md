CameraStore Python/Flask sample application
===========================================

This is a demonstration of using Tradenity SDK with Flask to build ecommerce web application

This sample application is free and opensource, we encourage you to fork it and use it as a base for your future applications.

To run it on your local machine:

## Prerequisites

-  Python 2.7

## Get the application

Choose one of the following:

- Download the source code.
- Clone `git clone git@github.com:tradenity/camerastore-python-flask-sample.git`
- Fork this repository

## Edit Credentials

Open main.py, modify this line: 

`Tradenity.API_KEY = 'sk_xxxxxxxxxxxxxxxxx'` 

to reflect your store's API key

If you configured your store to use stripe for payment processing, then edit this line:

`STRIPE_PUBLIC_KEY = 'pk_xxxxxxxxxxxxxxxxxxxxxxxxxx'` to reflect your public key.

## Install requirements

`pip install -r requirements.txt`


## Run

python main.py

## Documentation & Explanation

Refer to this [tutorial](http://docs.tradenity.com/kb/tutorials/python/flask/)
on our knowledge base for full explanation of the source code