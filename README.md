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

### Example
  ```python
PZserver_serverlog="C:/Users/Testing/Zomboid/Logs" # <Your location>/Zomboid/Logs
server_ip="127.0.0.1" # Use local IP example: 127.0.0.1
rcon_port="27015" # Check in servertest.ini for the RCONPort
rcon_password="123456789" # Check in servertest.ini for the RCONPassword
time=10 # Amount of time before restarting server. IN SECONDS !!
loop_time=20 # time loop of the update. IN SECONDS !! Recommend 10 minutes = 600 seconds
  ```

1. For Windows:
```python
rcon_path="C:/Users/Testing/Downloads/rcon-0.10.3-win64/rcon-0.10.3-win64/rcon.exe" # The location where rcon.exe located (Change base on your system)
startserver_path="""C:/Users/Testing/Downloads/steamcmd/steamapps/common/PZserver/StartServer64.bat""" # Location of StartServer.bat (Change base on your system)
```
2. For Linux:
```python
startserver_path="/opt/pzserver/'Project Zomboid Dedicated Server'/start_server.sh" # Location of start_server.sh (Change base on your system)
```

To run the script: 
```python
python auto_reset.py
```
<p align="right">(<a href="#readme-top">back to top</a>)</p>





<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[Rcon.js]: https://img.shields.io/badge/RCON--CLI-blue
[Rcon-url]: https://github.com/gorcon/rcon-cli
[Python.js]: https://img.shields.io/badge/PYTHON-yellow?logo=python
[Python-url]: https://www.python.org/
