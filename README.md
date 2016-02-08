A flask app that can be deployed to heroku which returns a list of fashion items.
I have deployed the project on heroku with the url: https://fashion-webapp-heroku.herokuapp.com/
The github link with the source code is at: https://github.com/leightonlee/fashion_heroku

The Procfile contains a web and an init.

The web process will start up the flask app.  The '/' route will serve index.html.  index.html will
call /fashion/page/<page> and /fashion/img/<image> to retrieve the json data and images.

The init process should create and populate the db.  Since the free version of heroku
only lets you run one process at a time, I was not able to test if the init process works.
If the DB is not populated when you test it, you can import and run populate_db from create_db.

I have tested the website with chrome and IE.  For the layout, I am using a js plugin called pinto.
I don't know if you expected me to write my own layout to handle it but it would probably take me
some time to figure out everything I needed to do it because I do not normally use javascript.
Pinto seems to have problems with handling images during the loading phase.  It could probably be
done better but for the purpose of this, I think it's fine.

