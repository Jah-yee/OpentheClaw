#!/usr/bin/env bash
# 在组织 opentheclaw 下建好仓库 opentheclaw.github.io 后运行此脚本，把首页迁过去并开启 Pages。
set -e
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
echo '{"source":{"branch":"main","path":"/"}}' | gh api "repos/$ORG_REPO/pages" -X POST --input -
echo ""
echo "Done. Site will be at: https://opentheclaw.github.io"
rm -rf "$WORK_DIR"
