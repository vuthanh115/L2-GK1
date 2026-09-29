# -*- coding: utf-8 -*-
import json

with open('assets/listening_b64.json', 'r', encoding='utf-8') as f:
    images = json.load(f)

print(f"Loaded {len(images)} listening images.")

# Assembly script for listening.html
head_html = """<!DOCTYPE html>
<html lang="vi">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Listening 2 - Review for Midterm Test 1 | Luyện Nghe Tiếng Anh Lớp 2</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Nunito:wght@400;600;700;800;900&display=swap" rel="stylesheet">
  <style>
    :root {
      --primary: #ec4899;
      --primary-hover: #db2777;
      --primary-light: #fdf2f8;
      --accent: #f59e0b;
      --accent-light: #fef3c7;
      --success: #10b981;
      --success-light: #d1fae5;
      --danger: #ef4444;
      --danger-light: #fee2e2;
      --bg: #f8fafc;
      --card-bg: #ffffff;
      --text: #1e293b;
      --text-muted: #64748b;
      --border: #e2e8f0;
      --radius: 18px;
      --shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.07), 0 2px 4px -2px rgba(0, 0, 0, 0.05);
      --shadow-lg: 0 10px 15px -3px rgba(0, 0, 0, 0.08), 0 4px 6px -4px rgba(0, 0, 0, 0.04);
    }

    * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
      -webkit-tap-highlight-color: transparent;
    }

    body {
      font-family: 'Nunito', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
      background: var(--bg);
      color: var(--text);
      line-height: 1.6;
      padding-bottom: 120px;
    }

    .header-banner {
      background: linear-gradient(135deg, #f43f5e 0%, #ec4899 50%, #8b5cf6 100%);
      color: white;
      padding: 24px 16px 28px;
      border-radius: 0 0 28px 28px;
      box-shadow: 0 10px 25px -5px rgba(236, 72, 153, 0.35);
      position: relative;
      overflow: hidden;
    }

    .header-banner::before {
      content: '';
      position: absolute;
      top: -40px;
      right: -40px;
      width: 140px;
      height: 140px;
      background: rgba(255, 255, 255, 0.12);
      border-radius: 50%;
    }

    .header-banner::after {
      content: '';
      position: absolute;
      bottom: -30px;
      left: 10%;
      width: 90px;
      height: 90px;
      background: rgba(255, 255, 255, 0.08);
      border-radius: 50%;
    }

    .header-container {
      max-width: 960px;
      margin: 0 auto;
      position: relative;
      z-index: 1;
    }

    .nav-links {
      display: flex;
      gap: 10px;
      margin-bottom: 14px;
      flex-wrap: wrap;
    }

    .nav-btn {
      text-decoration: none;
      color: white;
      background: rgba(255, 255, 255, 0.22);
      padding: 6px 14px;
      border-radius: 12px;
      font-weight: 800;
      font-size: 0.95rem;
      display: inline-flex;
      align-items: center;
      gap: 6px;
      transition: all 0.2s;
    }

    .nav-btn:hover {
      background: rgba(255, 255, 255, 0.35);
      transform: translateY(-1px);
    }

    .title-row {
      display: flex;
      flex-wrap: wrap;
      align-items: center;
      justify-content: space-between;
      gap: 16px;
    }

    .main-title {
      font-size: 1.85rem;
      font-weight: 900;
      letter-spacing: -0.5px;
      text-shadow: 0 2px 4px rgba(0, 0, 0, 0.15);
      display: flex;
      align-items: center;
      gap: 10px;
    }

    .sub-title {
      font-size: 1.05rem;
      font-weight: 600;
      color: #ffe4e6;
      margin-top: 4px;
    }

    .student-info-bar {
      margin-top: 20px;
      display: flex;
      flex-wrap: wrap;
      gap: 12px;
      background: rgba(255, 255, 255, 0.18);
      padding: 12px 18px;
      border-radius: 16px;
      backdrop-filter: blur(8px);
    }

    .info-group {
      display: flex;
      align-items: center;
      gap: 8px;
      flex: 1;
      min-width: 200px;
    }

    .info-group label {
      font-weight: 700;
      font-size: 0.95rem;
      white-space: nowrap;
    }

    .info-group input {
      flex: 1;
      padding: 6px 12px;
      border-radius: 10px;
      border: 1px solid rgba(255, 255, 255, 0.4);
      background: rgba(255, 255, 255, 0.95);
      color: var(--text);
      font-family: inherit;
      font-size: 0.95rem;
      font-weight: 700;
      outline: none;
      transition: all 0.2s;
    }

    .info-group input:focus {
      background: #ffffff;
      box-shadow: 0 0 0 3px rgba(255, 255, 255, 0.5);
    }

    .header-score-pill {
      background: #f59e0b;
      color: #78350f;
      padding: 8px 18px;
      border-radius: 20px;
      font-weight: 900;
      font-size: 1.15rem;
      display: flex;
      align-items: center;
      gap: 8px;
      box-shadow: 0 4px 10px rgba(0, 0, 0, 0.12);
      white-space: nowrap;
    }

    /* Fixed Audio Player Bar */
    .audio-player-panel {
      background: #ffffff;
      border-radius: 18px;
      padding: 16px 20px;
      box-shadow: 0 4px 15px rgba(0,0,0,0.08);
      border: 2px solid #fbcfe8;
      margin-bottom: 24px;
      display: flex;
      flex-direction: column;
      gap: 12px;
    }

    .player-controls {
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 14px;
      flex-wrap: wrap;
    }

    .player-left {
      display: flex;
      align-items: center;
      gap: 12px;
    }

    .btn-play-master {
      width: 46px;
      height: 46px;
      border-radius: 50%;
      background: linear-gradient(135deg, #ec4899 0%, #db2777 100%);
      border: none;
      color: white;
      font-size: 1.4rem;
      display: flex;
      align-items: center;
      justify-content: center;
      cursor: pointer;
      box-shadow: 0 4px 10px rgba(236, 72, 153, 0.35);
      transition: all 0.2s;
    }

    .btn-play-master:hover {
      transform: scale(1.06);
    }

    .time-display {
      font-size: 1rem;
      font-weight: 800;
      color: #475569;
      font-variant-numeric: tabular-nums;
    }

    .player-progress-wrap {
      flex: 1;
      min-width: 200px;
      display: flex;
      align-items: center;
      gap: 8px;
    }

    .seek-slider {
      flex: 1;
      height: 8px;
      border-radius: 4px;
      accent-color: var(--primary);
      cursor: pointer;
    }

    .speed-select {
      padding: 4px 10px;
      border-radius: 8px;
      border: 1px solid #cbd5e1;
      font-weight: 800;
      font-size: 0.9rem;
      color: #334155;
      background: #f8fafc;
      outline: none;
    }

    .jump-parts-bar {
      display: flex;
      align-items: center;
      gap: 8px;
      flex-wrap: wrap;
      border-top: 1px dashed #e2e8f0;
      padding-top: 10px;
    }

    .btn-jump {
      background: #fdf2f8;
      border: 1px solid #fbcfe8;
      color: #db2777;
      padding: 5px 12px;
      border-radius: 10px;
      font-size: 0.9rem;
      font-weight: 800;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 6px;
      transition: all 0.15s;
    }

    .btn-jump:hover {
      background: #fce7f3;
      transform: translateY(-1px);
    }

    .btn-audio-jump {
      background: #eff6ff;
      border: 1px solid #bfdbfe;
      color: #2563eb;
      padding: 4px 10px;
      border-radius: 8px;
      font-size: 0.85rem;
      font-weight: 800;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 4px;
      transition: all 0.15s;
    }

    .btn-audio-jump:hover {
      background: #dbeafe;
    }

    .container {
      max-width: 960px;
      margin: 24px auto;
      padding: 0 16px;
    }

    .part-section {
      background: var(--card-bg);
      border-radius: var(--radius);
      padding: 24px;
      margin-bottom: 28px;
      box-shadow: var(--shadow);
      border: 1px solid var(--border);
      transition: transform 0.2s, box-shadow 0.2s;
    }

    .part-section:hover {
      box-shadow: var(--shadow-lg);
    }

    .part-header {
      display: flex;
      align-items: flex-start;
      justify-content: space-between;
      gap: 12px;
      margin-bottom: 18px;
      border-bottom: 2px dashed #f1f5f9;
      padding-bottom: 14px;
    }

    .part-title {
      font-size: 1.3rem;
      font-weight: 800;
      color: #1e1b4b;
      display: flex;
      align-items: center;
      gap: 8px;
      flex-wrap: wrap;
    }

    .part-badge {
      background: var(--primary-light);
      color: var(--primary);
      font-size: 0.85rem;
      padding: 4px 10px;
      border-radius: 8px;
      font-weight: 800;
    }

    .part-vi {
      font-size: 0.95rem;
      font-weight: 600;
      color: var(--text-muted);
      margin-top: 3px;
    }

    /* Part 1 Tick Cards */
    .part1-row {
      background: #f8fafc;
      border: 1px solid #e2e8f0;
      border-radius: 16px;
      padding: 16px;
      margin-bottom: 18px;
    }

    .p1-row-header {
      display: flex;
      align-items: center;
      justify-content: space-between;
      margin-bottom: 12px;
    }

    .p1-grid {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 14px;
    }

    @media (max-width: 640px) {
      .p1-grid {
        grid-template-columns: 1fr;
      }
    }

    .p1-card {
      background: #ffffff;
      border: 2px solid #cbd5e1;
      border-radius: 14px;
      padding: 12px;
      display: flex;
      flex-direction: column;
      align-items: center;
      cursor: pointer;
      transition: all 0.2s;
      position: relative;
    }

    .p1-card:hover {
      border-color: var(--primary);
      transform: translateY(-2px);
    }

    .p1-card.selected {
      border-color: var(--primary);
      background: #fdf2f8;
      box-shadow: 0 4px 10px rgba(236, 72, 153, 0.15);
    }

    .p1-card.correct {
      border-color: var(--success) !important;
      background: var(--success-light) !important;
    }

    .p1-card.wrong {
      border-color: var(--danger) !important;
      background: var(--danger-light) !important;
    }

    .p1-img-wrap {
      width: 100%;
      height: 120px;
      display: flex;
      align-items: center;
      justify-content: center;
      margin-bottom: 10px;
    }

    .p1-img-wrap img {
      max-height: 100%;
      max-width: 100%;
      object-fit: contain;
    }

    .tick-box {
      width: 32px;
      height: 32px;
      border-radius: 8px;
      border: 2px solid #94a3b8;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 1.3rem;
      font-weight: 900;
      color: var(--primary);
      background: #ffffff;
      transition: all 0.15s;
    }

    .p1-card.selected .tick-box {
      border-color: var(--primary);
      background: var(--primary);
      color: white;
    }

    /* Part 2: Grid 4x2 */
    .part2-grid {
      display: grid;
      grid-template-columns: repeat(2, 1fr);
      gap: 18px;
    }

    @media (max-width: 640px) {
      .part2-grid {
        grid-template-columns: 1fr;
      }
    }

    .p2-card {
      background: #ffffff;
      border: 2px solid #e2e8f0;
      border-radius: 16px;
      padding: 14px;
      display: flex;
      flex-direction: column;
      align-items: center;
      text-align: center;
      position: relative;
    }

    .p2-img-wrap {
      width: 100%;
      height: 140px;
      display: flex;
      align-items: center;
      justify-content: center;
      margin-bottom: 12px;
    }

    .p2-img-wrap img {
      max-height: 100%;
      max-width: 100%;
      object-fit: contain;
    }

    .num-slot {
      display: flex;
      align-items: center;
      gap: 8px;
    }

    .num-input {
      width: 55px;
      height: 48px;
      border: 2px solid #cbd5e1;
      border-radius: 10px;
      font-family: inherit;
      font-size: 1.4rem;
      font-weight: 900;
      text-align: center;
      color: #1e293b;
      outline: none;
      transition: all 0.2s;
    }

    .num-input:focus {
      border-color: var(--primary);
      background: #fdf2f8;
      box-shadow: 0 0 0 3px rgba(236, 72, 153, 0.15);
    }

    .num-input.correct {
      border-color: var(--success) !important;
      background: #f0fdf4 !important;
      color: #15803d !important;
    }

    .num-input.wrong {
      border-color: var(--danger) !important;
      background: #fef2f2 !important;
      color: #b91c1c !important;
    }

    /* Part 3 */
    .part3-layout {
      display: grid;
      grid-template-columns: 1fr 1.6fr;
      gap: 24px;
      align-items: start;
    }

    @media (max-width: 768px) {
      .part3-layout {
        grid-template-columns: 1fr;
      }
    }

    .p3-img-wrap {
      background: #fdf2f8;
      border: 2px solid #fbcfe8;
      border-radius: 16px;
      padding: 16px;
      text-align: center;
      position: sticky;
      top: 90px;
    }

    .p3-img-wrap img {
      max-width: 100%;
      border-radius: 12px;
    }

    .p3-q-list {
      display: flex;
      flex-direction: column;
      gap: 14px;
    }

    .p3-item {
      background: #f8fafc;
      border: 1px solid #e2e8f0;
      border-radius: 14px;
      padding: 14px 18px;
    }

    .p3-item-header {
      font-weight: 800;
      font-size: 1.05rem;
      margin-bottom: 8px;
      display: flex;
      align-items: center;
      justify-content: space-between;
    }

    .p3-input-row {
      display: flex;
      align-items: center;
      gap: 8px;
      flex-wrap: wrap;
      font-size: 1.1rem;
      font-weight: 700;
    }

    .text-input-line {
      flex: 1;
      min-width: 140px;
      padding: 6px 12px;
      border: 2px solid #cbd5e1;
      border-radius: 10px;
      font-family: inherit;
      font-size: 1.1rem;
      font-weight: 800;
      color: var(--primary);
      outline: none;
      background: #fff;
    }

    .text-input-line:focus {
      border-color: var(--primary);
    }

    .text-input-line.correct {
      border-color: var(--success) !important;
      background: #f0fdf4 !important;
      color: #15803d !important;
    }

    .text-input-line.wrong {
      border-color: var(--danger) !important;
      background: #fef2f2 !important;
      color: #b91c1c !important;
    }

    /* Part 4 Canvas & Tasks */
    .part4-layout {
      display: grid;
      grid-template-columns: 1.2fr 1fr;
      gap: 20px;
      align-items: start;
    }

    @media (max-width: 820px) {
      .part4-layout {
        grid-template-columns: 1fr;
      }
    }

    .canvas-container {
      position: relative;
      background: #ffffff;
      border: 2px solid #cbd5e1;
      border-radius: 16px;
      overflow: hidden;
      box-shadow: 0 4px 10px rgba(0,0,0,0.06);
    }

    .canvas-bg-img {
      width: 100%;
      height: auto;
      display: block;
      user-select: none;
      pointer-events: none;
    }

    .draw-canvas {
      position: absolute;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      cursor: crosshair;
      touch-action: none;
    }

    .canvas-toolbar {
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 8px;
      background: #f8fafc;
      border: 1px solid #e2e8f0;
      border-radius: 12px;
      padding: 8px 12px;
      margin-top: 10px;
      flex-wrap: wrap;
    }

    .color-swatch-list {
      display: flex;
      gap: 6px;
      align-items: center;
    }

    .color-btn {
      width: 26px;
      height: 26px;
      border-radius: 50%;
      border: 2px solid #ffffff;
      box-shadow: 0 1px 3px rgba(0,0,0,0.25);
      cursor: pointer;
      transition: all 0.15s;
    }

    .color-btn:hover {
      transform: scale(1.15);
    }

    .color-btn.active {
      transform: scale(1.25);
      box-shadow: 0 0 0 2px #0f172a;
    }

    .p4-tasks-list {
      display: flex;
      flex-direction: column;
      gap: 12px;
    }

    .p4-task-card {
      background: #ffffff;
      border: 2px solid #e2e8f0;
      border-radius: 14px;
      padding: 12px 16px;
    }

    .p4-task-title {
      font-weight: 800;
      font-size: 1rem;
      margin-bottom: 8px;
      display: flex;
      align-items: center;
      justify-content: space-between;
    }

    .color-select-chips {
      display: flex;
      gap: 6px;
      flex-wrap: wrap;
    }

    .chip-color {
      padding: 5px 12px;
      border-radius: 20px;
      border: 2px solid #cbd5e1;
      background: #ffffff;
      font-weight: 800;
      font-size: 0.88rem;
      cursor: pointer;
      transition: all 0.15s;
    }

    .chip-color:hover {
      border-color: var(--primary);
    }

    .chip-color.selected {
      border-color: var(--primary);
      background: var(--primary);
      color: white;
    }

    .chip-color.correct {
      border-color: var(--success) !important;
      background: var(--success) !important;
      color: white !important;
    }

    .chip-color.wrong {
      border-color: var(--danger) !important;
      background: var(--danger) !important;
      color: white !important;
    }

    .feedback-tip {
      font-size: 0.88rem;
      font-weight: 700;
      margin-top: 6px;
      display: none;
    }

    .feedback-tip.show-correct {
      display: block;
      color: #15803d;
    }

    .feedback-tip.show-wrong {
      display: block;
      color: #b91c1c;
    }

    /* Sticky Bottom Control Bar */
    .sticky-bar {
      position: fixed;
      bottom: 0;
      left: 0;
      right: 0;
      background: rgba(255, 255, 255, 0.96);
      backdrop-filter: blur(12px);
      border-top: 1px solid var(--border);
      padding: 12px 20px;
      box-shadow: 0 -4px 15px rgba(0, 0, 0, 0.08);
      z-index: 100;
    }

    .sticky-container {
      max-width: 960px;
      margin: 0 auto;
      width: 100%;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 12px;
      flex-wrap: wrap;
    }

    .btn-action {
      padding: 12px 22px;
      border-radius: 12px;
      font-size: 1.05rem;
      font-weight: 800;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 8px;
      transition: all 0.2s;
      border: none;
      outline: none;
    }

    .btn-primary {
      background: linear-gradient(135deg, #f43f5e 0%, #ec4899 100%);
      color: white;
      box-shadow: 0 4px 12px rgba(236, 72, 153, 0.35);
    }

    .btn-primary:hover {
      transform: translateY(-2px);
      box-shadow: 0 6px 16px rgba(236, 72, 153, 0.45);
    }

    .btn-secondary {
      background: #f1f5f9;
      color: #334155;
      border: 1px solid #cbd5e1;
    }

    .btn-secondary:hover {
      background: #e2e8f0;
    }

    .btn-accent {
      background: #fffbeb;
      color: #b45309;
      border: 1px solid #fde68a;
    }

    .btn-accent:hover {
      background: #fef3c7;
    }

    /* Modal */
    .modal-backdrop {
      position: fixed;
      top: 0;
      left: 0;
      right: 0;
      bottom: 0;
      background: rgba(15, 23, 42, 0.65);
      backdrop-filter: blur(5px);
      display: none;
      align-items: center;
      justify-content: center;
      z-index: 200;
      padding: 20px;
    }

    .modal-card {
      background: white;
      border-radius: 24px;
      max-width: 520px;
      width: 100%;
      padding: 32px 28px;
      text-align: center;
      box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.25);
      animation: popIn 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275);
    }

    @keyframes popIn {
      from { transform: scale(0.85); opacity: 0; }
      to { transform: scale(1); opacity: 1; }
    }

    .modal-trophy {
      font-size: 4rem;
      margin-bottom: 10px;
    }

    .modal-title {
      font-size: 1.8rem;
      font-weight: 900;
      color: #1e1b4b;
      margin-bottom: 8px;
    }

    .modal-score {
      font-size: 2.8rem;
      font-weight: 900;
      color: var(--primary);
      margin: 12px 0;
    }

    .modal-breakdown {
      background: #f8fafc;
      border-radius: 16px;
      padding: 14px 18px;
      margin: 18px 0;
      text-align: left;
      font-size: 0.95rem;
      font-weight: 600;
    }

    .breakdown-row {
      display: flex;
      justify-content: space-between;
      padding: 5px 0;
      border-bottom: 1px dashed #e2e8f0;
    }

    .breakdown-row:last-child {
      border-bottom: none;
    }

    @media print {
      body { background: #fff !important; color: #000 !important; padding-bottom: 0 !important; }
      .header-banner { background: none !important; color: #000 !important; box-shadow: none !important; border-bottom: 2px solid #000; }
      .header-banner::before, .header-banner::after, .header-score-pill, .sticky-bar, .audio-player-panel, .canvas-toolbar, .btn-audio-jump, .modal-backdrop, .feedback-tip, .nav-links { display: none !important; }
      .student-info-bar { background: none !important; border: 1px solid #000 !important; }
      .part-section { box-shadow: none !important; border: 1px solid #ccc !important; page-break-inside: avoid; margin-bottom: 20px; }
      .text-input-line, .num-input { border-bottom: 1px solid #000 !important; border-top: none !important; border-left: none !important; border-right: none !important; border-radius: 0 !important; }
    }
  </style>
</head>
<body>

  <!-- Hidden native Audio element -->
  <audio id="mainAudio" src="Listening 2 - Review for Midterm Test 1.mp3" preload="metadata"></audio>

  <!-- Header Banner -->
  <header class="header-banner">
    <div class="header-container">
      <div class="nav-links">
        <a href="index.html" class="nav-btn">🏠 Về Trang Chủ</a>
        <a href="english.html" class="nav-btn">🇬🇧 Môn Tiếng Anh (English 2)</a>
        <a href="maths.html" class="nav-btn">🔢 Môn Toán (Maths 2)</a>
        <a href="grammar.html" class="nav-btn">📖 Môn Ngữ Pháp (Grammar 2)</a>
      </div>

      <div class="title-row">
        <div>
          <h1 class="main-title">
            <span>🎧</span> Listening 2 - Midterm Test 1
          </h1>
          <p class="sub-title">Đề Ôn Tập Luyện Nghe Tiếng Anh Lớp 2 (Cambridge Starters)</p>
        </div>
        <div class="header-score-pill" id="scoreIndicator">
          <span>⭐ Điểm:</span> <span id="currentScore">0</span> / <span id="totalScore">24</span>
        </div>
      </div>

      <div class="student-info-bar">
        <div class="info-group">
          <label for="studentName">👤 Name (Họ tên):</label>
          <input type="text" id="studentName" placeholder="Nhập tên bé...">
        </div>
        <div class="info-group">
          <label for="studentClass">🏫 Class (Lớp):</label>
          <input type="text" id="studentClass" placeholder="Ví dụ: 2A1">
        </div>
      </div>
    </div>
  </header>

  <!-- Main Container -->
  <main class="container">

    <!-- MASTER AUDIO PLAYER BAR -->
    <div class="audio-player-panel" id="audioPanel">
      <div class="player-controls">
        <div class="player-left">
          <button type="button" class="btn-play-master" id="btnPlayMaster" onclick="togglePlayAudio()">
            <span id="playIcon">▶</span>
          </button>
          <div>
            <div style="font-weight:900; font-size:1.05rem; color:#831843;">Audio Đề Thi Listening 2</div>
            <div class="time-display"><span id="currTime">00:00</span> / <span id="durTime">17:42</span></div>
          </div>
        </div>

        <div class="player-progress-wrap">
          <input type="range" class="seek-slider" id="seekSlider" min="0" max="100" value="0" oninput="onSeekChange(this.value)">
          <select class="speed-select" id="speedSelect" onchange="setPlaybackSpeed(this.value)">
            <option value="1">Tốc độ: 1.0x</option>
            <option value="0.9">Tốc độ: 0.9x (Chậm nhẹ)</option>
            <option value="0.8">Tốc độ: 0.8x (Chậm dễ nghe)</option>
          </select>
        </div>
      </div>

      <!-- Jump to Parts -->
      <div class="jump-parts-bar">
        <span style="font-size:0.88rem; font-weight:800; color:#9d174d;">Chuyển nhanh tới:</span>
        <button type="button" class="btn-jump" onclick="seekTo(41)">▶ Part 1 (00:41)</button>
        <button type="button" class="btn-jump" onclick="seekTo(147)">▶ Part 2 (02:27)</button>
        <button type="button" class="btn-jump" onclick="seekTo(317)">▶ Part 3 (05:17)</button>
        <button type="button" class="btn-jump" onclick="seekTo(554)">▶ Part 4 (09:14)</button>
      </div>
    </div>
"""

