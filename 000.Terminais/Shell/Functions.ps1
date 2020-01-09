function Set-Algo {
    param( $String, $N )
    Write-Host "Você diz -- $String com número $N!"
}

Set-Algo 'Algo' 10

# dir *.txt | ForEach-Object {mv $_ '.\infos txt\'}

# 1..10 | ForEach-Object {
#     Write-Host $_
# }