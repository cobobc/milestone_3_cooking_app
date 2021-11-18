# Milestone Project 3

## Purpose 

The purpose of this site is to complete the third Milestone Project for the Code Institute's Full Stack Developer course and can can be found [here](https://cobobc.github.io/milestone_project_2/).

## Cookbook Website

![TTT site desktop overview](assets/images/read_me/ttt_home_desktop.png)

![TTT site mobile overview](assets/images/read_me/ttt_home_mobile.png)

Ciaran O'Brien has been requested to create a cook book app which allows users to create and manage a their own cooking recipes. The app will allows users to create a profile in which they can store their favourite recipes. Users will be able to view other user recipes too. An administation user will be able to do everything a regular user can do but will also have the capacity to create and manage the recipe categories the regular users choose.

## User Experience (UX)

### User stories

#### First Time User Goals

*   As a First Time user, I want to view clear and concise content on mobile and tablet.
*   As a First Time user, I want to learn and understand what the site offers.
*   As a First Time user, I want to find the registration page.
*   As a First Time user, I want to easily register a Cookbook account.
*   As a First Time user, I want to recieve an email that welcomes me and acknowledges that I have created an account.
*   As a First Time user, I want to add a recipe.
*   As a First Time user, I want to view the recipe on the recipes page.
*   As a First Time user, I want to view other user's recipes on the recipes page.
*   As a First Time user, I want to be able to edit my recipes.
*   As a First Time user, I want to be able to delete my recipes.
*   As a First Time user, I want to seemlessly navigate through all pages of the site.
*   As a First Time user, I want to easily connect with Cookbook's social platforms.
*   As a First Time user, I want to log out of my account.

#### Returning User Goals

*   As a Returning user, I want to easily use a recipe while cooking.
*   As a Returning user, I want to easily add more recipes.
*   As a Returning user, I want to categorize all my recipes.
*   As a Returning user, I want to search for certain recipes on the recipes page.
*   As a Returning user, I want to navigate back to the recipe page after finding a recipe using the search tool.

#### Frequent User Goals

The frequent user wants the following:

*   As a Frequent user, I want to add, edit and delete as many of my recipes as I want.
*   As a Frequent user, I want to use this app as my only cooking tool.
*   As a Frequent user, I want to search for new recipes other users have added over time.

#### Admin User Goals

The admin user wants the following:

*   As an admin user, I want to manage (add, edit and delete) the recipe categories.


### Design

#### Colour Scheme

The main colours used are #009170 (green) and #000 (white). The green is a common colour associated with golf.
For the special quiz pages a #003399 (blue) and a #FFCC00 (yellow) are used. These colours are that of the EU flag and the European Ryder Cup team.

#### Font

The **Rubik** font is used through the whole app.

#### Imagery

The images used in the app are sourced from google images and was granted permission to use for this project.

#### Wireframes

For complete wireframes see this [PDF](assets/images/read_me/Wireframes_m2.pdf).


### Limitations

There were no limitations.

## Features 

The features throughout the site are mininal text, larger text and clear buttons for clear navigation throughout the app. Use of Bootstrap buttons helped this.

### Existing Features

*   Navigation bar

    *   Featured on every page, but depending on the user can differ in the following scenarios:
        1.  A user that has not registered or logged in - the nav bar contains links to the home, register and login pages.
        1.  A user that has register and is logged in - the nav bar contains links to the home, profile, add recipe and recipes pages, and a link to log out. 
        1.  An admin user - the nav bar contains links to the home, profile, add recipe, recipes and manage recipe categories pages, and a link to log out.
            *   If the user selects the Log Out option on the nav bar, a pop up will appear to confirm the log out. If the user confirms, the user in navigated to the Login page.
        
    *   The title in the nav bar provides the user with a link back to the home page. 
    *   The navigation options becomes contained in a responsive Bootstrap burger icon for tablet and mobile devices that provides the page option in a dropdown form. 
    *   When a user has scrolled down a page to a point where the nav bar is no longer visible, as soon as the user begins scrolling up the page, the navbar becomes visible    again.

*   Footer

    *   Featured identically on every page and contains Font Awesome icons used to provide external links to Cookbook's social platforms. Each external link has the attribute of target="_blank" which opens the link in a new tab, keeping the user on the site and allowing for seemless UX.

*   Home page

    *   Provies a friendly/inviting cooking image with the Cookbook title and a one line summary of the site over the image.
    *   Underneath the image there is a jumbtron that provides the user with more detail about what the app offers. 