# Let's generate Part 1 HTML
part1_html = f"""
    <!-- PART 1: TICK THE CORRECT PICTURE -->
    <section class="part-section" id="section-1">
      <div class="part-header">
        <div>
          <div class="part-title">
            <span class="part-badge">PART 1</span>
            Part 1: Listen and write a tick “✓” on the correct picture.
          </div>
          <p class="part-vi">Nghe từ và bấm vào bức tranh đúng để đánh dấu tích (✓).</p>
        </div>
        <button type="button" class="btn-jump" onclick="seekTo(41)">🎧 Nghe Part 1 (00:41)</button>
      </div>

      <!-- 1. ox -->
      <div class="part1-row" id="row-p1_1">
        <div class="p1-row-header">
          <span style="font-weight:900; font-size:1.15rem;">Câu 1:</span>
          <button type="button" class="btn-audio-jump" onclick="seekTo(48)">🎧 Nghe câu 1 (00:48)</button>
        </div>
        <div class="p1-grid">
          <div class="p1-card" data-q="p1_1" data-opt="a" data-correct="false" onclick="selectTick('p1_1', 'a')">
            <div class="p1-img-wrap"><img src="{images['p1_1a_whale.png']}" alt="Whale"></div>
            <div class="tick-box" id="tick-p1_1_a"></div>
          </div>
          <div class="p1-card" data-q="p1_1" data-opt="b" data-correct="true" onclick="selectTick('p1_1', 'b')">
            <div class="p1-img-wrap"><img src="{images['p1_1b_ox.png']}" alt="Ox"></div>
            <div class="tick-box" id="tick-p1_1_b"></div>
          </div>
          <div class="p1-card" data-q="p1_1" data-opt="c" data-correct="false" onclick="selectTick('p1_1', 'c')">
            <div class="p1-img-wrap"><img src="{images['p1_1c_ant.png']}" alt="Ant"></div>
            <div class="tick-box" id="tick-p1_1_c"></div>
          </div>
        </div>
        <div class="feedback-tip" id="fb-p1_1">Đáp án: <b>Hình B - ox</b> (con bò đực)</div>
      </div>

      <!-- 2. pot -->
      <div class="part1-row" id="row-p1_2">
        <div class="p1-row-header">
          <span style="font-weight:900; font-size:1.15rem;">Câu 2:</span>
          <button type="button" class="btn-audio-jump" onclick="seekTo(57)">🎧 Nghe câu 2 (00:57)</button>
        </div>
        <div class="p1-grid">
          <div class="p1-card" data-q="p1_2" data-opt="a" data-correct="true" onclick="selectTick('p1_2', 'a')">
            <div class="p1-img-wrap"><img src="{images['p1_2a_pot.png']}" alt="Pot"></div>
            <div class="tick-box" id="tick-p1_2_a"></div>
          </div>
          <div class="p1-card" data-q="p1_2" data-opt="b" data-correct="false" onclick="selectTick('p1_2', 'b')">
            <div class="p1-img-wrap"><img src="{images['p1_2b_socks.png']}" alt="Socks"></div>
            <div class="tick-box" id="tick-p1_2_b"></div>
          </div>
          <div class="p1-card" data-q="p1_2" data-opt="c" data-correct="false" onclick="selectTick('p1_2', 'c')">
            <div class="p1-img-wrap"><img src="{images['p1_2c_tub.png']}" alt="Bathtub"></div>
            <div class="tick-box" id="tick-p1_2_c"></div>
          </div>
        </div>
        <div class="feedback-tip" id="fb-p1_2">Đáp án: <b>Hình A - pot</b> (cái nồi)</div>
      </div>

      <!-- 3. ink -->
      <div class="part1-row" id="row-p1_3">
        <div class="p1-row-header">
          <span style="font-weight:900; font-size:1.15rem;">Câu 3:</span>
          <button type="button" class="btn-audio-jump" onclick="seekTo(68)">🎧 Nghe câu 3 (01:08)</button>
        </div>
        <div class="p1-grid">
          <div class="p1-card" data-q="p1_3" data-opt="a" data-correct="false" onclick="selectTick('p1_3', 'a')">
            <div class="p1-img-wrap"><img src="{images['p1_3a_dig.png']}" alt="Dig"></div>
            <div class="tick-box" id="tick-p1_3_a"></div>
          </div>
          <div class="p1-card" data-q="p1_3" data-opt="b" data-correct="false" onclick="selectTick('p1_3', 'b')">
            <div class="p1-img-wrap"><img src="{images['p1_3b_sick.png']}" alt="Sick"></div>
            <div class="tick-box" id="tick-p1_3_b"></div>
          </div>
          <div class="p1-card" data-q="p1_3" data-opt="c" data-correct="true" onclick="selectTick('p1_3', 'c')">
            <div class="p1-img-wrap"><img src="{images['p1_3c_ink.png']}" alt="Ink"></div>
            <div class="tick-box" id="tick-p1_3_c"></div>
          </div>
        </div>
        <div class="feedback-tip" id="fb-p1_3">Đáp án: <b>Hình C - ink</b> (bình mực)</div>
      </div>

      <!-- 4. jet -->
      <div class="part1-row" id="row-p1_4">
        <div class="p1-row-header">
          <span style="font-weight:900; font-size:1.15rem;">Câu 4:</span>
          <button type="button" class="btn-audio-jump" onclick="seekTo(76)">🎧 Nghe câu 4 (01:16)</button>
        </div>
        <div class="p1-grid">
          <div class="p1-card" data-q="p1_4" data-opt="a" data-correct="true" onclick="selectTick('p1_4', 'a')">
            <div class="p1-img-wrap"><img src="{images['p1_4a_jet.png']}" alt="Jet"></div>
            <div class="tick-box" id="tick-p1_4_a"></div>
          </div>
          <div class="p1-card" data-q="p1_4" data-opt="b" data-correct="false" onclick="selectTick('p1_4', 'b')">
            <div class="p1-img-wrap"><img src="{images['p1_4b_pen.png']}" alt="Pen"></div>
            <div class="tick-box" id="tick-p1_4_b"></div>
          </div>
          <div class="p1-card" data-q="p1_4" data-opt="c" data-correct="false" onclick="selectTick('p1_4', 'c')">
            <div class="p1-img-wrap"><img src="{images['p1_4c_legs.png']}" alt="Legs"></div>
            <div class="tick-box" id="tick-p1_4_c"></div>
          </div>
        </div>
        <div class="feedback-tip" id="fb-p1_4">Đáp án: <b>Hình A - jet</b> (máy bay phản lực)</div>
      </div>

      <!-- 5. seed -->
      <div class="part1-row" id="row-p1_5">
        <div class="p1-row-header">
          <span style="font-weight:900; font-size:1.15rem;">Câu 5:</span>
          <button type="button" class="btn-audio-jump" onclick="seekTo(84)">🎧 Nghe câu 5 (01:24)</button>
        </div>
        <div class="p1-grid">
          <div class="p1-card" data-q="p1_5" data-opt="a" data-correct="false" onclick="selectTick('p1_5', 'a')">
            <div class="p1-img-wrap"><img src="{images['p1_5a_map.png']}" alt="Map"></div>
            <div class="tick-box" id="tick-p1_5_a"></div>
          </div>
          <div class="p1-card" data-q="p1_5" data-opt="b" data-correct="false" onclick="selectTick('p1_5', 'b')">
            <div class="p1-img-wrap"><img src="{images['p1_5b_ax.png']}" alt="Ax"></div>
            <div class="tick-box" id="tick-p1_5_b"></div>
          </div>
          <div class="p1-card" data-q="p1_5" data-opt="c" data-correct="true" onclick="selectTick('p1_5', 'c')">
            <div class="p1-img-wrap"><img src="{images['p1_5c_seed.png']}" alt="Seed"></div>
            <div class="tick-box" id="tick-p1_5_c"></div>
          </div>
        </div>
        <div class="feedback-tip" id="fb-p1_5">Đáp án: <b>Hình C - seed</b> (hạt giống)</div>
      </div>
    </section>
"""

