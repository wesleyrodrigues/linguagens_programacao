function Diga-Algo {
    param( $String )
    Write-Host "Você diz -- $String!"
}

Diga-Algo -String 'Algo'

# dir *.txt | ForEach-Object {mv $_ '.\infos txt\'}
