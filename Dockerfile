FROM python:3.10

RUN groupadd --gid 1000 azamat \
  && useradd --uid 1000 --gid azamat --shell /bin/bash --create-home azamat

WORKDIR /home/azamat
USER azamat

RUN echo "export PATH=\"/home/azamat/.local/bin:\$PATH\"" >> ~/.bashrc
RUN . ~/.bashrc

COPY ./src /home/azamat/src
COPY ./requirements.txt /home/azamat/requirements.txt

RUN pip3 install -r requirements.txt --no-warn-script-location

EXPOSE 8000
