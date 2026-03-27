Write-Host "--- Iniciando configuración del entorno ---" -ForegroundColor Cyan

# 1. Crear el entorno virtual
python -m venv venv

# 2. Activar el entorno virtual
.\venv\Scripts\Activate.ps1

# 3. Actualizar pip
python -m pip install --upgrade pip

# 4. Instalar dependencias
if (Test-Path requirements.txt) {
    pip install -r requirements.txt
    Write-Host "--- Dependencias instaladas con éxito ---" -ForegroundColor Green
} else {
    Write-Host "Error: No se encontró el archivo requirements.txt" -ForegroundColor Red
}

Write-Host "--- Proceso finalizado ---"