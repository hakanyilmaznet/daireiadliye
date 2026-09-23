const { execSync } = require('child_process');
const path = require('path');
const fs = require('fs');

const edge = 'C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe';

const outOttoman = path.join(__dirname, '..', 'personality_scored_preview.png');
const outModern = path.join(__dirname, '..', 'personality_modern_preview.png');

console.log('Capturing Ottoman scored personality preview...');
execSync(`"${edge}" --headless --no-sandbox --disable-gpu --virtual-time-budget=4000 --screenshot="${outOttoman}" --window-size=1260,980 "http://localhost:3000/test_runner.html"`);

console.log('Capturing Modern scored personality preview...');
execSync(`"${edge}" --headless --no-sandbox --disable-gpu --virtual-time-budget=4000 --screenshot="${outModern}" --window-size=1260,980 "http://localhost:3000/test_runner_modern.html"`);

console.log('Done capturing screenshots!');