# Let's generate Part 2 HTML
part2_html = f"""
    <!-- PART 2: NUMBER THE PICTURES -->
    <section class="part-section" id="section-2">
      <div class="part-header">
        <div>
          <div class="part-title">
            <span class="part-badge">PART 2</span>
            Part 2: Look, listen and write the correct number for each picture.
          </div>
          <p class="part-vi">Nghe 8 câu mô tả và điền số tương ứng từ 1 đến 8 vào ô dưới mỗi tranh.</p>
        </div>
        <button type="button" class="btn-jump" onclick="seekTo(147)">🎧 Nghe Part 2 (02:27)</button>
      </div>

      <div class="part2-grid">
        <!-- 1. Sing -> 2 -->
        <div class="p2-card">
          <div class="p2-img-wrap"><img src="{images['p2_sing.png']}" alt="Singing"></div>
          <div class="num-slot">
            <span style="font-weight:700;">Số:</span>
            <input type="text" class="num-input" id="p2_sing" data-answer="2" maxlength="1" placeholder="?">
            <button type="button" class="btn-audio-jump" onclick="seekTo(164)">🎧 Câu 2 (02:44)</button>
          </div>
          <div class="feedback-tip" id="fb-p2_sing">Đáp án: <b>2</b> ("I like to sing")</div>
        </div>

        <!-- 2. Sheep / Lamb -> 4 -->
        <div class="p2-card">
          <div class="p2-img-wrap"><img src="{images['p2_sheep.png']}" alt="Sheep"></div>
          <div class="num-slot">
            <span style="font-weight:700;">Số:</span>
            <input type="text" class="num-input" id="p2_sheep" data-answer="4" maxlength="1" placeholder="?">
            <button type="button" class="btn-audio-jump" onclick="seekTo(183)">🎧 Câu 4 (03:03)</button>
          </div>
          <div class="feedback-tip" id="fb-p2_sheep">Đáp án: <b>4</b> ("In one year, this baby lamb will be a grown-up")</div>
        </div>

        <!-- 3. Wash dishes -> 1 -->
        <div class="p2-card">
          <div class="p2-img-wrap"><img src="{images['p2_wash_dishes.png']}" alt="Washing dishes"></div>
          <div class="num-slot">
            <span style="font-weight:700;">Số:</span>
            <input type="text" class="num-input" id="p2_wash_dishes" data-answer="1" maxlength="1" placeholder="?">
            <button type="button" class="btn-audio-jump" onclick="seekTo(154)">🎧 Câu 1 (02:34)</button>
          </div>
          <div class="feedback-tip" id="fb-p2_wash_dishes">Đáp án: <b>1</b> ("I wash the dishes")</div>
        </div>

        <!-- 4. Clean sink -> 3 -->
        <div class="p2-card">
          <div class="p2-img-wrap"><img src="{images['p2_clean_sink.png']}" alt="Cleaning kitchen sink"></div>
          <div class="num-slot">
            <span style="font-weight:700;">Số:</span>
            <input type="text" class="num-input" id="p2_clean_sink" data-answer="3" maxlength="1" placeholder="?">
            <button type="button" class="btn-audio-jump" onclick="seekTo(173)">🎧 Câu 3 (02:53)</button>
          </div>
          <div class="feedback-tip" id="fb-p2_clean_sink">Đáp án: <b>3</b> ("I clean the kitchen sink")</div>
        </div>

        <!-- 5. Fold wash -> 6 -->
        <div class="p2-card">
          <div class="p2-img-wrap"><img src="{images['p2_fold_wash.png']}" alt="Folding laundry"></div>
          <div class="num-slot">
            <span style="font-weight:700;">Số:</span>
            <input type="text" class="num-input" id="p2_fold_wash" data-answer="6" maxlength="1" placeholder="?">
            <button type="button" class="btn-audio-jump" onclick="seekTo(202)">🎧 Câu 6 (03:22)</button>
          </div>
          <div class="feedback-tip" id="fb-p2_fold_wash">Đáp án: <b>6</b> ("They can fold the wash")</div>
        </div>

        <!-- 6. Yams -> 8 -->
        <div class="p2-card">
          <div class="p2-img-wrap"><img src="{images['p2_yams.png']}" alt="Yams"></div>
          <div class="num-slot">
            <span style="font-weight:700;">Số:</span>
            <input type="text" class="num-input" id="p2_yams" data-answer="8" maxlength="1" placeholder="?">
            <button type="button" class="btn-audio-jump" onclick="seekTo(222)">🎧 Câu 8 (03:42)</button>
          </div>
          <div class="feedback-tip" id="fb-p2_yams">Đáp án: <b>8</b> ("She can buy yams")</div>
        </div>

        <!-- 7. Ham -> 7 -->
        <div class="p2-card">
          <div class="p2-img-wrap"><img src="{images['p2_ham.png']}" alt="Ham"></div>
          <div class="num-slot">
            <span style="font-weight:700;">Số:</span>
            <input type="text" class="num-input" id="p2_ham" data-answer="7" maxlength="1" placeholder="?">
            <button type="button" class="btn-audio-jump" onclick="seekTo(212)">🎧 Câu 7 (03:32)</button>
          </div>
          <div class="feedback-tip" id="fb-p2_ham">Đáp án: <b>7</b> ("He can buy a ham")</div>
        </div>

        <!-- 8. Townhouse -> 5 -->
        <div class="p2-card">
          <div class="p2-img-wrap"><img src="{images['p2_townhouse.png']}" alt="Townhouse"></div>
          <div class="num-slot">
            <span style="font-weight:700;">Số:</span>
            <input type="text" class="num-input" id="p2_townhouse" data-answer="5" maxlength="1" placeholder="?">
            <button type="button" class="btn-audio-jump" onclick="seekTo(192)">🎧 Câu 5 (03:12)</button>
          </div>
          <div class="feedback-tip" id="fb-p2_townhouse">Đáp án: <b>5</b> ("We live in a small townhouse")</div>
        </div>
      </div>
    </section>
"""

