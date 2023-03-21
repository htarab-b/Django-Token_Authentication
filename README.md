# Django - Token Authentication

## Description

Tokens are important for writing backend APIs. In order to combine a backend project that requires login and signup functionalities with a frontend framework like React/Angular, the code and backend data has to be secured and should not be accessed through the frontend. In order to acheive security of data (especially user data), tokens are used. Every registered user will have their own token. These tokens cannot even be accessed by the owner of the token themselves. This will provide security of the APIs.

## Copying the code
* Open 'serializers.py' inside 'api' folder and copy the content into your app's serializer file.
* The 'views.py' contains the API view of the login and signup functions with token authentication. Copy them into your app's views file.
* Copying the url is not necessary but the url for signup and login API is inside the 'urls.py' file.

## Test the code
* Open your localhost, default : http://127.0.0.1:8000/
* Navigate to the login/signup view using the urls provided in 'urls.py'.
* The API can be viewed in the browser and Signup/Login can be done in the browser.
* Though both APIs can be viewed in the browser, it is recommended to use any API testing software like postman.
* In case of signup, user details should be Posted and once Posted a new user will be registered.
* In case of login, the user details should be Posted and if the credentials match, the token of the user will be generated and obtained in the API.