# Pegar o diretorio atual

$scriptDirectory = Split-Path -Path $MyInvocation.MyCommand.Definition -Parent

# Arquivo de saída 
$outputFile = Join-Path -Path $scriptDirectory -ChildPath "migration.sql"

# Verifica se arquivo já existe 

if (Test-Path $outputFile){
    Remove-Item $outputFile
}

# Pega conteúdo dos arquivos 

$sqlFiles = Get-ChildItem -Path $scriptDirectory -Filter *.sql -File | Sort-Object Name

# Concatena arquivos 

foreach($file in $sqlFiles){
    Get-Content $file.FullName | Out-File -Append -FilePath $outputFile
    "GO" | Out-File -Append -FilePath $outputFile
}

Write-Host "Todos os Arquivos foram combinados em $outputFile"