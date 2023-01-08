# NukeTwitter
A script to clear you Twitter accuount and start fresh. Work in progress!

Old version needed a new login every time you start the script while this version takes over existing Chrome session, old and new script are available, but some parts of the old script are missing.

## Getting started
> S1. Launch Chrome in debug mode  
> * locate Chrome exe folder and open cmd in that directory (right click Chrome shortcut -> open file location)
> * type following command, it will launch Chrome in debug mode and they you can go on and log in to Twitter, and then you can run the script
> > chrome.exe --remote-debugging-port=8989 --user-data-dir=<some_dir>  

<br>

> Run:
> Activate your venv  
> 
> python OpenSession.py <args>

### Working functions:
- 2 - Remove Followers
- 3 - Remove who you Follow

### In progress:
- 1 - Delete all Tweets
- 4 - Remove all likes


### TO DO:
- Improve performance
- Better user controls


## Documentation:
>https://chromedriver.chromium.org/home    
>https://www.selenium.dev/selenium/docs/api/py/index.html   
>https://selenium-python.readthedocs.io/installation.html
>https://chromedevtools.github.io/devtools-protocol/
