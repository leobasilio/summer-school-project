# Running the demo

Starting at the repository's root directory.

1. Compile the application

```
$ cd application
$ dnc .
$ cd ..
```

2. Create the virtual network

```
$ docker network create --subnet=172.20.0.0/24 demo
```

3. Build the dana image

```
$ docker build --tag dana .
```

4. Run the main application

```
$ docker run --rm -it -v "$PWD:/app" -p 8080:8080 --network=demo --ip 172.20.0.2 -w /app/pal dana dana -sp ../application/ InteractiveAssembly.o ../application/TCPNetwork.o
```

5. Run the remote application

```
$ docker run --rm -it -v "$PWD:/app" --network=demo --ip 172.20.0.3 -w /app/pal dana dana -sp ../application/  InteractiveAssembly.o ../application/TCPNetwork.o
```
