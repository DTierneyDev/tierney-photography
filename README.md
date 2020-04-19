# Tierney Photography [![Build Status](https://travis-ci.org/Cobonkoi/tierney-photography.svg?branch=master)](https://travis-ci.org/Cobonkoi/tierney-photography)

Welcome to Tierney Photography. This is the official website for the photographer, Tierney.

Using this website you will learn more about him as a person, see examples of his work and be able to buy his photosets for your own use.

The goals of this site are to:
- Allow users to learn more about the photographer, Tierney.
- Allow users to see examples of his past works.
- Allow the owner of the site to login and upload/edit photosets to sell.
- Allow users to register/login so that they can access the full features of the site.
- Allow users to buy photosets from him, and download them to use as they wish.

## Demo

A demo can be viewed on Heroku [here](https://tierney-photography.herokuapp.com/).

Superuser login details are below:  
User: admin  
Password: Ph0toP4ck$  
  
Stripe is in test mode so you can use any of the test card numbers from their documentation.  
4242 4242 4242 4242 is a valid card. You may use any 3 digits for cvc and a future date for expiry.

## UX

My goal with the design of this site, was to make it look professional.
This was because I wanted people to be able to trust that what they were buying, was of a high quality.

#### User Stories

1. As a new visitor to the site, I want to be able to easily navigate the site, so that I can find what I want easily.
2. As a new visitor to the site, I want to see examples of the owners work, so I can decide whether I want to buy some of it.
3. As a new visitor to the site, I want to learn more about the owner, so that I can decide whether to follow their journey on social media.
4. As a new visitor to the site, I want to be able to register/login to the site, so that I can checkout photosets.
5. As an interested shopper, I want to be able to access the shop and see what is on sale, so that I can browse photosets.
6. As an interested shopper, I want to be able to add photosets to my cart, so that I can purchase more than one at a time.
7. As a purchaser, I want to be able to view and download my past orders, so that I can access the content that I have paid for.
8. As an admin of the website, I want to be able to login to my superuser account, so that I can upload new photosets to the shop.
9. As an admin of the website, I want to be able to login to my superuser account, so that I can edit photosets that have been uploaded.
10. As an admin of the website, I want to be able to see all of the orders that have been made, so that I can see what customers are most interested in.

#### Wireframe Mockups

- [Index - Desktop](wireframes/index-desktop.png).
- [Index - Tablet](wireframes/index-tablet.png).
- [Index - Mobile](wireframes/index-mobile.png).
- [Index - Mobile - Menu Open](wireframes/index-mobile-menuopen.png).
- [Gallery - Desktop](wireframes/gallery-desktop.png).
- [Gallery - Tablet](wireframes/gallery-tablet.png).
- [Gallery - Mobile](wireframes/gallery-mobile.png).
- [Shop - Desktop](wireframes/shop-desktop.png).
- [Shop - Tablet](wireframes/shop-tablet.png).
- [Shop - Mobile](wireframes/shop-mobile.png).
- [Cart - Desktop](wireframes/cart-desktop.png).
- [Cart - Tablet](wireframes/cart-tablet.png).
- [Cart - Mobile](wireframes/cart-mobile.png).
- [About - Desktop](wireframes/about-desktop.png).
- [About - Tablet](wireframes/about-tablet.png).
- [About - Mobile](wireframes/about-mobile.png).
- [Register - Desktop](wireframes/register-desktop.png).
- [Register - Tablet](wireframes/register-tablet.png).
- [Register - Mobile](wireframes/register-mobile.png).
- [Login - Desktop](wireframes/login-desktop.png).
- [Login - Tablet](wireframes/login-tablet.png).
- [Login - Mobile](wireframes/login-mobile.png).
- [Account Details - Desktop](wireframes/accountdetails-desktop.png).
- [Account Details - Tablet](wireframes/accountdetails-tablet.png).
- [Account Details - Mobile](wireframes/accountdetails-mobile.png).
- [Orders - Desktop](wireframes/orders-desktop.png).
- [Orders - Tablet](wireframes/orders-tablet.png).
- [Orders - Mobile](wireframes/orders-mobile.png).
- [Downloads - Desktop](wireframes/downloads-desktop.png).
- [Downloads - Tablet](wireframes/downloads-tablet.png).
- [Downloads - Mobile](wireframes/downloads-mobile.png).

## Features

Each page features a navigation bar with a brand-logo. On mobile this become a toggle navbar.  
I have added a javascript function to highlight the cart green when more than 0 photosets are in it. This is to highlight to the customer that there are items inside their cart, and where to click to see those items.  
The pages also feature a footer with social media links.
 
#### Index

This page features a carousel, which has 2 slides.  
These slides provide information on 2 new features on the site and provide links to the pages.

#### Gallery

This page features a carousel, which has 3 slides.  
These slides show preview pictures/information on upcoming photosets.  
This page also features a button to take you to the shop.

#### Shop

This page features cards containing all of the details of each photoset that is for sale.  
You can use the add to cart button to add these sets to your cart, as well as click elsewhere on the card to be taken to a page with more details.

#### Shop-Details

This page features the card of the photoset you clicked from the shop.  
Unlike the shop, this shows the full description.

#### About

This page features 2 sections of information to learn about the website/owner.

#### Login

This page contains a login form that will log a user into the website.  
There is also a link to the registration page, for if the user doesn't yet have an account.

#### Register

This page contains a registration form that will create an account for the website.  
There is also a link to the login page, for if the user already has an account.

#### Account

This page is split into 3 different pages, navigated between via the pills.  

The account details page will show the username & email address for the current user.  

The orders page shows details of past orders by the current user.  

The downloads page shows each photoset that the current user has purchased. Using the download button, the user can download the photoset for their own use.

#### Logout

Using this link on the navbar will log the current user out and direct them back to the home page.

#### Cart

This page shows all of the photosets that have been added to the cart by the user.  
Using the red X next to photoset they can remove them from the cart.  
If they press the checkout button they will be sent to the checkout page.

#### Checkout

This page shows what's in the cart as well as providing forms for the user to complete their purchase.  
If the user provides valid details in the forms and clicks the submit payment button, the order will go through via stripe and they will be able to access the purchased photosets via the downloads page.  
If the user provides invalid details, the order will not go through and they will be given an error message.

#### Admin
If the user is logged into a superuser account, the admin link will appear on the navbar.  
This takes the user to the django administration backend and will allow them to add/edit photosets and look through orders that have been made.

### Features Left to Implement
- A search feature for the shop. This was left out due to time constraints and could certainly be added in the future.
- Editing user details through the profile page. This was left out due to time constraints and could certainly be added in the future.
- Saving billing information for future purchases. This was left out due to time constraints and could certainly be added in the future.

## Technologies Used

1. HTML
2. CSS
3. Bootstrap (4.4)
5. Jquery
6. Django
8. Python
9. Postgres
10. Heroku
11. Amazon S3
12. Stripe
13. Javascript
14. FontAwesome
15. Bootswatch

## Testing

HTML documents were tested using: https://www.freeformatter.com/html-validator.html  
My CSS sheet was tested using: https://jigsaw.w3.org/css-validator/

1. Login - Login form
    1. Went to the login page.
    2. Tried to submit with any empty fields. Confirmed that an error message appears about the required fields.
    3. Tried to submit incorrect login data. Confirmed that an error message appears about invalid username/password.
    4. Submitted correct data. Confirmed that the user is logged in.

2. Register - Registration form
    1. Went to the register page.
    2. Tried to submit with any empty fields. Confirmed that an error message appears about the required fields.
    3. Tried to submit invalid email address. Confirmed that an error message appears about the format.
    4. Tried to submit an already used username. Confirmed that an error message appears about username being taken.
    5. Tried to submit different passwords. Confirmed that an error message appears stating passwords must match.
    6. Submitted correct data. Confirmed that the user is registered/logged in.

3. Cart 
    1. Tried to checkout with an empty cart. Confirmed an error message appears and stops the user checking out with no items.
    2. Tried to checkout with items in the cart. Confirmed that it sent me to the checkout page with correct items showing.

4. Checkout - Checkout form
    1. Went to checkout page.
    2. Tried to submit form with any empty fields. Confirmed that an error message appears about the required fields.
    3. Tried to submit incorrect card data. Confirmed that an error message appears that we couldn't take payment and order wasn't processed.
    4. Tried to submit correct test card data. Confirmed that the order has gone through and appears on user's download page.

In addition to the above I had my friend test the site for me as he is a QA Tester. He found a few small issues that were recitified.  
Although there was one issue that he found that I haven't had time to fix. If you put in certain incorrect card data, such as wrong length of number. The stripe error is printed into the console but no feedback is given to the user.

## Deployment

This site is hosted using Heroku, it is linked directly to this Github repositories' master branch. The deployment on Heroku is updated automatically everytime a new push is made to the Github repo.

In order for the deployed site to work correctly on Heroku, there must be a procfile, requirements.txt file and an app file.

While working on the project, an env.py file was used to store any keys that I didn't want the public to see. This includes:  
SECRET_KEY, DATABASE_URL, STRIPE_PUBLISHABLE, STRIPE_SECRET, AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY.  

On the Heroku deployment the above keys are input into the config vars directlty. This keeps them out of the local files and stops anyone being able to use them.

A demo can be viewed on Heroku [here](https://tierney-photography.herokuapp.com/).

## Credits

The websites initial bootstrap/css theme was "Lux", which was acquired from [Bootswatch](https://bootswatch.com/lux/)

### Media
- The photos used on this site were taken by myself (As you can tell I'm not a real photographer).
- The image of the camera on the about page was found on [Pexels](https://www.pexels.com/), a stock image website.

This is for educational use.