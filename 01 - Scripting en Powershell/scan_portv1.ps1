# Escaneo de equipos activos en la subred

# Determinando gateway
$subred = (Get-Netroute -DestinationPrefix 0.0.0.0/0).NextHop
Write-host "== Determinando tu gateway . . ."
Write-Host "Tu gateway: $subred"

# Determinando rango de subred
$rango = $subred.Substring(0,$subred.IndexOf('.') + 1 + $subred.Substring($subred.IndexOf('.') + 1).IndexOf('.') + 3 )
Write-host "== Determinando tu rango de subred . . ."
echo $rango

# Determinando si $rango termina en "."
# En ocasiones el rango de subred no termina en punto, necesitamos forzarlo.
$punto = $rango.EndsWith('.')
if ($punto -like "False")
{
    $rango = $rango + '.'
}

# Definimos un array con puertos a escanear
# Establecemos una variable para waittime
$portstoscan = @(20,21,22,23,25,50,51,53,80,110,119,135,136,137,138,139,143,161,162,389,443,445,636,1025,1443,3389,5985,5986,8080,100000)
$waittime=100

# Solicitamos direccion ip a escanear:
Write-host "Direccion ip a escanear: " -NoNewLine
$direccion = Read-host

## Generamos un bucle foreach para evaluar cada puerto en $portstoscan
foreach ($p in $portstoscan)
{
    $TCPObject = new-object System.Net.Sockets.TcpClient
        try{ $resultado = $TCPObject.ConnectAsync($direccion,$p).Wait($waittime)}catch{}
    if ($resultado -eq "True")
    {
        write-host "Puerto abierto: " -NoNewLine; write-host $p -Foregroundcolor green
    }
}