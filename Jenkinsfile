pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                git branch: 'main',
                    url: 'your-repository-url'
            }
        }
        stage('Build') {
            steps {
                sh 'python3 -m py_compile sources/*.py'
            }
        }
        stage('Test') {
            steps {
                sh 'python3 -m pytest --junit-xml=test-reports/results.xml'
            }
        }
        stage('Deliver') {
            steps {
                sh 'python3 setup.py bdist_wheel'
            }
        }
    }
}
