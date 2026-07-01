pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/lokeshwaran22007-source/online-food-ordering.git'
            }
        }

        stage('Build') {
            steps {
                sh 'echo Build Successful'
            }
        }
    }
}
