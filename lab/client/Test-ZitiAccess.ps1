param(
    [Parameter(Mandatory = $true)]
    [ValidateSet('Alice', 'Bob')]
    [string]$Mode,
    [string]$Url = 'http://portal.ziti.internal/'
)

$ErrorActionPreference = 'Stop'
$timestamp = Get-Date -Format 'yyyy-MM-ddTHH:mm:ssK'
Write-Host "[$timestamp] Test identity mode: $Mode"
Write-Host 'Đảm bảo chỉ identity tương ứng đang bật trong Ziti Desktop Edge.'

try {
    $response = Invoke-WebRequest -Uri $Url -Method Head -TimeoutSec 15 -UseBasicParsing
    Write-Host "HTTP status: $([int]$response.StatusCode)"
    if ($Mode -eq 'Alice') {
        Write-Host 'PASS candidate: Alice truy cập được. Cần lưu ảnh client identity và policy-advisor.'
        exit 0
    }
    Write-Error 'FAIL: Bob truy cập được dù kỳ vọng không có Dial policy.'
}
catch {
    Write-Host "Request failed: $($_.Exception.Message)"
    if ($Mode -eq 'Bob') {
        Write-Host 'PASS candidate: Bob bị từ chối. Chỉ xác nhận PASS khi Alice đã PASS trên cùng hệ thống.'
        exit 0
    }
    Write-Error 'FAIL: Alice không truy cập được; chưa được dùng lỗi Bob để chứng minh policy.'
}

