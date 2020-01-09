Não execute esse arquivo inteiro multiplos erros
Linhas executaveis: 4, 10, 16, 21, 26, 31

Get-ChildItem *.txt | ForEach-Object { Move-Item $_ '.\infos txt\' } # excecutavel

Cmdlet Get-ChildItem        Cmdlet ForEach-Object       Cmdlet Move-Item
ALIASES -> gci, ls, dir     ALIASES -> foreach, %       ALIASES -> mi, mv, move


Get-ChildItem comands.txt | Set-ItemProperty -Name IsReadOnly -Value $True # excecutavel

\\         \\               Cmdlet Set-ItemProperty 
\\         \\               ALIASES -> sp


New-Item '.\scripts.txt' | Rename-Item -NewName '.\apaga.txt' -PassThru | Remove-Item # excecutavel

Cmdlet New-Item             Cmdlet Rename-Item          Cmdlet Remove-Item
ALIASES -> ni               ALIASES -> rni, ren         ALIASES -> ri, rm, rmdir, del, erase, rd

Start-Process -FilePath "notepad" -Wait -WindowStyle Minimized  # excecutavel

Cmdlet Start-Process
ALIASES -> saps, start

Stop-Process -Name notepad # excecutavel

Cmdlet Stop-Process
ALIASES -> spps, kill

Set-Location '.\infos txt' # excecutavel

Cmdlet Set-Location
ALIASES -> sl, cd, chdir

Clear-Item
Clear-ItemProperty
Copy-Item
Copy-ItemProperty
Get-Item
Get-ItemProperty
Get-ItemPropertyValue
Invoke-Item
Move-ItemProperty
New-ItemProperty 
Remove-ItemProperty
Rename-ItemProperty
Set-Item -Path alias:np -Value "c:\windows\notepad.exe"




