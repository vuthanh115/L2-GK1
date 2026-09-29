# -*- coding: utf-8 -*-
import json
import os

with open('assets/maths_b64.json', 'r', encoding='utf-8') as f:
    maths_images = json.load(f)

print(f"Loaded {len(maths_images)} maths images.")

head_html = """<!DOCTYPE html>
<html lang="vi">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Maths 2 - Review for Midterm Test 1 | Ôn Tập Toán Tiếng Anh Lớp 2</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Nunito:wght@400;600;700;800;900&display=swap" rel="stylesheet">
  <style>
    :root {
      --primary: #0284c7;
      --primary-hover: #0369a1;
      --primary-light: #e0f2fe;
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
      padding-bottom: 100px;
    }

    .header-banner {
      background: linear-gradient(135deg, #0ea5e9 0%, #0284c7 50%, #2563eb 100%);
      color: white;
      padding: 24px 16px 28px;
      border-radius: 0 0 28px 28px;
      box-shadow: 0 10px 25px -5px rgba(2, 132, 199, 0.35);
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
      color: #e0f2fe;
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
      color: #0f172a;
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

    .btn-audio {
      background: #f0f9ff;
      border: 1px solid #bae6fd;
      color: #0284c7;
      cursor: pointer;
      padding: 6px 12px;
      border-radius: 10px;
      font-size: 0.9rem;
      display: inline-flex;
      align-items: center;
      gap: 6px;
      font-weight: 700;
      transition: all 0.2s;
      flex-shrink: 0;
    }

    .btn-audio:hover {
      background: #e0f2fe;
      transform: scale(1.05);
    }

    .btn-audio:active {
      transform: scale(0.96);
    }

    /* Math inputs */
    .math-input {
      width: 75px;
      padding: 8px 10px;
      border: 2px solid #cbd5e1;
      border-radius: 10px;
      font-family: inherit;
      font-size: 1.2rem;
      font-weight: 800;
      text-align: center;
      color: #1e293b;
      outline: none;
      transition: all 0.2s;
      background: #ffffff;
    }

    .math-input:focus {
      border-color: var(--primary);
      background: #f0f9ff;
      box-shadow: 0 0 0 3px rgba(2, 132, 199, 0.15);
    }

    .math-input.correct {
      border-color: var(--success) !important;
      background: #f0fdf4 !important;
      color: #15803d !important;
    }

    .math-input.wrong {
      border-color: var(--danger) !important;
      background: #fef2f2 !important;
      color: #b91c1c !important;
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

    /* Grid for subquestions */
    .math-grid-2 {
      display: grid;
      grid-template-columns: repeat(2, 1fr);
      gap: 16px;
    }

    .math-grid-3 {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 16px;
    }

    .math-grid-4 {
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 16px;
    }

    @media (max-width: 768px) {
      .math-grid-2, .math-grid-3, .math-grid-4 {
        grid-template-columns: 1fr;
      }
    }

    .math-card {
      background: #f8fafc;
      border: 1px solid #e2e8f0;
      border-radius: 14px;
      padding: 16px;
      display: flex;
      flex-direction: column;
      gap: 10px;
    }

    .math-row {
      display: flex;
      align-items: center;
      gap: 8px;
      font-size: 1.25rem;
      font-weight: 800;
      flex-wrap: wrap;
    }

    /* Interactive Abacus */
    .abacus-card {
      background: #ffffff;
      border: 2px solid #e2e8f0;
      border-radius: 16px;
      padding: 16px;
      display: flex;
      flex-direction: column;
      align-items: center;
      text-align: center;
    }

    .abacus-title {
      font-size: 1.35rem;
      font-weight: 900;
      color: var(--primary);
      margin-bottom: 8px;
    }

    .abacus-frame {
      width: 150px;
      height: 180px;
      background: #f8fafc;
      border: 2px solid #cbd5e1;
      border-radius: 12px;
      position: relative;
      display: flex;
      justify-content: space-around;
      padding-top: 10px;
      margin-bottom: 8px;
    }

    .abacus-rod {
      width: 50px;
      height: 130px;
      display: flex;
      flex-direction: column-reverse;
      align-items: center;
      position: relative;
      cursor: pointer;
    }

    .abacus-rod::before {
      content: '';
      position: absolute;
      top: 0;
      bottom: 0;
      left: 50%;
      width: 4px;
      background: #94a3b8;
      transform: translateX(-50%);
      border-radius: 2px;
      z-index: 1;
    }

    .bead {
      width: 32px;
      height: 12px;
      border-radius: 8px;
      background: #3b82f6;
      border: 1px solid #1d4ed8;
      box-shadow: 0 1px 3px rgba(0,0,0,0.2);
      z-index: 2;
      margin-bottom: 1px;
      animation: beadDrop 0.2s ease-out;
    }

    .bead.tens {
      background: #f59e0b;
      border-color: #d97706;
    }

    .bead.units {
      background: #10b981;
      border-color: #059669;
    }

    @keyframes beadDrop {
      from { transform: translateY(-10px); opacity: 0; }
      to { transform: translateY(0); opacity: 1; }
    }

    .abacus-base {
      position: absolute;
      bottom: 0;
      left: 0;
      right: 0;
      height: 38px;
      background: #e2e8f0;
      border-top: 2px solid #cbd5e1;
      display: flex;
      justify-content: space-around;
      align-items: center;
      font-weight: 800;
      font-size: 0.85rem;
      color: #334155;
      border-radius: 0 0 10px 10px;
    }

    .abacus-controls {
      display: flex;
      gap: 12px;
      margin-top: 6px;
    }

    .rod-control {
      display: flex;
      flex-direction: column;
      align-items: center;
      gap: 4px;
    }

    .btn-step {
      width: 28px;
      height: 28px;
      border-radius: 50%;
      border: 1px solid #cbd5e1;
      background: #ffffff;
      font-size: 1rem;
      font-weight: 800;
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: center;
      transition: all 0.15s;
    }

    .btn-step:hover {
      background: var(--primary-light);
      color: var(--primary);
      border-color: var(--primary);
    }

    /* Arrow cards */
    .arrow-card-wrap {
      display: inline-flex;
      align-items: center;
      gap: 4px;
    }

    .arrow-card {
      padding: 8px 18px 8px 14px;
      color: white;
      font-weight: 900;
      font-size: 1.25rem;
      display: inline-flex;
      align-items: center;
      clip-path: polygon(0% 0%, 82% 0%, 100% 50%, 82% 100%, 0% 100%);
      box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }

    .card-hundreds {
      background: #3b82f6;
      min-width: 85px;
    }

    .card-tens {
      background: #f59e0b;
      min-width: 65px;
    }

    .card-units {
      background: #10b981;
      min-width: 50px;
    }

    /* Clickable digits */
    .digit-box {
      display: inline-flex;
      gap: 4px;
      background: #f1f5f9;
      padding: 4px 8px;
      border-radius: 12px;
      border: 1px solid #cbd5e1;
    }

    .digit-btn {
      width: 38px;
      height: 42px;
      border-radius: 8px;
      border: 2px solid transparent;
      background: #ffffff;
      font-size: 1.35rem;
      font-weight: 900;
      color: #1e293b;
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: center;
      transition: all 0.15s;
    }

    .digit-btn:hover {
      background: var(--primary-light);
      color: var(--primary);
    }

    .digit-btn.selected {
      border-color: var(--primary);
      background: var(--primary-light);
      color: var(--primary);
      transform: scale(1.08);
      box-shadow: 0 2px 6px rgba(2, 132, 199, 0.25);
    }

    .digit-btn.correct {
      border-color: var(--success) !important;
      background: var(--success-light) !important;
      color: #065f46 !important;
    }

    .digit-btn.wrong {
      border-color: var(--danger) !important;
      background: var(--danger-light) !important;
      color: #991b1b !important;
    }

    /* Underlined digits */
    .num-underlined {
      font-size: 1.5rem;
      font-weight: 900;
      letter-spacing: 2px;
      color: #1e293b;
    }

    .num-underlined u {
      text-decoration: underline 4px #0284c7;
      text-underline-offset: 4px;
      color: #0284c7;
    }

    /* Vertical math */
    .vertical-math {
      display: inline-flex;
      flex-direction: column;
      align-items: flex-end;
      font-family: inherit;
      font-size: 1.35rem;
      font-weight: 800;
      padding: 10px 16px;
      background: #ffffff;
      border: 2px solid #e2e8f0;
      border-radius: 12px;
      min-width: 100px;
    }

    .vertical-line {
      width: 100%;
      height: 2px;
      background: #1e293b;
      margin: 6px 0;
    }

    /* Addition Wall */
    .brick-wall {
      display: flex;
      flex-direction: column;
      align-items: center;
      gap: 6px;
      padding: 14px;
      background: #fffbeb;
      border: 2px solid #fde68a;
      border-radius: 16px;
    }

    .wall-row {
      display: flex;
      gap: 6px;
    }

    .wall-brick {
      min-width: 70px;
      height: 48px;
      background: #ffffff;
      border: 2px solid #d97706;
      border-radius: 8px;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 1.25rem;
      font-weight: 900;
      color: #b45309;
      box-shadow: 0 2px 4px rgba(0,0,0,0.06);
    }

    .wall-brick input {
      width: 100%;
      height: 100%;
      border: none;
      background: transparent;
      text-align: center;
      font-size: 1.25rem;
      font-weight: 900;
      color: #0284c7;
      outline: none;
    }

    /* Sticky Bottom Bar */
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
      background: linear-gradient(135deg, #0ea5e9 0%, #0284c7 100%);
      color: white;
      box-shadow: 0 4px 12px rgba(2, 132, 199, 0.35);
    }

    .btn-primary:hover {
      transform: translateY(-2px);
      box-shadow: 0 6px 16px rgba(2, 132, 199, 0.45);
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
      max-width: 540px;
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
      color: #0f172a;
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
      max-height: 220px;
      overflow-y: auto;
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
      .header-banner::before, .header-banner::after, .header-score-pill, .sticky-bar, .btn-audio, .btn-step, .modal-backdrop, .feedback-tip, .nav-links { display: none !important; }
      .student-info-bar { background: none !important; border: 1px solid #000 !important; }
      .part-section { box-shadow: none !important; border: 1px solid #ccc !important; page-break-inside: avoid; margin-bottom: 20px; }
      .math-input { border-bottom: 1px solid #000 !important; border-top: none !important; border-left: none !important; border-right: none !important; border-radius: 0 !important; }
    }
  </style>
</head>
<body>

  <!-- Header Banner -->
  <header class="header-banner">
    <div class="header-container">
      <div class="nav-links">
        <a href="index.html" class="nav-btn">
          🏠 Về Trang Chủ
        </a>
        <a href="english.html" class="nav-btn">
          🇬🇧 Sang Môn Tiếng Anh (English 2)
        </a>
      </div>

      <div class="title-row">
        <div>
          <h1 class="main-title">
            <span>🔢</span> Maths 2 - Review for Midterm Test 1
          </h1>
          <p class="sub-title">Đề Ôn Tập Thi Giữa Học Kì 1 - Môn Toán Tiếng Anh Lớp 2</p>
        </div>
        <div class="header-score-pill" id="scoreIndicator">
          <span>⭐ Điểm:</span> <span id="currentScore">0</span> / <span id="totalScore">90</span>
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

  <!-- Main Content -->
  <main class="container">
"""

