## GitHub Pages 迁移脚本说明（仅维护者）

本仓库本身只是 `OpentheClaw` 启动器程序，GitHub Pages 站点托管在组织仓库 `opentheclaw/opentheclaw.github.io` 中。  
之前根目录下有一个 `migrate-pages-to-org.sh` 脚本，用来帮助维护者把首页迁移到组织的 Pages 仓库并开启 Pages 服务。为避免工具脚本和程序本身混在一起，脚本已从仓库中移除，这里仅记录其用途和等价步骤。

### 原脚本逻辑

- 假设 GitHub 组织 `opentheclaw` 下已经创建仓库 `opentheclaw.github.io`
- 从本地当前仓库旁边的 `OpentheClaw.github.io/index.html` 复制首页到组织仓库
- 提交并推送到 `main` 分支
- 通过 `gh api` 开启 Pages，并指定源为 `main` 分支根目录

原脚本等价的命令流程（供有权限的维护者在本机终端中手动执行）：

```bash
# 1. 预备条件
# - 已在 GitHub 组织 opentheclaw 下创建仓库 opentheclaw.github.io
# - 本机已安装并登录 GitHub CLI：gh auth login
# - 当前项目旁边存在 OpentheClaw.github.io/index.html

ORG_REPO="opentheclaw/opentheclaw.github.io"
SOURCE_DIR="$(cd "$(dirname "$0")/OpentheClaw.github.io" && pwd)"
WORK_DIR="/tmp/opentheclaw-pages-migrate"

rm -rf "$WORK_DIR"
gh repo clone "$ORG_REPO" "$WORK_DIR"

cd "$WORK_DIR"
cp "$SOURCE_DIR/index.html" .

git add index.html
git status -sb
git commit -m "Add initial index page" || true
git push -u origin main

# 开启 Pages，指定 source 为 main 分支根目录
echo '{"source":{"branch":"main","path":"/"}}' | \
  gh api "repos/$ORG_REPO/pages" -X POST --input -

echo ""
echo "Done. Site will be at: https://opentheclaw.github.io"

rm -rf "$WORK_DIR"
```

如需调整 Pages 设置（例如改用不同分支或路径），可以直接在 GitHub Web 界面中修改 `opentheclaw/opentheclaw.github.io` 仓库的 Pages 配置。

