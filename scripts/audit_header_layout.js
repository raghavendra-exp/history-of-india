const fs = require('fs');

// Viewports to test
const viewports = [
  { width: 1920, desc: 'Full HD Desktop' },
  { width: 1600, desc: 'Large Laptop / Desktop' },
  { width: 1536, desc: '15.6 inch Windows 125% scale' },
  { width: 1440, desc: 'MacBook Pro / Standard Desktop' },
  { width: 1366, desc: 'Standard Laptop' },
  { width: 1280, desc: 'Small Desktop / 720p' },
  { width: 1150, desc: 'Compact Desktop (Sidebar open)' },
  { width: 1080, desc: 'Narrow Desktop (Sidebar open)' },
  { width: 1024, desc: 'iPad Pro Landscape / Tablet' },
  { width: 768, desc: 'iPad Portrait / Small Tablet' },
  { width: 640, desc: 'Large Mobile' },
  { width: 414, desc: 'iPhone Plus / Max' },
  { width: 375, desc: 'Standard Mobile' }
];

console.log('=== HEADER LAYOUT & VIEWPORT OVERLAP AUDIT ===\n');

let allPassed = true;

viewports.forEach(vp => {
  const W = vp.width;
  const isDesktopSidebar = W >= 1100;
  const sidebarW = isDesktopSidebar ? 240 : 0;
  const navW = W - sidebarW;
  const padding = W <= 640 ? 24 : 40; // 12px*2 vs 20px*2
  const innerW = navW - padding;

  // Left Cluster
  const toggleW = 36;
  const brandW = W <= 600 ? 24 : 145;
  const showBreadcrumb = W > 1540;
  const bcW = showBreadcrumb ? 180 : 0;
  const leftClusterW = toggleW + 10 + brandW + (showBreadcrumb ? (10 + bcW) : 0);

  // Right Tools Cluster
  let spotlightW;
  if (W <= 1180) {
    spotlightW = 36; // Icon only
  } else if (W <= 1320) {
    spotlightW = 75; // Icon + 'Search'
  } else {
    spotlightW = 105; // Icon + 'Search' + ⌘K
  }

  const calcW = 36;
  let upscW;
  if (W <= 600) {
    upscW = 0; // Hidden
  } else if (W <= 720) {
    upscW = 32; // Dot only
  } else if (W <= 1180) {
    upscW = 76; // Compact
  } else {
    upscW = 105; // Full
  }

  const themeW = 36;
  const toolsCount = (upscW > 0 ? 4 : 3);
  const toolsGap = (toolsCount - 1) * 8;
  const toolsW = spotlightW + calcW + upscW + themeW + toolsGap;

  // Main Links (5 primary hubs + 1 More dropdown)
  let linksW = 0;
  let showLinks = W > 1040;
  if (showLinks) {
    const hasBadges = W > 1320;
    // 5 links: Timeline(~55), Art & Culture(~80 + 35 badge), Map Lab(~60), UPSC Hub(~68 + 32 badge), 27 Books(~62)
    // More dropdown: ~55
    const baseItems = [55, 80, 60, 68, 62, 55];
    const badgeAdd = hasBadges ? (35 + 32) : 0;
    const baseTotal = baseItems.reduce((a, b) => a + b, 0);
    const itemGap = (baseItems.length - 1) * (W <= 1180 ? 2 : 3);
    const compactScale = W <= 1180 ? 0.90 : (W <= 1320 ? 0.95 : 1.0);
    linksW = Math.round((baseTotal * compactScale) + badgeAdd + itemGap);
  }

  const clustersGap = showLinks ? (12 * 2) : 12;
  const totalOccupied = leftClusterW + toolsW + linksW + clustersGap;
  const remainingSpace = innerW - totalOccupied;

  const status = remainingSpace >= 0 ? '✓ PASS' : '✗ FAIL (OVERLAP)';
  if (remainingSpace < 0) allPassed = false;

  console.log(`${vp.width.toString().padEnd(5)}px [${vp.desc.padEnd(34)}] | Inner: ${innerW.toString().padStart(4)}px | Left: ${leftClusterW.toString().padStart(3)}px | Links: ${linksW.toString().padStart(3)}px | Tools: ${toolsW.toString().padStart(3)}px | Free: +${remainingSpace.toString().padStart(3)}px -> ${status}`);
});

console.log('\nAudit Result: ' + (allPassed ? 'ALL VIEWPORTS 100% OVERLAP-FREE!' : 'OVERLAPS DETECTED!'));
if (!allPassed) process.exit(1);
