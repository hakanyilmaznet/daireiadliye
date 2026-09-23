const { execSync } = require('child_process');
const os = require('os');
const path = require('path');
const fs = require('fs');

const edge = 'C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe';
const tempModernPng = path.join(os.tmpdir(), 'hud_modern_mode_screenshot.png');

try {
  execSync(`"${edge}" --headless --no-sandbox --disable-gpu --screenshot="${tempModernPng}" --window-size=1240,920 "http://localhost:3000/?mode=modern"`);
  if (fs.existsSync(tempModernPng)) {
    fs.copyFileSync(tempModernPng, 'hud_modern_mode_screenshot.png');
    console.log('Saved hud_modern_mode_screenshot.png successfully!');
  }
} catch (e) {
  console.error('Error taking screenshot:', e.message);
}
