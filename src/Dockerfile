FROM ubuntu:latest

RUN apt update
RUN apt install -y unzip xvfb libxi6 default-jdk wget

RUN wget http://archive.ubuntu.com/ubuntu/pool/universe/g/gconf/libgconf-2-4_3.2.6-4ubuntu1_amd64.deb
RUN apt install -y ./libgconf-2-4_3.2.6-4ubuntu1_amd64.deb

RUN wget --no-check-certificate https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
RUN apt install -y ./google-chrome-stable_current_amd64.deb

RUN wget --no-check-certificate -O chromedriver.zip https://storage.googleapis.com/chrome-for-testing-public/122.0.6261.94/linux64/chrome-linux64.zip
RUN unzip chromedriver.zip -d ./chromedriver
RUN mv ./chromedriver /usr/bin/chromedriver
RUN chown root:root /usr/bin/chromedriver
RUN chmod +x /usr/bin/chromedriver

COPY main.py ./main.py
COPY requirements.txt .

RUN apt install python3 python3-pip -y
RUN pip install --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host files.pythonhosted.org -r requirements.txt

COPY main.py ./main.py

ENV FLASK_APP=main.py
ENV FLASK_RUN_HOST=0.0.0.0

EXPOSE 5000

CMD ["flask", "run"]