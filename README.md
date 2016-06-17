![](https://raw.githubusercontent.com/peterwallhead/robot-arm-programmer/master/screen.png)

## Notes
-----

This will only run on a Raspberry Pi with the latest RPi.GPIO library installed:
```
sudo apt-get update
sudo apt-get install python-dev python-rpi.gpio
```

## Set up and run server
```
sudo pip install flask
git clone https://github.com/peterwallhead/robot-arm-programmer.git
cd robot-arm-programmer/src/
python app.py
```

Head to http://localhost:8000 to view the app.
