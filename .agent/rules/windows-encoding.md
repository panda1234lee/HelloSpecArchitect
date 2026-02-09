# Windows PowerShell 编码规范

## 上下文
当在 Windows 环境下的 PowerShell 中执行后台命令时，默认的 GBK (CP936) 编码会导致 AI 界面显示的输出结果出现乱码。

## 规则
1. **强制 UTF-8 会话**: 
   - 每次执行复杂的 `run_command`（尤其是涉及中文输出或报错信息的命令）时，应在命令前缀中包含编码切换指令：
     `$OutputEncoding = [Console]::OutputEncoding = [System.Text.Encoding]::UTF8; <你的命令>`
2. **错误处理**: 如果命令返回乱码，应优先检查是否是因为编码未切换至 UTF-8。
3. **输出验证**: 保持 CodePage 为 `65001` 以确保与 AI 界面的最佳兼容性。

---
*注：此规则仅在当前 Workspace 生效，不影响系统全局设置。*
