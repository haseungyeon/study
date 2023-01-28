#### hyper-v 확인
```powershell
    Get-WindowsOptionalFeature -Online -FeatureName Microsoft-Hyper-V
```

#### hyper-v 설치

```powershell
    Enable-WindowsOptionalFeature -Online -FeatureName Microsoft-Hyper-V -All
```

#### hyper-v 삭제

```powershell
    Disable-WindowsOptionalFeature -Online -FeatureName Microsoft-Hyper-V-Hypervisor
```