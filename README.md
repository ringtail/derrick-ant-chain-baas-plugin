# BaaS Plugin

## Usage
1. install derrick
```
    pip install python-derrick
```


2. check derrick installation
```
    derrick --version

    output:

    8888888b.                       d8b        888
    888  "Y88b                      Y8P        888
    888    888                                 888
    888    888 .d88b. 888d888888d888888 .d8888b888  888
    888    888d8P  Y8b888P"  888P"  888d88P"   888 .88P
    888    88888888888888    888    888888     888888K
    888  .d88PY8b.    888    888    888Y88b.   888 "88b
    8888888P"  "Y8888 888    888    888 "Y8888P888  888

    ===================================================
    Derrick is a scaffold tool to migrate applications
    You can use Derrick to migrate your project simply.
    ===================================================

    This is the first time to run Derrick.

    Successfully create DERRICK_HOME in /Users/ringtail/.derrick
```


2. install plugin
```
    pip install pyyaml

    # then place this src folder to ~/.derrick/rigging and named as baas_rigging
```

3. demo

```
    # create a file called baas.yaml

    project_name: "demo"
    base_image: "openjdk:8-jre"
    ports:
      - "8080"
      - "8081"
    jar_file: "app.jar"


    # run derrick init


```