# Let's generate Part 3 HTML
part3_html = f"""
    <!-- PART 3: LISTEN AND WRITE A WORD OR A NUMBER -->
    <section class="part-section" id="section-3">
      <div class="part-header">
        <div>
          <div class="part-title">
            <span class="part-badge">PART 3</span>
            Part 3: Read the questions. Listen and write a word or a number on the line.
          </div>
          <p class="part-vi">Nghe cuộc trò chuyện và viết một từ hoặc một con số vào chỗ trống.</p>
        </div>
        <button type="button" class="btn-jump" onclick="seekTo(317)">🎧 Nghe Part 3 (05:17)</button>
      </div>

      <div class="part3-layout">
        <div class="p3-img-wrap">
          <img src="{images['p3_boy_girl.png']}" alt="Jan and Gramps">
          <div style="font-weight:800; color:#831843; margin-top:8px;">Jan & Gramps</div>
        </div>

        <div class="p3-q-list">
          <!-- 1 -->
          <div class="p3-item">
            <div class="p3-item-header">
              <span>1. What is the boy’s name?</span>
              <button type="button" class="btn-audio-jump" onclick="seekTo(325)">🎧 Nghe câu 1 (05:25)</button>
            </div>
            <div class="p3-input-row">
              <input type="text" class="text-input-line" id="p3_1" data-answer="gramps" placeholder="Viết tên...">
            </div>
            <div class="feedback-tip" id="fb-p3_1">Đáp án: <b>Gramps</b> (G-R-A-M-P-S)</div>
          </div>

          <!-- 2 -->
          <div class="p3-item">
            <div class="p3-item-header">
              <span>2. Where does he live?</span>
              <button type="button" class="btn-audio-jump" onclick="seekTo(361)">🎧 Nghe câu 2 (06:01)</button>
            </div>
            <div class="p3-input-row">
              <span>in a</span>
              <input type="text" class="text-input-line" id="p3_2" data-answer="house" placeholder="...">
            </div>
            <div class="feedback-tip" id="fb-p3_2">Đáp án: <b>house</b> (in a house)</div>
          </div>

          <!-- 3 -->
          <div class="p3-item">
            <div class="p3-item-header">
              <span>3. What color is his house?</span>
              <button type="button" class="btn-audio-jump" onclick="seekTo(383)">🎧 Nghe câu 3 (06:23)</button>
            </div>
            <div class="p3-input-row">
              <input type="text" class="text-input-line" id="p3_3" data-answer="yellow" placeholder="Màu sắc...">
            </div>
            <div class="feedback-tip" id="fb-p3_3">Đáp án: <b>yellow</b> (màu vàng)</div>
          </div>

          <!-- 4 -->
          <div class="p3-item">
            <div class="p3-item-header">
              <span>4. How many rooms are there?</span>
              <button type="button" class="btn-audio-jump" onclick="seekTo(403)">🎧 Nghe câu 4 (06:43)</button>
            </div>
            <div class="p3-input-row">
              <input type="text" class="text-input-line" id="p3_4" data-answer="5|five" placeholder="Số phòng..." style="max-width:110px;">
              <span>rooms</span>
            </div>
            <div class="feedback-tip" id="fb-p3_4">Đáp án: <b>5</b> hoặc <b>five</b> (5 rooms)</div>
          </div>

          <!-- 5 -->
          <div class="p3-item">
            <div class="p3-item-header">
              <span>5. What can he do at home?</span>
              <button type="button" class="btn-audio-jump" onclick="seekTo(421)">🎧 Nghe câu 5 (07:01)</button>
            </div>
            <div class="p3-input-row">
              <span>wash and</span>
              <input type="text" class="text-input-line" id="p3_5" data-answer="clean" placeholder="...">
            </div>
            <div class="feedback-tip" id="fb-p3_5">Đáp án: <b>clean</b> (wash and clean)</div>
          </div>
        </div>
      </div>
    </section>
"""

