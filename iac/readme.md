# Install Docker (linux)
## 1. Set up the repository
### Update the apt package index and install packages to allow apt to use a repository over HTTPS:

    sudo apt-get update

    sudo apt-get install ca-certificates curl gnupg lsb-release

### Add Docker’s official GPG key:

    sudo mkdir -p /etc/apt/keyrings

    curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg

### Use the following command to set up the repository:

    echo \
    "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
    $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

---
## 2. Install Docker Engine
### Update the apt package index:

    sudo apt-get update

### Install Docker Engine, containerd, and Docker Compose.

    sudo apt-get install docker-ce docker-ce-cli containerd.io docker-compose-plugin

### Verify that the Docker Engine installation is successful by running the hello-world image:

    sudo docker run hello-world

## 3. Manage Docker as a non-root user

### Create the docker group.

    sudo groupadd docker

### Add your user to the docker group. (Change USER for you user)

    sudo usermod -aG docker $USER

### Log out and log back in so that your group membership is re-evaluated.

    If you’re running Linux in a virtual machine, it may be necessary to restart the virtual machine for changes to take effect.

You can also run the following command to activate the changes to groups:

    newgrp docker

### Verify that you can run docker commands without sudo.

    docker run hello-world
# Run commands to create containers from repository

Now you are able to build and run containers.
These commands will create an start the containers needed for testing the services defined on the project.

    docker compose -f iac/docker-compose.yml -p fake_wiga up -d --build

You should now see the app on the web browser, to check it out visit: [app](http://localhost:80)