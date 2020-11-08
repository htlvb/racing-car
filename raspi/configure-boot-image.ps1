param (
    [Parameter(Mandatory=$true)][string]$driveLetter,
    [System.Management.Automation.PSCredential]
    [System.Management.Automation.Credential()]
    $wifiCredential = $(Get-Credential -Message "WIFI credentials (User => Network SSID)")
)

$wifiSetupConfig = @"
ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
update_config=1

network={
    ssid="$($wifiCredential.UserName)"
    psk="$($wifiCredential.GetNetworkCredential().Password)"
    scan_ssid=1
    key_mgmt=WPA-PSK
}
"@
Set-Content "${driveLetter}:\wpa_supplicant.conf" $wifiSetupConfig

New-Item "${driveLetter}:\ssh" -Force | Out-Null

$file = "${driveLetter}:\config.txt"
(Get-Content $file) `
    -replace "^#(?=dtparam=i2c_arm=on$)","" `
    -replace "^#(?=dtparam=spi=on$)","" `
    | Set-Content $file -Encoding UTF8