# Let's generate Part 4 HTML
part4_html = f"""
    <!-- PART 4: LISTEN, COLOR AND DRAW -->
    <section class="part-section" id="section-4">
      <div class="part-header">
        <div>
          <div class="part-title">
            <span class="part-badge">PART 4</span>
            Part 4: Listen, color and draw.
          </div>
          <p class="part-vi">Nghe hướng dẫn để chọn màu tô cho các đồ vật và vẽ quả táo lên bàn.</p>
        </div>
        <button type="button" class="btn-jump" onclick="seekTo(554)">🎧 Nghe Part 4 (09:14)</button>
      </div>

      <div class="part4-layout">
        <!-- Canvas area -->
        <div>
          <div class="canvas-container" id="canvasWrap">
            <img src="{images['p4_scene_full.png']}" alt="Bedroom scene" class="canvas-bg-img" id="canvasBgImg">
            <canvas id="drawingCanvas" class="draw-canvas"></canvas>
          </div>

          <!-- Digital color palette for drawing -->
          <div class="canvas-toolbar">
            <span style="font-weight:800; font-size:0.88rem; color:#475569;">Bút màu vẽ:</span>
            <div class="color-swatch-list">
              <button type="button" class="color-btn" style="background:#ea580c;" onclick="setBrushColor('#ea580c')" title="Orange"></button>
              <button type="button" class="color-btn" style="background:#2563eb;" onclick="setBrushColor('#2563eb')" title="Blue"></button>
              <button type="button" class="color-btn" style="background:#dc2626;" onclick="setBrushColor('#dc2626')" title="Red"></button>
              <button type="button" class="color-btn" style="background:#eab308;" onclick="setBrushColor('#eab308')" title="Yellow"></button>
              <button type="button" class="color-btn" style="background:#16a34a;" onclick="setBrushColor('#16a34a')" title="Green"></button>
              <button type="button" class="color-btn" style="background:#9333ea;" onclick="setBrushColor('#9333ea')" title="Purple"></button>
            </div>
            <button type="button" class="btn-jump" style="padding:4px 8px; font-size:0.8rem;" onclick="clearDrawingCanvas()">Xóa nét vẽ</button>
          </div>
          <div style="font-size:0.85rem; color:#64748b; margin-top:6px; font-weight:600;">(Bé có thể dùng ngón tay hoặc chuột vẽ màu trực tiếp lên hình!)</div>
        </div>

        <!-- Interactive checklist for grading -->
        <div class="p4-tasks-list">
          <!-- Task 1: Bag -> Orange -->
          <div class="p4-task-card" id="card-p4_1">
            <div class="p4-task-title">
              <span>1. The bag (Chiếc cặp/ba lô)</span>
              <button type="button" class="btn-audio-jump" onclick="seekTo(561)">🎧 09:21</button>
            </div>
            <div class="color-select-chips">
              <button type="button" class="chip-color" data-q="p4_1" data-val="orange" onclick="selectColor('p4_1', 'orange', this)">Cam (Orange)</button>
              <button type="button" class="chip-color" data-q="p4_1" data-val="blue" onclick="selectColor('p4_1', 'blue', this)">Xanh dương (Blue)</button>
              <button type="button" class="chip-color" data-q="p4_1" data-val="red" onclick="selectColor('p4_1', 'red', this)">Đỏ (Red)</button>
              <button type="button" class="chip-color" data-q="p4_1" data-val="green" onclick="selectColor('p4_1', 'green', this)">Xanh lá (Green)</button>
            </div>
            <div class="feedback-tip" id="fb-p4_1">Đáp án: Tô màu <b>Orange (Cam)</b></div>
          </div>

          <!-- Task 2: Small ship -> Blue -->
          <div class="p4-task-card" id="card-p4_2">
            <div class="p4-task-title">
              <span>2. The small paper ship (Thuyền giấy nhỏ)</span>
              <button type="button" class="btn-audio-jump" onclick="seekTo(600)">🎧 10:00</button>
            </div>
            <div class="color-select-chips">
              <button type="button" class="chip-color" data-q="p4_2" data-val="yellow" onclick="selectColor('p4_2', 'yellow', this)">Vàng (Yellow)</button>
              <button type="button" class="chip-color" data-q="p4_2" data-val="blue" onclick="selectColor('p4_2', 'blue', this)">Xanh dương (Blue)</button>
              <button type="button" class="chip-color" data-q="p4_2" data-val="orange" onclick="selectColor('p4_2', 'orange', this)">Cam (Orange)</button>
              <button type="button" class="chip-color" data-q="p4_2" data-val="purple" onclick="selectColor('p4_2', 'purple', this)">Tím (Purple)</button>
            </div>
            <div class="feedback-tip" id="fb-p4_2">Đáp án: Tô màu <b>Blue (Xanh dương)</b></div>
          </div>

          <!-- Task 3: Fan -> Red -->
          <div class="p4-task-card" id="card-p4_3">
            <div class="p4-task-title">
              <span>3. The fan (Cây quạt)</span>
              <button type="button" class="btn-audio-jump" onclick="seekTo(635)">🎧 10:35</button>
            </div>
            <div class="color-select-chips">
              <button type="button" class="chip-color" data-q="p4_3" data-val="red" onclick="selectColor('p4_3', 'red', this)">Đỏ (Red)</button>
              <button type="button" class="chip-color" data-q="p4_3" data-val="green" onclick="selectColor('p4_3', 'green', this)">Xanh lá (Green)</button>
              <button type="button" class="chip-color" data-q="p4_3" data-val="yellow" onclick="selectColor('p4_3', 'yellow', this)">Vàng (Yellow)</button>
              <button type="button" class="chip-color" data-q="p4_3" data-val="blue" onclick="selectColor('p4_3', 'blue', this)">Xanh dương (Blue)</button>
            </div>
            <div class="feedback-tip" id="fb-p4_3">Đáp án: Tô màu <b>Red (Đỏ)</b></div>
          </div>

          <!-- Task 4: Bell -> Yellow -->
          <div class="p4-task-card" id="card-p4_4">
            <div class="p4-task-title">
              <span>4. The bell under the table (Chiếc chuông dưới gầm bàn)</span>
              <button type="button" class="btn-audio-jump" onclick="seekTo(671)">🎧 11:11</button>
            </div>
            <div class="color-select-chips">
              <button type="button" class="chip-color" data-q="p4_4" data-val="orange" onclick="selectColor('p4_4', 'orange', this)">Cam (Orange)</button>
              <button type="button" class="chip-color" data-q="p4_4" data-val="yellow" onclick="selectColor('p4_4', 'yellow', this)">Vàng (Yellow)</button>
              <button type="button" class="chip-color" data-q="p4_4" data-val="green" onclick="selectColor('p4_4', 'green', this)">Xanh lá (Green)</button>
              <button type="button" class="chip-color" data-q="p4_4" data-val="red" onclick="selectColor('p4_4', 'red', this)">Đỏ (Red)</button>
            </div>
            <div class="feedback-tip" id="fb-p4_4">Đáp án: Tô màu <b>Yellow (Vàng)</b></div>
          </div>

          <!-- Task 5: Hat -> Green -->
          <div class="p4-task-card" id="card-p4_5">
            <div class="p4-task-title">
              <span>5. The hat on the bed (Chiếc mũ lưỡi trai trên giường)</span>
              <button type="button" class="btn-audio-jump" onclick="seekTo(711)">🎧 11:51</button>
            </div>
            <div class="color-select-chips">
              <button type="button" class="chip-color" data-q="p4_5" data-val="blue" onclick="selectColor('p4_5', 'blue', this)">Xanh dương (Blue)</button>
              <button type="button" class="chip-color" data-q="p4_5" data-val="green" onclick="selectColor('p4_5', 'green', this)">Xanh lá (Green)</button>
              <button type="button" class="chip-color" data-q="p4_5" data-val="yellow" onclick="selectColor('p4_5', 'yellow', this)">Vàng (Yellow)</button>
              <button type="button" class="chip-color" data-q="p4_5" data-val="orange" onclick="selectColor('p4_5', 'orange', this)">Cam (Orange)</button>
            </div>
            <div class="feedback-tip" id="fb-p4_5">Đáp án: Tô màu <b>Green (Xanh lá cây)</b></div>
          </div>

          <!-- Task 6: Draw apple -->
          <div class="p4-task-card" id="card-p4_6">
            <div class="p4-task-title">
              <span>6. On the table: Draw what? (Vẽ cái gì lên bàn?)</span>
              <button type="button" class="btn-audio-jump" onclick="seekTo(751)">🎧 12:31</button>
            </div>
            <div class="color-select-chips">
              <button type="button" class="chip-color" data-q="p4_6" data-val="apple" onclick="selectColor('p4_6', 'apple', this)">Quả táo (an apple)</button>
              <button type="button" class="chip-color" data-q="p4_6" data-val="ball" onclick="selectColor('p4_6', 'ball', this)">Quả bóng (a ball)</button>
              <button type="button" class="chip-color" data-q="p4_6" data-val="book" onclick="selectColor('p4_6', 'book', this)">Quyển sách (a book)</button>
            </div>
            <div class="feedback-tip" id="fb-p4_6">Đáp án: Vẽ <b>an apple</b> (một quả táo trên mặt bàn)</div>
          </div>
        </div>
      </div>
    </section>
"""

