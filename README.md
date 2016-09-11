[![Gitter](https://badges.gitter.im/template_python_docker_selenium/Lobby.svg)](https://gitter.im/template_python_docker_selenium/Lobby?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

# Dockerizing Python WebDriver Tests

This is a sample repo which runs selenium WebDriver tests inside docker container.

Make sure you have docker installed on your machine.(https://docs.docker.com/engine/installation/linux/ubuntulinux/)

## Run Command

docker-compose up -d && docker wait tests && docker logs tests

Now check [GridConsole](http://localhost:4444/grid/console) you will see all the nodes are registered to the hub and test would be triggered inside the containers.

If you want to scale you node

docker-compose scale chromenode=3

To view the test running within the container, open the vnc_dash.html in Chrome and input the below host and address.

VNC Dash:
[![ScreenShot](# Dockerizing Python WebDriver Tests

This is a sample repo which runs selenium WebDriver tests inside docker container.

Make sure you have docker installed on your machine.(https://docs.docker.com/engine/installation/linux/ubuntulinux/)

## Run Command

docker-compose up -d && docker wait tests && docker logs tests

Now check [GridConsole](http://localhost:4444/grid/console) you will see all the nodes are registered to the hub and test would be triggered inside the containers.

If you want to scale you node

docker-compose scale chromenode=3

To view the test running within the container, open the vnc_dash.html in Chrome and input the below host and address.

VNC Dash:
[![ScreenShot](https://github.com/jaydeepc/template_python_docker_selenium/blob/master/vnc.png))]

$ docker port <container-name|container-id> 5900
0.0.0.0:49338
0.0.0.0:49339

or you can install a VNC viewer locally and try:
./vncviewer 127.0.0.1:49338

When you are prompted for the password it is "secret", which will bring the container view.


))]

$ docker port <container-name|container-id> 5900
0.0.0.0:49338
0.0.0.0:49339

or you can install a VNC viewer locally and try:
./vncviewer 127.0.0.1:49338

When you are prompted for the password it is "secret", which will bring the container view.
