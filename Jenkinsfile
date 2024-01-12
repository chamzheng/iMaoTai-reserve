pipeline {
    agent any

    environment {
        HTTPS_PROXY = 'socks5://192.168.30.7:7899'
        HTTP_PROXY  = 'socks5://192.168.30.7:7899'
    }

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