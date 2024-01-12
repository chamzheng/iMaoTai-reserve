pipeline {
    agent { image 'python:latest' }

    stages{
        stage('Activate Conda Envs') {
            steps{
                sh '''#!/bin/bash
                      . /opt/miniconda3/bin/activate maotai'''
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