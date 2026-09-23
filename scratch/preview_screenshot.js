const { execSync } = require('child_process');
const os = require('os');
const path = require('path');
const fs = require('fs');

const edge = 'C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe';
const tempPng = path.join(os.tmpdir(), 'hud_full_preview.png');
const tempModernPng = path.join(os.tmpdir(), 'hud_modern_preview.png');

try {
  // Capture Ottoman default
  execSync(`"${edge}" --headless --no-sandbox --disable-gpu --screenshot="${tempPng}" --window-size=1240,920 "http://localhost:3000/"`);
  if (fs.existsSync(tempPng)) {
    fs.copyFileSync(tempPng, 'hud_full_preview.png');
    console.log('Saved hud_full_preview.png (Ottoman mode)');
  }

  // Also capture with modern mode by injecting hash or script query
  // Let's create a temporary test wrapper that defaults to modern
  const modernWrapperHtml = `<!DOCTYPE html>
<html>
<body>
<iframe id="f" src="http://localhost:3000/" style="width:1240px;height:920px;border:none;"></iframe>
<script>
  window.onload = () => {
    setTimeout(() => {
      const doc = document.getElementById('f').contentWindow;
      doc.game.setDeckMode('modern', true);
    }, 500);
  };
</script>
</body>
</html>`;
  const wrapperPath = path.join(os.tmpdir(), 'modern_preview_wrap.html');
  fs.writeFileSync(wrapperPath, modernWrapperHtml, 'utf8');

  execSync(`"${edge}" --headless --no-sandbox --disable-gpu --virtual-time-budget=2000 --screenshot="${tempModernPng}" --window-size=1240,920 "file:///${wrapperPath.replace(/\\\\/g, '/')}"`);
  if (fs.existsSync(tempModernPng)) {
    fs.copyFileSync(tempModernPng, 'hud_modern_preview.png');
    console.log('Saved hud_modern_preview.png (Modern mode)');
  }

} catch (e) {
  console.error('Error taking screenshot:', e.message);
}
