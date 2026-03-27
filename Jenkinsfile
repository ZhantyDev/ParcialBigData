pipeline {
    agent any
    stages {
        stage('Instalación de Librerías') {
            steps {
                // Usamos 'bat' en lugar de 'sh' para Windows
                bat 'pip install --upgrade pip'
                bat 'pip install -r requirements.txt'
            }
        }
        stage('Ejecución del Modelo') {
            steps {
                // Ejecuta tu script de astronomía
                bat 'python main.py'
            }
        }
    }
    post {
        always {
            archiveArtifacts artifacts: 'outputs/*.*', fingerprint: true
        }
    }
}