#$Hello = "Hello, Powershell"
#Write-Host($Hello)

function getIP{
(Get-NetIPAddress).ipv4address | Select-String "192*"
}

$IP = getIP
Write-Host("This machines IP is $IP")
