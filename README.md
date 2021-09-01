# FoodStorageManagement.com
![Screen Shot 2021-08-27 at 16 01 33](https://user-images.githubusercontent.com/47679109/131193070-0e8c5482-405d-413e-b95a-0887fbcd2d85.png)

https://ms3-food-store.herokuapp.com/ - Tool for food storage management.

## Author
Gabriel Perguer Figueiro

## Project Overview
![Screen Shot 2021-08-27 at 16 06 28](https://user-images.githubusercontent.com/47679109/131193389-5e91a635-fa4b-4f96-8173-21e1299d1c77.png)
https://ms3-food-store.herokuapp.com/

This website is designed for people to manage their personal food storages. It allow the users to have an updated record of their food inventory. This can be done with food inventory managers updating, adding, removing records in the database.
The website provide a simple user interface that is meant to be easy to use even for a person who is not technoligly confortable.

- deployed site: https://ms3-food-store.herokuapp.com/


## HOW TO USE

### Unauthenticated User
- Look at the inventory table:
	1. Go to the home page https://ms3-food-store.herokuapp.com/.
	2. Note the table in the middle of the page.
	3. The header of the table indicates the content on the table.
- Login
	1. Go to the home page https://ms3-food-store.herokuapp.com/.
	2. On the menu navigator click the option 'Login' (if the option 'Login' does not appear once the page is loaded click the hamburger icon, then click the option 'Login)
	3. In the middle of the page, enter credential:
		- Username: gab1
		- Password: gab1
	4. Click the button 'Log in'.
	5. Note that the user user is successfuly logged in because:
 		-  a welcome message in blue below the menu navigation confirm that the user successfully logged in.
 		-  user is redirected to the homepage.
 		-  Below the menu navigator to the left side of the page, there is a text indicating the name of the user that is currently logged in. Also, the button to delete the user account is presented below the mentioned text.

- Register
	1. Go to the home page https://ms3-food-store.herokuapp.com/.
	2. On the menu navigator click the option 'Login' (if the option 'Login' does not appear once the page is loaded click the hamburger icon, then click the option 'Login)
	3. In the middle of the page, just below the text box to enter credetional you will find a sentence that says:
		- "Don't have an account? Register"
	4. To registe enter a username and password on the text spaces that says 'Username' and 'Password'.
		- The username and password must be 3-25 characters long.
 
- Searching on the table. Search result will search for the key words withing the fields name and description.
	1. Go to the home page https://ms3-food-store.herokuapp.com/.
	2. On the menu navigator click the text box found on the right side of the menunavigator (if the text box is not showing right away after the page is loaded, click the hamburger icon see the text box).
	3. Type a word in the text box.
	4. Click the button 'Search' that is found on the right side of the text box.
	5. If the the work is found withing the table columns 'Name' or 'Detail', the page will refresh and the table in the center of the page will show only items that have the key word(s) in the 'Name' or 'Detail' field.
	6. If the key word(s) is not found within the 'Name' or 'Detail' column, then a message saying "There are no food items to list" and a button to refresh the page will show below this message. This button will refresh the page without search results.

- Sort the table based on the expitation date:
	1. Go to the home page https://ms3-food-store.herokuapp.com/.
	2. On the table column 'Expiration Date', click on the blue icon that looks like a funel.
	3. The page will refresh and show the same table sorted by 'Expiration Date' values in ascending order.


### Authenticated users:
- Username and password for a user that is established in the system (set up this user to have some order history)

### Admin User
- only necessary if some functionality is limited to admin users only

## UX
 
1- Who this website is for?  
Answer: This website is for house holders interested in storing food.

2- What it is that users want to achieve with this website?  
Answer: The user would like to have make sure that their foodstorage is well mantain. For example, they want to know that their food storage have everything they need to survive and that they are in proper state to be used if necessary.

3- How your project is the best way to help them achieve these things?  
Answer: The website provide a way for the house holder to remotelly check on the current state of it's food storage. The website will contain information fundamental for food storage management such as food name, quantity, description, expiration dates. It also allow food storage owner to personally update the food storage database to reflect changes on the fisical food storage space.


__User Stories:__   
  
| User Action        | Goal          |
| ------------- |:-------------:| 
| User access website when he is not near the foor storage location.     | To know the current state of  his food storage, for peace of mind or planning purposes.   | 
| User study the foodstorage data.    | To make sure the storage contains the food diversity necessary for human to healthly live off of it. | 
| User update the foodstorage database using the website.  | To have the foodstorage data online matching the food storage actual state      |


  
__Link to wireframe:__     
- [Click here to see wireframe in PDF format. This should take you to the file stored on github repository](https://github.com/Gaberoids/MS3-gf-foodStorage-MongoDb/blob/master/ProjectMockup.pdf)

## Features
 
- ### Existing Features
#### navigation
The purpose of this navigation is to help user to easily find the login and search functionality.
![Screen Shot 2021-08-25 at 22 18 31](https://user-images.githubusercontent.com/47679109/130899892-c74d43ed-20be-473e-b48b-b7605d705567.png)
![Screen Shot 2021-08-25 at 22 19 22](https://user-images.githubusercontent.com/47679109/130899949-4326a69d-c210-4c1e-bec3-59363037f08d.png)


    - Database to store data.
    - Capacity to CRUD the database.
    - Login, registration and deletion for users.
    - Search for items based on name and detail fields.
    - Field validation.

- ### Features Left to Implement
    - Notification and alert box before deleting items in the database or deleting profile.
    - Sort table based on expiration data.
    - To make expire items to stand out or generate notification and alerts when items expire.
    - Validation to date field on other browsers than Chrome.
    - Table style: text vertical alignment for the fields but Descrition column
    

## Technologies Used

[Bootstrap](https://getbootstrap.com/docs/4.0/utilities/display/) 
    - The navigation bar (in all pages), the table, the login and registration pages.

[Ionicons](https://cdnjs.cloudflare.com/ajax/libs/ionicons/2.0.1/css/ionicons.min.css)
- Source for website icons.  

[Javascript](https://www.javascript.com/)
    - This technology was used to put a limit on the total number of characters on the areatext tag. 

[Jquery](https://jquery.com/)
    - This library was used on the menu navigator. 

[Mongodb](https://www.mongodb.com/)
    - This was used to host and manage the database. 

[Heroku](https://heroku.com)
    - Website hosting tool. 


## Testing

Non-automated tests
1. Security (user should only be able to CRUD if logged in) and login:
    1. As a non-authenticated user go to homepage (https://ms3-food-store.herokuapp.com/).
    2. Note that it is not possible to perform CRUD on the database. Buttons to add, edit and delete item are not visible.
    3. On the menu navigator, click login.
    4. Enter the following credentials: 
        - Username: gab4
        - Password: gab4
    5. User gets logged in and is redirected to homepage.
    6. Note that the menu item 'Add item' appear on the munu navigator.
    7. Note that the icons to edit and delete items now appear on the table.

2. Register, validation and login:
    1. Go to the "Home" page (https://ms3-food-store.herokuapp.com/)
    2. On the menu navigator, click login.
    3. Click the link "Don't have an account? Register.".  
    4. Enter Username and password of your choice.
        - User won't be able to submit the form if the these inputs have less then 4 or more than 25 characters. 
    5. User is created and taken to the homepage.
    6. Click logout.
    7. Go to login page.
    8. Enter the Username and password from item number 4.
        - User won't be able to submit the form if the these inputs have less then 4 or more than 25 characters. 
    9. User is taken to homepage and his account information shows on the top left side of the screen.
    10. Click "Delete account" and note that account is deleted (try to login but will get error) and message shows in blue to confirm.

3. Search functionality:
    1. Go to the "Home" page (https://ms3-food-store.herokuapp.com/)
    2. On the menu navigator search box, type "rice".
        - Note that food items that contains "rice" on "Food Item" and "Details" columns are return.
    3. On the menu navigator search box, type a word that cannot be found in the "Food Item" and "Details" columns. For example, "politics".
        - Note that food items are not returned. Instead the message "There are no food items to list" and the button "Refresh" shows.
    4. Click the button "refresh" to return to homepage.

3. Add, edit validation and delete item:
    1. Go to the "Home" page (https://ms3-food-store.herokuapp.com/)
    2. Login or create an account.
    3. On the menu navigator, click "Add item".
    3. Fill out the form
        - User won't be able to submit the form with "Food Item" inputs with less then 3 or more than 49 characters. 
        - User won't be able to submit the form with "Quantity" inputs with less then 2 or more than 49 characters. 
        - User won't be able to enter more than 400 characters on the input field under "Details".
        - User won't be able to submit the form with "Expiration dates" after year 2099. (This validation is only supported on Chrome browser) 
    4. Click submit. Note that the item was added to the table. If you cannot see it, try search to it.
    5. Click the "delete" icon by the new item and note that the item will no longer be found in the table.

4. Mobile test:
    1. Go to a mobile screen.
    2. Perform all tests listed above.
    3. Notice that the menu navigator is collapsable.


**Bugs:**  
- There is an error message on that shows up sometimes on the console. The error is about favicon.ico. According to information found on slack, this can be ignored. See details in the following link: ???
    - https://code-institute-room.slack.com/archives/C7EJUQT2N/p1613656600182700?thread_ts=1613656263.182600&cid=C7EJUQT2N
- Found 500 error on search page when running the page on a Code validator site.
    - See: https://validator.w3.org/nu/?doc=http%3A%2F%2Fms3-food-store.herokuapp.com%2Fsearch
    - This error is not relevant for the search page because the page needs a search term to work with.
- In a css validator, the following error was found:
    - "Value Error : speak none is not a speak value : none"
    - This error came from a 3rd party library. See https://generatepress.com/forums/topic/css-speak-none-is-not-a-speak-value/ .


## Deployment

Link to the github repository https://github.com/Gaberoids/MS3-gf-foodStorage-MongoDb .

Link to the Heroku site that is deploying the project https://dashboard.heroku.com/apps/ms3-food-store . ???

Link to the deployed site https://ms3-food-store.herokuapp.com/ .

Deplyed and development versions have no differences.

**Deployment steps:**
1. Go to heroku and create the app
	1. Login to heroku and Click “new” > “Create new app”
	2. give a name
	3. enter region (USA) or Europe. (the region closest to you)
	4. Click Create
	5. Select GitHub from “Deployment method”
	6. (You may need to connect your github here in this same place before the following step) on the section “Connect to Github” choose the repository you want and enter the repository name that you are using to build the app. Click search, find the repository, and click connect.
	7. Go to “settings” (it is a menu item )
		1. click the button “reveal config vars”
		2. enter the default environment variables from env.py file (enter only the stuff inside the parenteses in the env.py. Like (“Key”, “Value”)
	8. If not done yet, Go to gitPod and commit and push the procfile and requirements.txt
	9. Go back to heroku to deploy page
		1. Click “enable automatic deployment”
		2. Click “deploy branch”
2. Go to terminal in gitpod (This step may not be necessary. Use it if you needed it)
	1. type:
		1. pip3 install flask-pymongo
		2. pip3 install dnspython (to use mongo snd connection string)
		3. pip3 freeze - -local > requirements.txt (to update the requirements.txt file)

**Cloning Repository steps:**
1. Go to the link https://github.com/Gaberoids/MS3-gf-foodStorage-MongoDb .
2. Click the green button "Code".
3. Select the option "Download Zip".
(For more information on how to clone the repository, visit https://docs.github.com/en/enterprise/2.13/user/articles/cloning-a-repository)


## Credits
- My tutor at code academy Moosa. He helped me with directions on how to how to improve the visual presentation of the site.
- Special thanks to open source codes such as bootstrap, ionicon, and the coding comunities/forums such as StackOverflow, Reddit, etc.

### Content
- The content of this website is original.

### Media - Source of all pictures that are not original
    - This website does not contain images that are not original.

### Acknowledgements

I received inspiration for this project from [Codeacademy](https://courses.codeinstitute.net/) classes.
 
