pipeline {
    agent any

    stages{
        stage('Activate Conda Envs') {
            steps{
                sh """#!/usr/bin/env bash
                   source /opt/conda/etc/profile.d/conda.sh
                   conda activate maotai
                   """
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