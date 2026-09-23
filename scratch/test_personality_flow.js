const { execSync } = require('child_process');
const os = require('os');
const path = require('path');
const fs = require('fs');

const edge = 'C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe';
const tempTestHtml = path.join(os.tmpdir(), 'test_game_session.html');
const tempTestPng = path.join(os.tmpdir(), 'personality_table_preview.png');

// HTML test harness that opens the game, clicks several choice buttons, and captures the state
const testHarness = `<!DOCTYPE html>
<html>
<body style="margin:0;padding:0;background:#060a12;">
<iframe id="gameIframe" src="http://localhost:3000/" style="width:1260px;height:980px;border:none;"></iframe>
<script>
  window.addEventListener('load', () => {
    setTimeout(() => {
      try {
        const gameWin = document.getElementById('gameIframe').contentWindow;
        const g = gameWin.game;
        if (!g) return;

        // Simulate 4 choices to test personality card updates:
        // Let's click choice buttons
        const stack = gameWin.document.getElementById('optionsStack');
        if (stack && stack.children.length > 0) {
          stack.children[0].click(); // Choice 1 (adli)
        }
        
        setTimeout(() => {
          if (stack && stack.children.length > 0) {
            stack.children[0].click(); // Choice 2 (adli again -> dominant Sultan-ı Âdil)
          }
        }, 300);

        setTimeout(() => {
          if (stack && stack.children.length > 2) {
            stack.children[2].click(); // Choice 3 (mali)
          }
        }, 600);

      } catch (err) {
        console.error(err);
      }
    }, 1000);
  });
</script>
</body>
</html>`;

fs.writeFileSync(tempTestHtml, testHarness, 'utf8');

try {
  console.log('Testing game session and personality table updates...');
  execSync(`"${edge}" --headless --no-sandbox --disable-gpu --virtual-time-budget=3000 --screenshot="${tempTestPng}" --window-size=1260,980 "file:///${tempTestHtml.replace(/\\/g, '/')}"`);
  if (fs.existsSync(tempTestPng)) {
    fs.copyFileSync(tempTestPng, path.join(__dirname, '..', 'personality_table_preview.png'));
    console.log('Successfully captured personality_table_preview.png');
  }
} catch (e) {
  console.error('Screenshot error:', e.message);
}
