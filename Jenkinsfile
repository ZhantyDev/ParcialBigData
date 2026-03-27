pipeline {
    agent any
    
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Preparacion e Instalacion') {
            steps {
                // Instalamos librerías
                bat 'python -m pip install --upgrade pip'
                bat 'python -m pip install -r requirements.txt'
                // Creamos la carpeta de salida si no existe para evitar el error de Python
                bat 'if not exist outputs mkdir outputs'
            }
        }

        stage('Validacion de Datos') {
            steps {
                bat 'if not exist data\\sdss_sample.csv (exit 1)'
                echo 'Dataset encontrado.'
            }
        }

        stage('Ejecucion del Modelo') {
            steps {
                // Corremos el script de Big Data
                bat 'python main.py'
            }
        }
    }

    post {
        always {
            // Esto permite que descargues la Matriz de Confusión desde Jenkins
            archiveArtifacts artifacts: 'outputs/*.png', allowEmptyArchive: true
        }
    }
}