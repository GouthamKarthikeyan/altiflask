pipeline {
    agent any 

    parameters {
        string (name: 'ORG_NAME', defaultValue: 'ABC', description: 'Enter the org name')
    }
    
    stages {
        stage('Create Namespaces'){
            steps{
                script {
                    def namespaces = ['BitBucket' , 'Jenkins' , 'JFrog']
                    namespaces.each {tool ->
                        sh "kubectl create namespace ${params.ORG_NAME}-${tool} || echo 'Namespace exists'"
                    }
                }
            }
        }
        
        stage('Deploy Tools') { 
            steps {
                parallel (
                    "Deploy BitBucket" : {
                        sh "helm install bitbucket stable/bitbucket -n ${params.ORG_NAME}-BitBucket"
                    }
                     "Deploy Jenkins" : {
                        sh "helm install jenkins stable/jenkins -n ${params.ORG_NAME}-Jenkins"
                     }
                    "Deploy JFrog" : {
                        sh "helm install jfrog artifactory/jfrog-platform -n ${params.ORG_NAME}-JFrog"
                    }
                    )
            }
            }
        }
    post {
        success {
            echo "Deployment is successfull"
        }
        failure {
            echo "Deployment failed. Please check the logs"
        }
    }
}
