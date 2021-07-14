####DOCKERFILE####
FROM python:3.8

WORKDIR /app

COPY . .

CMD python hello-world.py
###END DOCKERFILE###

####.dockerignore####
Dockerfile
###END DOCKERFILE###


####hello-world.py####
print("Hello world")

####END .py############
