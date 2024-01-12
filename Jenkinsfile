pipeline {
    agent any

    stages{
        stage('Install dependencies') {
            steps{
                sh "python -m pip install --upgrade pip"
                sh "pip install -r requirements.txt"
            }
        }
    }

    post {
        always {
            deleteDir()
        }
    }

}