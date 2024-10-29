#!/bin/sh

set -e

# Abort if DEVICE_CONNECTION_STRING is not set as environment variable
if [ -z "$DEVICE_CONNECTION_STRING" ]; then
    echo "DEVICE_CONNECTION_STRING is not set. Aborting."
    exit 1
fi

# Print OS information to confirm the OS version is Ubuntu 22.04
uname -a

# Install iotedge
wget https://packages.microsoft.com/config/ubuntu/22.04/packages-microsoft-prod.deb -O packages-microsoft-prod.deb
dpkg -i packages-microsoft-prod.deb
rm packages-microsoft-prod.deb

# Install moby-engine
apt-get update
apt-get install -y moby-engine

# Set docker daemon.json
echo '{"log-driver": "local"}' | tee /etc/docker/daemon.json
systemctl restart docker

# Install iotedge
apt-get update
apt-get install -y aziot-edge

# Download config.toml
mkdir -p /etc/aziot
wget https://raw.githubusercontent.com/Azure/iotedge-vm-deploy/master/config.toml -O /etc/aziot/config.toml

# Set connection string
sed -i "s#\(connection_string = \).*#\1\"$DEVICE_CONNECTION_STRING\"#g" /etc/aziot/config.toml

# Apply config
iotedge config apply -c /etc/aziot/config.toml

# Check iotedge status
iotedge check --verbose
