pipeline {
    agent any
    
    stages {
        stage('Checkout') {
            steps {
                // Esto ya lo hace Jenkins automáticamente, pero si lo tienes manual:
                checkout scm
            }
        }

        stage('Instalacion') {
            steps {
                // CAMBIO: Usamos 'bat' y 'python -m pip' para asegurar que encuentre pip
                bat 'python -m pip install --upgrade pip'
                bat 'python -m pip install -r requirements.txt'
            }
        }
        
        stage('Ejecucion Principal') {
            steps {
                // Creamos la carpeta desde Windows antes de correr el python
                bat 'if not exist outputs mkdir outputs'
                bat 'python main.py'
            }
        }

        stage('Pruebas Básicas') {
            steps {
                // CAMBIO: 'test -f' es de Linux. En Windows se usa 'if exist'
                bat 'if not exist data\\sdss_sample.csv (exit 1)'
                echo 'Validación de datos exitosa.'
            }
        }

        stage('Ejecucion Principal') {
            steps {
                // CAMBIO: Usamos 'bat'
                bat 'python main.py'
            }
        }
    }
    
    post {
        always {
            // Esto está bien, guarda tus gráficas
            archiveArtifacts artifacts: 'outputs/*.*', fingerprint: true
        }
    }
}