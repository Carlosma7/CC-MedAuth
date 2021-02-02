# Update apt packages
sudo apt-get update

# Get GPG and add key of Docker
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | apt-key add -

# Add Docker repository and update packages
add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" && apt update

# Install Docker
sudo apt-get install -y docker-ce

# Add root user to docker group
gpasswd -a root docker

# Install Docker-compose
wget https://github.com/docker/compose/releases/download/1.28.2/docker-compose-Linux-x86_64 -O /usr/local/bin/docker-compose && chmod u+x /usr/local/bin/docker-compose

# Clone GitHub MedAuth repository
git clone https://github.com/Carlosma7/MedAuth.git

# Build project as daemon
docker-compose up -d
