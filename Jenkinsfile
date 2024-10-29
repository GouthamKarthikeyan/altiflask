pipeline {
    agent any 
    stages {
        stage('checkout scm'){
            steps{
                checkout scmGit(branches: [[name: '*/master']], extensions: [], userRemoteConfigs: [[credentialsId: '134af28f-bfc1-43b0-83a6-01ce48185589', url: 'https://github.com/GouthamKarthikeyan/altiflask.git']])
            }
        }
        stage('Build') { 
            steps {
                git branch: 'master', url: 'https://github.com/GouthamKarthikeyan/altiflask.git'
                sh 'python3 app.py'
            }
        }
        stage('Test'){
            steps {
                sh 'python3 -m pytest'
            }
        }
    }
}
