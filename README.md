Create EC2 --- with basic configuration -- my os is Ubuntu
Connect EC2 or make a remote-ssh through vs-code
    .config/
      Host public_ip
      HostName public_ip
      User ubuntu(os_name)
      IdentityFile path_of_.pem file
  save it ---- and connect to host ---- check your public_ip and connect it.
open folder home/ubuntu
create folder via terminal  
# mkdir openWeather_etl
go inside 
# cd openWeather_etl
make file main.py
# touch main.py
  write your data extraction code--- see main.py file in repo
