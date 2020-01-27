$h = "Hello" 
$w = "world"
$hw = $h + " " + $w
Write-Host $hw

[bool](([System.Security.Principal.WindowsIdentity]::GetCurrent()).groups -match"S-1-5-32-544")
