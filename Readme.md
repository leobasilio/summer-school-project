# Running the demo

Starting at the repository's root directory.

1. Create the virtual network

```
$ docker network create --subnet=172.20.0.0/24 demo
```

2. Build the project's image

```
$ docker build --tag summer-project .
```

3. Run the EDGE container

```
$ docker run --rm -it -p 8080:8080 --network=demo --ip 172.20.0.2 --cpus='0.2' -e LAYER=edge summer-project
```

4. Run the FOG container

```
$ docker run --rm -it --network=demo --ip 172.20.0.3 --cpus='0.4' -e LAYER=fog summer-project
```

5. Run the CLOUD container

```
$ docker run --rm -it --network=demo --ip 172.20.0.4 -e LAYER=cloud summer-project
```

6. Run the DEVICE simulator

```
$ python3 device/device.py
```
