# Set the idle time

$idleTime = New-TimeSpan -Minutes 2

# Get the last input time

$lastInput = [Win32]::GetLastInputInfo()

# Calculate the idle time

$idleSeconds = [Environment]::TickCount - $lastInput.dwTime
if ($idleSeconds -ge $idleTime.TotalMilliseconds) {
    # Lock the screen
    rundll32.exe user32.dll,LockWorkStation
}