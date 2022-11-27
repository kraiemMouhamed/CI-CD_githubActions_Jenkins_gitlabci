pipeline {
    agent any

    environment {
      DOCKERHUB_CREDENTIALS=credentials('docker-hub')
      DOCKER_TAG = getVersion()
    }
    // This pipeline will be executed using jenkins service
    // We add all credentials to the jenkins server
    // Jenkins service needs to be able to execute docker commands
    stages{
        stage('Checkout github repository'){
            steps{
                git branch: 'main', 
                url: 'https://github.com/kraiemMouhamed/CI-CD_githubActions_Jenkins_gitlabci.git'
            }
        }
        
        stage('Docker Build'){
            steps{
                sh "docker build . -t kraiembechir/dockerJenkins:${DOCKER_TAG} "
            }
        }
        stage('DockerHub Push'){
            steps{
                sh 'echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin'
                sh "docker push kraiembechir/dockerJenkins:${DOCKER_TAG} "
                
            }
        }
    }
}

def getVersion(){
    def commitHash = sh label: '', returnStdout: true, script: 'git rev-parse --short HEAD'
    return commitHash
}