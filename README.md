# Green-Screen-Software
This is a short program that helps remove a background from an image in order to allow that image to be overlaid on a different background.

## Set Up Environment
Open the directory in your command line. Make sure you have installed Python 3 and Virtualenv.
<br>
Run `source env/bin/activate`.

## File Structure
Your directory should look like the following. Create folders as needed.
```
Green Screen Software
│   README.md
│   greenScreenSoftware.py
│   env
│
└───images
│   │
│   └───backgrounds
│   │   │   file111.jpg
│   │   │   file112.jpg
│   │   │   ...
│   │
│   └───hardware (can be changed to whatever name you want, just make sure to also change it in the code)
│   │   │   
│   │   └───folder1
│   │   │   │   file111.jpg
│   │   │   │   file112.jpg
│   │   │   │   ...
│   │   │   
│   │   └───folder2
│   │   │   │   file111.jpg
│   │   │   │   file112.jpg
│   │   │   │   ...
│   │   │   
│   │   │   ...
│   │
│   └───result (empty directory, this is where the new images will come out)
│   │
│   ...
```

## Edit the Code
Depending on the background you choose to use, you will have to edit the code to remove that color. Don't worry it's really easy!
<br>
Find out which range of colors you want to "key" out. Go to the code and set values as the `lower_overhead` and `upper_overhead` so that range is included.
<br>
Also change the `hardwarePath` variable to the location of whatever folder holds the images that need to be stripped of backgrounds.

## Run the Code
Run `python3 greenScreenSoftware.py` from the command line in the GreenScreenSoftware Directory.
<br>
Your output should be shown in the result directory that was in the file structure.
