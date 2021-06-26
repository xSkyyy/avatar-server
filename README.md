# Avatar Server

![image](https://user-images.githubusercontent.com/36131887/123528177-77259400-d6dd-11eb-9e2e-58018259e98a.png)


Cool, light, performant, easy avatar server for osu servers. It is meant to handle all connections to the `a` subdomain for your osu server.

## Cool things

- Really fast, being able to handle multiple requests at once and serving avatars with speeds faster than 0.5ms.
- Lightweight, running the avatar server will not take a toll on your server.
- Partial caching, preventing unnecessary filesystem calls from being made and slowing everything down.

## Requirements
- Python >= 3.8
- Linux/MacOS Server

## How do I use it?
The avatar server is **EXTREMELY** simple to set up.
- Download the GitHub repository on your server. This can be done by running the command `git clone https://github.com/RealistikOsu/avatar-server`.
- Download all of the required modules. This is done by running `python3.9 -m pip install -r requirements.txt` in the downloaded server files folder.
- Copy the `config.sample.py` file and rename it to `config.py`.
- Open it and modify all the values according to your preferences (you might not even need to do it as the defaults are good).
- Get an avatar you want as your server's default and place it to your selected avatar location (usually just the `avatars` folder) and name it `-1.png`. **The server will not start without this step, therefore it is imperative**.
- Run the server using `python3.9 main.py`!
- Use a webserver such as Nginx or Apache to proxy the avatar server to a domain such as `a.ppy.sh` or `a.usssr.pl` used by the osu! client to fetch avatars.
- It is that simple! Enjoy!

## License
This avatar server is licensed under the M.I.T license, a REALLY permissive license that essentially lets you do anything with this. Have fun fellow osu server owners!
