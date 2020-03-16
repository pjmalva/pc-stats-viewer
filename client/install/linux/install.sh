#!/bin/bash
echo "Initializing instalation ..."

echo "Getting bin path ..."
bin_path="${PWD}/bin/PCStatus"
startup_file_name="pc_status.service"
startup_file_path="/etc/systemd/system/${startup_file_name}"

echo "Creating startup file ..."
touch $startup_file_path

echo "Mounting startup script ..."
cat > $startup_file_path <<EOL
[Unit]
Description=Status View
After=multi-user.target
[Service]
Type=simple
WorkingDirectory=${PWD}/bin/
ExecStart=${bin_path}
[Install]
WantedBy=multi-user.target
EOL

echo "OK! That is ready."
echo "Creating config file ..."

mkdir "${PWD}/bin/config"
touch "${PWD}/bin/config/mid.json"

echo "Mounting config file ..."
cat > "${PWD}/bin/config/mid.json" <<EOL
{
    "mID": "",
    "cID": "",
    "interval": 5,
    "save_file": true,
    "server": "https://msv.mitrix.com.br/info/update/",
    "disks": []
}
EOL

echo "OK, now go to your config file end finish him..."
echo "Dont know how?? That's fine, go to https://github.com/pjmalva/pc-stats-viewer and see it..."

echo "That is ready too."
echo "Now we will restart the services for you, wait a minute..."

systemctl daemon-reload
systemctl enable $startup_file_name
systemctl start $startup_file_name

echo "NICE! Everything is done, enjoy it."
