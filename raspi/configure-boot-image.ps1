param (
    [Parameter(Mandatory=$true)][string]$driveLetter,
    [System.Management.Automation.PSCredential]
    [System.Management.Automation.Credential()]
    $wifiCredential = $(Get-Credential -Message "WIFI credentials (User => Network SSID)")
)

$wifiSetupConfig = @"
ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
update_config=1
ap_scan=1
fast_reauth=1
country=JP

network={
    ssid="$($wifiCredential.UserName)"
    psk="$($wifiCredential.GetNetworkCredential().Password)"
    id_str="0"
    priority=100
}
"@
Set-Content "${driveLetter}:\wpa_supplicant.conf" $wifiSetupConfig

New-Item "${driveLetter}:\ssh" -Force | Out-Null