*   Register Page

    *   A header with short descriptive text on how to register.
    *   The form is houses the required fields (username, email, and password) a user must enter to register.
    *   A large register button makes it clear and easy to register.
    *   When the user the clicks the register button, the user is sent to their profile page, and their registration details are sent and stored in mongodb.
    *   When the user the clicks the register button, they will recieve an email welcoming them and affirming they have registered. This feature is via EmailJS funtionality embedded in the registration form.
    *   There is medium size text under the register button asking the user if they are already registered and provides a link to the log in page in case the user has mistakenly navigated to the register page.

*   Login Page

    *   A header with short descriptive text on how to log in.
    *   The form is houses the required fields (username and password) a user must enter to log in.
    *   A large log in button makes it clear and easy to login.
    *   When the user the clicks the login button, the user is sent to their profile page.
    *   There is medium size text under the register button asking the user if they are new to the site and provides a link to the register page in case the user has mistakenly navigated to the log in page.
    
*   Profile Page

    *   A header with short descriptive text informing the user about the options available on the page.
    *   For desktop and tablet, there are two cards on the same row with an image and a button each so the user can either go the recipes page or add recipes page. On mobile the cards will sit on top of each other in the same column.


*   Recipes Page

    *   A header with short descriptive text informing the user about the recipes page. 
    *   The search bar is postioned near the top of the page so that if the user doesn't want to scroll down the page to find what they want, they can just type keywords of what they are looking for. The search functionality - when prompted - searches through the data within the created recipes. Validation is coded (max and min lengths, and pattern) into the search bar to protect against the potential of someone breaking the site.
    *   If the user has a successful search, they will be presented with the recipe(s) that match the search. The reset button gives the option to the user if they want to see all the recipes again.
    *   All recipes are presented within cards. Within the cards is the recipe category as the main heading followed by the recipe name in a child heading. Underneath is two Bootstrap accordian components which house the ingredients and the cooking instructions respectively. The UX theory here is that if the user is using this app while cooking, they can open and close both accordians to suit their need. For example, It avoids the user having to scroll down through all of the ingredients to get to the cooking instructions. They can simply close the ingredients accordian and open only the cooking instructions.
    *   If the recipe was not created by the current user, the remaining content in the card is the cooking time and user name who created the recipe. If the recipe was created by the current user, they will have optinon to edit or delete the recipe in button form. If the user selects **Delete**, they are presented with a pop up asking them to confirm deletion. If they confrim the deletion, the recipe is removed for the Recipes page and is also removed from the mongodb database. If the user selects **Edit**, they are brought to the edit recipe page.
    *   Using the Bootstrap grid system three cards will appear on one row for the desktop. Two cards on one row for table, and one column for mobile.

*   Add Recipe Page

    *   A header with short descriptive text on how to add recipe.
    *   An easy to use form with the following fields:
        1.  Recipe category - this is a dropdown option. The user can choose from the different recipe categories. The categories and manged by an Admin account.
        1.  Recipe name - user types recipe name.
        1.  Cooking Time - user types cooking time.
        1.  Ingredients - user types ingredients.
        1.  Cooking Instructions - user types cooking instructions.
    *   The user then selects **Add Recipe**. This sends the user back to the Recipes pages with a message at the top of the page informing them that the recipe has been successfully added to the recipes page. The recipe data is sent and stored in mongodb.

*   Edit Recipe Page

    *   A header with short descriptive text on how to edit a recipe.
    *   An easy to use form with the fields that are already populated with the existing recipe data:
        1.  Recipe category - this is a dropdown option. The user can choose to edit from the different recipe categories.
        1.  Recipe name - user can edit recipe name.
        1.  Cooking Time - user can edit cooking time.
        1.  Ingredients - user can edit ingredients.
        1.  Cooking Instructions - user can edit cooking instructions.
    *   The user then selects **Edit**. This sends the user back to the Recipes pages with a message at the top of the page informing them that the recipe has been successfully updated. The updated recipe data is sent and stored in mongodb.  
    *   If the user doesn't want to edit or just wants to navigate back to the REcipes page they can select the **Cancel** button.
  
*   Manage Recipe Types Page

    *   A header with short descriptive text informing the user about how to manage the recipe categories. 
    *   A large button to add new category is predominant on this page to provide no confusion on how to add. The button links to Add Recipe Category page.
    *   The categories are presented in card form with the name of the category and an edit and delete button.
    *   The user is brought to the Edit category page if they click the **Edit** button. If they choose the **Delete** button, a pop up requesting deletion confirmation. If they confrim the deletion, the category is removed for the Manage Recipe Category page and is also removed from the mongodb database.
    *   Using the Bootstrap grid system four cards will appear on one row for the desktop. Two cards on one row for table, and one column for mobile.

