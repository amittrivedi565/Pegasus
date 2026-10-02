#!/bin/sh
# Copy only the public site into dist/ for Cloudflare (docs/ and tools/ stay private).
set -e
rm -rf dist
mkdir -p dist
cp -R *.html _headers css js assets dist/
find dist -name '.DS_Store' -delete
echo "Built dist/ ($(find dist -type f | wc -l | tr -d ' ') files)"
