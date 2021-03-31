# foodstorage.com ???

This website is designed for people to manage their personal food storage efforts.

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


**The pages in this website will be more simple in the mobile view compared to desktop view. For example:**
- links in the menu navigator will be replaced by the hamburger icon.
- In the index.html, the head shot from consultant will be removed on mobile screen.

**Bugs:**  
- There is an error message on index.html. It says "Uncaught TypeError: Cannot read property 'step' of undefined.". According to my research, this error has to do with Jquery CDNs. This bug is not breaking the page right now, so I left it alone for now.

## Deployment

Link to the github repository https://github.com/Gaberoids/genealogygenius .

Link to the deployed site https://gaberoids.github.io/genealogygenius/ .

Deplyed and development versions have no differences.

**Deployment steps:**
1. Go to the link https://github.com/Gaberoids/genealogygenius .
2. Click the tab "Settings".
3. Under the section "HUB Pages" click the drop down button under "Source" and select "Master Branch".
4. Go to under the "HUB Pages" section again, and click on the link. This link is the address to the deployed site.

**Cloning Repository steps:**
1. Go to the link https://github.com/Gaberoids/genealogygenius .
2. Click the green button "Code".
3. Select the option "Download Zip".
(For more information on how to clone the repository, visit https://docs.github.com/en/enterprise/2.13/user/articles/cloning-a-repository)


## Credits
- My tutor at code academy Moosa. He helped me with directions on how to how to improve the visual presentation of the site and helped me with some the jasmine test.
- Special thanks to [TMS Tree icon by Icons8](https://icons8.com/icon/34828/tms-tree) for providing the cool logo for this website.

### Content
- The content of this website is original.

### Media - Source of all pictures that are not original
* #### Index.html page
    * ##### Cover
        - [cover-tree.jpg](https://www.freeimages.com/photo/trees-1393133)
    * ##### Question Section
        * ###### How they look like?
            -  [old-headshot.jpg](https://www.freeimages.com/photo/old-framed-picture-1433232)
            -  [old-photos-multiple.jpg](https://www.freeimages.com/photo/old-photos-1434448)
            -  [old-family-bench](https://www.freeimages.com/photo/old-family-photo-2-1433934)
            -  [old-family-portrait](https://www.freeimages.com/photo/old-time-family-photo-1311342)
        * ###### Where they came from?
            -  [where_castle.jpg](https://www.freeimages.com/photo/irish-abbey-1214069)
            -  [where_africa.jpg](https://www.freeimages.com/photo/africa-1406054)
            -  [where_india.jpg](https://www.freeimages.com/photo/taj-1307962)
            -  [where_china.jpg](https://www.freeimages.com/photo/theatre-stage-1235519)
        * ###### How they came from?
            -  [how-wagon.jpg](https://unsplash.com/photos/QFhIVlX9wTs)
            -  [how-ship.jpg](https://www.freeimages.com/photo/sailing-ship-in-harbor-1450308)
            -  [how-train.jpg](https://www.freeimages.com/photo/steam-locomotive-1447997)
            -  [how-car.jpg](https://www.freeimages.com/photo/my-granny-in-old-car-1440617)

* ### Contact.html page
    -  [contact-tree.jpg](https://www.freeimages.com/photo/tree-on-the-hill-1385676)

* ### Search.html page
    -  [search-bk-image.jpg](https://www.freeimages.com/photo/old-family-photos-1423774)

### Acknowledgements

I received inspiration for this project from [Codeacademy](https://courses.codeinstitute.net/).
- The modal functionality and the Mobil hemburger buttons were built inspired on templates from bootstrap.
 
