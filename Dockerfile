FROM lintao0o0/baseofencrypter:0.1

WORKDIR /encrypter

COPY ./encrypter.py /encrypter/

RUN ["mkdir" , "/encrypter/encryptfolder"]

CMD ["/bin/bash"]

