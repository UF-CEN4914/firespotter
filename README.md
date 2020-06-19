# FireSpotter

## CEN4914 - University of Florida Computer Engineering Senior Design

### John Hodson, Luke Pfeiffer, Aaron Williams

California has been ravaged by wildfires in recent years. Wildfires in this region have
displaced tens of thousands of people and each fire can last for months at a time. These
wildfires are caused by several different sources, including but not limited to, natural events and
human negligence. Regardless of cause, organizations need to be swiftly alerted to fires in order
to perform damage control before they become catastrophic. Historically, a state will build large
fire spotting towers in strategic places and employ individuals to visually spot early signs of a fire. For our CEN4914 project, we decided to create a 21st century solution.

To accomplish this goal, we built a software application that utilizes a machine learning
model to detect a wildfire in an image provided by a low-cost internet protocol camera. If the
application detects the presence of a wildfire in the image, it automatically alerts the organization
of the positive result, allowing for swift action to be taken. Our final product resulted in a
convolutional neural network with a 94.5% accuracy rating and an interface that can
automatically fetch camera frames from low-cost internet protocol cameras.
In the future, we hope to commercialize our project by creating a brand (logo, design
patterns, social media) around the functioning application.

Camera Used: Amcrest 1920TVL

## How to run the website on localhost (assumes no dependencies installed in a Debian enviornment):

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

## The database may also optionally be seeded with dummy information. This includes fake cameras, organizations, and users.

1. Run the following commands in a terminal from the ./firespotter/website directory:

	```
	python3 ./manage.py seed
	```

2. Now the website may be launched as normal by using:

	```
	python3 ./manage.py runserver
	```

3. Navigate to 127.0.0.1:8000 in a browser and use the following credentials to login:

	username: john@gmail.com
	
	password: password
