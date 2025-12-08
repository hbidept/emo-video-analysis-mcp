<!--
 * @Date: 2025-11-27 15:29:25
 * @LastEditors: sunkr1995 35027245+sunkr1995@users.noreply.github.com
 * @LastEditTime: 2025-12-08 17:53:43
 * @FilePath: \emo-video-analysis-mcp\README.md
 * @Description: Do not edit
-->
## 🛠️ 环境设置 (Environment Setup)

<details>
<summary><strong><g-emoji class="g-emoji" alias="penguin" fallback-src="https://github.githubassets.com/images/icons/emoji/unicode/1f427.png">🐧</g-emoji> Linux / macOS Setup</strong></summary>

首先，安装uv并设置 Python 项目和环境

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```
之后请务必重启终端，以确保uv命令生效。

进入项目根目录，然后执行以下命令：
```bash
uv python install 3.13
```

通过uv添加mcp官方库
```bash
uv add "mcp[cli]" httpx
```



</details>

<details>
<summary><strong><g-emoji class="g-emoji" alias="window" fallback-src="https://github.githubassets.com/images/icons/emoji/unicode/1f5a5.png">🪟</g-emoji> Windows Setup</strong></summary>

这里是 Windows 的环境设置步骤。

首先，安装uv并设置 Python 项目和环境

```bash
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```
之后请务必重启终端，以确保uv命令生效。

进入项目根目录，然后执行以下命令：
```bash
uv python install 3.13
```

通过uv添加mcp官方库
```bash
uv add "mcp[cli]" httpx
```

</details>
不建议MCP Server 和 ai对话客户端分别放置在同一机器上的不同系统，如window和wsl2

## 🤖 在AI 对话客户端中使用  

打开AI 对话客户端 配置，在MCP中添加MCP Server

在文件中添加如下内容后保存

```json
{
  "mcpServers": {
    "hbidept": {
      "command": "uv",
      "args": [
        "--directory",
        "{YOUR_PATH}/emo-video-analysis-mcp",
        "run",
        "main.py"
      ],
      "env": {
        "APP_KEY": "<YOUR_APP_KEY>",
        "APP_SECRET": "<YOUR_APP_SECRET>"
      },
    }
  }
}
```


对应的APP_KEY APP_SECRET 需要到https://open.lianxinyun.com/  进行生成。


PS: cursor 目前对 stdio 的支持不佳，使用cursor 时建议使用 sse 或者 stream http 形式
