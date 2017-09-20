# Emotion AI

## Development

```
$ docker-compose build dev
$ docker-compose up dev
```

Log in to shell

```
$ sudo docker exec -i -t emotionai_dev_1 /bin/bash
```

Remove unused images

```
$ docker rmi $(docker images -f "dangling=true" -q)
```

### Deploy

```
$ heroku container:push web
```




<!-- Build a Docker image -->
<!--  -->
<!-- ``` -->
<!-- docker build -t emotion-ai . -->
<!-- ``` -->
<!--  -->
<!-- Run a Docker container -->
<!--  -->
<!-- ``` -->
<!-- docker run -->
<!-- ``` -->
