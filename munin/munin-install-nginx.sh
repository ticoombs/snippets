#!/bin/bash
sudo apt-get install -y libwww-perl && \
    sudo munin-node-configure --suggest --shell | sudo bash && \
    sudo munin-run nginx_status && \
    sudo service munin-node restart