# Let's generate all 18 questions in section markup
sections_html = f"""
    <!-- QUESTION 1 -->
    <section class="part-section" id="section-1">
      <div class="part-header">
        <div>
          <div class="part-title">
            <span class="part-badge">1</span>
            1- Write each number as tens and units.
          </div>
          <p class="part-vi">Tách mỗi số thành số tròn chục (tens) và số đơn vị (units).</p>
        </div>
        <button type="button" class="btn-audio" onclick="speak('Question one: Write each number as tens and units.')">🔊 Nghe đề bài</button>
      </div>

      <div class="math-grid-2">
        <div class="math-card">
          <div class="math-row">
            <span>a-) 45 ➜</span>
            <input type="text" class="math-input" id="q1_a_tens" data-answer="40|4" placeholder="Chục">
            <span>+</span>
            <input type="text" class="math-input" id="q1_a_units" data-answer="5" placeholder="Đơn vị">
          </div>
          <div class="feedback-tip" id="fb-q1_a">Đáp án: <b>40 + 5</b> (4 chục và 5 đơn vị)</div>
        </div>

        <div class="math-card">
          <div class="math-row">
            <span>b-) 87 ➜</span>
            <input type="text" class="math-input" id="q1_b_tens" data-answer="80|8" placeholder="Chục">
            <span>+</span>
            <input type="text" class="math-input" id="q1_b_units" data-answer="7" placeholder="Đơn vị">
          </div>
          <div class="feedback-tip" id="fb-q1_b">Đáp án: <b>80 + 7</b> (8 chục và 7 đơn vị)</div>
        </div>

        <div class="math-card">
          <div class="math-row">
            <span>c-) 63 ➜</span>
            <input type="text" class="math-input" id="q1_c_tens" data-answer="60|6" placeholder="Chục">
            <span>+</span>
            <input type="text" class="math-input" id="q1_c_units" data-answer="3" placeholder="Đơn vị">
          </div>
          <div class="feedback-tip" id="fb-q1_c">Đáp án: <b>60 + 3</b> (6 chục và 3 đơn vị)</div>
        </div>

        <div class="math-card">
          <div class="math-row">
            <span>d-) 29 ➜</span>
            <input type="text" class="math-input" id="q1_d_tens" data-answer="20|2" placeholder="Chục">
            <span>+</span>
            <input type="text" class="math-input" id="q1_d_units" data-answer="9" placeholder="Đơn vị">
          </div>
          <div class="feedback-tip" id="fb-q1_d">Đáp án: <b>20 + 9</b> (2 chục và 9 đơn vị)</div>
        </div>
      </div>
    </section>

    <!-- QUESTION 2 -->
    <section class="part-section" id="section-2">
      <div class="part-header">
        <div>
          <div class="part-title">
            <span class="part-badge">2</span>
            2- Draw the correct numbers of beads to show these numbers.
          </div>
          <p class="part-vi">Bấm nút + / - (hoặc bấm vào cột) để thêm các hạt cườm vào bàn tính thể hiện đúng số.</p>
        </div>
        <button type="button" class="btn-audio" onclick="speak('Question two: Draw the correct numbers of beads to show these numbers.')">🔊 Nghe đề bài</button>
      </div>

      <div class="math-grid-3">
        <!-- a-) 57 -->
        <div class="abacus-card">
          <div class="abacus-title">a-) 57</div>
          <div class="abacus-frame">
            <div class="abacus-rod" id="rod-q2_a_tens" onclick="addBead('q2_a', 'tens')"></div>
            <div class="abacus-rod" id="rod-q2_a_units" onclick="addBead('q2_a', 'units')"></div>
            <div class="abacus-base">
              <span>Tens (<b id="lbl-q2_a_tens">0</b>)</span>
              <span>Units (<b id="lbl-q2_a_units">0</b>)</span>
            </div>
          </div>
          <div class="abacus-controls">
            <div class="rod-control">
              <span style="font-size:0.8rem; font-weight:700;">Hàng chục:</span>
              <div style="display:flex; gap:4px;">
                <button type="button" class="btn-step" onclick="stepBead('q2_a', 'tens', -1)">-</button>
                <button type="button" class="btn-step" onclick="stepBead('q2_a', 'tens', 1)">+</button>
              </div>
            </div>
            <div class="rod-control">
              <span style="font-size:0.8rem; font-weight:700;">Đơn vị:</span>
              <div style="display:flex; gap:4px;">
                <button type="button" class="btn-step" onclick="stepBead('q2_a', 'units', -1)">-</button>
                <button type="button" class="btn-step" onclick="stepBead('q2_a', 'units', 1)">+</button>
              </div>
            </div>
          </div>
          <div class="feedback-tip" id="fb-q2_a">Đáp án: <b>5 hạt ở Tens</b> và <b>7 hạt ở Units</b></div>
        </div>

        <!-- b-) 81 -->
        <div class="abacus-card">
          <div class="abacus-title">b-) 81</div>
          <div class="abacus-frame">
            <div class="abacus-rod" id="rod-q2_b_tens" onclick="addBead('q2_b', 'tens')"></div>
            <div class="abacus-rod" id="rod-q2_b_units" onclick="addBead('q2_b', 'units')"></div>
            <div class="abacus-base">
              <span>Tens (<b id="lbl-q2_b_tens">0</b>)</span>
              <span>Units (<b id="lbl-q2_b_units">0</b>)</span>
            </div>
          </div>
          <div class="abacus-controls">
            <div class="rod-control">
              <span style="font-size:0.8rem; font-weight:700;">Hàng chục:</span>
              <div style="display:flex; gap:4px;">
                <button type="button" class="btn-step" onclick="stepBead('q2_b', 'tens', -1)">-</button>
                <button type="button" class="btn-step" onclick="stepBead('q2_b', 'tens', 1)">+</button>
              </div>
            </div>
            <div class="rod-control">
              <span style="font-size:0.8rem; font-weight:700;">Đơn vị:</span>
              <div style="display:flex; gap:4px;">
                <button type="button" class="btn-step" onclick="stepBead('q2_b', 'units', -1)">-</button>
                <button type="button" class="btn-step" onclick="stepBead('q2_b', 'units', 1)">+</button>
              </div>
            </div>
          </div>
          <div class="feedback-tip" id="fb-q2_b">Đáp án: <b>8 hạt ở Tens</b> và <b>1 hạt ở Units</b></div>
        </div>

        <!-- c-) 27 -->
        <div class="abacus-card">
          <div class="abacus-title">c-) 27</div>
          <div class="abacus-frame">
            <div class="abacus-rod" id="rod-q2_c_tens" onclick="addBead('q2_c', 'tens')"></div>
            <div class="abacus-rod" id="rod-q2_c_units" onclick="addBead('q2_c', 'units')"></div>
            <div class="abacus-base">
              <span>Tens (<b id="lbl-q2_c_tens">0</b>)</span>
              <span>Units (<b id="lbl-q2_c_units">0</b>)</span>
            </div>
          </div>
          <div class="abacus-controls">
            <div class="rod-control">
              <span style="font-size:0.8rem; font-weight:700;">Hàng chục:</span>
              <div style="display:flex; gap:4px;">
                <button type="button" class="btn-step" onclick="stepBead('q2_c', 'tens', -1)">-</button>
                <button type="button" class="btn-step" onclick="stepBead('q2_c', 'tens', 1)">+</button>
              </div>
            </div>
            <div class="rod-control">
              <span style="font-size:0.8rem; font-weight:700;">Đơn vị:</span>
              <div style="display:flex; gap:4px;">
                <button type="button" class="btn-step" onclick="stepBead('q2_c', 'units', -1)">-</button>
                <button type="button" class="btn-step" onclick="stepBead('q2_c', 'units', 1)">+</button>
              </div>
            </div>
          </div>
          <div class="feedback-tip" id="fb-q2_c">Đáp án: <b>2 hạt ở Tens</b> và <b>7 hạt ở Units</b></div>
        </div>

        <!-- d-) 34 -->
        <div class="abacus-card">
          <div class="abacus-title">d-) 34</div>
          <div class="abacus-frame">
            <div class="abacus-rod" id="rod-q2_d_tens" onclick="addBead('q2_d', 'tens')"></div>
            <div class="abacus-rod" id="rod-q2_d_units" onclick="addBead('q2_d', 'units')"></div>
            <div class="abacus-base">
              <span>Tens (<b id="lbl-q2_d_tens">0</b>)</span>
              <span>Units (<b id="lbl-q2_d_units">0</b>)</span>
            </div>
          </div>
          <div class="abacus-controls">
            <div class="rod-control">
              <span style="font-size:0.8rem; font-weight:700;">Hàng chục:</span>
              <div style="display:flex; gap:4px;">
                <button type="button" class="btn-step" onclick="stepBead('q2_d', 'tens', -1)">-</button>
                <button type="button" class="btn-step" onclick="stepBead('q2_d', 'tens', 1)">+</button>
              </div>
            </div>
            <div class="rod-control">
              <span style="font-size:0.8rem; font-weight:700;">Đơn vị:</span>
              <div style="display:flex; gap:4px;">
                <button type="button" class="btn-step" onclick="stepBead('q2_d', 'units', -1)">-</button>
                <button type="button" class="btn-step" onclick="stepBead('q2_d', 'units', 1)">+</button>
              </div>
            </div>
          </div>
          <div class="feedback-tip" id="fb-q2_d">Đáp án: <b>3 hạt ở Tens</b> và <b>4 hạt ở Units</b></div>
        </div>

        <!-- e-) 63 -->
        <div class="abacus-card">
          <div class="abacus-title">e-) 63</div>
          <div class="abacus-frame">
            <div class="abacus-rod" id="rod-q2_e_tens" onclick="addBead('q2_e', 'tens')"></div>
            <div class="abacus-rod" id="rod-q2_e_units" onclick="addBead('q2_e', 'units')"></div>
            <div class="abacus-base">
              <span>Tens (<b id="lbl-q2_e_tens">0</b>)</span>
              <span>Units (<b id="lbl-q2_e_units">0</b>)</span>
            </div>
          </div>
          <div class="abacus-controls">
            <div class="rod-control">
              <span style="font-size:0.8rem; font-weight:700;">Hàng chục:</span>
              <div style="display:flex; gap:4px;">
                <button type="button" class="btn-step" onclick="stepBead('q2_e', 'tens', -1)">-</button>
                <button type="button" class="btn-step" onclick="stepBead('q2_e', 'tens', 1)">+</button>
              </div>
            </div>
            <div class="rod-control">
              <span style="font-size:0.8rem; font-weight:700;">Đơn vị:</span>
              <div style="display:flex; gap:4px;">
                <button type="button" class="btn-step" onclick="stepBead('q2_e', 'units', -1)">-</button>
                <button type="button" class="btn-step" onclick="stepBead('q2_e', 'units', 1)">+</button>
              </div>
            </div>
          </div>
          <div class="feedback-tip" id="fb-q2_e">Đáp án: <b>6 hạt ở Tens</b> và <b>3 hạt ở Units</b></div>
        </div>

        <!-- f-) 19 -->
        <div class="abacus-card">
          <div class="abacus-title">f-) 19</div>
          <div class="abacus-frame">
            <div class="abacus-rod" id="rod-q2_f_tens" onclick="addBead('q2_f', 'tens')"></div>
            <div class="abacus-rod" id="rod-q2_f_units" onclick="addBead('q2_f', 'units')"></div>
            <div class="abacus-base">
              <span>Tens (<b id="lbl-q2_f_tens">0</b>)</span>
              <span>Units (<b id="lbl-q2_f_units">0</b>)</span>
            </div>
          </div>
          <div class="abacus-controls">
            <div class="rod-control">
              <span style="font-size:0.8rem; font-weight:700;">Hàng chục:</span>
              <div style="display:flex; gap:4px;">
                <button type="button" class="btn-step" onclick="stepBead('q2_f', 'tens', -1)">-</button>
                <button type="button" class="btn-step" onclick="stepBead('q2_f', 'tens', 1)">+</button>
              </div>
            </div>
            <div class="rod-control">
              <span style="font-size:0.8rem; font-weight:700;">Đơn vị:</span>
              <div style="display:flex; gap:4px;">
                <button type="button" class="btn-step" onclick="stepBead('q2_f', 'units', -1)">-</button>
                <button type="button" class="btn-step" onclick="stepBead('q2_f', 'units', 1)">+</button>
              </div>
            </div>
          </div>
          <div class="feedback-tip" id="fb-q2_f">Đáp án: <b>1 hạt ở Tens</b> và <b>9 hạt ở Units</b></div>
        </div>
      </div>
    </section>

    <!-- QUESTION 3 -->
    <section class="part-section" id="section-3">
      <div class="part-header">
        <div>
          <div class="part-title">
            <span class="part-badge">3</span>
            3- Write the numbers for these arrow cards.
          </div>
          <p class="part-vi">Ghép các thẻ mũi tên (trăm, chục, đơn vị) lại thành số hoàn chỉnh.</p>
        </div>
        <button type="button" class="btn-audio" onclick="speak('Question three: Write the numbers for these arrow cards.')">🔊 Nghe đề bài</button>
      </div>

      <div class="math-grid-3">
        <div class="math-card">
          <div style="font-weight:800; color:#475569; margin-bottom:4px;">a-)</div>
          <div class="math-row">
            <div class="arrow-card-wrap">
              <span class="arrow-card card-hundreds">300</span>
              <span class="arrow-card card-tens">70</span>
              <span class="arrow-card card-units">5</span>
            </div>
            <span>➜</span>
            <input type="text" class="math-input" id="q3_a" data-answer="375" placeholder="?">
          </div>
          <div class="feedback-tip" id="fb-q3_a">Đáp án: <b>375</b></div>
        </div>

        <div class="math-card">
          <div style="font-weight:800; color:#475569; margin-bottom:4px;">b-)</div>
          <div class="math-row">
            <div class="arrow-card-wrap">
              <span class="arrow-card card-hundreds">500</span>
              <span class="arrow-card card-tens">80</span>
              <span class="arrow-card card-units">4</span>
            </div>
            <span>➜</span>
            <input type="text" class="math-input" id="q3_b" data-answer="584" placeholder="?">
          </div>
          <div class="feedback-tip" id="fb-q3_b">Đáp án: <b>584</b></div>
        </div>

        <div class="math-card">
          <div style="font-weight:800; color:#475569; margin-bottom:4px;">c-)</div>
          <div class="math-row">
            <div class="arrow-card-wrap">
              <span class="arrow-card card-hundreds">900</span>
              <span class="arrow-card card-tens">20</span>
              <span class="arrow-card card-units">7</span>
            </div>
            <span>➜</span>
            <input type="text" class="math-input" id="q3_c" data-answer="927" placeholder="?">
          </div>
          <div class="feedback-tip" id="fb-q3_c">Đáp án: <b>927</b></div>
        </div>
      </div>
    </section>

    <!-- QUESTION 4 -->
    <section class="part-section" id="section-4">
      <div class="part-header">
        <div>
          <div class="part-title">
            <span class="part-badge">4</span>
            4- Write each number as hundreds, tens and units.
          </div>
          <p class="part-vi">Viết mỗi số thành tổng các số tròn trăm (hundreds), tròn chục (tens) và đơn vị (units).</p>
        </div>
        <button type="button" class="btn-audio" onclick="speak('Question four: Write each number as hundreds, tens and units.')">🔊 Nghe đề bài</button>
      </div>

      <div class="math-grid-2">
        <div class="math-card">
          <div class="math-row">
            <span>a-) 527 ➜</span>
            <input type="text" class="math-input" id="q4_a_h" data-answer="500|5" placeholder="Trăm">
            <span>+</span>
            <input type="text" class="math-input" id="q4_a_t" data-answer="20|2" placeholder="Chục">
            <span>+</span>
            <input type="text" class="math-input" id="q4_a_u" data-answer="7" placeholder="Đv">
          </div>
          <div class="feedback-tip" id="fb-q4_a">Đáp án: <b>500 + 20 + 7</b></div>
        </div>

        <div class="math-card">
          <div class="math-row">
            <span>b-) 268 ➜</span>
            <input type="text" class="math-input" id="q4_b_h" data-answer="200|2" placeholder="Trăm">
            <span>+</span>
            <input type="text" class="math-input" id="q4_b_t" data-answer="60|6" placeholder="Chục">
            <span>+</span>
            <input type="text" class="math-input" id="q4_b_u" data-answer="8" placeholder="Đv">
          </div>
          <div class="feedback-tip" id="fb-q4_b">Đáp án: <b>200 + 60 + 8</b></div>
        </div>

        <div class="math-card">
          <div class="math-row">
            <span>c-) 843 ➜</span>
            <input type="text" class="math-input" id="q4_c_h" data-answer="800|8" placeholder="Trăm">
            <span>+</span>
            <input type="text" class="math-input" id="q4_c_t" data-answer="40|4" placeholder="Chục">
            <span>+</span>
            <input type="text" class="math-input" id="q4_c_u" data-answer="3" placeholder="Đv">
          </div>
          <div class="feedback-tip" id="fb-q4_c">Đáp án: <b>800 + 40 + 3</b></div>
        </div>

        <div class="math-card">
          <div class="math-row">
            <span>d-) 371 ➜</span>
            <input type="text" class="math-input" id="q4_d_h" data-answer="300|3" placeholder="Trăm">
            <span>+</span>
            <input type="text" class="math-input" id="q4_d_t" data-answer="70|7" placeholder="Chục">
            <span>+</span>
            <input type="text" class="math-input" id="q4_d_u" data-answer="1" placeholder="Đv">
          </div>
          <div class="feedback-tip" id="fb-q4_d">Đáp án: <b>300 + 70 + 1</b></div>
        </div>
      </div>
    </section>

    <!-- QUESTION 5 -->
    <section class="part-section" id="section-5">
      <div class="part-header">
        <div>
          <div class="part-title">
            <span class="part-badge">5</span>
            5- Write these words as numbers.
          </div>
          <p class="part-vi">Đọc chữ số bằng tiếng Anh và viết thành số tương ứng.</p>
        </div>
        <button type="button" class="btn-audio" onclick="speak('Question five: Write these words as numbers.')">🔊 Nghe đề bài</button>
      </div>

      <div class="math-grid-2">
        <div class="math-card">
          <div style="font-weight:700; font-size:1.1rem; color:#1e293b;">
            a-) one hundred and seventy-six
            <button type="button" class="btn-audio" onclick="speak('one hundred and seventy-six')">🔊</button>
          </div>
          <div class="math-row">
            <span>➜ Số:</span>
            <input type="text" class="math-input" id="q5_a" data-answer="176" placeholder="?">
          </div>
          <div class="feedback-tip" id="fb-q5_a">Đáp án: <b>176</b></div>
        </div>

        <div class="math-card">
          <div style="font-weight:700; font-size:1.1rem; color:#1e293b;">
            b-) one hundred and thirty-one
            <button type="button" class="btn-audio" onclick="speak('one hundred and thirty-one')">🔊</button>
          </div>
          <div class="math-row">
            <span>➜ Số:</span>
            <input type="text" class="math-input" id="q5_b" data-answer="131" placeholder="?">
          </div>
          <div class="feedback-tip" id="fb-q5_b">Đáp án: <b>131</b></div>
        </div>

        <div class="math-card">
          <div style="font-weight:700; font-size:1.1rem; color:#1e293b;">
            c-) one hundred and fifty-two
            <button type="button" class="btn-audio" onclick="speak('one hundred and fifty-two')">🔊</button>
          </div>
          <div class="math-row">
            <span>➜ Số:</span>
            <input type="text" class="math-input" id="q5_c" data-answer="152" placeholder="?">
          </div>
          <div class="feedback-tip" id="fb-q5_c">Đáp án: <b>152</b></div>
        </div>

        <div class="math-card">
          <div style="font-weight:700; font-size:1.1rem; color:#1e293b;">
            d-) one hundred and ninety-eight
            <button type="button" class="btn-audio" onclick="speak('one hundred and ninety-eight')">🔊</button>
          </div>
          <div class="math-row">
            <span>➜ Số:</span>
            <input type="text" class="math-input" id="q5_d" data-answer="198" placeholder="?">
          </div>
          <div class="feedback-tip" id="fb-q5_d">Đáp án: <b>198</b></div>
        </div>
      </div>
    </section>

    <!-- QUESTION 6 -->
    <section class="part-section" id="section-6">
      <div class="part-header">
        <div>
          <div class="part-title">
            <span class="part-badge">6</span>
            6- Circle the digit in each number that shows these values.
          </div>
          <p class="part-vi">Bấm chọn (khoanh tròn) chữ số thể hiện đúng giá trị được hỏi.</p>
        </div>
        <button type="button" class="btn-audio" onclick="speak('Question six: Circle the digit in each number that shows these values.')">🔊 Nghe đề bài</button>
      </div>

      <div class="math-grid-2">
        <!-- a-) 189 -->
        <div class="math-card">
          <div style="font-weight:700; font-size:1.05rem;">
            a-) Which digit shows <b>one hundred</b>?
            <button type="button" class="btn-audio" onclick="speak('Which digit shows one hundred in 189?')">🔊</button>
          </div>
          <div class="math-row">
            <div class="digit-box" id="box-q6_a">
              <button type="button" class="digit-btn" data-q="q6_a" data-val="1" data-correct="true" onclick="selectDigit('q6_a', this)">1</button>
              <button type="button" class="digit-btn" data-q="q6_a" data-val="8" data-correct="false" onclick="selectDigit('q6_a', this)">8</button>
              <button type="button" class="digit-btn" data-q="q6_a" data-val="9" data-correct="false" onclick="selectDigit('q6_a', this)">9</button>
            </div>
          </div>
          <div class="feedback-tip" id="fb-q6_a">Đáp án: chữ số <b>1</b> (ở hàng trăm = 100)</div>
        </div>

        <!-- b-) 133 -->
        <div class="math-card">
          <div style="font-weight:700; font-size:1.05rem;">
            b-) Which digit shows <b>three</b> (3 đơn vị)?
            <button type="button" class="btn-audio" onclick="speak('Which digit shows three in 133?')">🔊</button>
          </div>
          <div class="math-row">
            <div class="digit-box" id="box-q6_b">
              <button type="button" class="digit-btn" data-q="q6_b" data-val="1" data-correct="false" onclick="selectDigit('q6_b', this)">1</button>
              <button type="button" class="digit-btn" data-q="q6_b" data-val="3_tens" data-correct="false" onclick="selectDigit('q6_b', this)">3</button>
              <button type="button" class="digit-btn" data-q="q6_b" data-val="3_units" data-correct="true" onclick="selectDigit('q6_b', this)">3</button>
            </div>
          </div>
          <div class="feedback-tip" id="fb-q6_b">Đáp án: chữ số <b>3</b> ở hàng đơn vị (chữ số 3 cuối cùng)</div>
        </div>

        <!-- c-) 175 -->
        <div class="math-card">
          <div style="font-weight:700; font-size:1.05rem;">
            c-) Which digit shows <b>70</b> (bảy mươi)?
            <button type="button" class="btn-audio" onclick="speak('Which digit shows 70 in 175?')">🔊</button>
          </div>
          <div class="math-row">
            <div class="digit-box" id="box-q6_c">
              <button type="button" class="digit-btn" data-q="q6_c" data-val="1" data-correct="false" onclick="selectDigit('q6_c', this)">1</button>
              <button type="button" class="digit-btn" data-q="q6_c" data-val="7" data-correct="true" onclick="selectDigit('q6_c', this)">7</button>
              <button type="button" class="digit-btn" data-q="q6_c" data-val="5" data-correct="false" onclick="selectDigit('q6_c', this)">5</button>
            </div>
          </div>
          <div class="feedback-tip" id="fb-q6_c">Đáp án: chữ số <b>7</b> (ở hàng chục = 70)</div>
        </div>

        <!-- d-) 147 -->
        <div class="math-card">
          <div style="font-weight:700; font-size:1.05rem;">
            d-) Which digit shows <b>forty</b> (bốn mươi)?
            <button type="button" class="btn-audio" onclick="speak('Which digit shows forty in 147?')">🔊</button>
          </div>
          <div class="math-row">
            <div class="digit-box" id="box-q6_d">
              <button type="button" class="digit-btn" data-q="q6_d" data-val="1" data-correct="false" onclick="selectDigit('q6_d', this)">1</button>
              <button type="button" class="digit-btn" data-q="q6_d" data-val="4" data-correct="true" onclick="selectDigit('q6_d', this)">4</button>
              <button type="button" class="digit-btn" data-q="q6_d" data-val="7" data-correct="false" onclick="selectDigit('q6_d', this)">7</button>
            </div>
          </div>
          <div class="feedback-tip" id="fb-q6_d">Đáp án: chữ số <b>4</b> (ở hàng chục = 40)</div>
        </div>
      </div>
    </section>

    <!-- QUESTION 7 -->
    <section class="part-section" id="section-7">
      <div class="part-header">
        <div>
          <div class="part-title">
            <span class="part-badge">7</span>
            7- Write the numbers shown on each mat.
          </div>
          <p class="part-vi">Đếm số khối vuông (hundreds), thanh que (tens), khối nhỏ (units) và viết số tương ứng.</p>
        </div>
        <button type="button" class="btn-audio" onclick="speak('Question seven: Write the numbers shown on each mat.')">🔊 Nghe đề bài</button>
      </div>

      <div style="display:flex; flex-direction:column; gap:18px;">
        <!-- a-) -->
        <div class="math-card">
          <div style="font-weight:800; color:#0284c7;">a-)</div>
          <div style="display:flex; align-items:center; gap:16px; flex-wrap:wrap;">
            <img src="{maths_images['p2_q7_mat_a.png']}" alt="Base 10 Mat a" style="max-height:85px; border-radius:8px; border:1px solid #cbd5e1; background:#fff;">
            <div class="math-row">
              <input type="text" class="math-input" id="q7_a_h" data-answer="2" style="width:55px;"> <span>hundreds</span>
              <input type="text" class="math-input" id="q7_a_t" data-answer="1" style="width:55px;"> <span>tens</span>
              <input type="text" class="math-input" id="q7_a_u" data-answer="6" style="width:55px;"> <span>units</span>
              <span>➜</span>
              <input type="text" class="math-input" id="q7_a_total" data-answer="216" style="width:90px;" placeholder="Tổng">
            </div>
          </div>
          <div class="feedback-tip" id="fb-q7_a">Đáp án: <b>2</b> hundreds, <b>1</b> tens, <b>6</b> units ➜ <b>216</b></div>
        </div>

        <!-- b-) -->
        <div class="math-card">
          <div style="font-weight:800; color:#0284c7;">b-)</div>
          <div style="display:flex; align-items:center; gap:16px; flex-wrap:wrap;">
            <img src="{maths_images['p2_q7_mat_b.png']}" alt="Base 10 Mat b" style="max-height:85px; border-radius:8px; border:1px solid #cbd5e1; background:#fff;">
            <div class="math-row">
              <input type="text" class="math-input" id="q7_b_h" data-answer="3" style="width:55px;"> <span>hundreds</span>
              <input type="text" class="math-input" id="q7_b_t" data-answer="2" style="width:55px;"> <span>tens</span>
              <input type="text" class="math-input" id="q7_b_u" data-answer="4" style="width:55px;"> <span>units</span>
              <span>➜</span>
              <input type="text" class="math-input" id="q7_b_total" data-answer="324" style="width:90px;" placeholder="Tổng">
            </div>
          </div>
          <div class="feedback-tip" id="fb-q7_b">Đáp án: <b>3</b> hundreds, <b>2</b> tens, <b>4</b> units ➜ <b>324</b></div>
        </div>

        <!-- c-) -->
        <div class="math-card">
          <div style="font-weight:800; color:#0284c7;">c-)</div>
          <div style="display:flex; align-items:center; gap:16px; flex-wrap:wrap;">
            <img src="{maths_images['p2_q7_mat_c.png']}" alt="Base 10 Mat c" style="max-height:85px; border-radius:8px; border:1px solid #cbd5e1; background:#fff;">
            <div class="math-row">
              <input type="text" class="math-input" id="q7_c_h" data-answer="2" style="width:55px;"> <span>hundreds</span>
              <input type="text" class="math-input" id="q7_c_t" data-answer="4" style="width:55px;"> <span>tens</span>
              <input type="text" class="math-input" id="q7_c_u" data-answer="1" style="width:55px;"> <span>unit</span>
              <span>➜</span>
              <input type="text" class="math-input" id="q7_c_total" data-answer="241" style="width:90px;" placeholder="Tổng">
            </div>
          </div>
          <div class="feedback-tip" id="fb-q7_c">Đáp án: <b>2</b> hundreds, <b>4</b> tens, <b>1</b> unit ➜ <b>241</b></div>
        </div>

        <!-- d-) -->
        <div class="math-card">
          <div style="font-weight:800; color:#0284c7;">d-)</div>
          <div style="display:flex; align-items:center; gap:16px; flex-wrap:wrap;">
            <img src="{maths_images['p2_q7_mat_d.png']}" alt="Base 10 Mat d" style="max-height:85px; border-radius:8px; border:1px solid #cbd5e1; background:#fff;">
            <div class="math-row">
              <input type="text" class="math-input" id="q7_d_h" data-answer="3" style="width:55px;"> <span>hundreds</span>
              <input type="text" class="math-input" id="q7_d_t" data-answer="3" style="width:55px;"> <span>tens</span>
              <input type="text" class="math-input" id="q7_d_u" data-answer="5" style="width:55px;"> <span>units</span>
              <span>➜</span>
              <input type="text" class="math-input" id="q7_d_total" data-answer="335" style="width:90px;" placeholder="Tổng">
            </div>
          </div>
          <div class="feedback-tip" id="fb-q7_d">Đáp án: <b>3</b> hundreds, <b>3</b> tens, <b>5</b> units ➜ <b>335</b></div>
        </div>
      </div>
    </section>

    <!-- QUESTION 8 -->
    <section class="part-section" id="section-8">
      <div class="part-header">
        <div>
          <div class="part-title">
            <span class="part-badge">8</span>
            8- Write the value of the underlined digits in the following numbers.
          </div>
          <p class="part-vi">Viết giá trị của chữ số được gạch chân trong mỗi số bên dưới.</p>
        </div>
        <button type="button" class="btn-audio" onclick="speak('Question eight: Write the value of the underlined digits in the following numbers.')">🔊 Nghe đề bài</button>
      </div>

      <div class="math-grid-4">
        <div class="math-card">
          <div class="num-underlined">a-) <u>3</u>65</div>
          <div class="math-row">
            <span>➜</span>
            <input type="text" class="math-input" id="q8_a" data-answer="300" placeholder="Giá trị">
          </div>
          <div class="feedback-tip" id="fb-q8_a">Đáp án: <b>300</b></div>
        </div>

        <div class="math-card">
          <div class="num-underlined">b-) <u>9</u>17</div>
          <div class="math-row">
            <span>➜</span>
            <input type="text" class="math-input" id="q8_b" data-answer="900" placeholder="Giá trị">
          </div>
          <div class="feedback-tip" id="fb-q8_b">Đáp án: <b>900</b></div>
        </div>

        <div class="math-card">
          <div class="num-underlined">c-) 7<u>2</u>8</div>
          <div class="math-row">
            <span>➜</span>
            <input type="text" class="math-input" id="q8_c" data-answer="20" placeholder="Giá trị">
          </div>
          <div class="feedback-tip" id="fb-q8_c">Đáp án: <b>20</b></div>
        </div>

        <div class="math-card">
          <div class="num-underlined">d-) 1<u>0</u>5</div>
          <div class="math-row">
            <span>➜</span>
            <input type="text" class="math-input" id="q8_d" data-answer="0" placeholder="Giá trị">
          </div>
          <div class="feedback-tip" id="fb-q8_d">Đáp án: <b>0</b></div>
        </div>

        <div class="math-card">
          <div class="num-underlined">e-) 24<u>8</u></div>
          <div class="math-row">
            <span>➜</span>
            <input type="text" class="math-input" id="q8_e" data-answer="8" placeholder="Giá trị">
          </div>
          <div class="feedback-tip" id="fb-q8_e">Đáp án: <b>8</b></div>
        </div>

        <div class="math-card">
          <div class="num-underlined">f-) 8<u>4</u>7</div>
          <div class="math-row">
            <span>➜</span>
            <input type="text" class="math-input" id="q8_f" data-answer="40" placeholder="Giá trị">
          </div>
          <div class="feedback-tip" id="fb-q8_f">Đáp án: <b>40</b></div>
        </div>

        <div class="math-card">
          <div class="num-underlined">g-) <u>3</u>26</div>
          <div class="math-row">
            <span>➜</span>
            <input type="text" class="math-input" id="q8_g" data-answer="300" placeholder="Giá trị">
          </div>
          <div class="feedback-tip" id="fb-q8_g">Đáp án: <b>300</b></div>
        </div>

        <div class="math-card">
          <div class="num-underlined">h-) 63<u>1</u></div>
          <div class="math-row">
            <span>➜</span>
            <input type="text" class="math-input" id="q8_h" data-answer="1" placeholder="Giá trị">
          </div>
          <div class="feedback-tip" id="fb-q8_h">Đáp án: <b>1</b></div>
        </div>
      </div>
    </section>

    <!-- QUESTION 9 -->
    <section class="part-section" id="section-9">
      <div class="part-header">
        <div>
          <div class="part-title">
            <span class="part-badge">9</span>
            9- Complete these.
          </div>
          <p class="part-vi">Hoàn thành các phép tính từ hàng trăm, hàng chục và hàng đơn vị.</p>
        </div>
        <button type="button" class="btn-audio" onclick="speak('Question nine: Complete these.')">🔊 Nghe đề bài</button>
      </div>

      <div class="math-grid-2">
        <div class="math-card">
          <div class="math-row">
            <span>a-) 3 hundreds 7 tens 5 units =</span>
            <input type="text" class="math-input" id="q9_a" data-answer="375" placeholder="?">
          </div>
          <div class="feedback-tip" id="fb-q9_a">Đáp án: <b>375</b></div>
        </div>

        <div class="math-card">
          <div class="math-row">
            <span>b-) 7 hundreds 2 tens 8 units =</span>
            <input type="text" class="math-input" id="q9_b" data-answer="728" placeholder="?">
          </div>
          <div class="feedback-tip" id="fb-q9_b">Đáp án: <b>728</b></div>
        </div>

        <div class="math-card">
          <div class="math-row">
            <span>c-) 4 hundreds 9 tens 3 units =</span>
            <input type="text" class="math-input" id="q9_c" data-answer="493" placeholder="?">
          </div>
          <div class="feedback-tip" id="fb-q9_c">Đáp án: <b>493</b></div>
        </div>

        <div class="math-card">
          <div class="math-row">
            <span>d-) 8 hundreds 3 tens 4 units =</span>
            <input type="text" class="math-input" id="q9_d" data-answer="834" placeholder="?">
          </div>
          <div class="feedback-tip" id="fb-q9_d">Đáp án: <b>834</b></div>
        </div>
      </div>
    </section>

    <!-- QUESTION 10 -->
    <section class="part-section" id="section-10">
      <div class="part-header">
        <div>
          <div class="part-title">
            <span class="part-badge">10</span>
            10- Complete these.
          </div>
          <p class="part-vi">Cộng các số tròn trăm, tròn chục và đơn vị.</p>
        </div>
        <button type="button" class="btn-audio" onclick="speak('Question ten: Complete these.')">🔊 Nghe đề bài</button>
      </div>

      <div class="math-grid-2">
        <div class="math-card">
          <div class="math-row">
            <span>a-) 500 + 80 + 4 =</span>
            <input type="text" class="math-input" id="q10_a" data-answer="584" placeholder="?">
          </div>
          <div class="feedback-tip" id="fb-q10_a">Đáp án: <b>584</b></div>
        </div>

        <div class="math-card">
          <div class="math-row">
            <span>b-) 200 + 60 + 7 =</span>
            <input type="text" class="math-input" id="q10_b" data-answer="267" placeholder="?">
          </div>
          <div class="feedback-tip" id="fb-q10_b">Đáp án: <b>267</b></div>
        </div>

        <div class="math-card">
          <div class="math-row">
            <span>c-) 800 + 30 + 5 =</span>
            <input type="text" class="math-input" id="q10_c" data-answer="835" placeholder="?">
          </div>
          <div class="feedback-tip" id="fb-q10_c">Đáp án: <b>835</b></div>
        </div>

        <div class="math-card">
          <div class="math-row">
            <span>d-) 300 + 90 + 2 =</span>
            <input type="text" class="math-input" id="q10_d" data-answer="392" placeholder="?">
          </div>
          <div class="feedback-tip" id="fb-q10_d">Đáp án: <b>392</b></div>
        </div>
      </div>
    </section>

    <!-- QUESTION 11 -->
    <section class="part-section" id="section-11">
      <div class="part-header">
        <div>
          <div class="part-title">
            <span class="part-badge">11</span>
            11- Complete these.
          </div>
          <p class="part-vi">Cộng các thanh chục (tens rods) và viết phép tính tương ứng.</p>
        </div>
        <button type="button" class="btn-audio" onclick="speak('Question eleven: Complete these.')">🔊 Nghe đề bài</button>
      </div>

      <div class="math-grid-2">
        <!-- a-) -->
        <div class="math-card">
          <div style="font-weight:800; color:#0284c7;">a-)</div>
          <img src="{maths_images['p3_q11_a.png']}" alt="Rods a" style="max-height:80px; align-self:flex-start; border-radius:8px;">
          <div class="math-row" style="margin-top:6px;">
            <span>4 tens + 3 tens =</span>
            <input type="text" class="math-input" id="q11_a_tens" data-answer="7 tens|7" style="width:90px;" placeholder="?"> <span>tens</span>
          </div>
          <div class="math-row">
            <span>40 + 30 =</span>
            <input type="text" class="math-input" id="q11_a_val" data-answer="70" placeholder="?">
          </div>
          <div class="feedback-tip" id="fb-q11_a">Đáp án: <b>7</b> tens và <b>70</b></div>
        </div>

        <!-- b-) -->
        <div class="math-card">
          <div style="font-weight:800; color:#0284c7;">b-)</div>
          <img src="{maths_images['p3_q11_b.png']}" alt="Rods b" style="max-height:80px; align-self:flex-start; border-radius:8px;">
          <div class="math-row" style="margin-top:6px;">
            <span>8 tens + 1 ten =</span>
            <input type="text" class="math-input" id="q11_b_tens" data-answer="9 tens|9" style="width:90px;" placeholder="?"> <span>tens</span>
          </div>
          <div class="math-row">
            <span>80 + 10 =</span>
            <input type="text" class="math-input" id="q11_b_val" data-answer="90" placeholder="?">
          </div>
          <div class="feedback-tip" id="fb-q11_b">Đáp án: <b>9</b> tens và <b>90</b></div>
        </div>

        <!-- c-) -->
        <div class="math-card">
          <div style="font-weight:800; color:#0284c7;">c-)</div>
          <img src="{maths_images['p3_q11_c.png']}" alt="Rods c" style="max-height:80px; align-self:flex-start; border-radius:8px;">
          <div class="math-row" style="margin-top:6px;">
            <span>6 tens + 2 tens =</span>
            <input type="text" class="math-input" id="q11_c_tens" data-answer="8 tens|8" style="width:90px;" placeholder="?"> <span>tens</span>
          </div>
          <div class="math-row">
            <span>60 + 20 =</span>
            <input type="text" class="math-input" id="q11_c_val" data-answer="80" placeholder="?">
          </div>
          <div class="feedback-tip" id="fb-q11_c">Đáp án: <b>8</b> tens và <b>80</b></div>
        </div>

        <!-- d-) -->
        <div class="math-card">
          <div style="font-weight:800; color:#0284c7;">d-)</div>
          <img src="{maths_images['p3_q11_d.png']}" alt="Rods d" style="max-height:80px; align-self:flex-start; border-radius:8px;">
          <div class="math-row" style="margin-top:6px;">
            <span>7 tens + 2 tens =</span>
            <input type="text" class="math-input" id="q11_d_tens" data-answer="9 tens|9" style="width:90px;" placeholder="?"> <span>tens</span>
          </div>
          <div class="math-row">
            <span>70 + 20 =</span>
            <input type="text" class="math-input" id="q11_d_val" data-answer="90" placeholder="?">
          </div>
          <div class="feedback-tip" id="fb-q11_d">Đáp án: <b>9</b> tens và <b>90</b></div>
        </div>
      </div>
    </section>

    <!-- QUESTION 12 -->
    <section class="part-section" id="section-12">
      <div class="part-header">
        <div>
          <div class="part-title">
            <span class="part-badge">12</span>
            12- Answer these.
          </div>
          <p class="part-vi">Thực hiện phép cộng hai số có hai chữ số (không nhớ).</p>
        </div>
        <button type="button" class="btn-audio" onclick="speak('Question twelve: Answer these.')">🔊 Nghe đề bài</button>
      </div>

      <div class="math-grid-3">
        <div class="math-card">
          <div class="math-row"><span>a-) 27 + 51 =</span> <input type="text" class="math-input" id="q12_a" data-answer="78"></div>
          <div class="feedback-tip" id="fb-q12_a">Đáp án: <b>78</b></div>
        </div>

        <div class="math-card">
          <div class="math-row"><span>b-) 45 + 32 =</span> <input type="text" class="math-input" id="q12_b" data-answer="77"></div>
          <div class="feedback-tip" id="fb-q12_b">Đáp án: <b>77</b></div>
        </div>

        <div class="math-card">
          <div class="math-row"><span>c-) 31 + 68 =</span> <input type="text" class="math-input" id="q12_c" data-answer="99"></div>
          <div class="feedback-tip" id="fb-q12_c">Đáp án: <b>99</b></div>
        </div>

        <div class="math-card">
          <div class="math-row"><span>d-) 65 + 12 =</span> <input type="text" class="math-input" id="q12_d" data-answer="77"></div>
          <div class="feedback-tip" id="fb-q12_d">Đáp án: <b>77</b></div>
        </div>

        <div class="math-card">
          <div class="math-row"><span>e-) 16 + 72 =</span> <input type="text" class="math-input" id="q12_e" data-answer="88"></div>
          <div class="feedback-tip" id="fb-q12_e">Đáp án: <b>88</b></div>
        </div>

        <div class="math-card">
          <div class="math-row"><span>f-) 53 + 36 =</span> <input type="text" class="math-input" id="q12_f" data-answer="89"></div>
          <div class="feedback-tip" id="fb-q12_f">Đáp án: <b>89</b></div>
        </div>
      </div>
    </section>

    <!-- QUESTION 13 -->
    <section class="part-section" id="section-13">
      <div class="part-header">
        <div>
          <div class="part-title">
            <span class="part-badge">13</span>
            13- Add these. Use tens and units to help.
          </div>
          <p class="part-vi">Quan sát các thanh chục và khối đơn vị để tính kết quả phép cộng.</p>
        </div>
        <button type="button" class="btn-audio" onclick="speak('Question thirteen: Add these. Use tens and units to help.')">🔊 Nghe đề bài</button>
      </div>

      <div class="math-grid-2">
        <div class="math-card">
          <div style="font-weight:800; color:#0284c7;">a-)</div>
          <img src="{maths_images['p3_q13_a.png']}" alt="Blocks a" style="max-height:75px; align-self:flex-start; border-radius:8px;">
          <div class="math-row">
            <span>67 + 8 =</span>
            <input type="text" class="math-input" id="q13_a" data-answer="75">
          </div>
          <div class="feedback-tip" id="fb-q13_a">Đáp án: <b>75</b> (67 + 3 = 70; 70 + 5 = 75)</div>
        </div>

        <div class="math-card">
          <div style="font-weight:800; color:#0284c7;">b-)</div>
          <img src="{maths_images['p3_q13_b.png']}" alt="Blocks b" style="max-height:75px; align-self:flex-start; border-radius:8px;">
          <div class="math-row">
            <span>19 + 5 =</span>
            <input type="text" class="math-input" id="q13_b" data-answer="24">
          </div>
          <div class="feedback-tip" id="fb-q13_b">Đáp án: <b>24</b> (19 + 1 = 20; 20 + 4 = 24)</div>
        </div>

        <div class="math-card">
          <div style="font-weight:800; color:#0284c7;">c-)</div>
          <img src="{maths_images['p3_q13_c.png']}" alt="Blocks c" style="max-height:75px; align-self:flex-start; border-radius:8px;">
          <div class="math-row">
            <span>23 + 8 =</span>
            <input type="text" class="math-input" id="q13_c" data-answer="31">
          </div>
          <div class="feedback-tip" id="fb-q13_c">Đáp án: <b>31</b> (23 + 7 = 30; 30 + 1 = 31)</div>
        </div>

        <div class="math-card">
          <div style="font-weight:800; color:#0284c7;">d-)</div>
          <img src="{maths_images['p3_q13_d.png']}" alt="Blocks d" style="max-height:75px; align-self:flex-start; border-radius:8px;">
          <div class="math-row">
            <span>42 + 9 =</span>
            <input type="text" class="math-input" id="q13_d" data-answer="51">
          </div>
          <div class="feedback-tip" id="fb-q13_d">Đáp án: <b>51</b> (42 + 8 = 50; 50 + 1 = 51)</div>
        </div>
      </div>
    </section>

    <!-- QUESTION 14 -->
    <section class="part-section" id="section-14">
      <div class="part-header">
        <div>
          <div class="part-title">
            <span class="part-badge">14</span>
            14- Answer these.
          </div>
          <p class="part-vi">Cộng nhẩm nhanh các số có nhớ qua mười.</p>
        </div>
        <button type="button" class="btn-audio" onclick="speak('Question fourteen: Answer these.')">🔊 Nghe đề bài</button>
      </div>

      <div class="math-grid-4">
        <div class="math-card">
          <div class="math-row"><span>a-) 34 + 6 =</span> <input type="text" class="math-input" id="q14_a" data-answer="40"></div>
          <div class="feedback-tip" id="fb-q14_a">Đáp án: <b>40</b></div>
        </div>

        <div class="math-card">
          <div class="math-row"><span>b-) 85 + 5 =</span> <input type="text" class="math-input" id="q14_b" data-answer="90"></div>
          <div class="feedback-tip" id="fb-q14_b">Đáp án: <b>90</b></div>
        </div>

        <div class="math-card">
          <div class="math-row"><span>c-) 29 + 1 =</span> <input type="text" class="math-input" id="q14_c" data-answer="30"></div>
          <div class="feedback-tip" id="fb-q14_c">Đáp án: <b>30</b></div>
        </div>

        <div class="math-card">
          <div class="math-row"><span>d-) 57 + 39 =</span> <input type="text" class="math-input" id="q14_d" data-answer="96"></div>
          <div class="feedback-tip" id="fb-q14_d">Đáp án: <b>96</b></div>
        </div>

        <div class="math-card">
          <div class="math-row"><span>e-) 66 + 7 =</span> <input type="text" class="math-input" id="q14_e" data-answer="73"></div>
          <div class="feedback-tip" id="fb-q14_e">Đáp án: <b>73</b></div>
        </div>

        <div class="math-card">
          <div class="math-row"><span>f-) 48 + 6 =</span> <input type="text" class="math-input" id="q14_f" data-answer="54"></div>
          <div class="feedback-tip" id="fb-q14_f">Đáp án: <b>54</b></div>
        </div>

        <div class="math-card">
          <div class="math-row"><span>g-) 14 + 9 =</span> <input type="text" class="math-input" id="q14_g" data-answer="23"></div>
          <div class="feedback-tip" id="fb-q14_g">Đáp án: <b>23</b></div>
        </div>

        <div class="math-card">
          <div class="math-row"><span>h-) 87 + 5 =</span> <input type="text" class="math-input" id="q14_h" data-answer="92"></div>
          <div class="feedback-tip" id="fb-q14_h">Đáp án: <b>92</b></div>
        </div>
      </div>
    </section>

    <!-- QUESTION 15 -->
    <section class="part-section" id="section-15">
      <div class="part-header">
        <div>
          <div class="part-title">
            <span class="part-badge">15</span>
            15- Complete these. (Partitioning Method)
          </div>
          <p class="part-vi">Cộng bằng cách tách thành chục + chục và đơn vị + đơn vị rồi cộng lại.</p>
        </div>
        <button type="button" class="btn-audio" onclick="speak('Question fifteen: Complete these.')">🔊 Nghe đề bài</button>
      </div>

      <div class="math-grid-2">
        <!-- a-) 56 + 27 -->
        <div class="math-card">
          <div style="font-size:1.15rem; font-weight:800; color:#1e293b; line-height:1.8;">
            <b>a-) 56 + 27</b> ➜ <br>
            &nbsp;&nbsp;&nbsp;&nbsp;50 + 6 <br>
            + &nbsp;20 + 7 <br>
            <div style="height:1px; background:#cbd5e1; margin:6px 0;"></div>
            <div class="math-row">
              <input type="text" class="math-input" id="q15_a_t" data-answer="70" placeholder="50+20">
              <span>+</span>
              <input type="text" class="math-input" id="q15_a_u" data-answer="13" placeholder="6+7">
              <span>➜</span>
              <input type="text" class="math-input" id="q15_a_total" data-answer="83" placeholder="Tổng">
            </div>
          </div>
          <div class="feedback-tip" id="fb-q15_a">Đáp án: <b>70 + 13 = 83</b></div>
        </div>

        <!-- b-) 26 + 55 -->
        <div class="math-card">
          <div style="font-size:1.15rem; font-weight:800; color:#1e293b; line-height:1.8;">
            <b>b-) 26 + 55</b> ➜ <br>
            &nbsp;&nbsp;&nbsp;&nbsp;20 + 6 <br>
            + &nbsp;50 + 5 <br>
            <div style="height:1px; background:#cbd5e1; margin:6px 0;"></div>
            <div class="math-row">
              <input type="text" class="math-input" id="q15_b_t" data-answer="70" placeholder="20+50">
              <span>+</span>
              <input type="text" class="math-input" id="q15_b_u" data-answer="11" placeholder="6+5">
              <span>➜</span>
              <input type="text" class="math-input" id="q15_b_total" data-answer="81" placeholder="Tổng">
            </div>
          </div>
          <div class="feedback-tip" id="fb-q15_b">Đáp án: <b>70 + 11 = 81</b></div>
        </div>

        <!-- c-) 37 + 49 -->
        <div class="math-card">
          <div style="font-size:1.15rem; font-weight:800; color:#1e293b; line-height:1.8;">
            <b>c-) 37 + 49</b> ➜ <br>
            &nbsp;&nbsp;&nbsp;&nbsp;30 + 7 <br>
            + &nbsp;40 + 9 <br>
            <div style="height:1px; background:#cbd5e1; margin:6px 0;"></div>
            <div class="math-row">
              <input type="text" class="math-input" id="q15_c_t" data-answer="70" placeholder="30+40">
              <span>+</span>
              <input type="text" class="math-input" id="q15_c_u" data-answer="16" placeholder="7+9">
              <span>➜</span>
              <input type="text" class="math-input" id="q15_c_total" data-answer="86" placeholder="Tổng">
            </div>
          </div>
          <div class="feedback-tip" id="fb-q15_c">Đáp án: <b>70 + 16 = 86</b></div>
        </div>

        <!-- d-) 48 + 38 -->
        <div class="math-card">
          <div style="font-size:1.15rem; font-weight:800; color:#1e293b; line-height:1.8;">
            <b>d-) 48 + 38</b> ➜ <br>
            &nbsp;&nbsp;&nbsp;&nbsp;40 + 8 <br>
            + &nbsp;30 + 8 <br>
            <div style="height:1px; background:#cbd5e1; margin:6px 0;"></div>
            <div class="math-row">
              <input type="text" class="math-input" id="q15_d_t" data-answer="70" placeholder="40+30">
              <span>+</span>
              <input type="text" class="math-input" id="q15_d_u" data-answer="16" placeholder="8+8">
              <span>➜</span>
              <input type="text" class="math-input" id="q15_d_total" data-answer="86" placeholder="Tổng">
            </div>
          </div>
          <div class="feedback-tip" id="fb-q15_d">Đáp án: <b>70 + 16 = 86</b></div>
        </div>
      </div>
    </section>

    <!-- QUESTION 16 -->
    <section class="part-section" id="section-16">
      <div class="part-header">
        <div>
          <div class="part-title">
            <span class="part-badge">16</span>
            16- Answer these. (Mathematical Language)
          </div>
          <p class="part-vi">Đọc hiểu thuật ngữ toán tiếng Anh (add = cộng, total = tổng, sum = tổng).</p>
        </div>
        <button type="button" class="btn-audio" onclick="speak('Question sixteen: Answer these.')">🔊 Nghe đề bài</button>
      </div>

      <div class="math-grid-2">
        <div class="math-card">
          <div style="font-weight:700; font-size:1.1rem;">
            a-) 35 add 62 equals
            <button type="button" class="btn-audio" onclick="speak('35 add 62 equals')">🔊</button>
          </div>
          <div class="math-row">
            <span>➜</span>
            <input type="text" class="math-input" id="q16_a" data-answer="97" placeholder="?">
          </div>
          <div class="feedback-tip" id="fb-q16_a">Đáp án: <b>97</b> (35 + 62 = 97)</div>
        </div>

        <div class="math-card">
          <div style="font-weight:700; font-size:1.1rem;">
            b-) The total of 47 and 31 is
            <button type="button" class="btn-audio" onclick="speak('The total of 47 and 31 is')">🔊</button>
          </div>
          <div class="math-row">
            <span>➜</span>
            <input type="text" class="math-input" id="q16_b" data-answer="78" placeholder="?">
          </div>
          <div class="feedback-tip" id="fb-q16_b">Đáp án: <b>78</b> (47 + 31 = 78)</div>
        </div>

        <div class="math-card">
          <div style="font-weight:700; font-size:1.1rem;">
            c-) 26 added to 43 is
            <button type="button" class="btn-audio" onclick="speak('26 added to 43 is')">🔊</button>
          </div>
          <div class="math-row">
            <span>➜</span>
            <input type="text" class="math-input" id="q16_c" data-answer="69" placeholder="?">
          </div>
          <div class="feedback-tip" id="fb-q16_c">Đáp án: <b>69</b> (43 + 26 = 69)</div>
        </div>

        <div class="math-card">
          <div style="font-weight:700; font-size:1.1rem;">
            d-) The sum of 52 and 45 is
            <button type="button" class="btn-audio" onclick="speak('The sum of 52 and 45 is')">🔊</button>
          </div>
          <div class="math-row">
            <span>➜</span>
            <input type="text" class="math-input" id="q16_d" data-answer="97" placeholder="?">
          </div>
          <div class="feedback-tip" id="fb-q16_d">Đáp án: <b>97</b> (52 + 45 = 97)</div>
        </div>
      </div>
    </section>

    <!-- QUESTION 17 -->
    <section class="part-section" id="section-17">
      <div class="part-header">
        <div>
          <div class="part-title">
            <span class="part-badge">17</span>
            17- Answer these. (Column Addition)
          </div>
          <p class="part-vi">Đặt tính rồi tính theo cột dọc (cộng từ hàng đơn vị sang hàng chục).</p>
        </div>
        <button type="button" class="btn-audio" onclick="speak('Question seventeen: Answer these.')">🔊 Nghe đề bài</button>
      </div>

      <div class="math-grid-3">
        <!-- a-) 57 + 31 -->
        <div class="math-card" style="align-items:center;">
          <div style="font-weight:800; color:#0284c7; align-self:flex-start;">a-)</div>
          <div class="vertical-math">
            <div>&nbsp;&nbsp;57</div>
            <div>+ 31</div>
            <div class="vertical-line"></div>
            <input type="text" class="math-input" id="q17_a" data-answer="88" style="width:85px;">
          </div>
          <div class="feedback-tip" id="fb-q17_a">Đáp án: <b>88</b></div>
        </div>

        <!-- b-) 25 + 66 -->
        <div class="math-card" style="align-items:center;">
          <div style="font-weight:800; color:#0284c7; align-self:flex-start;">b-)</div>
          <div class="vertical-math">
            <div>&nbsp;&nbsp;25</div>
            <div>+ 66</div>
            <div class="vertical-line"></div>
            <input type="text" class="math-input" id="q17_b" data-answer="91" style="width:85px;">
          </div>
          <div class="feedback-tip" id="fb-q17_b">Đáp án: <b>91</b></div>
        </div>

        <!-- c-) 48 + 44 -->
        <div class="math-card" style="align-items:center;">
          <div style="font-weight:800; color:#0284c7; align-self:flex-start;">c-)</div>
          <div class="vertical-math">
            <div>&nbsp;&nbsp;48</div>
            <div>+ 44</div>
            <div class="vertical-line"></div>
            <input type="text" class="math-input" id="q17_c" data-answer="92" style="width:85px;">
          </div>
          <div class="feedback-tip" id="fb-q17_c">Đáp án: <b>92</b></div>
        </div>

        <!-- d-) 69 + 24 -->
        <div class="math-card" style="align-items:center;">
          <div style="font-weight:800; color:#0284c7; align-self:flex-start;">d-)</div>
          <div class="vertical-math">
            <div>&nbsp;&nbsp;69</div>
            <div>+ 24</div>
            <div class="vertical-line"></div>
            <input type="text" class="math-input" id="q17_d" data-answer="93" style="width:85px;">
          </div>
          <div class="feedback-tip" id="fb-q17_d">Đáp án: <b>93</b></div>
        </div>

        <!-- e-) 16 + 37 -->
        <div class="math-card" style="align-items:center;">
          <div style="font-weight:800; color:#0284c7; align-self:flex-start;">e-)</div>
          <div class="vertical-math">
            <div>&nbsp;&nbsp;16</div>
            <div>+ 37</div>
            <div class="vertical-line"></div>
            <input type="text" class="math-input" id="q17_e" data-answer="53" style="width:85px;">
          </div>
          <div class="feedback-tip" id="fb-q17_e">Đáp án: <b>53</b></div>
        </div>

        <!-- f-) 38 + 45 -->
        <div class="math-card" style="align-items:center;">
          <div style="font-weight:800; color:#0284c7; align-self:flex-start;">f-)</div>
          <div class="vertical-math">
            <div>&nbsp;&nbsp;38</div>
            <div>+ 45</div>
            <div class="vertical-line"></div>
            <input type="text" class="math-input" id="q17_f" data-answer="83" style="width:85px;">
          </div>
          <div class="feedback-tip" id="fb-q17_f">Đáp án: <b>83</b></div>
        </div>
      </div>
    </section>

    <!-- QUESTION 18 -->
    <section class="part-section" id="section-18">
      <div class="part-header">
        <div>
          <div class="part-title">
            <span class="part-badge">18</span>
            18- Complete these addition walls.
          </div>
          <p class="part-vi">Kim tự tháp số: Mỗi viên gạch phía trên bằng tổng của hai viên gạch ngay bên dưới nó.</p>
        </div>
        <button type="button" class="btn-audio" onclick="speak('Question eighteen: Complete these addition walls. Each number is the sum of the two numbers below it.')">🔊 Nghe đề bài</button>
      </div>

      <div class="math-grid-2">
        <!-- Wall a -->
        <div class="brick-wall">
          <div style="font-weight:800; color:#b45309; font-size:1.15rem; margin-bottom:8px;">Bức tường a-)</div>
          <div class="wall-row">
            <div class="wall-brick" style="background:#fef3c7;">
              <input type="text" id="q18_a_top" data-answer="95" placeholder="?">
            </div>
          </div>
          <div class="wall-row">
            <div class="wall-brick">
              <input type="text" id="q18_a_m1" data-answer="55" placeholder="?">
            </div>
            <div class="wall-brick">
              <input type="text" id="q18_a_m2" data-answer="40" placeholder="?">
            </div>
          </div>
          <div class="wall-row">
            <div class="wall-brick" style="background:#e2e8f0; color:#334155;">42</div>
            <div class="wall-brick" style="background:#e2e8f0; color:#334155;">13</div>
            <div class="wall-brick" style="background:#e2e8f0; color:#334155;">27</div>
          </div>
          <div class="feedback-tip" id="fb-q18_a" style="margin-top:10px;">
            Giải thích: 42 + 13 = <b>55</b>; 13 + 27 = <b>40</b>; 55 + 40 = <b>95</b>
          </div>
        </div>

        <!-- Wall b -->
        <div class="brick-wall">
          <div style="font-weight:800; color:#b45309; font-size:1.15rem; margin-bottom:8px;">Bức tường b-)</div>
          <div class="wall-row">
            <div class="wall-brick" style="background:#fef3c7;">
              <input type="text" id="q18_b_top" data-answer="91" placeholder="?">
            </div>
          </div>
          <div class="wall-row">
            <div class="wall-brick">
              <input type="text" id="q18_b_m1" data-answer="42" placeholder="?">
            </div>
            <div class="wall-brick">
              <input type="text" id="q18_b_m2" data-answer="49" placeholder="?">
            </div>
          </div>
          <div class="wall-row">
            <div class="wall-brick" style="background:#e2e8f0; color:#334155;">25</div>
            <div class="wall-brick" style="background:#e2e8f0; color:#334155;">17</div>
            <div class="wall-brick" style="background:#e2e8f0; color:#334155;">32</div>
          </div>
          <div class="feedback-tip" id="fb-q18_b" style="margin-top:10px;">
            Giải thích: 25 + 17 = <b>42</b>; 17 + 32 = <b>49</b>; 42 + 49 = <b>91</b>
          </div>
        </div>
      </div>
    </section>
"""

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
      
      <div class="modal-score" id="modalScoreDisplay">90 / 90</div>
      <p style="font-weight: 800; color: #10b981; font-size: 1.15rem;" id="modalMessage">Bé rất giỏi toán! Đã sẵn sàng cho kì thi giữa kì 1!</p>

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
    function speak(text) {
      if (!('speechSynthesis' in window)) return;
      window.speechSynthesis.cancel();
      const utterance = new SpeechSynthesisUtterance(text);
      utterance.lang = 'en-US';
      utterance.rate = 0.88;
      utterance.pitch = 1.05;
      window.speechSynthesis.speak(utterance);
    }

    let audioCtx = null;
    function getAudioContext() {
      if (!audioCtx) {
        audioCtx = new (window.AudioContext || window.webkitAudioContext)();
      }
      return audioCtx;
    }

    function playTone(freq, duration, type = 'sine', delay = 0) {
      try {
        const ctx = getAudioContext();
        if (ctx.state === 'suspended') ctx.resume();
        const osc = ctx.createOscillator();
        const gain = ctx.createGain();
        osc.type = type;
        osc.frequency.setValueAtTime(freq, ctx.currentTime + delay);
        gain.gain.setValueAtTime(0.15, ctx.currentTime + delay);
        gain.gain.exponentialRampToValueAtTime(0.001, ctx.currentTime + delay + duration);
        osc.connect(gain);
        gain.connect(ctx.destination);
        osc.start(ctx.currentTime + delay);
        osc.stop(ctx.currentTime + delay + duration);
      } catch (e) {}
    }

    function playCorrectChime() {
      playTone(523.25, 0.15, 'triangle', 0);
      playTone(659.25, 0.15, 'triangle', 0.1);
      playTone(783.99, 0.25, 'triangle', 0.2);
    }

    function playVictoryFanfare() {
      playTone(523.25, 0.12, 'triangle', 0);
      playTone(659.25, 0.12, 'triangle', 0.12);
      playTone(783.99, 0.12, 'triangle', 0.24);
      playTone(1046.50, 0.45, 'triangle', 0.36);
    }

    /* Abacus State */
    const abacusState = {
      q2_a: { tens: 0, units: 0, targetTens: 5, targetUnits: 7 },
      q2_b: { tens: 0, units: 0, targetTens: 8, targetUnits: 1 },
      q2_c: { tens: 0, units: 0, targetTens: 2, targetUnits: 7 },
      q2_d: { tens: 0, units: 0, targetTens: 3, targetUnits: 4 },
      q2_e: { tens: 0, units: 0, targetTens: 6, targetUnits: 3 },
      q2_f: { tens: 0, units: 0, targetTens: 1, targetUnits: 9 }
    };

    function renderAbacus(qId) {
      const state = abacusState[qId];
      const rodTens = document.getElementById(`rod-${qId}_tens`);
      const rodUnits = document.getElementById(`rod-${qId}_units`);
      const lblTens = document.getElementById(`lbl-${qId}_tens`);
      const lblUnits = document.getElementById(`lbl-${qId}_units`);

      if (rodTens && lblTens) {
        rodTens.innerHTML = '';
        for (let i = 0; i < state.tens; i++) {
          const b = document.createElement('div');
          b.className = 'bead tens';
          rodTens.appendChild(b);
        }
        lblTens.innerText = state.tens;
      }

      if (rodUnits && lblUnits) {
        rodUnits.innerHTML = '';
        for (let i = 0; i < state.units; i++) {
          const b = document.createElement('div');
          b.className = 'bead units';
          rodUnits.appendChild(b);
        }
        lblUnits.innerText = state.units;
      }
    }

    function addBead(qId, type) {
      if (abacusState[qId][type] < 9) {
        abacusState[qId][type]++;
        renderAbacus(qId);
        playTone(type === 'tens' ? 440 : 580, 0.06, 'sine');
        saveProgress();
      }
    }

    function stepBead(qId, type, delta) {
      const cur = abacusState[qId][type];
      const next = cur + delta;
      if (next >= 0 && next <= 9) {
        abacusState[qId][type] = next;
        renderAbacus(qId);
        playTone(delta > 0 ? 520 : 380, 0.06, 'sine');
        saveProgress();
      }
    }

    /* Digit Selector for Q6 */
    const digitSelections = {};
    function selectDigit(qId, btn) {
      const box = document.getElementById(`box-${qId}`);
      box.querySelectorAll('.digit-btn').forEach(b => b.classList.remove('selected'));
      btn.classList.add('selected');
      digitSelections[qId] = btn.dataset.val;
      playTone(460, 0.08, 'sine');
      saveProgress();
    }

    /* Grading */
    function gradeAll() {
      let score = 0;
      let total = 0;

      // Grade text inputs
      const inputs = document.querySelectorAll('input.math-input, .wall-brick input');
      inputs.forEach(inp => {
        if (!inp.dataset.answer) return;
        total++;
        const userVal = inp.value.trim().toLowerCase();
        const expected = inp.dataset.answer.split('|');
        const isOk = expected.some(exp => exp.trim().toLowerCase() === userVal);

        inp.classList.remove('correct', 'wrong');
        if (isOk) {
          score++;
          inp.classList.add('correct');
        } else {
          inp.classList.add('wrong');
        }
      });

      // Grade Abacus (6 questions x 2 rods = 12 points)
      for (let q in abacusState) {
        const s = abacusState[q];
        total += 2;
        const fb = document.getElementById(`fb-${q}`);
        let tensOk = s.tens === s.targetTens;
        let unitsOk = s.units === s.targetUnits;
        if (tensOk) score++;
        if (unitsOk) score++;

        if (fb) {
          if (tensOk && unitsOk) {
            fb.classList.remove('show-wrong');
          } else {
            fb.classList.add('show-wrong');
          }
        }
      }

      // Grade Q6 digits (4 items)
      ['q6_a', 'q6_b', 'q6_c', 'q6_d'].forEach(qId => {
        total++;
        const chosen = digitSelections[qId];
        const btn = document.querySelector(`.digit-btn[data-q="${qId}"][data-val="${chosen}"]`);
        const fb = document.getElementById(`fb-${qId}`);

        document.querySelectorAll(`.digit-btn[data-q="${qId}"]`).forEach(b => b.classList.remove('correct', 'wrong'));

        if (btn && btn.dataset.correct === 'true') {
          score++;
          btn.classList.add('correct');
          if (fb) fb.classList.remove('show-wrong');
        } else {
          if (btn) btn.classList.add('wrong');
          if (fb) fb.classList.add('show-wrong');
        }
      });

      // Update feedback tips for other questions
      for (let i = 1; i <= 18; i++) {
        const fb = document.getElementById(`fb-q${i}`);
        if (fb && !fb.classList.contains('show-wrong')) {
          // check if inputs inside section have any wrong
          const sec = document.getElementById(`section-${i}`);
          if (sec && sec.querySelector('.wrong')) {
            fb.classList.add('show-wrong');
          }
        }
      }

      document.getElementById('currentScore').innerText = score;
      document.getElementById('totalScore').innerText = total;

      if (score === total) {
        playVictoryFanfare();
        triggerConfetti();
      } else if (score >= total * 0.8) {
        playCorrectChime();
        triggerConfetti();
      } else {
        playTone(440, 0.2, 'triangle');
      }

      showScoreModal(score, total);
    }

    function showScoreModal(score, total) {
      const studentName = document.getElementById('studentName').value.trim();
      document.getElementById('modalStudentName').innerText = studentName ? `Học sinh: ${studentName}` : '';
      document.getElementById('modalScoreDisplay').innerText = `${score} / ${total} Điểm`;

      let trophy = '🏆';
      let title = 'Tuyệt vời!';
      let msg = 'Bé hoàn thành rất tốt đề ôn tập Toán!';

      const pct = (score / total) * 100;
      if (pct === 100) {
        trophy = '🌟';
        title = 'Xuất Sắc! Điểm Tuyệt Đối!';
        msg = 'Bé tính toán cực kì xuất sắc! Đạt 100% điểm số!';
      } else if (pct >= 85) {
        trophy = '🥇';
        title = 'Giỏi Quá!';
        msg = 'Bé làm đúng gần như toàn bộ đề bài! Rất đáng khen ngợi!';
      } else if (pct >= 65) {
        trophy = '🥈';
        title = 'Khá Tốt!';
        msg = 'Bé đã nắm vững nhiều dạng toán, xem lại các câu chưa đúng nhé!';
      } else {
        trophy = '💪';
        title = 'Cần Ôn Luyện Thêm!';
        msg = 'Bé hãy bấm nút Xem đáp án để học lại các bước tính nhé!';
      }

      document.getElementById('modalTrophy').innerText = trophy;
      document.getElementById('modalTitle').innerText = title;
      document.getElementById('modalMessage').innerText = msg;

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
        if (showingAnswers) {
          t.classList.add('show-correct');
        } else {
          t.classList.remove('show-correct', 'show-wrong');
        }
      });
      document.getElementById('toggleAnswersText').innerText = showingAnswers ? 'Ẩn đáp án' : 'Xem đáp án';
      playTone(550, 0.08, 'sine');
    }

    function resetAll() {
      if (confirm('Bé có muốn làm lại đề thi Toán từ đầu không?')) {
        document.querySelectorAll('input.math-input, .wall-brick input').forEach(inp => {
          inp.value = '';
          inp.classList.remove('correct', 'wrong');
        });

        for (let q in abacusState) {
          abacusState[q].tens = 0;
          abacusState[q].units = 0;
          renderAbacus(q);
        }

        for (let k in digitSelections) delete digitSelections[k];
        document.querySelectorAll('.digit-btn').forEach(b => b.classList.remove('selected', 'correct', 'wrong'));

        document.querySelectorAll('.feedback-tip').forEach(t => t.classList.remove('show-correct', 'show-wrong'));

        document.getElementById('currentScore').innerText = '0';
        showingAnswers = false;
        document.getElementById('toggleAnswersText').innerText = 'Xem đáp án';

        try { localStorage.removeItem('maths2_midterm1_answers'); } catch(e) {}

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
      const colors = ['#0ea5e9', '#3b82f6', '#10b981', '#f59e0b', '#ec4899', '#8b5cf6'];

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
        if (alive && frame < 200) {
          requestAnimationFrame(animate);
        } else {
          ctx.clearRect(0, 0, canvas.width, canvas.height);
        }
      }
      requestAnimationFrame(animate);
    }

    const STORAGE_KEY = 'maths2_midterm1_answers';
    function saveProgress() {
      const data = {
        name: document.getElementById('studentName').value,
        className: document.getElementById('studentClass').value,
        inputs: {},
        abacus: abacusState,
        digits: digitSelections
      };
      document.querySelectorAll('input.math-input, .wall-brick input').forEach(inp => {
        data.inputs[inp.id] = inp.value;
      });
      try {
        localStorage.setItem(STORAGE_KEY, JSON.stringify(data));
        // Also sync profile name across subjects
        localStorage.setItem('student_profile', JSON.stringify({ name: data.name, className: data.className }));
      } catch(e) {}
    }

    function loadProgress() {
      try {
        // load profile
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
        if (data.inputs) {
          for (let id in data.inputs) {
            const el = document.getElementById(id);
            if (el) el.value = data.inputs[id];
          }
        }
        if (data.abacus) {
          for (let q in data.abacus) {
            abacusState[q].tens = data.abacus[q].tens || 0;
            abacusState[q].units = data.abacus[q].units || 0;
            renderAbacus(q);
          }
        }
        if (data.digits) {
          for (let q in data.digits) {
            const val = data.digits[q];
            const btn = document.querySelector(`.digit-btn[data-q="${q}"][data-val="${val}"]`);
            if (btn) selectDigit(q, btn);
          }
        }
      } catch(e) {}
    }

    document.addEventListener('input', () => {
      saveProgress();
    });

    window.addEventListener('load', () => {
      // init abacus displays
      for (let q in abacusState) renderAbacus(q);
      loadProgress();
    });
  </script>
</body>
</html>
"""

full_maths_html = head_html + sections_html + footer_html

with open('maths.html', 'w', encoding='utf-8') as f:
    f.write(full_maths_html)

print(f"Generated maths.html successfully with {len(full_maths_html)} bytes.")
