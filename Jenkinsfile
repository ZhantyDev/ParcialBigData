pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Instalacion') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Pruebas Básicas') {
            steps {
                // Validar que el CSV existe antes de correr el ML
                sh 'test -f data/sdss_sample.csv'
            }
        }
        stage('Ejecucion Principal') {
            steps {
                sh 'python main.py'
            }
        }
    }
    post {
        always {
            // Guarda los resultados en la interfaz de Jenkins
            archiveArtifacts artifacts: 'outputs/*.*', fingerprint: true
        }
    }
}