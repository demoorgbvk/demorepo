pipeline {
    agent any
    parameters {
        string(name: 'inputvar', description: "Hello test params", defaultValue: 'testparams')
    }
    stages {
        stage('Build') {
            steps {
                echo "Building..${params.inputvar}"
            }
        }
        stage('Test') {
            steps {
                echo 'Testing..'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
            }
        }
    }
}
