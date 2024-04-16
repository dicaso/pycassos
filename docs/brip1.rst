# To run container with Windows powershell

    mkdir C:\Users\$ENV:USERNAME\data # if data folder does not exist yet
    docker run -it pycassos -v C:\Users\$ENV:USERNAME\data:/root/LSData/private /bin/bash

# TODO

- debug centromereshg38 = LSD.get_centromeres()
