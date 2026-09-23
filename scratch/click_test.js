const { execSync } = require('child_process');
const os = require('os');
const path = require('path');
const fs = require('fs');

const edge = 'C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe';
const tempModernPng = path.join(os.tmpdir(), 'hud_clicked_modern.png');

// Test page that loads index.html and simulates clicking #tabModern
const html = `<!DOCTYPE html>
<html>
<body style="margin:0;">
<iframe id="appFrame" src="http://localhost:3000/" style="width:1240px;height:920px;border:none;"></iframe>
<script>
  const iframe = document.getElementById('appFrame');
  iframe.onload = () => {
    setTimeout(() => {
      const tab = iframe.contentDocument.getElementById('tabModern');
      if (tab) tab.click();
    }, 400);
  };
</script>
</body>
</html>`;

const wrapPath = path.join(os.tmpdir(), 'click_test.html');
fs.writeFileSync(wrapPath, html, 'utf8');

execSync(`"${edge}" --headless --no-sandbox --disable-gpu --virtual-time-budget=2000 --screenshot="${tempModernPng}" --window-size=1240,920 "file:///${wrapPath.replace(/\\\\/g, '/')}"`);
if (fs.existsSync(tempModernPng)) {
  fs.copyFileSync(tempModernPng, 'hud_clicked_modern.png');
  console.log('Saved hud_clicked_modern.png');
}