# Let's generate footer and scripts
footer_html = """
  </main>

  <!-- Sticky Bottom Control Bar -->
  <div class="sticky-bar">
    <div class="sticky-container">
      <div style="display:flex; align-items:center; gap:8px;">
        <button type="button" class="btn-action btn-primary" onclick="gradeAll()">
          <span>🎯</span> Nộp bài & Chấm điểm
        </button>
        <button type="button" class="btn-action btn-accent" onclick="toggleAnswers()">
          <span>💡</span> <span id="toggleAnswersText">Xem đáp án</span>
        </button>
      </div>

      <div style="display:flex; align-items:center; gap:8px;">
        <button type="button" class="btn-action btn-secondary" onclick="resetAll()">
          <span>🔄</span> Làm lại
        </button>
        <button type="button" class="btn-action btn-secondary" onclick="window.print()">
          <span>🖨️</span> In đề
        </button>
      </div>
    </div>
  </div>

  <!-- Score Modal -->
  <div class="modal-backdrop" id="scoreModal">
    <div class="modal-card">
      <div class="modal-trophy" id="modalTrophy">🏆</div>
      <h2 class="modal-title" id="modalTitle">Tuyệt vời! Hoàn thành xuất sắc!</h2>
      <p style="color: #64748b; font-weight: 700;" id="modalStudentName"></p>
      
      <div class="modal-score" id="modalScoreDisplay">24 / 24</div>
      <p style="font-weight: 800; color: #10b981; font-size: 1.15rem;" id="modalMessage">Bé luyện nghe tiếng Anh rất siêu!</p>

      <div class="modal-breakdown" id="modalBreakdown"></div>

      <div style="display:flex; gap:10px; justify-content:center; margin-top:20px;">
        <button type="button" class="btn-action btn-primary" onclick="closeModal()">
          <span>👍</span> Đóng & Xem bài làm
        </button>
        <button type="button" class="btn-action btn-secondary" onclick="closeModal(); resetAll();">
          <span>🔄</span> Làm lại lần nữa
        </button>
      </div>
    </div>
  </div>

  <canvas id="confettiCanvas" style="position:fixed;top:0;left:0;width:100%;height:100%;pointer-events:none;z-index:999;"></canvas>

  <script>
    /* AUDIO CONTROLLER */
    const audio = document.getElementById('mainAudio');
    const playIcon = document.getElementById('playIcon');
    const currTimeEl = document.getElementById('currTime');
    const durTimeEl = document.getElementById('durTime');
    const seekSlider = document.getElementById('seekSlider');

    function fmtTime(sec) {
      if (!sec || isNaN(sec)) return '00:00';
      const m = Math.floor(sec / 60);
      const s = Math.floor(sec % 60);
      return (m < 10 ? '0' : '') + m + ':' + (s < 10 ? '0' : '') + s;
    }

    function togglePlayAudio() {
      if (audio.paused) {
        audio.play();
        playIcon.innerText = '⏸';
      } else {
        audio.pause();
        playIcon.innerText = '▶';
      }
    }

    function seekTo(seconds) {
      audio.currentTime = seconds;
      if (audio.paused) {
        audio.play();
        playIcon.innerText = '⏸';
      }
      playTone(520, 0.08, 'sine');
    }

    function onSeekChange(val) {
      if (audio.duration) {
        audio.currentTime = (val / 100) * audio.duration;
      }
    }

    function setPlaybackSpeed(spd) {
      audio.playbackRate = parseFloat(spd);
    }

    audio.addEventListener('timeupdate', () => {
      currTimeEl.innerText = fmtTime(audio.currentTime);
      if (audio.duration) {
        durTimeEl.innerText = fmtTime(audio.duration);
        seekSlider.value = (audio.currentTime / audio.duration) * 100;
      }
    });

    audio.addEventListener('play', () => { playIcon.innerText = '⏸'; });
    audio.addEventListener('pause', () => { playIcon.innerText = '▶'; });

    /* TONE SYNTHESIZER */
    let audioCtx = null;
    function getAudioContext() {
      if (!audioCtx) audioCtx = new (window.AudioContext || window.webkitAudioContext)();
      return audioCtx;
    }

    function playTone(freq, duration, type = 'sine') {
      try {
        const ctx = getAudioContext();
        if (ctx.state === 'suspended') ctx.resume();
        const osc = ctx.createOscillator();
        const gain = ctx.createGain();
        osc.type = type;
        osc.frequency.setValueAtTime(freq, ctx.currentTime);
        gain.gain.setValueAtTime(0.15, ctx.currentTime);
        gain.gain.exponentialRampToValueAtTime(0.001, ctx.currentTime + duration);
        osc.connect(gain);
        gain.connect(ctx.destination);
        osc.start();
        osc.stop(ctx.currentTime + duration);
      } catch (e) {}
    }

    function playCorrectChime() {
      playTone(523.25, 0.15, 'triangle');
      setTimeout(() => playTone(659.25, 0.15, 'triangle'), 100);
      setTimeout(() => playTone(783.99, 0.25, 'triangle'), 200);
    }

    function playVictoryFanfare() {
      playTone(523.25, 0.12, 'triangle');
      setTimeout(() => playTone(659.25, 0.12, 'triangle'), 120);
      setTimeout(() => playTone(783.99, 0.12, 'triangle'), 240);
      setTimeout(() => playTone(1046.50, 0.45, 'triangle'), 360);
    }

    /* PART 1 TICK SELECTION */
    const tickAnswers = {};
    function selectTick(qId, opt) {
      tickAnswers[qId] = opt;
      const cards = document.querySelectorAll(`.p1-card[data-q="${qId}"]`);
      cards.forEach(card => {
        const isMatch = card.dataset.opt === opt;
        const tickBox = card.querySelector('.tick-box');
        if (isMatch) {
          card.classList.add('selected');
          tickBox.innerText = '✓';
        } else {
          card.classList.remove('selected');
          tickBox.innerText = '';
        }
      });
      playTone(460, 0.08, 'sine');
      saveProgress();
    }

    /* PART 4 COLOR SELECTION */
    const p4Selections = {};
    function selectColor(qId, val, btn) {
      p4Selections[qId] = val;
      const chips = document.querySelectorAll(`.chip-color[data-q="${qId}"]`);
      chips.forEach(c => c.classList.remove('selected'));
      btn.classList.add('selected');
      playTone(500, 0.08, 'triangle');
      saveProgress();
    }

    /* DRAWING CANVAS ON PART 4 */
    let currentBrushColor = '#ea580c';
    let isDrawing = false;
    let canvas, ctx;

    function initCanvas() {
      canvas = document.getElementById('drawingCanvas');
      const wrap = document.getElementById('canvasWrap');
      canvas.width = wrap.clientWidth;
      canvas.height = wrap.clientHeight;
      ctx = canvas.getContext('2d');
      ctx.lineWidth = 5;
      ctx.lineCap = 'round';
      ctx.lineJoin = 'round';

      function getPos(e) {
        const rect = canvas.getBoundingClientRect();
        const clientX = e.touches ? e.touches[0].clientX : e.clientX;
        const clientY = e.touches ? e.touches[0].clientY : e.clientY;
        return {
          x: (clientX - rect.left) * (canvas.width / rect.width),
          y: (clientY - rect.top) * (canvas.height / rect.height)
        };
      }

      function startDraw(e) {
        isDrawing = true;
        const pos = getPos(e);
        ctx.beginPath();
        ctx.moveTo(pos.x, pos.y);
      }

      function draw(e) {
        if (!isDrawing) return;
        const pos = getPos(e);
        ctx.strokeStyle = currentBrushColor;
        ctx.lineTo(pos.x, pos.y);
        ctx.stroke();
      }

      function stopDraw() { isDrawing = false; }

      canvas.addEventListener('mousedown', startDraw);
      canvas.addEventListener('mousemove', draw);
      canvas.addEventListener('mouseup', stopDraw);
      canvas.addEventListener('mouseleave', stopDraw);

      canvas.addEventListener('touchstart', (e) => { e.preventDefault(); startDraw(e); }, { passive: false });
      canvas.addEventListener('touchmove', (e) => { e.preventDefault(); draw(e); }, { passive: false });
      canvas.addEventListener('touchend', stopDraw);
    }

    function setBrushColor(color) {
      currentBrushColor = color;
      document.querySelectorAll('.color-btn').forEach(b => {
        b.classList.toggle('active', b.style.backgroundColor === color);
      });
      playTone(560, 0.06, 'sine');
    }

    function clearDrawingCanvas() {
      if (ctx) {
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        playTone(330, 0.08, 'sine');
      }
    }

    /* GRADING LOGIC */
    const correctPart1 = { p1_1: 'b', p1_2: 'a', p1_3: 'c', p1_4: 'a', p1_5: 'c' };
    const correctPart2 = { p2_sing: '2', p2_sheep: '4', p2_wash_dishes: '1', p2_clean_sink: '3', p2_fold_wash: '6', p2_yams: '8', p2_ham: '7', p2_townhouse: '5' };
    const correctPart3 = { p3_1: 'gramps', p3_2: 'house', p3_3: 'yellow', p3_4: ['5', 'five'], p3_5: 'clean' };
    const correctPart4 = { p4_1: 'orange', p4_2: 'blue', p4_3: 'red', p4_4: 'yellow', p4_5: 'green', p4_6: 'apple' };

    function gradeAll() {
      let score = 0;
      let partScores = { p1: 0, p2: 0, p3: 0, p4: 0 };
      let partTotals = { p1: 5, p2: 8, p3: 5, p4: 6 };

      // Part 1
      for (let q in correctPart1) {
        const userChoice = tickAnswers[q];
        const rightChoice = correctPart1[q];
        const cards = document.querySelectorAll(`.p1-card[data-q="${q}"]`);
        cards.forEach(c => c.classList.remove('correct', 'wrong'));

        if (userChoice === rightChoice) {
          score++;
          partScores.p1++;
          const sel = document.querySelector(`.p1-card[data-q="${q}"][data-opt="${userChoice}"]`);
          if (sel) sel.classList.add('correct');
        } else {
          if (userChoice) {
            const sel = document.querySelector(`.p1-card[data-q="${q}"][data-opt="${userChoice}"]`);
            if (sel) sel.classList.add('wrong');
          }
        }
      }

      // Part 2
      for (let id in correctPart2) {
        const inp = document.getElementById(id);
        const expected = correctPart2[id];
        const userVal = inp.value.trim();
        inp.classList.remove('correct', 'wrong');
        if (userVal === expected) {
          score++;
          partScores.p2++;
          inp.classList.add('correct');
        } else {
          inp.classList.add('wrong');
        }
      }

      // Part 3
      for (let id in correctPart3) {
        const inp = document.getElementById(id);
        const expected = correctPart3[id];
        const userVal = inp.value.trim().toLowerCase();
        let isOk = false;
        if (Array.isArray(expected)) isOk = expected.includes(userVal);
        else isOk = (expected === userVal);

        inp.classList.remove('correct', 'wrong');
        if (isOk) {
          score++;
          partScores.p3++;
          inp.classList.add('correct');
        } else {
          inp.classList.add('wrong');
        }
      }

      // Part 4
      for (let q in correctPart4) {
        const userChoice = p4Selections[q];
        const rightChoice = correctPart4[q];
        const chips = document.querySelectorAll(`.chip-color[data-q="${q}"]`);
        chips.forEach(c => c.classList.remove('correct', 'wrong'));

        if (userChoice === rightChoice) {
          score++;
          partScores.p4++;
          const sel = document.querySelector(`.chip-color[data-q="${q}"][data-val="${userChoice}"]`);
          if (sel) sel.classList.add('correct');
        } else {
          if (userChoice) {
            const sel = document.querySelector(`.chip-color[data-q="${q}"][data-val="${userChoice}"]`);
            if (sel) sel.classList.add('wrong');
          }
        }
      }

      // Show tips for wrong ones
      document.querySelectorAll('.part-section').forEach(sec => {
        sec.querySelectorAll('.wrong').forEach(w => {
          const parent = w.closest('.part1-row, .p2-card, .p3-item, .p4-task-card');
          if (parent) {
            const tip = parent.querySelector('.feedback-tip');
            if (tip) tip.classList.add('show-wrong');
          }
        });
      });

      document.getElementById('currentScore').innerText = score;

      const total = 24;
      if (score === total) {
        playVictoryFanfare();
        triggerConfetti();
      } else if (score >= total * 0.8) {
        playCorrectChime();
        triggerConfetti();
      } else {
        playTone(440, 0.2, 'triangle');
      }

      showScoreModal(score, partScores, partTotals, total);
    }

    function showScoreModal(score, partScores, partTotals, total) {
      const studentName = document.getElementById('studentName').value.trim();
      document.getElementById('modalStudentName').innerText = studentName ? `Học sinh: ${studentName}` : '';
      document.getElementById('modalScoreDisplay').innerText = `${score} / ${total} Điểm`;

      let trophy = '🏆';
      let title = 'Tuyệt vời!';
      let msg = 'Bé nghe tiếng Anh rất tốt!';

      const pct = (score / total) * 100;
      if (pct === 100) {
        trophy = '🌟';
        title = 'Xuất Sắc! Điểm Tuyệt Đối!';
        msg = 'Bé nghe hiểu 100% bài nghe Cambridge Starters!';
      } else if (pct >= 85) {
        trophy = '🥇';
        title = 'Giỏi Quá!';
        msg = 'Bé làm đúng hầu hết bài nghe! Rất đáng khen ngợi!';
      } else if (pct >= 65) {
        trophy = '🥈';
        title = 'Khá Tốt!';
        msg = 'Bé hãy bấm vào các mốc thời gian để nghe lại câu chưa đúng nhé!';
      } else {
        trophy = '💪';
        title = 'Cần Luyện Nghe Thêm!';
        msg = 'Bé hãy bấm nút Xem đáp án và tua lại audio để nghe kĩ hơn nha!';
      }

      document.getElementById('modalTrophy').innerText = trophy;
      document.getElementById('modalTitle').innerText = title;
      document.getElementById('modalMessage').innerText = msg;

      const breakdownEl = document.getElementById('modalBreakdown');
      breakdownEl.innerHTML = `
        <div class="breakdown-row"><span>Part 1 (Tick the correct picture):</span> <b>${partScores.p1} / ${partTotals.p1}</b></div>
        <div class="breakdown-row"><span>Part 2 (Number the pictures):</span> <b>${partScores.p2} / ${partTotals.p2}</b></div>
        <div class="breakdown-row"><span>Part 3 (Write a word or number):</span> <b>${partScores.p3} / ${partTotals.p3}</b></div>
        <div class="breakdown-row"><span>Part 4 (Listen, color and draw):</span> <b>${partScores.p4} / ${partTotals.p4}</b></div>
      `;

      document.getElementById('scoreModal').style.display = 'flex';
    }

    function closeModal() {
      document.getElementById('scoreModal').style.display = 'none';
    }

    let showingAnswers = false;
    function toggleAnswers() {
      showingAnswers = !showingAnswers;
      const tips = document.querySelectorAll('.feedback-tip');
      tips.forEach(t => {
        if (showingAnswers) t.classList.add('show-correct');
        else t.classList.remove('show-correct', 'show-wrong');
      });
      document.getElementById('toggleAnswersText').innerText = showingAnswers ? 'Ẩn đáp án' : 'Xem đáp án';
      playTone(550, 0.08, 'sine');
    }

    function resetAll() {
      if (confirm('Bé có muốn làm lại đề thi Listening từ đầu không?')) {
        for (let k in tickAnswers) delete tickAnswers[k];
        document.querySelectorAll('.p1-card').forEach(c => {
          c.classList.remove('selected', 'correct', 'wrong');
          c.querySelector('.tick-box').innerText = '';
        });

        document.querySelectorAll('input.num-input, input.text-input-line').forEach(inp => {
          inp.value = '';
          inp.classList.remove('correct', 'wrong');
        });

        for (let k in p4Selections) delete p4Selections[k];
        document.querySelectorAll('.chip-color').forEach(c => c.classList.remove('selected', 'correct', 'wrong'));
        document.querySelectorAll('.feedback-tip').forEach(t => t.classList.remove('show-correct', 'show-wrong'));

        clearDrawingCanvas();
        document.getElementById('currentScore').innerText = '0';
        showingAnswers = false;
        document.getElementById('toggleAnswersText').innerText = 'Xem đáp án';

        try { localStorage.removeItem('listening2_midterm1_answers'); } catch(e) {}

        window.scrollTo({ top: 0, behavior: 'smooth' });
        playTone(600, 0.1, 'sine');
      }
    }

    function triggerConfetti() {
      const canvas = document.getElementById('confettiCanvas');
      const ctx = canvas.getContext('2d');
      canvas.width = window.innerWidth;
      canvas.height = window.innerHeight;

      const particles = [];
      const colors = ['#f43f5e', '#ec4899', '#8b5cf6', '#3b82f6', '#10b981', '#f59e0b'];

      for (let i = 0; i < 120; i++) {
        particles.push({
          x: canvas.width / 2,
          y: canvas.height / 2,
          w: Math.random() * 10 + 6,
          h: Math.random() * 8 + 4,
          color: colors[Math.floor(Math.random() * colors.length)],
          vx: (Math.random() - 0.5) * 18,
          vy: (Math.random() - 0.7) * 18,
          rot: Math.random() * 360,
          vrot: (Math.random() - 0.5) * 10,
          gravity: 0.35,
          alpha: 1
        });
      }

      let frame = 0;
      function animate() {
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        let alive = false;
        particles.forEach(p => {
          p.x += p.vx;
          p.y += p.vy;
          p.vy += p.gravity;
          p.rot += p.vrot;
          p.alpha -= 0.008;
          if (p.alpha > 0) {
            alive = true;
            ctx.save();
            ctx.globalAlpha = p.alpha;
            ctx.translate(p.x, p.y);
            ctx.rotate((p.rot * Math.PI) / 180);
            ctx.fillStyle = p.color;
            ctx.fillRect(-p.w / 2, -p.h / 2, p.w, p.h);
            ctx.restore();
          }
        });
        frame++;
        if (alive && frame < 200) requestAnimationFrame(animate);
        else ctx.clearRect(0, 0, canvas.width, canvas.height);
      }
      requestAnimationFrame(animate);
    }

    const STORAGE_KEY = 'listening2_midterm1_answers';
    function saveProgress() {
      const data = {
        name: document.getElementById('studentName').value,
        className: document.getElementById('studentClass').value,
        ticks: tickAnswers,
        numInputs: {},
        textInputs: {},
        p4Colors: p4Selections
      };
      document.querySelectorAll('.num-input').forEach(i => data.numInputs[i.id] = i.value);
      document.querySelectorAll('.text-input-line').forEach(i => data.textInputs[i.id] = i.value);

      try {
        localStorage.setItem(STORAGE_KEY, JSON.stringify(data));
        localStorage.setItem('student_profile', JSON.stringify({ name: data.name, className: data.className }));
      } catch(e) {}
    }

    function loadProgress() {
      try {
        const profRaw = localStorage.getItem('student_profile');
        if (profRaw) {
          const prof = JSON.parse(profRaw);
          if (prof.name) document.getElementById('studentName').value = prof.name;
          if (prof.className) document.getElementById('studentClass').value = prof.className;
        }

        const raw = localStorage.getItem(STORAGE_KEY);
        if (!raw) return;
        const data = JSON.parse(raw);
        if (data.name) document.getElementById('studentName').value = data.name;
        if (data.className) document.getElementById('studentClass').value = data.className;

        if (data.ticks) {
          for (let q in data.ticks) selectTick(q, data.ticks[q]);
        }
        if (data.numInputs) {
          for (let id in data.numInputs) {
            const el = document.getElementById(id);
            if (el) el.value = data.numInputs[id];
          }
        }
        if (data.textInputs) {
          for (let id in data.textInputs) {
            const el = document.getElementById(id);
            if (el) el.value = data.textInputs[id];
          }
        }
        if (data.p4Colors) {
          for (let q in data.p4Colors) {
            const val = data.p4Colors[q];
            const btn = document.querySelector(`.chip-color[data-q="${q}"][data-val="${val}"]`);
            if (btn) selectColor(q, val, btn);
          }
        }
      } catch(e) {}
    }

    document.addEventListener('input', () => { saveProgress(); });

    window.addEventListener('load', () => {
      initCanvas();
      loadProgress();
    });

    window.addEventListener('resize', () => {
      if (canvas && document.getElementById('canvasWrap')) {
        const wrap = document.getElementById('canvasWrap');
        canvas.width = wrap.clientWidth;
        canvas.height = wrap.clientHeight;
      }
    });
  </script>
</body>
</html>
"""

full_html = head_html + part1_html + part2_html + part3_html + part4_html + footer_html

with open('listening.html', 'w', encoding='utf-8') as f:
    f.write(full_html)

print(f"Generated listening.html successfully with {len(full_html)} bytes.")
