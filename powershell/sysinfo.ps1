function getIP{
(Get-NetIPAddress).ipv4address | Select-String "192*"
}

function getUser{
(Get-LocalUser) | Select-String "Admin*"
}

function getHostName{
(Get-ComputerInfo).CsDNSHostName
}

$IP = getIP
$USER = getUSER
$HOSTNAME = getHostName
$DATE =Get-Date

$BODY="This machine's ip address is $IP. The user logged in is $USER. The DNS hostname is $HOSTNAME. Right now, the time is $DATE"

Send-MailMessage -To "botheaj@ucmail.uc.edu" -From "xavierbaszuk@gmail.com" -Subject "IT3038C Windows SysInfo" -Body $BODY -SmtpServer smtp.gmail.com -Port 587 -UseSsl -Credential (Get-Credential)

