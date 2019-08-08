router side
* static IP
* LAN Setup
* Port Forwarding / Port Triggering


* [Flask File Uploading - Tutorialspoint](https://www.google.com/search?q=tutorialspoint+flask+file+uploading&oq=tutorialpoint+flask+&aqs=chrome.3.69i57j0l5.13899j0j4&sourceid=chrome&ie=UTF-8) 
add vedio links from youtue CS folder


server side
```
set FLASK_APP=app.py
flask run --host=192.168.1.4

heroku deploy

Install the Heroku CLI
Download and install the Heroku CLI.

tutorial
* [datademofun/heroku-basic-flask](https://github.com/datademofun/heroku-basic-flask)


If you haven't already, log in to your Heroku account and follow the prompts to create a new SSH public key.

$ heroku login
Clone the repository
Use Git to clone usimulation's source code to your local machine.

$ heroku git:clone -a usimulation
$ cd usimulation
Deploy your changes
Make some changes to the code you just cloned and deploy them to Heroku using Git.

git add .
git commit -am "make it better"
git push heroku master

Bugs:
* H14
[Couldn't find that process type, Heroku](https://stackoverflow.com/questions/48512013/couldnt-find-that-process-type-heroku)
* code=H10 desc="App crashed" 
[Heroku deployment error H10 (App crashed)](https://stackoverflow.com/questions/13496827/heroku-deployment-error-h10-app-crashed)
[Heroku can't find gunicorn command](https://stackoverflow.com/questions/28977018/heroku-cant-find-gunicorn-command?rq=1)

