pipeline {
    agent any

    environment {
        IMAGE_NAME = 'flask-app'
        CONTAINER_NAME = 'flask-container'
        PORT = '50001'
    }

    stages {
        stage('Clone Repo') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                sh "docker build -t $IMAGE_NAME ."
            }
        }

        stage('Stop Old Container') {
            steps {
                sh "docker rm -f $CONTAINER_NAME || true"
            }
        }

        stage('Run New Container') {
            steps {
                sh "docker run -d --name $CONTAINER_NAME -p $PORT:$PORT $IMAGE_NAME"
            }
        }
    }
}
