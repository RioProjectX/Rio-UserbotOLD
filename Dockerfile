# Using Python Slim-Buster
FROM vckyouuu/geezprojects:buster
# Halo kak yahaha
# RIO-UBOT
#
RUN git clone -b Rio-Userbot https://github.com/RioProjectX/Rio-UserbotNEW /root/userbot
RUN mkdir /root/userbot/.bin
RUN pip install --upgrade pip setuptools
WORKDIR /root/userbot

#Install python requirements
RUN pip3 install -r https://raw.githubusercontent.com/RioProjectX/Rio-Userbot/Rio-Userbot/requirements.txt

EXPOSE 80 443

# Finalization
CMD ["python3","-m","userbot"]
