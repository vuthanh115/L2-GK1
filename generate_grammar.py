# -*- coding: utf-8 -*-

html_content = """<!DOCTYPE html>
<html lang="vi">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Grammar 2 - Starters 2 - Review for Midterm Test 1 | Ôn Tập Ngữ Pháp Tiếng Anh Lớp 2</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Nunito:wght@400;600;700;800;900&display=swap" rel="stylesheet">
  <style>
    :root {
      --primary: #7c3aed;
      --primary-hover: #6d28d9;
      --primary-light: #f5f3ff;
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
      background: linear-gradient(135deg, #8b5cf6 0%, #7c3aed 50%, #4f46e5 100%);
      color: white;
      padding: 24px 16px 28px;
      border-radius: 0 0 28px 28px;
      box-shadow: 0 10px 25px -5px rgba(124, 58, 237, 0.35);
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
      color: #ede9fe;
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

    .example-box {
      background: #faf5ff;
      border: 1px solid #e9d5ff;
      border-left: 4px solid var(--primary);
      border-radius: 12px;
      padding: 12px 18px;
      margin-bottom: 20px;
      font-size: 1.05rem;
      font-weight: 700;
      color: #581c87;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 10px;
      flex-wrap: wrap;
    }

    .btn-audio {
      background: #f5f3ff;
      border: 1px solid #ddd6fe;
      color: #7c3aed;
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
      background: #ede9fe;
      transform: scale(1.05);
    }

    .btn-audio:active {
      transform: scale(0.96);
    }

    /* Questions List */
    .question-list {
      display: flex;
      flex-direction: column;
      gap: 16px;
    }

    .question-card {
      background: #ffffff;
      border: 2px solid #e2e8f0;
      border-radius: 14px;
      padding: 16px 20px;
      display: flex;
      flex-direction: column;
      gap: 8px;
      transition: all 0.2s;
    }

    .question-card:focus-within {
      border-color: var(--primary);
      box-shadow: 0 0 0 3px rgba(124, 58, 237, 0.12);
    }

    .sentence-row {
      display: flex;
      align-items: center;
      flex-wrap: wrap;
      gap: 8px;
      font-size: 1.15rem;
      font-weight: 700;
      color: #1e293b;
    }

    .q-num {
      font-weight: 800;
      color: #64748b;
      min-width: 24px;
    }

    .grammar-input {
      padding: 6px 12px;
      border: 2px solid #cbd5e1;
      border-radius: 10px;
      font-family: inherit;
      font-size: 1.1rem;
      font-weight: 800;
      color: var(--primary);
      text-align: center;
      outline: none;
      background: #f8fafc;
      transition: all 0.2s;
      min-width: 100px;
    }

    .grammar-input:focus {
      border-color: var(--primary);
      background: #ffffff;
      box-shadow: 0 0 0 3px rgba(124, 58, 237, 0.15);
    }

    .grammar-input.correct {
      border-color: var(--success) !important;
      background: #f0fdf4 !important;
      color: #15803d !important;
    }

    .grammar-input.wrong {
      border-color: var(--danger) !important;
      background: #fef2f2 !important;
      color: #b91c1c !important;
    }

    /* Quick choice pills */
    .quick-chips {
      display: flex;
      gap: 6px;
      margin-top: 4px;
      flex-wrap: wrap;
    }

    .chip-btn {
      background: #f1f5f9;
      border: 1px solid #cbd5e1;
      padding: 4px 10px;
      border-radius: 8px;
      font-weight: 800;
      font-size: 0.88rem;
      color: #475569;
      cursor: pointer;
      transition: all 0.15s;
    }

    .chip-btn:hover {
      background: var(--primary-light);
      color: var(--primary);
      border-color: var(--primary);
    }

    /* Radio choices for Part VI */
    .radio-group {
      display: flex;
      gap: 12px;
      margin-top: 8px;
      flex-wrap: wrap;
    }

    .radio-choice {
      flex: 1;
      min-width: 140px;
      border: 2px solid #cbd5e1;
      border-radius: 12px;
      padding: 10px 16px;
      display: flex;
      align-items: center;
      gap: 10px;
      cursor: pointer;
      font-size: 1.05rem;
      font-weight: 700;
      color: #334155;
      background: #ffffff;
      transition: all 0.2s;
      user-select: none;
    }

    .radio-choice:hover {
      border-color: var(--primary);
      background: var(--primary-light);
    }

    .radio-choice.selected {
      border-color: var(--primary);
      background: var(--primary-light);
      color: var(--primary-hover);
    }

    .radio-choice.correct {
      border-color: var(--success) !important;
      background: var(--success-light) !important;
      color: #065f46 !important;
    }

    .radio-choice.wrong {
      border-color: var(--danger) !important;
      background: var(--danger-light) !important;
      color: #991b1b !important;
    }

    .radio-circle {
      width: 18px;
      height: 18px;
      border-radius: 50%;
      border: 2px solid #94a3b8;
      display: flex;
      align-items: center;
      justify-content: center;
      flex-shrink: 0;
    }

    .radio-choice.selected .radio-circle {
      border-color: var(--primary);
      background: var(--primary);
      box-shadow: inset 0 0 0 3px #ffffff;
    }

    .feedback-tip {
      font-size: 0.9rem;
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
      background: linear-gradient(135deg, #8b5cf6 0%, #7c3aed 100%);
      color: white;
      box-shadow: 0 4px 12px rgba(124, 58, 237, 0.35);
    }

    .btn-primary:hover {
      transform: translateY(-2px);
      box-shadow: 0 6px 16px rgba(124, 58, 237, 0.45);
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
      .header-banner::before, .header-banner::after, .header-score-pill, .sticky-bar, .btn-audio, .chip-btn, .modal-backdrop, .feedback-tip, .nav-links { display: none !important; }
      .student-info-bar { background: none !important; border: 1px solid #000 !important; }
      .part-section { box-shadow: none !important; border: 1px solid #ccc !important; page-break-inside: avoid; margin-bottom: 20px; }
      .grammar-input { border-bottom: 1px solid #000 !important; border-top: none !important; border-left: none !important; border-right: none !important; border-radius: 0 !important; }
    }
  </style>
</head>
<body>

  <!-- Header Banner -->
  <header class="header-banner">
    <div class="header-container">
      <div class="nav-links">
        <a href="index.html" class="nav-btn">🏠 Về Trang Chủ</a>
        <a href="english.html" class="nav-btn">🇬🇧 Môn Tiếng Anh (English 2)</a>
        <a href="maths.html" class="nav-btn">🔢 Môn Toán (Maths 2)</a>
      </div>

      <div class="title-row">
        <div>
          <h1 class="main-title">
            <span>📖</span> GRAMMAR – STARTERS 2
          </h1>
          <p class="sub-title">Review for Midterm Test 1 - Đề Ôn Tập Ngữ Pháp Tiếng Anh Lớp 2</p>
        </div>
        <div class="header-score-pill" id="scoreIndicator">
          <span>⭐ Điểm:</span> <span id="currentScore">0</span> / <span id="totalScore">37</span>
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

    <!-- PART I: CAN / CAN'T -->
    <section class="part-section" id="section-1">
      <div class="part-header">
        <div>
          <div class="part-title">
            <span class="part-badge">PART I</span>
            I. Add can or can’t.
          </div>
          <p class="part-vi">Điền <b>can</b> hoặc <b>can’t</b> vào chỗ trống để hoàn thành câu hỏi và câu trả lời về khả năng.</p>
        </div>
        <button type="button" class="btn-audio" onclick="speak('Part one: Add can or can\'t.')">🔊 Nghe đề bài</button>
      </div>

      <div class="example-box">
        <span><b>Example:</b> <u>Can</u> your brother ride a bike? No, he <u>can’t</u>.</span>
        <button type="button" class="btn-audio" onclick="speak('Can your brother ride a bike? No, he can\'t.')">🔊 Nghe ví dụ</button>
      </div>

      <div class="question-list">
        <!-- 1 -->
        <div class="question-card">
          <div class="sentence-row">
            <span class="q-num">1.</span>
            <input type="text" class="grammar-input" id="q1_1_a" data-answer="can" placeholder="Can..." style="width:90px;">
            <span>George fly a kite? Yes, he</span>
            <input type="text" class="grammar-input" id="q1_1_b" data-answer="can" placeholder="can..." style="width:90px;">
            <span>.</span>
            <button type="button" class="btn-audio" onclick="speak('Can George fly a kite? Yes, he can.')">🔊</button>
          </div>
          <div class="quick-chips">
            <button type="button" class="chip-btn" onclick="fillInput('q1_1_a', 'Can')">Điền Can</button>
            <button type="button" class="chip-btn" onclick="fillInput('q1_1_b', 'can')">Điền can</button>
            <button type="button" class="chip-btn" onclick="fillInput('q1_1_b', 'can\'t')">Điền can't</button>
          </div>
          <div class="feedback-tip" id="fb-q1_1">Đáp án: <b>Can</b> George fly a kite? Yes, he <b>can</b>. (George có biết thả diều không? Có, cậu ấy biết.)</div>
        </div>

        <!-- 2 -->
        <div class="question-card">
          <div class="sentence-row">
            <span class="q-num">2.</span>
            <input type="text" class="grammar-input" id="q1_2_a" data-answer="can" placeholder="Can..." style="width:90px;">
            <span>dogs play the piano? No, they</span>
            <input type="text" class="grammar-input" id="q1_2_b" data-answer="can't|cant" placeholder="can't..." style="width:95px;">
            <span>.</span>
            <button type="button" class="btn-audio" onclick="speak('Can dogs play the piano? No, they can\'t.')">🔊</button>
          </div>
          <div class="quick-chips">
            <button type="button" class="chip-btn" onclick="fillInput('q1_2_a', 'Can')">Điền Can</button>
            <button type="button" class="chip-btn" onclick="fillInput('q1_2_b', 'can')">Điền can</button>
            <button type="button" class="chip-btn" onclick="fillInput('q1_2_b', 'can\'t')">Điền can't</button>
          </div>
          <div class="feedback-tip" id="fb-q1_2">Đáp án: <b>Can</b> dogs play the piano? No, they <b>can’t</b>. (Chó có biết chơi đàn piano không? Không, chúng không biết.)</div>
        </div>

        <!-- 3 -->
        <div class="question-card">
          <div class="sentence-row">
            <span class="q-num">3.</span>
            <input type="text" class="grammar-input" id="q1_3_a" data-answer="can" placeholder="Can..." style="width:90px;">
            <span>tigers run? Yes, they</span>
            <input type="text" class="grammar-input" id="q1_3_b" data-answer="can" placeholder="can..." style="width:90px;">
            <span>.</span>
            <button type="button" class="btn-audio" onclick="speak('Can tigers run? Yes, they can.')">🔊</button>
          </div>
          <div class="quick-chips">
            <button type="button" class="chip-btn" onclick="fillInput('q1_3_a', 'Can')">Điền Can</button>
            <button type="button" class="chip-btn" onclick="fillInput('q1_3_b', 'can')">Điền can</button>
            <button type="button" class="chip-btn" onclick="fillInput('q1_3_b', 'can\'t')">Điền can't</button>
          </div>
          <div class="feedback-tip" id="fb-q1_3">Đáp án: <b>Can</b> tigers run? Yes, they <b>can</b>. (Hổ có biết chạy không? Có, chúng có thể chạy.)</div>
        </div>

        <!-- 4 -->
        <div class="question-card">
          <div class="sentence-row">
            <span class="q-num">4.</span>
            <input type="text" class="grammar-input" id="q1_4_a" data-answer="can" placeholder="Can..." style="width:90px;">
            <span>the baby clean his room? No, he</span>
            <input type="text" class="grammar-input" id="q1_4_b" data-answer="can't|cant" placeholder="can't..." style="width:95px;">
            <span>.</span>
            <button type="button" class="btn-audio" onclick="speak('Can the baby clean his room? No, he can\'t.')">🔊</button>
          </div>
          <div class="quick-chips">
            <button type="button" class="chip-btn" onclick="fillInput('q1_4_a', 'Can')">Điền Can</button>
            <button type="button" class="chip-btn" onclick="fillInput('q1_4_b', 'can')">Điền can</button>
            <button type="button" class="chip-btn" onclick="fillInput('q1_4_b', 'can\'t')">Điền can't</button>
          </div>
          <div class="feedback-tip" id="fb-q1_4">Đáp án: <b>Can</b> the baby clean his room? No, he <b>can’t</b>. (Em bé có biết dọn phòng không? Không, bé chưa biết.)</div>
        </div>

        <!-- 5 -->
        <div class="question-card">
          <div class="sentence-row">
            <span class="q-num">5.</span>
            <input type="text" class="grammar-input" id="q1_5_a" data-answer="can" placeholder="Can..." style="width:90px;">
            <span>Louisa do her chores? Yes, she</span>
            <input type="text" class="grammar-input" id="q1_5_b" data-answer="can" placeholder="can..." style="width:90px;">
            <span>.</span>
            <button type="button" class="btn-audio" onclick="speak('Can Louisa do her chores? Yes, she can.')">🔊</button>
          </div>
          <div class="quick-chips">
            <button type="button" class="chip-btn" onclick="fillInput('q1_5_a', 'Can')">Điền Can</button>
            <button type="button" class="chip-btn" onclick="fillInput('q1_5_b', 'can')">Điền can</button>
            <button type="button" class="chip-btn" onclick="fillInput('q1_5_b', 'can\'t')">Điền can't</button>
          </div>
          <div class="feedback-tip" id="fb-q1_5">Đáp án: <b>Can</b> Louisa do her chores? Yes, she <b>can</b>. (Louisa có thể làm việc nhà không? Có, bạn ấy làm được.)</div>
        </div>
      </div>
    </section>

    <!-- PART II: SIMPLE PRESENT FORM OF VERB -->
    <section class="part-section" id="section-2">
      <div class="part-header">
        <div>
          <div class="part-title">
            <span class="part-badge">PART II</span>
            II. Complete the sentences using the simple present form of the verb in ().
          </div>
          <p class="part-vi">Chia động từ trong ngoặc ở thì Hiện tại đơn (Simple Present Tense).</p>
        </div>
        <button type="button" class="btn-audio" onclick="speak('Part two: Complete the sentences using the simple present form of the verb in parentheses.')">🔊 Nghe đề bài</button>
      </div>

      <div class="example-box">
        <span><b>Example:</b> He <u>buys</u> food at the grocery store. (buy)</span>
        <button type="button" class="btn-audio" onclick="speak('He buys food at the grocery store.')">🔊 Nghe ví dụ</button>
      </div>

      <div class="question-list">
        <!-- 1 -->
        <div class="question-card">
          <div class="sentence-row">
            <span class="q-num">1.</span>
            <span>He</span>
            <input type="text" class="grammar-input" id="q2_1" data-answer="learns" placeholder="learn..." style="width:120px;">
            <span>from his parents. (learn)</span>
            <button type="button" class="btn-audio" onclick="speak('He learns from his parents.')">🔊</button>
          </div>
          <div class="feedback-tip" id="fb-q2_1">Đáp án: <b>learns</b> (Chủ ngữ là He nên động từ learn thêm -s ➜ learns)</div>
        </div>

        <!-- 2 -->
        <div class="question-card">
          <div class="sentence-row">
            <span class="q-num">2.</span>
            <span>My sister does not</span>
            <input type="text" class="grammar-input" id="q2_2" data-answer="like" placeholder="like..." style="width:110px;">
            <span>dogs. (like)</span>
            <button type="button" class="btn-audio" onclick="speak('My sister does not like dogs.')">🔊</button>
          </div>
          <div class="feedback-tip" id="fb-q2_2">Đáp án: <b>like</b> (Sau trợ động từ 'does not', động từ giữ nguyên thể ➜ like)</div>
        </div>

        <!-- 3 -->
        <div class="question-card">
          <div class="sentence-row">
            <span class="q-num">3.</span>
            <span>She</span>
            <input type="text" class="grammar-input" id="q2_3" data-answer="washes" placeholder="wash..." style="width:120px;">
            <span>her clothes on Saturdays. (wash)</span>
            <button type="button" class="btn-audio" onclick="speak('She washes her clothes on Saturdays.')">🔊</button>
          </div>
          <div class="feedback-tip" id="fb-q2_3">Đáp án: <b>washes</b> (Chủ ngữ She, động từ kết thúc bằng -sh nên thêm -es ➜ washes)</div>
        </div>

        <!-- 4 -->
        <div class="question-card">
          <div class="sentence-row">
            <span class="q-num">4.</span>
            <span>The sun is nice. It</span>
            <input type="text" class="grammar-input" id="q2_4" data-answer="feels" placeholder="feel..." style="width:110px;">
            <span>warm. (feel)</span>
            <button type="button" class="btn-audio" onclick="speak('The sun is nice. It feels warm.')">🔊</button>
          </div>
          <div class="feedback-tip" id="fb-q2_4">Đáp án: <b>feels</b> (Chủ ngữ là It nên động từ feel thêm -s ➜ feels)</div>
        </div>

        <!-- 5 -->
        <div class="question-card">
          <div class="sentence-row">
            <span class="q-num">5.</span>
            <span>He</span>
            <input type="text" class="grammar-input" id="q2_5" data-answer="watches" placeholder="watch..." style="width:125px;">
            <span>TV with his brother in the evening. (watch)</span>
            <button type="button" class="btn-audio" onclick="speak('He watches TV with his brother in the evening.')">🔊</button>
          </div>
          <div class="feedback-tip" id="fb-q2_5">Đáp án: <b>watches</b> (Chủ ngữ He, động từ kết thúc bằng -ch nên thêm -es ➜ watches)</div>
        </div>
      </div>
    </section>

    <!-- PART III: DOES / DOESN'T -->
    <section class="part-section" id="section-3">
      <div class="part-header">
        <div>
          <div class="part-title">
            <span class="part-badge">PART III</span>
            III. Add does, doesn’t, or Does.
          </div>
          <p class="part-vi">Điền <b>Does</b> (đầu câu), <b>does</b> hoặc <b>doesn’t</b> vào chỗ trống.</p>
        </div>
        <button type="button" class="btn-audio" onclick="speak('Part three: Add does, doesn\'t, or Does.')">🔊 Nghe đề bài</button>
      </div>

      <div class="example-box">
        <span><b>Example:</b> <u>Does</u> he always do his chores? No, he <u>doesn’t</u>.</span>
        <button type="button" class="btn-audio" onclick="speak('Does he always do his chores? No, he doesn\'t.')">🔊 Nghe ví dụ</button>
      </div>

      <div class="question-list">
        <!-- 1 -->
        <div class="question-card">
          <div class="sentence-row">
            <span class="q-num">1.</span>
            <input type="text" class="grammar-input" id="q3_1_a" data-answer="does" placeholder="Does..." style="width:95px;">
            <span>Jack help Lucas hit the ball? No, he</span>
            <input type="text" class="grammar-input" id="q3_1_b" data-answer="doesn't|doesnt" placeholder="doesn't..." style="width:105px;">
            <span>.</span>
            <button type="button" class="btn-audio" onclick="speak('Does Jack help Lucas hit the ball? No, he doesn\'t.')">🔊</button>
          </div>
          <div class="quick-chips">
            <button type="button" class="chip-btn" onclick="fillInput('q3_1_a', 'Does')">Điền Does</button>
            <button type="button" class="chip-btn" onclick="fillInput('q3_1_b', 'does')">Điền does</button>
            <button type="button" class="chip-btn" onclick="fillInput('q3_1_b', 'doesn\'t')">Điền doesn't</button>
          </div>
          <div class="feedback-tip" id="fb-q3_1">Đáp án: <b>Does</b> Jack help Lucas hit the ball? No, he <b>doesn’t</b>.</div>
        </div>

        <!-- 2 -->
        <div class="question-card">
          <div class="sentence-row">
            <span class="q-num">2.</span>
            <input type="text" class="grammar-input" id="q3_2_a" data-answer="does" placeholder="Does..." style="width:95px;">
            <span>your brother like pizza? Yes, he</span>
            <input type="text" class="grammar-input" id="q3_2_b" data-answer="does" placeholder="does..." style="width:95px;">
            <span>.</span>
            <button type="button" class="btn-audio" onclick="speak('Does your brother like pizza? Yes, he does.')">🔊</button>
          </div>
          <div class="quick-chips">
            <button type="button" class="chip-btn" onclick="fillInput('q3_2_a', 'Does')">Điền Does</button>
            <button type="button" class="chip-btn" onclick="fillInput('q3_2_b', 'does')">Điền does</button>
            <button type="button" class="chip-btn" onclick="fillInput('q3_2_b', 'doesn\'t')">Điền doesn't</button>
          </div>
          <div class="feedback-tip" id="fb-q3_2">Đáp án: <b>Does</b> your brother like pizza? Yes, he <b>does</b>.</div>
        </div>

        <!-- 3 -->
        <div class="question-card">
          <div class="sentence-row">
            <span class="q-num">3.</span>
            <input type="text" class="grammar-input" id="q3_3_a" data-answer="does" placeholder="Does..." style="width:95px;">
            <span>your best friend play basketball? No, she</span>
            <input type="text" class="grammar-input" id="q3_3_b" data-answer="doesn't|doesnt" placeholder="doesn't..." style="width:105px;">
            <span>.</span>
            <button type="button" class="btn-audio" onclick="speak('Does your best friend play basketball? No, she doesn\'t.')">🔊</button>
          </div>
          <div class="quick-chips">
            <button type="button" class="chip-btn" onclick="fillInput('q3_3_a', 'Does')">Điền Does</button>
            <button type="button" class="chip-btn" onclick="fillInput('q3_3_b', 'does')">Điền does</button>
            <button type="button" class="chip-btn" onclick="fillInput('q3_3_b', 'doesn\'t')">Điền doesn't</button>
          </div>
          <div class="feedback-tip" id="fb-q3_3">Đáp án: <b>Does</b> your best friend play basketball? No, she <b>doesn’t</b>.</div>
        </div>
      </div>
    </section>

    <!-- PART IV: AM, IS, ARE -->
    <section class="part-section" id="section-4">
      <div class="part-header">
        <div>
          <div class="part-title">
            <span class="part-badge">PART IV</span>
            IV. Add am, is, or are.
          </div>
          <p class="part-vi">Điền động từ To Be thích hợp: <b>am</b>, <b>is</b>, hoặc <b>are</b>.</p>
        </div>
        <button type="button" class="btn-audio" onclick="speak('Part four: Add am, is, or are.')">🔊 Nghe đề bài</button>
      </div>

      <div class="example-box">
        <span><b>Example:</b> They <u>are</u> my parents.</span>
        <button type="button" class="btn-audio" onclick="speak('They are my parents.')">🔊 Nghe ví dụ</button>
      </div>

      <div class="question-list">
        <!-- 1 -->
        <div class="question-card">
          <div class="sentence-row">
            <span class="q-num">1.</span>
            <span>You</span>
            <input type="text" class="grammar-input" id="q4_1" data-answer="are" placeholder="am/is/are" style="width:110px;">
            <span>beautiful.</span>
            <button type="button" class="btn-audio" onclick="speak('You are beautiful.')">🔊</button>
          </div>
          <div class="quick-chips">
            <button type="button" class="chip-btn" onclick="fillInput('q4_1', 'am')">am</button>
            <button type="button" class="chip-btn" onclick="fillInput('q4_1', 'is')">is</button>
            <button type="button" class="chip-btn" onclick="fillInput('q4_1', 'are')">are</button>
          </div>
          <div class="feedback-tip" id="fb-q4_1">Đáp án: <b>are</b> (You are beautiful - Bạn thật xinh đẹp)</div>
        </div>

        <!-- 2 -->
        <div class="question-card">
          <div class="sentence-row">
            <span class="q-num">2.</span>
            <span>It</span>
            <input type="text" class="grammar-input" id="q4_2" data-answer="is" placeholder="am/is/are" style="width:110px;">
            <span>my new bag.</span>
            <button type="button" class="btn-audio" onclick="speak('It is my new bag.')">🔊</button>
          </div>
          <div class="quick-chips">
            <button type="button" class="chip-btn" onclick="fillInput('q4_2', 'am')">am</button>
            <button type="button" class="chip-btn" onclick="fillInput('q4_2', 'is')">is</button>
            <button type="button" class="chip-btn" onclick="fillInput('q4_2', 'are')">are</button>
          </div>
          <div class="feedback-tip" id="fb-q4_2">Đáp án: <b>is</b> (It is my new bag - Đó là chiếc cặp mới của tôi)</div>
        </div>

        <!-- 3 -->
        <div class="question-card">
          <div class="sentence-row">
            <span class="q-num">3.</span>
            <span>We</span>
            <input type="text" class="grammar-input" id="q4_3" data-answer="are" placeholder="am/is/are" style="width:110px;">
            <span>good friends.</span>
            <button type="button" class="btn-audio" onclick="speak('We are good friends.')">🔊</button>
          </div>
          <div class="quick-chips">
            <button type="button" class="chip-btn" onclick="fillInput('q4_3', 'am')">am</button>
            <button type="button" class="chip-btn" onclick="fillInput('q4_3', 'is')">is</button>
            <button type="button" class="chip-btn" onclick="fillInput('q4_3', 'are')">are</button>
          </div>
          <div class="feedback-tip" id="fb-q4_3">Đáp án: <b>are</b> (We are good friends - Chúng tôi là những người bạn tốt)</div>
        </div>

        <!-- 4 -->
        <div class="question-card">
          <div class="sentence-row">
            <span class="q-num">4.</span>
            <span>My teacher</span>
            <input type="text" class="grammar-input" id="q4_4" data-answer="is" placeholder="am/is/are" style="width:110px;">
            <span>nice.</span>
            <button type="button" class="btn-audio" onclick="speak('My teacher is nice.')">🔊</button>
          </div>
          <div class="quick-chips">
            <button type="button" class="chip-btn" onclick="fillInput('q4_4', 'am')">am</button>
            <button type="button" class="chip-btn" onclick="fillInput('q4_4', 'is')">is</button>
            <button type="button" class="chip-btn" onclick="fillInput('q4_4', 'are')">are</button>
          </div>
          <div class="feedback-tip" id="fb-q4_4">Đáp án: <b>is</b> (My teacher is nice - Giáo viên của tôi rất dễ mến)</div>
        </div>

        <!-- 5 -->
        <div class="question-card">
          <div class="sentence-row">
            <span class="q-num">5.</span>
            <span>She</span>
            <input type="text" class="grammar-input" id="q4_5" data-answer="is" placeholder="am/is/are" style="width:110px;">
            <span>my mother.</span>
            <button type="button" class="btn-audio" onclick="speak('She is my mother.')">🔊</button>
          </div>
          <div class="quick-chips">
            <button type="button" class="chip-btn" onclick="fillInput('q4_5', 'am')">am</button>
            <button type="button" class="chip-btn" onclick="fillInput('q4_5', 'is')">is</button>
            <button type="button" class="chip-btn" onclick="fillInput('q4_5', 'are')">are</button>
          </div>
          <div class="feedback-tip" id="fb-q4_5">Đáp án: <b>is</b> (She is my mother - Bà ấy là mẹ của tôi)</div>
        </div>

        <!-- 6 -->
        <div class="question-card">
          <div class="sentence-row">
            <span class="q-num">6.</span>
            <span>I</span>
            <input type="text" class="grammar-input" id="q4_6" data-answer="am" placeholder="am/is/are" style="width:110px;">
            <span>a student.</span>
            <button type="button" class="btn-audio" onclick="speak('I am a student.')">🔊</button>
          </div>
          <div class="quick-chips">
            <button type="button" class="chip-btn" onclick="fillInput('q4_6', 'am')">am</button>
            <button type="button" class="chip-btn" onclick="fillInput('q4_6', 'is')">is</button>
            <button type="button" class="chip-btn" onclick="fillInput('q4_6', 'are')">are</button>
          </div>
          <div class="feedback-tip" id="fb-q4_6">Đáp án: <b>am</b> (I am a student - Tôi là một học sinh)</div>
        </div>
      </div>
    </section>

    <!-- PART V: AM NOT, IS NOT, ARE NOT -->
    <section class="part-section" id="section-5">
      <div class="part-header">
        <div>
          <div class="part-title">
            <span class="part-badge">PART V</span>
            V. Add am not, is not, or are not to write the negative statements.
          </div>
          <p class="part-vi">Chuyển câu khẳng định thành câu phủ định bằng cách điền <b>am not</b>, <b>is not</b>, hoặc <b>are not</b>.</p>
        </div>
        <button type="button" class="btn-audio" onclick="speak('Part five: Add am not, is not, or are not to write the negative statements.')">🔊 Nghe đề bài</button>
      </div>

      <div class="example-box">
        <span><b>Example:</b> They are my parents. ➜ They <u>are not</u> my parents.</span>
        <button type="button" class="btn-audio" onclick="speak('They are my parents. They are not my parents.')">🔊 Nghe ví dụ</button>
      </div>

      <div class="question-list">
        <!-- 1 -->
        <div class="question-card">
          <div class="sentence-row">
            <span class="q-num">1.</span>
            <span>We are at home. ➜ We</span>
            <input type="text" class="grammar-input" id="q5_1" data-answer="are not|aren't" placeholder="..." style="width:140px;">
            <span>at home.</span>
            <button type="button" class="btn-audio" onclick="speak('We are at home. We are not at home.')">🔊</button>
          </div>
          <div class="quick-chips">
            <button type="button" class="chip-btn" onclick="fillInput('q5_1', 'am not')">am not</button>
            <button type="button" class="chip-btn" onclick="fillInput('q5_1', 'is not')">is not</button>
            <button type="button" class="chip-btn" onclick="fillInput('q5_1', 'are not')">are not</button>
          </div>
          <div class="feedback-tip" id="fb-q5_1">Đáp án: <b>are not</b> (Chúng tôi không ở nhà)</div>
        </div>

        <!-- 2 -->
        <div class="question-card">
          <div class="sentence-row">
            <span class="q-num">2.</span>
            <span>She is my sister. ➜ She</span>
            <input type="text" class="grammar-input" id="q5_2" data-answer="is not|isn't" placeholder="..." style="width:140px;">
            <span>my sister.</span>
            <button type="button" class="btn-audio" onclick="speak('She is my sister. She is not my sister.')">🔊</button>
          </div>
          <div class="quick-chips">
            <button type="button" class="chip-btn" onclick="fillInput('q5_2', 'am not')">am not</button>
            <button type="button" class="chip-btn" onclick="fillInput('q5_2', 'is not')">is not</button>
            <button type="button" class="chip-btn" onclick="fillInput('q5_2', 'are not')">are not</button>
          </div>
          <div class="feedback-tip" id="fb-q5_2">Đáp án: <b>is not</b> (Cô ấy không phải là chị/em gái tôi)</div>
        </div>

        <!-- 3 -->
        <div class="question-card">
          <div class="sentence-row">
            <span class="q-num">3.</span>
            <span>I am in bed. ➜ I</span>
            <input type="text" class="grammar-input" id="q5_3" data-answer="am not" placeholder="..." style="width:140px;">
            <span>in bed.</span>
            <button type="button" class="btn-audio" onclick="speak('I am in bed. I am not in bed.')">🔊</button>
          </div>
          <div class="quick-chips">
            <button type="button" class="chip-btn" onclick="fillInput('q5_3', 'am not')">am not</button>
            <button type="button" class="chip-btn" onclick="fillInput('q5_3', 'is not')">is not</button>
            <button type="button" class="chip-btn" onclick="fillInput('q5_3', 'are not')">are not</button>
          </div>
          <div class="feedback-tip" id="fb-q5_3">Đáp án: <b>am not</b> (Tôi không ở trên giường)</div>
        </div>
      </div>
    </section>

    <!-- PART VI: CIRCLE THE CORRECT ANSWERS -->
    <section class="part-section" id="section-6">
      <div class="part-header">
        <div>
          <div class="part-title">
            <span class="part-badge">PART VI</span>
            VI. Circle the correct answers.
          </div>
          <p class="part-vi">Chọn đáp án đúng nhất (a, b, hoặc c) cho mỗi câu bên dưới.</p>
        </div>
        <button type="button" class="btn-audio" onclick="speak('Part six: Circle the correct answers.')">🔊 Nghe đề bài</button>
      </div>

      <div class="example-box">
        <span><b>Example:</b> Can Ava dance well? Yes, she _________. ➜ <b>a. can</b></span>
        <button type="button" class="btn-audio" onclick="speak('Can Ava dance well? Yes, she can.')">🔊 Nghe ví dụ</button>
      </div>

      <div class="question-list">
        <!-- 1 -->
        <div class="question-card" id="card-q6_1">
          <div class="sentence-row">
            <span class="q-num">1.</span>
            <span>Can Anna swim? No, she _________.</span>
            <button type="button" class="btn-audio" onclick="speak('Can Anna swim? No, she can\'t.')">🔊</button>
          </div>
          <div class="radio-group">
            <div class="radio-choice" data-q="q6_1" data-val="a" data-correct="true" onclick="selectChoice('q6_1', 'a')">
              <div class="radio-circle"></div> <span>a. can't</span>
            </div>
            <div class="radio-choice" data-q="q6_1" data-val="b" data-correct="false" onclick="selectChoice('q6_1', 'b')">
              <div class="radio-circle"></div> <span>b. can</span>
            </div>
            <div class="radio-choice" data-q="q6_1" data-val="c" data-correct="false" onclick="selectChoice('q6_1', 'c')">
              <div class="radio-circle"></div> <span>c. isn't</span>
            </div>
          </div>
          <div class="feedback-tip" id="fb-q6_1">Đáp án đúng: <b>a. can’t</b> (Hỏi bằng Can và trả lời No ➜ No, she can't)</div>
        </div>

        <!-- 2 -->
        <div class="question-card" id="card-q6_2">
          <div class="sentence-row">
            <span class="q-num">2.</span>
            <span>The dogs _________ big.</span>
            <button type="button" class="btn-audio" onclick="speak('The dogs are big.')">🔊</button>
          </div>
          <div class="radio-group">
            <div class="radio-choice" data-q="q6_2" data-val="a" data-correct="false" onclick="selectChoice('q6_2', 'a')">
              <div class="radio-circle"></div> <span>a. am</span>
            </div>
            <div class="radio-choice" data-q="q6_2" data-val="b" data-correct="true" onclick="selectChoice('q6_2', 'b')">
              <div class="radio-circle"></div> <span>b. are</span>
            </div>
            <div class="radio-choice" data-q="q6_2" data-val="c" data-correct="false" onclick="selectChoice('q6_2', 'c')">
              <div class="radio-circle"></div> <span>c. is</span>
            </div>
          </div>
          <div class="feedback-tip" id="fb-q6_2">Đáp án đúng: <b>b. are</b> (Chủ ngữ số nhiều 'The dogs' đi với are)</div>
        </div>

        <!-- 3 -->
        <div class="question-card" id="card-q6_3">
          <div class="sentence-row">
            <span class="q-num">3.</span>
            <span>Your mother _________ at home.</span>
            <button type="button" class="btn-audio" onclick="speak('Your mother is not at home.')">🔊</button>
          </div>
          <div class="radio-group">
            <div class="radio-choice" data-q="q6_3" data-val="a" data-correct="false" onclick="selectChoice('q6_3', 'a')">
              <div class="radio-circle"></div> <span>a. am not</span>
            </div>
            <div class="radio-choice" data-q="q6_3" data-val="b" data-correct="false" onclick="selectChoice('q6_3', 'b')">
              <div class="radio-circle"></div> <span>b. are not</span>
            </div>
            <div class="radio-choice" data-q="q6_3" data-val="c" data-correct="true" onclick="selectChoice('q6_3', 'c')">
              <div class="radio-circle"></div> <span>c. is not</span>
            </div>
          </div>
          <div class="feedback-tip" id="fb-q6_3">Đáp án đúng: <b>c. is not</b> (Your mother là ngôi thứ 3 số ít ➜ is not)</div>
        </div>

        <!-- 4 -->
        <div class="question-card" id="card-q6_4">
          <div class="sentence-row">
            <span class="q-num">4.</span>
            <span>Does she swim at a gym? No, she _________.</span>
            <button type="button" class="btn-audio" onclick="speak('Does she swim at a gym? No, she doesn\'t.')">🔊</button>
          </div>
          <div class="radio-group">
            <div class="radio-choice" data-q="q6_4" data-val="a" data-correct="false" onclick="selectChoice('q6_4', 'a')">
              <div class="radio-circle"></div> <span>a. does</span>
            </div>
            <div class="radio-choice" data-q="q6_4" data-val="b" data-correct="false" onclick="selectChoice('q6_4', 'b')">
              <div class="radio-circle"></div> <span>b. isn't</span>
            </div>
            <div class="radio-choice" data-q="q6_4" data-val="c" data-correct="true" onclick="selectChoice('q6_4', 'c')">
              <div class="radio-circle"></div> <span>c. doesn't</span>
            </div>
          </div>
          <div class="feedback-tip" id="fb-q6_4">Đáp án đúng: <b>c. doesn’t</b> (Hỏi bằng Does và trả lời No ➜ No, she doesn't)</div>
        </div>

        <!-- 5 -->
        <div class="question-card" id="card-q6_5">
          <div class="sentence-row">
            <span class="q-num">5.</span>
            <span>Mr. Lin does not _________ science.</span>
            <button type="button" class="btn-audio" onclick="speak('Mr. Lin does not teach science.')">🔊</button>
          </div>
          <div class="radio-group">
            <div class="radio-choice" data-q="q6_5" data-val="a" data-correct="true" onclick="selectChoice('q6_5', 'a')">
              <div class="radio-circle"></div> <span>a. teach</span>
            </div>
            <div class="radio-choice" data-q="q6_5" data-val="b" data-correct="false" onclick="selectChoice('q6_5', 'b')">
              <div class="radio-circle"></div> <span>b. teaches</span>
            </div>
            <div class="radio-choice" data-q="q6_5" data-val="c" data-correct="false" onclick="selectChoice('q6_5', 'c')">
              <div class="radio-circle"></div> <span>c. teachs</span>
            </div>
          </div>
          <div class="feedback-tip" id="fb-q6_5">Đáp án đúng: <b>a. teach</b> (Sau 'does not' là động từ nguyên thể không chia)</div>
        </div>

        <!-- 6 -->
        <div class="question-card" id="card-q6_6">
          <div class="sentence-row">
            <span class="q-num">6.</span>
            <span>It _________ good to play outside.</span>
            <button type="button" class="btn-audio" onclick="speak('It feels good to play outside.')">🔊</button>
          </div>
          <div class="radio-group">
            <div class="radio-choice" data-q="q6_6" data-val="a" data-correct="false" onclick="selectChoice('q6_6', 'a')">
              <div class="radio-circle"></div> <span>a. feel</span>
            </div>
            <div class="radio-choice" data-q="q6_6" data-val="b" data-correct="true" onclick="selectChoice('q6_6', 'b')">
              <div class="radio-circle"></div> <span>b. feels</span>
            </div>
            <div class="radio-choice" data-q="q6_6" data-val="c" data-correct="false" onclick="selectChoice('q6_6', 'c')">
              <div class="radio-circle"></div> <span>c. feeles</span>
            </div>
          </div>
          <div class="feedback-tip" id="fb-q6_6">Đáp án đúng: <b>b. feels</b> (Chủ ngữ là It nên động từ feel thêm -s ➜ feels)</div>
        </div>

        <!-- 7 -->
        <div class="question-card" id="card-q6_7">
          <div class="sentence-row">
            <span class="q-num">7.</span>
            <span>_________ your father play soccer? Yes, he can.</span>
            <button type="button" class="btn-audio" onclick="speak('Can your father play soccer? Yes, he can.')">🔊</button>
          </div>
          <div class="radio-group">
            <div class="radio-choice" data-q="q6_7" data-val="a" data-correct="false" onclick="selectChoice('q6_7', 'a')">
              <div class="radio-circle"></div> <span>a. Does</span>
            </div>
            <div class="radio-choice" data-q="q6_7" data-val="b" data-correct="false" onclick="selectChoice('q6_7', 'b')">
              <div class="radio-circle"></div> <span>b. Is</span>
            </div>
            <div class="radio-choice" data-q="q6_7" data-val="c" data-correct="true" onclick="selectChoice('q6_7', 'c')">
              <div class="radio-circle"></div> <span>c. Can</span>
            </div>
          </div>
          <div class="feedback-tip" id="fb-q6_7">Đáp án đúng: <b>c. Can</b> (Câu trả lời là 'Yes, he can' nên câu hỏi bắt đầu bằng Can)</div>
        </div>
      </div>
    </section>

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
      
      <div class="modal-score" id="modalScoreDisplay">37 / 37</div>
      <p style="font-weight: 800; color: #10b981; font-size: 1.15rem;" id="modalMessage">Bé rất giỏi ngữ pháp tiếng Anh!</p>

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

    function fillInput(id, val) {
      const el = document.getElementById(id);
      if (el) {
        el.value = val;
        el.dispatchEvent(new Event('input'));
        playTone(480, 0.08, 'sine');
      }
    }

    const choiceAnswers = {};
    function selectChoice(qId, val) {
      choiceAnswers[qId] = val;
      const choices = document.querySelectorAll(`.radio-choice[data-q="${qId}"]`);
      choices.forEach(c => {
        if (c.dataset.val === val) {
          c.classList.add('selected');
        } else {
          c.classList.remove('selected');
        }
      });
      playTone(520, 0.08, 'sine');
      saveProgress();
    }

    function gradeAll() {
      let score = 0;
      let partScores = { p1: 0, p2: 0, p3: 0, p4: 0, p5: 0, p6: 0 };
      let partTotals = { p1: 10, p2: 5, p3: 6, p4: 6, p5: 3, p6: 7 };

      // Grade text inputs (Parts 1 to 5)
      for (let p = 1; p <= 5; p++) {
        const inputs = document.querySelectorAll(`input[id^="q${p}_"]`);
        inputs.forEach(inp => {
          const expected = inp.dataset.answer.split('|').map(s => s.trim().toLowerCase());
          const userVal = inp.value.trim().toLowerCase();
          const isOk = expected.includes(userVal);

          inp.classList.remove('correct', 'wrong');
          if (isOk) {
            score++;
            partScores[`p${p}`]++;
            inp.classList.add('correct');
          } else {
            inp.classList.add('wrong');
          }
        });
      }

      // Grade Part VI (Multiple choice 1 to 7)
      const correctMC = {
        q6_1: 'a',
        q6_2: 'b',
        q6_3: 'c',
        q6_4: 'c',
        q6_5: 'a',
        q6_6: 'b',
        q6_7: 'c'
      };

      for (let q in correctMC) {
        const userChoice = choiceAnswers[q];
        const rightChoice = correctMC[q];
        const cards = document.querySelectorAll(`.radio-choice[data-q="${q}"]`);
        cards.forEach(c => c.classList.remove('correct', 'wrong'));

        if (userChoice === rightChoice) {
          score++;
          partScores.p6++;
          const selected = document.querySelector(`.radio-choice[data-q="${q}"][data-val="${userChoice}"]`);
          if (selected) selected.classList.add('correct');
        } else {
          if (userChoice) {
            const selected = document.querySelector(`.radio-choice[data-q="${q}"][data-val="${userChoice}"]`);
            if (selected) selected.classList.add('wrong');
          }
        }
      }

      // Show feedback for any wrong questions
      document.querySelectorAll('.part-section').forEach(sec => {
        const wrongItems = sec.querySelectorAll('.wrong');
        wrongItems.forEach(w => {
          const card = w.closest('.question-card');
          if (card) {
            const tip = card.querySelector('.feedback-tip');
            if (tip) tip.classList.add('show-wrong');
          }
        });
      });

      document.getElementById('currentScore').innerText = score;

      const total = 37;
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
      let msg = 'Bé hoàn thành rất tốt đề ôn tập Ngữ Pháp!';

      const pct = (score / total) * 100;
      if (pct === 100) {
        trophy = '🌟';
        title = 'Xuất Sắc! Điểm Tuyệt Đối!';
        msg = 'Bé nắm vững 100% ngữ pháp tiếng Anh Lớp 2!';
      } else if (pct >= 85) {
        trophy = '🥇';
        title = 'Giỏi Quá!';
        msg = 'Bé làm đúng hầu hết các câu! Rất đáng khen ngợi!';
      } else if (pct >= 65) {
        trophy = '🥈';
        title = 'Khá Tốt!';
        msg = 'Bé hãy xem lại các câu chưa đúng để ôn tập thêm nhé!';
      } else {
        trophy = '💪';
        title = 'Cần Ôn Tập Thêm!';
        msg = 'Bé hãy bấm nút Xem đáp án để ghi nhớ các cấu trúc câu nhé!';
      }

      document.getElementById('modalTrophy').innerText = trophy;
      document.getElementById('modalTitle').innerText = title;
      document.getElementById('modalMessage').innerText = msg;

      const breakdownEl = document.getElementById('modalBreakdown');
      breakdownEl.innerHTML = `
        <div class="breakdown-row"><span>Part I (Add can / can't):</span> <b>${partScores.p1} / ${partTotals.p1}</b></div>
        <div class="breakdown-row"><span>Part II (Simple present form):</span> <b>${partScores.p2} / ${partTotals.p2}</b></div>
        <div class="breakdown-row"><span>Part III (Does / doesn't):</span> <b>${partScores.p3} / ${partTotals.p3}</b></div>
        <div class="breakdown-row"><span>Part IV (Add am, is, are):</span> <b>${partScores.p4} / ${partTotals.p4}</b></div>
        <div class="breakdown-row"><span>Part V (Negative am/is/are not):</span> <b>${partScores.p5} / ${partTotals.p5}</b></div>
        <div class="breakdown-row"><span>Part VI (Multiple choice):</span> <b>${partScores.p6} / ${partTotals.p6}</b></div>
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
      if (confirm('Bé có muốn làm lại đề thi Ngữ pháp từ đầu không?')) {
        document.querySelectorAll('input.grammar-input').forEach(inp => {
          inp.value = '';
          inp.classList.remove('correct', 'wrong');
        });

        for (let k in choiceAnswers) delete choiceAnswers[k];
        document.querySelectorAll('.radio-choice').forEach(c => c.classList.remove('selected', 'correct', 'wrong'));
        document.querySelectorAll('.feedback-tip').forEach(t => t.classList.remove('show-correct', 'show-wrong'));

        document.getElementById('currentScore').innerText = '0';
        showingAnswers = false;
        document.getElementById('toggleAnswersText').innerText = 'Xem đáp án';

        try { localStorage.removeItem('grammar2_midterm1_answers'); } catch(e) {}

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
      const colors = ['#8b5cf6', '#a855f7', '#3b82f6', '#10b981', '#f59e0b', '#ec4899'];

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

    window.addEventListener('resize', () => {
      const canvas = document.getElementById('confettiCanvas');
      if (canvas) {
        canvas.width = window.innerWidth;
        canvas.height = window.innerHeight;
      }
    });

    const STORAGE_KEY = 'grammar2_midterm1_answers';
    function saveProgress() {
      const data = {
        name: document.getElementById('studentName').value,
        className: document.getElementById('studentClass').value,
        inputs: {},
        choices: choiceAnswers
      };
      document.querySelectorAll('input.grammar-input').forEach(inp => {
        data.inputs[inp.id] = inp.value;
      });
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
        if (data.inputs) {
          for (let id in data.inputs) {
            const el = document.getElementById(id);
            if (el) el.value = data.inputs[id];
          }
        }
        if (data.choices) {
          for (let q in data.choices) {
            selectChoice(q, data.choices[q]);
          }
        }
      } catch(e) {}
    }

    document.addEventListener('input', () => {
      saveProgress();
    });

    window.addEventListener('load', () => {
      loadProgress();
    });
  </script>
</body>
</html>
"""

with open('grammar.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print(f"Generated grammar.html successfully with {len(html_content)} bytes.")