*   Add Recipe Types Page

    *   A header with short descriptive text on how to add a new recipe category.
    *   A simple form with one text input option for the admin user to type a new category.
    *   Validation is coded (max length) into the form to protect against the potential of someone breaking the site or accidently creating a jargon category.
    *   Large Add Category button is underneath the form to make it clear to click the button when done typing the new category. If the user selects the add new category button they will be naviagted back to the Manage Recipe Categories page. The new category data is sent and stored in mongodb.

*   Edit Recipe Types Page

    *   A header with short descriptive text on how to edit a recipe category.
    *   A simple form with one text input option for the admin user to edit the category. The category is prepopulated with the existing category the user wants to edit.
    *   Validation is coded (max length) into the form to protect against the potential of someone breaking the site or accidently creating a jargon category.
    *   Large Edit Category button is underneath the form to make it clear to click the button when done typing the edited category. If the user selects the edit category button they will be naviagted back to the Manage Recipe Categories page. The updated category data is sent and stored in mongodb.
    *   The user can click the Cancel button to discard any edits and return to the Manage Recipe Categories page. 

*   Flash Messages

    *   A heading with relevant information for the user appears (with a hr underneath to give spacing) in the following user interactions with the app:
        *   If a user trying to register enters a username that already exists (top of registration page) - **Oops! This username already exists**
        *   If a user trying to register enters an email that already exists (top of registration page) - **Oops! This email already exists**
        *   If a user trying to register enters an email that already exists (top of profile page) - **You have successfully registered! Happy cooking!**
        *   If a returning user successfully logs in (top of the profile page) - **Welcome, {username}**
        *   If a returning user enters an incorrect password (top of the log in page) - **Incorrect Username and/or Password**
        *   If a returning user enters an incorrect username (top of the log in page) - **Incorrect Username and/or Password**
            * The **Incorrect Username and/or Password** message was chosen for both password and username protection. This is user security protection. The hypothtetical hacker will not know what field they have entered incorrect details into.
        *   If a user has logged out (top of the log in page) - **You have been logged out**
        *   When a user has added a new recipe (top of Recipes page) - **Your recipe has been added**
        *   When a user has edited a recipe (top of Recipes page) - **Your recipe has been updated**
        *   When a user has deleted a recipe (top of Recipes page) - **Your recipe was successfully deleted**
        *   When an admin user has added a new recipe category (top of Recipes page) - **New Recipe Type Added**
        *   When an admin user has edited a recipe category (top of Recipes page) - **Recipe Type Successfully Updated**
        *   When an admin user has deleted a recipe category (top of Recipes page) - **Recipe Type Successfully Deleted**
    *   If a user refreshes the page on which a flash message is displayed, the flash message with disappear. 
        


### Features Left to Implement

*   Popup aleart to confirm if the user wants to log out.


## Technologies Used

*   HTML - Used for the structure of the website.

*   CSS - Used to style the website.

*   JavaScript - used to provide interactive features to the navbar (sourced from startbootstrap.com) and to always keep the copyright year in the current year (source: Tim Nelson - Tutor at Code Institute)

*   Python - used to provide the main app backend functionality, user registration, log in, log out, user data interacting with MongoDB, jinja templating.

*   Flask - a web framework that provided the tools, libraries and technologies required to build the Cookbook app.

