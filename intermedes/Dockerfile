FROM alpine/socat:latest

RUN apk add python3 py3-pip gcc libc-dev
RUN pip3 install pycryptodome gmpy2 inputimeout

RUN adduser ctf --disabled-password
WORKDIR /home/ctf
COPY v1.py .
COPY vulpin.txt .
COPY test.txt .

USER ctf
EXPOSE 4000

CMD [ "-d","-d","tcp-listen:4000,reuseaddr,fork", "exec:'python3 v1.py'" ]

#bon en vrai faut changer les ports
