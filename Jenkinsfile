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
                sh 'python3 -m coverage run -m unittest discover -v -s tests
                    python3 -m coverage xml -o test-reports/coverage.xml
                    python3 -m coverage report'
            }
        }
        stage('Deliver') {
            steps {
                sh 'python3 setup.py bdist_wheel'
            }
        }
    }
}
