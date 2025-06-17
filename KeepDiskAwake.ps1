while ($true) {
    $drives = @("J:\", "H:\")
    foreach ($drive in $drives) {
        try {
            $file = Join-Path $drive ("keepalive_" + [guid]::NewGuid().ToString() + ".tmp")
            $data = [byte[]]::new(10240)
            (New-Object System.Random).NextBytes($data)
            [System.IO.File]::WriteAllBytes($file, $data)
            Write-Host "Written to $file"
            Remove-Item $file -Force
        } catch {
            Write-Warning "Failed to access $drive : $_"
        }
    }
    Start-Sleep -Seconds 180
}
