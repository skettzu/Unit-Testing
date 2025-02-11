pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                sh 'python3 -m py_compile sources/*.py'
            }
        }
        stage('Test') {
            steps {
                sh 'python3 -m pytest'
            }
        }
        stage('Deliver') {
            steps {
                sh 'python3 setup.py bdist_wheel'
            }
        }
    }
}
