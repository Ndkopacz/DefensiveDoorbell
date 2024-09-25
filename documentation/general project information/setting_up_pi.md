#

# Commands run for setting up the pi
## Connectin to wifi
```
sudo apt update 
sudo apt upgrade -y
sudo apt install network-manager -y
sudo nano /etc/netplan/50-cloud-init.yaml
```
once in the .yaml file make sure it matches the following
```
network:
  version: 2
  renderer: NetworkManager
  ethernets:
    eth0:
      dhcp4: true
  wifis:
    wlan0:
      dhcp4: true
      access-points:
        "Your_SSID":
          password: "Your_WiFi_Password"
```
Then run the following
```sudo netplan apply```
And to check the connection use ```nmcli device status```

## Changing the hostname
```sudo nano /etc/hostname``` and changing the name in there to the new name ADAM
```sudo nano /etc/hosts``` and adding the line ```127.0.1.1   ADAM```

## Setting up ssh
Ensure that TWO files have ```PasswordAuthentication yes``` in them. These files are ```/etc/ssh/sshd_config``` and ```/etc/ssh/sshd_config.d/50-cloud-init.conf``` Typically the .conf file will have it set to "no" which really messes you up.
Restart the ssh ```systemctl restart ssh.service```


Check the logs for errors if needed```sudo cat /var/log/auth.log | grep ssh```

## Releasing the IP address and getting a dedicated one from the router
Reserve the IP address in the routers homepage "192.168.1.1" it will link the MAC address of the server to the new ip address
restart Network Manager on the server ```sudo systemctl restart NetworkManager```

Probably don't need to do all that. Just make sure to hit "apply" on the router website lol
