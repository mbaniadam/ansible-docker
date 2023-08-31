pipeline {
  agent any
  stages {
    stage('Checkout Code') {
      steps {
        git 'https://github.com/mbaniadam/ASA-Project.git'
      }
    }

    stage('Build ') {
      steps {
        sh 'docker build -f N4/Dockerfile .'
      }
    }

  }
}