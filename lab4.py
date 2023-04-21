

# Reverse your configuration 

# Disable SMB v1 client driver
Set-SmbClientConfiguration -EnableSMB1Protocol $false
# Enable password complexity requirements
$LocalPolicy = Get-Item -Path "HKLM:\SYSTEM\CurrentControlSet\Services\Netlogon\Parameters"
$LocalPolicy."requirecomplexpasswords" = 1




# Configure SMB v1 client driver
Set-ItemProperty -Path "HKLM:\SYSTEM\CurrentControlSet\Services\LanmanWorkstation\Parameters" -Name "SMB1" -Type DWORD -Value 0 -Force

# Set password complexity requirements
$policy = Get-WmiObject -Class Win32_AccountPolicy -Namespace "root\SecurityCenter2"
$policy.PasswordComplexity = 1
$policy.Put()
