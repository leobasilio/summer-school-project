# Running the demo

Starting at the repository's root directory.

1. Compile the application

```
$ cd application
$ dnc .
$ cd ..
```

2. Compile the PAL Framework

```
$ cd pal
$ dnc . -sp ../application/
$ cd ..
```

3. Create the virtual network

```
$ docker network create --subnet=172.20.0.0/24 demo
```

4. Build the Dana image

```
$ docker build --tag dana .
```

5. Run the EmergentSys component

```
$ docker run --rm -it -v "$PWD:/app" -p 8080:8080 --network=demo --ip 172.20.0.2 -w /app/pal dana dana -sp ../application/ EmergentSys.o
```

6. Run the Autonomous Perception

```
$ docker run --rm -it -v "$PWD:/app" --network=demo --ip 172.20.0.3 -w /app/pal dana dana -sp ../application/ AutonomousPerception.o
```

7. Run the remote application

```
# to be fixed
$ docker run --rm -it -v "$PWD:/app" --network=demo --ip 172.20.0.4 -w /app/pal dana dana -sp ../application/ ../application/TCPNetwork.o
```
