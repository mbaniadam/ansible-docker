# Provisioning and configuring infrastructure using Terraform and Ansible, as well as implementing Continuous Deployment with Jenkins.
## Application: Get Linux system metrics via RestAPI  

This repository focuses on automating infrastructure provisioning and configuration using Terraform and Ansible, while also implementing a Continuous Deployment pipeline with Jenkins.

Additionally, I have developed a sample Flask API server with Python for automatic deployment on the Hetzner cloud provider.

This API server provides some system metrics such as current date and time, memory and CPU usage using the psutil library. It is protected with SSL using Caddy v2.

### Prerequisites
Before you begin make sure you have met the following requirements;

- Hetzner Cloud account and an API token.
- Github Token for Jenkins
- Linux machine with Ansible and Terraform installed.
- Docker Hub account and an API token to push image.


### Step 1: Create a Virtual Server on Hetzner Cloud, then Install Docker and Configure iptables
- Clone this repository to your local machine.
```console bash
git clone https://github.com/mbaniadam/get-linux-metric-api.git
```
- Set up your Hetzner Cloud API token in the variables.tfvars file.
- Create SSH key pair for authentication
```console bash
ssh-keygen -t rsa -m PEM
```
- Run Terraform to create the virtual server:
```console bash
terraform apply 
```
This will create the virtual server and copy your SSH public key onto it.
Uses Ansible to install Docker and configure iptables on the VM.


### Step 2: CI/CD Pipeline with Jenkins
- Set up Jenkins and install necessary plugins.(publish-over-ssh)

**_NOTE:_**  You can use my ansible playbook in the ansible directory of this repository for this purpose.

Repository address:
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
                checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[credentialsId: 'github_token', url: 'https://github.com/mbaniadam/get-linux-metric-api.git']])
            }
        }
    
        stage('Build docker image') {
            steps {
                sh 'docker build --network host -t mortalbm/lininfo:v1.0 -f Ansible-Configure/Build-Run-Docker/Dockerfile .'
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
                sshPublisher(publishers: [sshPublisherDesc(configName: '<USER>@<YOUR_SERVER_PUBLIC_IP>', transfers: [sshTransfer(cleanRemote: false, excludes: '', execCommand: 'docker-compose -f Ansible-Configure/Build-Run-Docker/docker-compose.yml up -d', execTimeout: 120000, flatten: false, makeEmptyDirs: false, noDefaultExcludes: false, patternSeparator: '[, ]+', remoteDirectory: '', remoteDirectorySDF: false, removePrefix: '', sourceFiles: 'Ansible-Configure/Build-Run-Docker/')], usePromotionTimestamp: false, useWorkspaceInPromotion: false, verbose: false)])
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
### After the successful build, the pushed image will be deployed to the machine in the Hetzner cloud during the deployment phase. 
### Accessing the API

After completing the setup, the program will be listening on port 443, and you can send a GET request to VM public IP address to receive system metrics in JSON format.

Make sure to replace placeholders (**YOUR_SERVER_PUBLIC_IP**, USER, etc.) with your actual values.

Feel free to customize this README.md as needed and add any additional information or details specific to your project.

