Não execute esse arquivo inteiro multiplos erros

Get-ChildItem *.txt | ForEach-Object { Move-Item $_ '.\infos txt\' } # excecutavel
Cmdlet Get-ChildItem        Cmdlet ForEach-Object       Cmdlet Move-Item
ALIASES -> gci, ls, dir     ALIASES -> foreach, %       ALIASES -> mi, mv, move
# Key-words: listar, for, mover

Get-ChildItem comands.txt | Set-ItemProperty -Name IsReadOnly -Value $True # excecutavel
\\         \\               Cmdlet Set-ItemProperty 
\\         \\               ALIASES -> sp
# Key-words: propriedade item, legivel

New-Item '.\scripts.txt' | Rename-Item -NewName '.\apaga.txt' -PassThru | Remove-Item # excecutavel
Cmdlet New-Item             Cmdlet Rename-Item          Cmdlet Remove-Item
ALIASES -> ni               ALIASES -> rni, ren         ALIASES -> ri, rm, rmdir, del, erase, rd
# Key-words: novo, criar, renomear, remover

New-Item examplecopy.txt | Copy-Item -Destination '.\infos txt' # excecutavel
\\         \\               Cmdlet Copy-Item
\\         \\               ALIASES -> cpi, cp, copy
# Key-words: copiar

Get-Item *.txt | Invoke-Item # excecutavel
Cmdlet Get-Item             Cmdlet Invoke-Item
ALIASES -> gi               ALIASES -> ii
# Key-words: obter, chamar item, executar item

Get-ItemProperty .\alias.txt | Get-ItemPropertyValue -Name Name # excecutavel
Cmdlet Get-ItemProperty     Cmdlet Get-ItemPropertyValue
ALIASES -> gp               ALIASES -> gpv
# Key-words: Obter propriedade

Add-Content -Path .\*.txt -Exclude comands* -Value 'End of file'  # excecutavel
1..100 | ForEach-Object { Add-Content -Path .\LineNumbers.txt -Value "This is line $_." }  # excecutavel
\\         \\               Cmdlet Add-Content
\\         \\               ALIASES -> ac 
# Key-words: Adicionar linha, texto

(Get-Content -Path .\LineNumbers.txt -TotalCount 25)[-10, -1, 3]  # excecutavel
Cmdlet Get-Content
ALIASES -> gc, cat, type
# Key-words: Ler arquivo, linha, texto

Set-Item -Path alias:np -Value "c:\windows\notepad.exe" # excecutavel
Cmdlet Set-Item
ALIASES -> si 
# Key-words: definir item, alias

Get-Process | Sort-Object –p CPU | Select-Object –last 5
Cmdlet Get-Process          Cmdlet Sort-Object          Cmdlet Select-Object
ALIASES -> gps, ps          ALIASES -> sort             ALIASES -> select 
# Key-words: Oter processos, listar, ordenar, selecionar

Start-Process -FilePath "notepad" -Wait -WindowStyle Minimized  # excecutavel
Cmdlet Start-Process
ALIASES -> saps, start
# Key-words: iniciar processo

Stop-Process -Name notepad # excecutavel
Cmdlet Stop-Process
ALIASES -> spps, kill
# Key-words: parar processo

Set-Location '.\infos txt' # excecutavel
Cmdlet Set-Location
ALIASES -> sl, cd, chdir
# Key-words: definir pasta, diretório

Get-Location
Cmdlet
ALIASES -> 

\\         \\
\\         \\

