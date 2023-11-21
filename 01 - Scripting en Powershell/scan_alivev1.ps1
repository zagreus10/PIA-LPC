# Escaneo de equipos activos en la subred

# Determinando gateway
$subred = (Get-Netroute -DestinationPrefix 0.0.0.0/0).NextHop
Write-Host "Tu gateway: $subred"

# Determinando rango de subred
$rango = $subred.Substring(0,$subred.IndexOf('.') + 1 + $subred.Substring($subred.IndexOf('.') + 1).IndexOf('.') + 3 )
echo $rango

# Determinando si $rango termina en "."
# En ocasiones el rango de subred no termina en punto, necesitamos forzarlo.
$punto = $rango.EndsWith('.')
if ($punto -like "False")
{
    $rango = $rango + '.'
}

# Creamos un array con 254 numeros y se almacenan
# en una variable que se llamara $rango_ip
$rango_ip = @(1..254)

# Generamos bucle foreach para validar hosts activos en nuestra subred
foreach ($r in $rango_ip)
{
    $actual = $rango + $r #se genera direccion ip
    $responde = Test-Connection $actual -Quiet -Count 1 # Validamos conecion contra ip en $actual
    if ( $response -eq "True")
    {
        write-output ""
        write-host "Host responde: " -NoNewLine; write-host $actual -Foregroundcolor Green
    }
}