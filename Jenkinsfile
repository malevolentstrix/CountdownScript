pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo "Hello Welcome"
                sh 'make'
                sh 'echo "Something wierd'
                archiveArtifacts artifacts: '**/target/*.jar', fingerprint: true
            }
        }
    }
}
