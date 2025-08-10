<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a id="readme-top"></a>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->


<!-- ABOUT THE PROJECT -->
## About The Project
This Project helps auto restart the Project Zomboid Server, whenever finds a new update from workshop. Available for Windows and Linux

### Built With

* [![Python][Python.js]][Python-url]
* [![Rcon][Rcon.js]][Rcon-url]




## Installation

1. Clone the repo
   ```sh
   git clone https://github.com/iimarky1234/PZomboid-Server-Auto-Update.git
   ```



<!-- USAGE EXAMPLES -->
## Usage

### Change the config base on your system: 
`config.yaml`
#### Example:
```yaml
# <Your location>/Zomboid/Logs
SERVER_LOG: "C:/Users/Testing/Zomboid/Logs"

# Use local IP example: 127.0.0.1
SERVER_IP: "127.0.0.1"

# Check in servertest.ini for the RCONPort
RCON_PORT: 27015

# Check in servertest.ini for the RCONPassword
RCON_PASSWORD: "123456789"

# Amount of time before restarting server. IN SECONDS !!
TIME_BEFORE_RESTART: 10

# time loop of the update. IN SECONDS !! Recommend 10 minutes = 600 seconds
LOOP_TIME: 20
```


### To run the script: 
Linux:
```sh
source bin/activate
```
```python
python auto_reset.py
```
Windows:
```
bin/activate
```
```python
py auto_reset.py
```

<p align="right">(<a href="#readme-top">back to top</a>)</p>





<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[Rcon.js]: https://img.shields.io/badge/RCON--python-blue
[Rcon-url]: https://github.com/conqp/rcon
[Python.js]: https://img.shields.io/badge/PYTHON-yellow?logo=python
[Python-url]: https://www.python.org/
