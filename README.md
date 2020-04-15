# FirePro

## CEN4914 - Computer Engineering Senior Design
## John Hodson, Luke Pfeiffer, Aaron Williams

Camera Used: Amcrest 1920TVL

How to run the website on localhost (assumes no dependencies installed):

	1. Run the following commands in a terminal:

		```
		sudo apt install git
		sudo apt install python3
		sudo apt install python3-pip

		pip3 install torch
		pip3 install numpy
		pip3 install django
		pip3 install amcrest
		pip3 install opencv-python

		git clone https://github.com/UF-CEN4914/firespotter.git
		cd ./firespotter/website/

		python3 ./manage.py migrate
		python3 ./manage.py runserver
		```

	2. Navigate to 127.0.0.1:8000 in a browser.

The database may also optionally be seeded with dummy information. This includes fake cameras, organizations, and users.

	1. Run the following commands in a terminal from the ./firespotter/website directory:

		```
		python3 ./manage.py seed
		```

	2. Now the website may be launched as normal by using:

		```
		python3 ./manage.py runserver
		```

	3. Navigate to 127.0.0.1:8000 in a browser and use the following credentials to login:

		Username: john@gmail.com
		password: password