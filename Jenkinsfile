pipeline {
    agent any

    stages{
        stage('initWorkspace') {
            steps{
                echo "123"
            }
        }
    }

    post {
        always {
            deleteDir()
        }
    }

}