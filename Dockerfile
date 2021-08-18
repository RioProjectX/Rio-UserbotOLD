# Using Python Slim-Buster
FROM vckyouuu/geezprojects:buster
# Halo kak yahaha
# RIO-UBOT
#
RUN git clone -b KEN-UBOT https://github.com/RioProjectX/Rio-Userbot /root/userbot
RUN mkdir /root/userbot/.bin
RUN pip install --upgrade pip setuptools
WORKDIR /root/userbot

#Install python requirements
RUN pip3 install -r https://raw.githubusercontent.com/RioProjectX/RIO-UBOT/RIO-UBOT/requirements.txt

EXPOSE 80 443

# Finalization
CMD ["python3","-m","userbot"]
