# ASA-Project

This repository contains a step-by-step guide to set up a cloud-based Flask API server on Hetzner Cloud using Terraform, Ansible, Docker, and Jenkins CI/CD pipeline. The API server provides system metrics using the psutil library and is secured with SSL via Caddy v2.

### Prerequisites
Before getting started, ensure you have the following prerequisites in place:

- Hetzner Cloud account and an API token.
- Github Token for Jenkins
- SSH key pair for authentication (generate using ssh-keygen -t rsa -m PEM).
- Linux machine with Ansible and Terraform installed.
  


### Step 1: Create a Virtual Server on Hetzner Cloud
- Clone this repository to your local machine.
```console bash
git clone https://github.com/mbaniadam/ASA-Project.git
```
- Set up your Hetzner Cloud API token in the variables.tfvars file.
- Run Terraform to create the virtual server:
```console bash
terraform apply --var-file variables.tfvars
```

This will create the virtual server and copy your SSH public key onto it.

### Step 2: Install Docker and Configure iptables
Use Ansible to install Docker and configure iptables on the VM. Ensure Ansible is installed on your local machine.
add VM public IP to the inventory.yml.
Run the playbook:
```console bash
ansible-playbook - inventory.yml
```

### Step 3: CI/CD Pipeline with Jenkins
- Set up Jenkins and install necessary plugins.
**Note**
  You can use my ansible playbook in the ansible directory of this repository for this purpose:
  ```console bash
  git clone https://github.com/mbaniadam/ansible-role-jenkins-via-terraform.git
  ```
- Add Github token and DockerHub token to the Credentials section.
- Create a Pipline
```console
pipeline {
    agent any
    
    environment {
        DOCKER_HUB = credentials('docker_hub')
    }


    stages {
        stage('Hello') {
            steps {
                checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[credentialsId: 'github_token', url: 'https://github.com/mbaniadam/ASA-Project.git']])
            }
        }
    
        stage('Build docker image') {
            steps {
                sh 'docker build --network host -t mortalbm/lininfo:v1.0 -f N4/Dockerfile .'
            }
        }
        
        stage('Login docker hub') {
            steps {
                sh 'echo $DOCKER_HUB_PSW | docker login -u $DOCKER_HUB_USR --password-stdin'
            }
        }
        
        stage('Push image to docker hub') {
            steps {
                sh 'docker push mortalbm/lininfo:v1.0'
            }
        }
        
        stage('Deploy to server') {
            steps {
                sshPublisher(publishers: [sshPublisherDesc(configName: '<USER>@<YOUR_SERVER_PUBLIC_IP>', transfers: [sshTransfer(cleanRemote: false, excludes: '', execCommand: 'docker-compose up -f N4/docker-compose.yml up -d', execTimeout: 120000, flatten: false, makeEmptyDirs: false, noDefaultExcludes: false, patternSeparator: '[, ]+', remoteDirectory: '', remoteDirectorySDF: false, removePrefix: '', sourceFiles: 'N4/')], usePromotionTimestamp: false, useWorkspaceInPromotion: false, verbose: false)])
            }
        }
    
    }
    post {
        always {
            sh 'docker logout'
        }
    }
}
```

### Accessing the API
After completing the setup, the program will be listening on port 443, and you can send a GET request to VM public IP address to receive system metrics in JSON format.

Make sure to replace placeholders (**YOUR_SERVER_PUBLIC_IP**, USER, etc.) with your actual values.

Feel free to customize this README.md as needed and add any additional information or details specific to your project.