*   [MongoDB](https://www.mongodb.com/) - used to store the users data.

*   Werkzeug - used for user password security.

*   [RandomKeyge](https://randomkeygen.com/) - used to create the secret key variable in the env.py file

*   [Heroku](https://id.heroku.com/login) -  used to ????????

*   [EmailJS](https://www.emailjs.com/) - used in conjuction with JS to allow the website to send email to the user.

*   [StartBootstrap](https://startbootstrap.com/theme/clean-blog) - used this as the source code for the theme of the app. Includes JS for interactive nav bar use.

*   [Bootstrap](https://getbootstrap.com/) - used throughout the site for layout and styling. 

*   [Google Fonts](https://fonts.google.com/) - provided the *Enriqueta* font used throughout the website.

*   [Font Awesome](https://fontawesome.com/) - provided the scocial media icons used in the Footer.

*   [Google Chrome Developer Tools](https://developer.chrome.com/docs/devtools/open/) - used to inpect each page, debug and mostly to test different CSS styles.

*   [GitHub](https://github.com/) - hosting site to store the websites source code and Git pages used to deploy the live site.

*   [Gitpod](https://gitpod.io/workspaces) - the version control to check status, add, commit and push code to GitHubs repository for storage.

*   [Microsoft PowerPoint](https://office.live.com/start/powerpoint.aspx) - used to create the wireframes.

*   [PX converter](https://nekocalc.com/px-to-rem-converter) - to covert px values to rem values.

*   [Stack Overflow](https://stackoverflow.com/questions/9139075/how-to-show-a-confirm-message-before-delete) - used to help create the pop up confirmation alerts when the user deletes data or tries to log out.


## Testing

### Testing Strategy

1.  Complete tests for user goals.

1.  Run all HTML pages through the [W3C HTML Validator](https://validator.w3.org/).

1.  Run all CSS files through the [W3C CSS Validator](http://www.css-validator.org/).

1.  Run all .js files through the [JShint](https://jshint.com/) validator.

1.  Run all python files through [PEP8 online](http://pep8online.com/)

1.  Run a lighthouse test for performance.


### Test Results

#### Validation Results

1.  Add Recipe

    *   The first child option element of a select element with a required attribute, and without a multiple attribute, and without a size attribute whose value is greater than 1, must have either an empty value attribute, or must have no text content. Consider either adding a placeholder option label, or adding a size attribute with a value equal to the number of option elements. = I added an empty value

    *   The aria-describedby attribute must point to an element in the same document. = changed the aria-describedby attribute to recipe_name to match for element in the label


1.  Recipe Page

    *   Duplicate ID accordionExample.
    *   Duplicate ID headingOne.
    *   Duplicate ID collapseOne.
    *   Duplicate ID headingTwo.
    *   Duplicate ID collapseTwo.

    These errors repeat depending on how many recipes are store in the data base. Trying to imlement the loop counter id.

1.  Add new category page

    *   The aria-describedby attribute must point to an element in the same document. = changed the aria-describedby attribute to recipe_type to match for element in the label


The HTML, CSS and JavaScript validations produced 0 errors.

#### User Goal Results

##### First Time users

*   As a First Time user, I want to view clear and concise content on mobile - Testing was performed to ensure there was no clusters of over information, well spaced and aesthically pleasing on tablet and mobile.

*   As a First Time user, I want to learn and understand what the site offers - Testing was performed to verify enough information is uploaded to tell the user about what the site offers.

*   As a First Time user, I want to find the registration page - Testing was performed to verify enough information is given to user about how to navigate to the regisration page.

*   As a First Time user, I want to easily register a Cookbook account - Testing was performed on the registration form to verify that a user can register an account on this app.

*   As a First Time user, I want to recieve an email that welcomes me and acknowledges that I have created an account - Testing was performed to verify that when a user create an account they recieve a personal email.

*   As a First Time user, I want to add a recipe - Testing was performed on the recipe form input fields and the add recipe buttons to ensure a user can create a recipe.

*   As a First Time user, I want to view the recipe on the recipes page - Testing was performed on the recipe cards and the accordian features within it to ensure the user can view their recipe.

*   As a First Time user, I want to view other user's recipes on the recipes page - Testing was performed on the recipe cards and the accordian features within them to ensure the user can view other user's recipes.

*   As a First Time user, I want to be able to edit my recipes - Testing was performed on the user recipe cards on the Recipes page to ensure the edit button navigates the user to the Edit Recipe page. Testing was performed on all inputs and buttons in the edit recipe form function correctly so that the user can successfully update their recipe.

*   As a First Time user, I want to be able to delete my recipes - Testing was performed on the user recipe cards on the Recipes page to ensure that when the Delete button is selected, a pop up appears to confirm that the user want to delete. If the user confirms deletion, testing was done to confirm that the recipe has been removed from the Recipes page.

*   As a First Time user, I want to seemlessly navigate through the 6 pages of the site - Testing was performed on all navigation links to ensure the user can seemlessly navigate throughout the site.

*   As a First Time user, I want to easily connect with Cookbook's social platforms - Testing was performed on the socail icon links in the footer to ensure that the user isnavigated to the chosen social media platform and that the link opens in a new tab to keep the user in the app allowing for seemless UX.

*   As a First Time user, I want to log out of my account - Testing was performed on the Log Out link in the Navigation bar to enusre that the user can successfully log out, that when the link is selected a pop up appear asking the user to confirm that they want to logout (as to avoid an unwanted log out), and the upon a successful logout, the user is redirected back to the log in page.

##### Returning Users

*   As a Returning user, I want to easily use a recipe while cooking - Testing was performed on the accordian features in the recipe cards to ensure the cook using the app can easily open and close the ingredients and cooking instructions accordians individuallty, so the user doesn't have to scroll through all the ingredients to get to the cooking instructions or visa versa. 

*   As a Returning user, I want to easily add more recipes - Testing was performed to ensure a user can create and store as many recipes as they would like and that they all appear on the Recipes page.

*   As a Returning user, I want to categorize all my recipes - Testing was performed on the choose category dropdown in the Add and Edit recipe forms to ensure a user can create and store as many recipes under a variety of categories.

*   As a Returning user, I want to search for certain recipes on the recipes page - Testing was perfomred on the search bar and the search button to ensure the user can search the recipe list using keywords and that the user is informed if no matches are found for the users keywords.

*   As a Returning user, I want to navigate back to the recipe page after finding a recipe using the search tool - Testing was performed on the reset button of the search tool so a user can easily navigate back the recipe page after using the search tool.

##### Frequent Users

*   As a Frequent user, I want to add, edit and delete as many of my recipes as I want - Testing was performed on the database and its capacity to (1) Store multiple recipes (2) handle recipe that are constantly being edited, updated, and delated, so that the user has confidence that their data wont be lost and the app can handle their demand for manipulating a recipe when that want.

*   As a Frequent user, I want to use this app as my only cooking tool - Testing cannot be performed on this parameter as this can be subjective and some users may prefer other simailar apps. If we had the capacity we could use analytics to measure rates of returning users and provide surveys to ask how users rate the app, is there other apps that they like too, etc

*   As a Frequent user, I want to search for new recipes other users have added over time - Continuous testing was performed on the search tool to ensure a user can easily search the recipe list using the search tool.

##### Admin User Goals

*   As an admin user, I want to manage (add, edit and delete) the recipe categories - Testing was perfomred on the manage category pages to ensure the admin user can easily and quickly manage the recipe categories to meet the demand of the regular users.


#### Lighthouse Test Results

See the following lighthouse test results:

![Lighthouse mobile results](assets/images/lighthouse/lighthouse_test_mobile.png) \
**Mobile test result**


![Lighthouse desktop results](assets/images/lighthouse/lighthouse_test_desktop.png) \
**Desktop test result**


These test results indicate that the site peforms very overall. It also shows that Accessibily and Best Practices could improved to further optimise the sites performance.
Due to the time constaints of this project it is not feasible to act further on this. In a normal working situation time would be taken to optimise performance.


## Deployment

### Project Creation

Created the project by:

1.  Navigating to my [user profile](https://github.com/cobobc).
2.  Selecting the **Respositories** tab.
3.  Selected the **New** button.
4.  Under Repository tempate, select the Code Institute template from the dropdown menu.
5.  Entered milestone_project_2 for the **Repository name**.
6.  Select **Create Repository**. 

### During the Project

The following commands were used throughout the project:

*   git add . - This command was used to add files to the staging area before commiting.
*   git commit -m "commit message explaining the updates" - This command was used to to commit changes to the local repository.
*   git push - This command is used to push all commited changes to the GitHub repository.

### Using Github Pages

1.  Navigate to the GitHub [Repository](https://github.com/cobobc/milestone_project_2).
1.  Select the **Settings** Tab.
1.  Scroll Down to the Git Hub Pages Heading.
1.  Select **Main Branch** as the source.
1.  Select the **Save button**.
1.  Select on the link to go to the live deployed page.

### Run Locally

1.  Navigate to the GitHub [Repository](https://github.com/cobobc/milestone_project_2).
1.  Select the Code drop down menu.
1.  Either Download the ZIP file, unpackage locally and open with IDE (This route ends here) OR Copy Git URL from the HTTPS dialogue box.
1.  Open your developement editor of choice and open a terminal window in a directory of your choice.
1.  Use the 'git clone' command in terminal followed by the copied git URL.
1.  A clone of the project will be created locally on your machine.

## Admin Credentials

Username: Admin
Password: admin123

## Credits

### Code

[W3Schools](https://www.w3schools.com/) helped throughout the project with general element and attribute uncertainties.

### Content 

The contents of the quiz questions came from various sources - BBC Sport, Sky Sports Golf, the R&A and Joe.ie. Headings, titles and paragraphs were all wrote by Ciaran O'Brien.

### Media 

The large background images used are sourced from www.theindependent.ie and permission was granted to use for this project.

### Acknowledgements

I'd like to thank my mentor Spencer Barriball for his guidance, efficiency and positivity throughout my project.
Thank you to Tim Nelson a Tutor at Code Institute whose teaching techniques helped me understand how to implement Python into a project. A lot of this project's code structing was sourced from Tim's amazing Mini Project and Flash Framework lessons.
Thank you to Matt Rudge the Senior Product Developer at Code Institute for his lessons on implementing EmailJS into a project.
Thanks to my fellow students on Slack for helping my link the js quiz code to the html and css code so that my quiz question could appear.

