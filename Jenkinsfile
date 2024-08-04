pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                sh 'make'
                sh 'echo "Something wierd'
                archiveArtifacts artifacts: '**/target/*.jar', fingerprint: true
            }
        }
    }
}