pipeline {
    agent any

    stages{
        stage('Activate Conda Envs') {
            steps{
                sh '''/opt/miniconda3/bin/conda activate maotai'''
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