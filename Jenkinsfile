pipeline {
    agent any
    stages {
        stage('Setup') {
            steps {
                sh 'python3 -m pip install -r requirements.txt'
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
