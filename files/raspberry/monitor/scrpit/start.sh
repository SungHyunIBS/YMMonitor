#!/bin/bash
#sleep 60
sleep 30
sudo supervisorctl start ssh_tunnel
sudo supervisorctl start run_cam
sudo supervisorctl start run_UA10

