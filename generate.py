# -*- coding: utf-8 -*-
import json
import os

with open('images_b64.json', 'r', encoding='utf-8') as f:
    images = json.load(f)

template_head = """<!DOCTYPE html>
<html lang="vi">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Review for Midterm Test 1 – English 2 | Đề Ôn Tập Giữa Kì 1 Tiếng Anh Lớp 2</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Nunito:wght@400;600;700;800;900&display=swap" rel="stylesheet">
  <style>
    :root {
      --primary: #4361ee;
      --primary-hover: #3a0ca3;
      --primary-light: #e0e7ff;
      --accent: #ff9f1c;
      --accent-light: #fff3cd;
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

    /* Header styling */
    .header-banner {
      background: linear-gradient(135deg, #6366f1 0%, #4361ee 50%, #3b82f6 100%);
      color: white;
      padding: 24px 16px 28px;
      border-radius: 0 0 28px 28px;
      box-shadow: 0 10px 25px -5px rgba(67, 97, 238, 0.35);
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
      color: #e0e7ff;
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
      background: #ffb703;
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

    .btn-audio {
      background: #eff6ff;
      border: 1px solid #bfdbfe;
      color: #2563eb;
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
      background: #dbeafe;
      transform: scale(1.05);
    }

    .btn-audio:active {
      transform: scale(0.96);
    }

    .word-bank {
      background: #f8fafc;
      border: 2px solid #e2e8f0;
      border-radius: 14px;
      padding: 14px 18px;
      margin-bottom: 22px;
      display: flex;
      flex-wrap: wrap;
      gap: 10px;
      align-items: center;
    }

    .word-bank-label {
      font-weight: 800;
      color: #475569;
      font-size: 0.9rem;
      text-transform: uppercase;
      letter-spacing: 0.5px;
      margin-right: 6px;
    }

    .word-chip {
      background: #ffffff;
      border: 2px solid #cbd5e1;
      padding: 7px 16px;
      border-radius: 30px;
      font-size: 1.05rem;
      font-weight: 800;
      color: #334155;
      cursor: pointer;
      box-shadow: 0 2px 4px rgba(0, 0, 0, 0.04);
      transition: all 0.2s;
      user-select: none;
      display: inline-flex;
      align-items: center;
      gap: 6px;
    }

    .word-chip:hover {
      border-color: var(--primary);
      color: var(--primary);
      transform: translateY(-2px);
      box-shadow: 0 4px 8px rgba(67, 97, 238, 0.15);
    }

    .word-chip.used {
      opacity: 0.45;
      background: #f1f5f9;
      text-decoration: line-through;
      border-color: #e2e8f0;
    }

    .pic-grid {
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 18px;
    }

    @media (max-width: 820px) {
      .pic-grid {
        grid-template-columns: repeat(2, 1fr);
      }
    }

    @media (max-width: 480px) {
      .pic-grid {
        grid-template-columns: 1fr;
      }
    }

    .pic-card {
      background: #ffffff;
      border: 2px solid #e2e8f0;
      border-radius: 16px;
      padding: 14px;
      display: flex;
      flex-direction: column;
      align-items: center;
      text-align: center;
      position: relative;
      transition: all 0.2s;
    }

    .pic-card:focus-within {
      border-color: var(--primary);
      box-shadow: 0 0 0 3px rgba(67, 97, 238, 0.15);
    }

    .pic-card-num {
      position: absolute;
      top: 10px;
      left: 10px;
      background: #e2e8f0;
      color: #475569;
      font-weight: 800;
      font-size: 0.85rem;
      width: 24px;
      height: 24px;
      border-radius: 50%;
      display: flex;
      align-items: center;
      justify-content: center;
    }

    .pic-img-wrap {
      width: 100%;
      height: 140px;
      display: flex;
      align-items: center;
      justify-content: center;
      margin-bottom: 12px;
      overflow: hidden;
      border-radius: 8px;
      background: #fafafa;
    }

    .pic-img-wrap img {
      max-width: 100%;
      max-height: 100%;
      object-fit: contain;
      cursor: zoom-in;
      transition: transform 0.2s;
    }

    .pic-img-wrap img:hover {
      transform: scale(1.05);
    }

    .input-slot {
      width: 100%;
      position: relative;
    }

    .text-input {
      width: 100%;
      padding: 10px 14px;
      border: 2px solid #cbd5e1;
      border-radius: 12px;
      font-family: inherit;
      font-size: 1.05rem;
      font-weight: 700;
      text-align: center;
      color: #1e293b;
      outline: none;
      transition: all 0.2s;
      background: #fff;
    }

    .text-input:focus {
      border-color: var(--primary);
      background: #f8faff;
      box-shadow: 0 0 0 3px rgba(67, 97, 238, 0.12);
    }

    .text-input.correct {
      border-color: var(--success) !important;
      background: #f0fdf4 !important;
      color: #15803d !important;
    }

    .text-input.wrong {
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

    /* Part II Unscramble */
    .unscramble-list {
      display: flex;
      flex-direction: column;
      gap: 16px;
    }

    .unscramble-item {
      background: #f8fafc;
      border: 1px solid #e2e8f0;
      border-radius: 14px;
      padding: 14px 18px;
      display: flex;
      flex-wrap: wrap;
      align-items: center;
      gap: 16px;
    }

    .unscramble-num {
      font-weight: 800;
      font-size: 1.15rem;
      color: #475569;
      min-width: 24px;
    }

    .letter-tiles {
      display: flex;
      flex-wrap: wrap;
      gap: 6px;
    }

    .tile-btn {
      background: #ffffff;
      border: 2px solid #cbd5e1;
      width: 38px;
      height: 40px;
      border-radius: 8px;
      font-size: 1.15rem;
      font-weight: 800;
      color: #1e293b;
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: center;
      box-shadow: 0 2px 0 #94a3b8;
      transition: all 0.15s;
      user-select: none;
    }

    .tile-btn:hover {
      border-color: var(--primary);
      color: var(--primary);
      transform: translateY(-2px);
      box-shadow: 0 4px 0 #94a3b8;
    }

    .tile-btn:active {
      transform: translateY(1px);
      box-shadow: 0 1px 0 #94a3b8;
    }

    .unscramble-input-wrap {
      flex: 1;
      min-width: 220px;
      display: flex;
      gap: 8px;
      align-items: center;
    }

    .unscramble-input-wrap input {
      flex: 1;
      padding: 9px 14px;
      border: 2px solid #cbd5e1;
      border-radius: 10px;
      font-family: inherit;
      font-size: 1.1rem;
      font-weight: 700;
      color: #1e293b;
      letter-spacing: 0.5px;
      outline: none;
    }

    .btn-clear-tile {
      background: #f1f5f9;
      border: 1px solid #cbd5e1;
      color: #64748b;
      border-radius: 8px;
      padding: 8px 12px;
      cursor: pointer;
      font-weight: 700;
      font-size: 0.9rem;
    }

    .btn-clear-tile:hover {
      background: #e2e8f0;
      color: #1e293b;
    }

    /* Part III Sentences */
    .sentence-list {
      display: flex;
      flex-direction: column;
      gap: 14px;
    }

    .sentence-item {
      background: #ffffff;
      border: 2px solid #e2e8f0;
      border-radius: 14px;
      padding: 16px 20px;
      display: flex;
      align-items: center;
      flex-wrap: wrap;
      gap: 10px;
      font-size: 1.15rem;
      font-weight: 700;
      color: #1e293b;
    }

    .sentence-item input {
      padding: 6px 12px;
      border: 2px solid #94a3b8;
      border-radius: 10px;
      font-family: inherit;
      font-size: 1.1rem;
      font-weight: 800;
      color: var(--primary);
      background: #f8fafc;
      outline: none;
      min-width: 120px;
      text-align: center;
    }

    .sentence-item input:focus {
      border-color: var(--primary);
      background: #ffffff;
    }

    .sentence-vi-hint {
      width: 100%;
      font-size: 0.92rem;
      font-weight: 500;
      color: var(--text-muted);
      margin-left: 28px;
      margin-top: -4px;
    }

    /* Part V completion */
    .fill-grid {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(210px, 1fr));
      gap: 18px;
    }

    .fill-card {
      background: #ffffff;
      border: 2px solid #e2e8f0;
      border-radius: 16px;
      padding: 16px;
      display: flex;
      flex-direction: column;
      align-items: center;
      position: relative;
    }

    .fill-img-wrap {
      width: 100%;
      height: 125px;
      display: flex;
      align-items: center;
      justify-content: center;
      margin-bottom: 12px;
      background: #fafafa;
      border-radius: 10px;
    }

    .fill-img-wrap img {
      max-height: 100%;
      max-width: 100%;
      object-fit: contain;
    }

    .fill-word-prompt {
      font-size: 1.4rem;
      font-weight: 900;
      letter-spacing: 1px;
      margin-bottom: 10px;
      color: #1e293b;
      display: flex;
      align-items: center;
      gap: 6px;
    }

    .letter-options {
      display: flex;
      gap: 6px;
      margin-top: 8px;
      flex-wrap: wrap;
      justify-content: center;
    }

    .letter-btn {
      background: #f1f5f9;
      border: 1px solid #cbd5e1;
      padding: 5px 12px;
      border-radius: 8px;
      font-weight: 800;
      font-size: 0.95rem;
      color: #334155;
      cursor: pointer;
      transition: all 0.15s;
    }

    .letter-btn:hover {
      background: var(--primary-light);
      color: var(--primary);
      border-color: var(--primary);
    }

    /* Part VI Reading Stories */
    .story-box {
      background: #fdfbf7;
      border: 2px solid #fde68a;
      border-radius: 16px;
      padding: 20px 24px;
      margin-bottom: 22px;
    }

    .story-text {
      font-size: 1.25rem;
      font-weight: 700;
      color: #78350f;
      line-height: 1.8;
      margin-bottom: 12px;
    }

    .story-controls {
      display: flex;
      align-items: center;
      gap: 12px;
      flex-wrap: wrap;
    }

    .question-block {
      background: #ffffff;
      border: 1px solid #e2e8f0;
      border-radius: 14px;
      padding: 16px 20px;
      margin-bottom: 14px;
    }

    .q-title {
      font-size: 1.15rem;
      font-weight: 800;
      color: #1e293b;
      margin-bottom: 12px;
      display: flex;
      align-items: center;
      gap: 8px;
    }

    .options-row {
      display: flex;
      flex-wrap: wrap;
      gap: 12px;
    }

    .radio-card {
      flex: 1;
      min-width: 220px;
      border: 2px solid #cbd5e1;
      border-radius: 12px;
      padding: 12px 18px;
      display: flex;
      align-items: center;
      gap: 12px;
      cursor: pointer;
      font-size: 1.05rem;
      font-weight: 700;
      color: #334155;
      transition: all 0.2s;
      background: #ffffff;
      user-select: none;
    }

    .radio-card:hover {
      border-color: var(--primary);
      background: #f8faff;
    }

    .radio-card.selected {
      border-color: var(--primary);
      background: var(--primary-light);
      color: var(--primary-hover);
    }

    .radio-card.correct {
      border-color: var(--success) !important;
      background: var(--success-light) !important;
      color: #065f46 !important;
    }

    .radio-card.wrong {
      border-color: var(--danger) !important;
      background: var(--danger-light) !important;
      color: #991b1b !important;
    }

    .radio-dot {
      width: 20px;
      height: 20px;
      border-radius: 50%;
      border: 2px solid #94a3b8;
      display: flex;
      align-items: center;
      justify-content: center;
      flex-shrink: 0;
    }

    .radio-card.selected .radio-dot {
      border-color: var(--primary);
      background: var(--primary);
      box-shadow: inset 0 0 0 4px #ffffff;
    }

    /* Part VII Look & Yes/No */
    .part7-layout {
      display: grid;
      grid-template-columns: 1fr 1.3fr;
      gap: 24px;
      align-items: start;
    }

    @media (max-width: 768px) {
      .part7-layout {
        grid-template-columns: 1fr;
      }
    }

    .p7-img-wrapper {
      background: #f8fafc;
      border: 2px solid #e2e8f0;
      border-radius: 16px;
      padding: 14px;
      text-align: center;
      position: sticky;
      top: 90px;
    }

    .p7-img-wrapper img {
      width: 100%;
      max-height: 480px;
      object-fit: contain;
      border-radius: 10px;
      cursor: zoom-in;
    }

    .yesno-list {
      display: flex;
      flex-direction: column;
      gap: 12px;
    }

    .yesno-item {
      background: #ffffff;
      border: 1px solid #e2e8f0;
      border-radius: 12px;
      padding: 14px 18px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 12px;
      flex-wrap: wrap;
    }

    .yesno-text {
      font-size: 1.08rem;
      font-weight: 700;
      color: #1e293b;
      flex: 1;
      min-width: 200px;
    }

    .yesno-buttons {
      display: flex;
      gap: 8px;
      align-items: center;
    }

    .btn-yn {
      padding: 8px 20px;
      border-radius: 20px;
      font-size: 1rem;
      font-weight: 800;
      border: 2px solid #cbd5e1;
      background: #ffffff;
      color: #475569;
      cursor: pointer;
      transition: all 0.15s;
    }

    .btn-yn:hover {
      border-color: var(--primary);
    }

    .btn-yn.active-yes {
      background: var(--success);
      color: #ffffff;
      border-color: var(--success);
    }

    .btn-yn.active-no {
      background: var(--danger);
      color: #ffffff;
      border-color: var(--danger);
    }

    /* Fixed Sticky Bottom Control Bar */
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
      background: linear-gradient(135deg, #4361ee 0%, #3a0ca3 100%);
      color: white;
      box-shadow: 0 4px 12px rgba(67, 97, 238, 0.35);
    }

    .btn-primary:hover {
      transform: translateY(-2px);
      box-shadow: 0 6px 16px rgba(67, 97, 238, 0.45);
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

    /* Modal dialog */
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
      padding: 4px 0;
      border-bottom: 1px dashed #e2e8f0;
    }

    .breakdown-row:last-child {
      border-bottom: none;
    }

    /* Print styles */
    @media print {
      body {
        background: #fff !important;
        color: #000 !important;
        padding-bottom: 0 !important;
      }
      .header-banner {
        background: none !important;
        color: #000 !important;
        box-shadow: none !important;
        padding: 0 0 16px 0 !important;
        border-radius: 0 !important;
        border-bottom: 2px solid #000;
      }
      .header-banner::before,
      .header-banner::after,
      .header-score-pill,
      .sticky-bar,
      .btn-audio,
      .tile-btn,
      .btn-clear-tile,
      .letter-options,
      .modal-backdrop,
      .feedback-tip {
        display: none !important;
      }
      .student-info-bar {
        background: none !important;
        border: 1px solid #000 !important;
        color: #000 !important;
      }
      .student-info-bar input {
        border-bottom: 1px solid #000 !important;
        border-top: none !important;
        border-left: none !important;
        border-right: none !important;
        background: none !important;
      }
      .part-section {
        box-shadow: none !important;
        border: 1px solid #ccc !important;
        page-break-inside: avoid;
        margin-bottom: 20px;
      }
      .text-input {
        border-bottom: 1px solid #000 !important;
        border-top: none !important;
        border-left: none !important;
        border-right: none !important;
        border-radius: 0 !important;
        background: none !important;
      }
    }
  </style>
</head>
<body>

  <!-- Header Banner -->
  <header class="header-banner">
    <div class="header-container">
      <div class="title-row">
        <div>
          <h1 class="main-title">
            <span>📝</span> Review for Midterm Test 1 – English 2
          </h1>
          <p class="sub-title">Đề Ôn Tập Thi Giữa Học Kì 1 - Môn Tiếng Anh Lớp 2</p>
        </div>
        <div class="header-score-pill" id="scoreIndicator">
          <span>⭐ Điểm:</span> <span id="currentScore">0</span> / <span id="totalScore">48</span>
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

part1_html = f"""
    <!-- PART I -->
    <section class="part-section" id="section-1">
      <div class="part-header">
        <div>
          <div class="part-title">
            <span class="part-badge">PART I</span>
            I. Look and label the pictures.
          </div>
          <p class="part-vi">Nhìn tranh và điền từ thích hợp từ ô từ vựng bên dưới.</p>
        </div>
        <button type="button" class="btn-audio" onclick="speak('Part one: Look and label the pictures.')">
          🔊 Nghe đề bài
        </button>
      </div>

      <div class="word-bank" id="wordbank-p1">
        <span class="word-bank-label">🔤 Word Bank:</span>
        <button type="button" class="word-chip" data-word="five" onclick="handleWordChipClick(this, 'p1')">five</button>
        <button type="button" class="word-chip" data-word="chores" onclick="handleWordChipClick(this, 'p1')">chores</button>
        <button type="button" class="word-chip" data-word="buy" onclick="handleWordChipClick(this, 'p1')">buy</button>
        <button type="button" class="word-chip" data-word="eat" onclick="handleWordChipClick(this, 'p1')">eat</button>
        <button type="button" class="word-chip" data-word="apartment" onclick="handleWordChipClick(this, 'p1')">apartment</button>
        <button type="button" class="word-chip" data-word="map" onclick="handleWordChipClick(this, 'p1')">map</button>
        <button type="button" class="word-chip" data-word="house" onclick="handleWordChipClick(this, 'p1')">house</button>
        <button type="button" class="word-chip" data-word="grown-up" onclick="handleWordChipClick(this, 'p1')">grown-up</button>
      </div>

      <div class="pic-grid">
        <!-- 1. chores -->
        <div class="pic-card" id="card-p1-1">
          <div class="pic-card-num">1</div>
          <div class="pic-img-wrap">
            <img src="{images['p1_chores.png']}" alt="Family doing chores" onclick="speak('chores')">
          </div>
          <div class="input-slot">
            <input type="text" class="text-input" id="p1_1" data-answer="chores" placeholder="Type word..." autocomplete="off">
            <div class="feedback-tip" id="fb-p1_1">Đáp án: <b>chores</b> (việc nhà)</div>
          </div>
        </div>

        <!-- 2. house -->
        <div class="pic-card" id="card-p1-2">
          <div class="pic-card-num">2</div>
          <div class="pic-img-wrap">
            <img src="{images['p1_house.png']}" alt="House" onclick="speak('house')">
          </div>
          <div class="input-slot">
            <input type="text" class="text-input" id="p1_2" data-answer="house" placeholder="Type word..." autocomplete="off">
            <div class="feedback-tip" id="fb-p1_2">Đáp án: <b>house</b> (ngôi nhà)</div>
          </div>
        </div>

        <!-- 3. map -->
        <div class="pic-card" id="card-p1-3">
          <div class="pic-card-num">3</div>
          <div class="pic-img-wrap">
            <img src="{images['p1_map.png']}" alt="Map" onclick="speak('map')">
          </div>
          <div class="input-slot">
            <input type="text" class="text-input" id="p1_3" data-answer="map" placeholder="Type word..." autocomplete="off">
            <div class="feedback-tip" id="fb-p1_3">Đáp án: <b>map</b> (bản đồ)</div>
          </div>
        </div>

        <!-- 4. eat -->
        <div class="pic-card" id="card-p1-4">
          <div class="pic-card-num">4</div>
          <div class="pic-img-wrap">
            <img src="{images['p1_eat.png']}" alt="Eat" onclick="speak('eat')">
          </div>
          <div class="input-slot">
            <input type="text" class="text-input" id="p1_4" data-answer="eat" placeholder="Type word..." autocomplete="off">
            <div class="feedback-tip" id="fb-p1_4">Đáp án: <b>eat</b> (ăn)</div>
          </div>
        </div>

        <!-- 5. buy -->
        <div class="pic-card" id="card-p1-5">
          <div class="pic-card-num">5</div>
          <div class="pic-img-wrap">
            <img src="{images['p1_buy.png']}" alt="Buy" onclick="speak('buy')">
          </div>
          <div class="input-slot">
            <input type="text" class="text-input" id="p1_5" data-answer="buy" placeholder="Type word..." autocomplete="off">
            <div class="feedback-tip" id="fb-p1_5">Đáp án: <b>buy</b> (mua hàng)</div>
          </div>
        </div>

        <!-- 6. apartment -->
        <div class="pic-card" id="card-p1-6">
          <div class="pic-card-num">6</div>
          <div class="pic-img-wrap">
            <img src="{images['p1_apartment.png']}" alt="Apartment" onclick="speak('apartment')">
          </div>
          <div class="input-slot">
            <input type="text" class="text-input" id="p1_6" data-answer="apartment" placeholder="Type word..." autocomplete="off">
            <div class="feedback-tip" id="fb-p1_6">Đáp án: <b>apartment</b> (căn hộ chung cư)</div>
          </div>
        </div>

        <!-- 7. five -->
        <div class="pic-card" id="card-p1-7">
          <div class="pic-card-num">7</div>
          <div class="pic-img-wrap">
            <img src="{images['p1_five.png']}" alt="Five" onclick="speak('five')">
          </div>
          <div class="input-slot">
            <input type="text" class="text-input" id="p1_7" data-answer="five" placeholder="Type word..." autocomplete="off">
            <div class="feedback-tip" id="fb-p1_7">Đáp án: <b>five</b> (số 5)</div>
          </div>
        </div>

        <!-- 8. grown-up -->
        <div class="pic-card" id="card-p1-8">
          <div class="pic-card-num">8</div>
          <div class="pic-img-wrap">
            <img src="{images['p1_grownup.png']}" alt="Grown-up" onclick="speak('grown-up')">
          </div>
          <div class="input-slot">
            <input type="text" class="text-input" id="p1_8" data-answer="grown-up" placeholder="Type word..." autocomplete="off">
            <div class="feedback-tip" id="fb-p1_8">Đáp án: <b>grown-up</b> (người lớn)</div>
          </div>
        </div>
      </div>
    </section>
"""

part2_html = """
    <!-- PART II -->
    <section class="part-section" id="section-2">
      <div class="part-header">
        <div>
          <div class="part-title">
            <span class="part-badge">PART II</span>
            II. Unscramble the words.
          </div>
          <p class="part-vi">Bé hãy bấm vào các chữ cái hoặc gõ từ để ghép thành từ tiếng Anh đúng.</p>
        </div>
        <button type="button" class="btn-audio" onclick="speak('Part two: Unscramble the words.')">
          🔊 Nghe đề bài
        </button>
      </div>

      <div class="unscramble-list">
        <!-- 1. townhouse -->
        <div class="unscramble-item">
          <span class="unscramble-num">1.</span>
          <div class="letter-tiles" id="tiles-p2_1">
            <button type="button" class="tile-btn" onclick="appendLetter('p2_1', 'w')">w</button>
            <button type="button" class="tile-btn" onclick="appendLetter('p2_1', 'n')">n</button>
            <button type="button" class="tile-btn" onclick="appendLetter('p2_1', 'o')">o</button>
            <button type="button" class="tile-btn" onclick="appendLetter('p2_1', 't')">t</button>
            <button type="button" class="tile-btn" onclick="appendLetter('p2_1', 'u')">u</button>
            <button type="button" class="tile-btn" onclick="appendLetter('p2_1', 'o')">o</button>
            <button type="button" class="tile-btn" onclick="appendLetter('p2_1', 's')">s</button>
            <button type="button" class="tile-btn" onclick="appendLetter('p2_1', 'h')">h</button>
            <button type="button" class="tile-btn" onclick="appendLetter('p2_1', 'e')">e</button>
          </div>
          <div class="unscramble-input-wrap">
            <input type="text" id="p2_1" data-answer="townhouse" placeholder="Từ hoàn chỉnh..." autocomplete="off">
            <button type="button" class="btn-clear-tile" onclick="popLetter('p2_1')">⌫ Xóa</button>
            <button type="button" class="btn-audio" onclick="speak(document.getElementById('p2_1').value || 'townhouse')">🔊</button>
          </div>
          <div class="feedback-tip" id="fb-p2_1" style="width:100%; margin-left:36px;">Đáp án: <b>townhouse</b> (nhà phố liên kế)</div>
        </div>

        <!-- 2. own / now -->
        <div class="unscramble-item">
          <span class="unscramble-num">2.</span>
          <div class="letter-tiles" id="tiles-p2_2">
            <button type="button" class="tile-btn" onclick="appendLetter('p2_2', 'n')">n</button>
            <button type="button" class="tile-btn" onclick="appendLetter('p2_2', 'o')">o</button>
            <button type="button" class="tile-btn" onclick="appendLetter('p2_2', 'w')">w</button>
          </div>
          <div class="unscramble-input-wrap">
            <input type="text" id="p2_2" data-answer="own|now" placeholder="Từ hoàn chỉnh..." autocomplete="off">
            <button type="button" class="btn-clear-tile" onclick="popLetter('p2_2')">⌫ Xóa</button>
            <button type="button" class="btn-audio" onclick="speak(document.getElementById('p2_2').value || 'own')">🔊</button>
          </div>
          <div class="feedback-tip" id="fb-p2_2" style="width:100%; margin-left:36px;">Đáp án: <b>own</b> (của riêng mình) hoặc <b>now</b> (bây giờ)</div>
        </div>

        <!-- 3. yellow -->
        <div class="unscramble-item">
          <span class="unscramble-num">3.</span>
          <div class="letter-tiles" id="tiles-p2_3">
            <button type="button" class="tile-btn" onclick="appendLetter('p2_3', 'w')">w</button>
            <button type="button" class="tile-btn" onclick="appendLetter('p2_3', 'l')">l</button>
            <button type="button" class="tile-btn" onclick="appendLetter('p2_3', 'l')">l</button>
            <button type="button" class="tile-btn" onclick="appendLetter('p2_3', 'o')">o</button>
            <button type="button" class="tile-btn" onclick="appendLetter('p2_3', 'y')">y</button>
            <button type="button" class="tile-btn" onclick="appendLetter('p2_3', 'e')">e</button>
          </div>
          <div class="unscramble-input-wrap">
            <input type="text" id="p2_3" data-answer="yellow" placeholder="Từ hoàn chỉnh..." autocomplete="off">
            <button type="button" class="btn-clear-tile" onclick="popLetter('p2_3')">⌫ Xóa</button>
            <button type="button" class="btn-audio" onclick="speak(document.getElementById('p2_3').value || 'yellow')">🔊</button>
          </div>
          <div class="feedback-tip" id="fb-p2_3" style="width:100%; margin-left:36px;">Đáp án: <b>yellow</b> (màu vàng)</div>
        </div>

        <!-- 4. five -->
        <div class="unscramble-item">
          <span class="unscramble-num">4.</span>
          <div class="letter-tiles" id="tiles-p2_4">
            <button type="button" class="tile-btn" onclick="appendLetter('p2_4', 'e')">e</button>
            <button type="button" class="tile-btn" onclick="appendLetter('p2_4', 'f')">f</button>
            <button type="button" class="tile-btn" onclick="appendLetter('p2_4', 'i')">i</button>
            <button type="button" class="tile-btn" onclick="appendLetter('p2_4', 'v')">v</button>
          </div>
          <div class="unscramble-input-wrap">
            <input type="text" id="p2_4" data-answer="five" placeholder="Từ hoàn chỉnh..." autocomplete="off">
            <button type="button" class="btn-clear-tile" onclick="popLetter('p2_4')">⌫ Xóa</button>
            <button type="button" class="btn-audio" onclick="speak(document.getElementById('p2_4').value || 'five')">🔊</button>
          </div>
          <div class="feedback-tip" id="fb-p2_4" style="width:100%; margin-left:36px;">Đáp án: <b>five</b> (số 5)</div>
        </div>

        <!-- 5. baby -->
        <div class="unscramble-item">
          <span class="unscramble-num">5.</span>
          <div class="letter-tiles" id="tiles-p2_5">
            <button type="button" class="tile-btn" onclick="appendLetter('p2_5', 'y')">y</button>
            <button type="button" class="tile-btn" onclick="appendLetter('p2_5', 'b')">b</button>
            <button type="button" class="tile-btn" onclick="appendLetter('p2_5', 'a')">a</button>
            <button type="button" class="tile-btn" onclick="appendLetter('p2_5', 'b')">b</button>
          </div>
          <div class="unscramble-input-wrap">
            <input type="text" id="p2_5" data-answer="baby" placeholder="Từ hoàn chỉnh..." autocomplete="off">
            <button type="button" class="btn-clear-tile" onclick="popLetter('p2_5')">⌫ Xóa</button>
            <button type="button" class="btn-audio" onclick="speak(document.getElementById('p2_5').value || 'baby')">🔊</button>
          </div>
          <div class="feedback-tip" id="fb-p2_5" style="width:100%; margin-left:36px;">Đáp án: <b>baby</b> (em bé)</div>
        </div>

        <!-- 6. year -->
        <div class="unscramble-item">
          <span class="unscramble-num">6.</span>
          <div class="letter-tiles" id="tiles-p2_6">
            <button type="button" class="tile-btn" onclick="appendLetter('p2_6', 'r')">r</button>
            <button type="button" class="tile-btn" onclick="appendLetter('p2_6', 'e')">e</button>
            <button type="button" class="tile-btn" onclick="appendLetter('p2_6', 'y')">y</button>
            <button type="button" class="tile-btn" onclick="appendLetter('p2_6', 'a')">a</button>
          </div>
          <div class="unscramble-input-wrap">
            <input type="text" id="p2_6" data-answer="year" placeholder="Từ hoàn chỉnh..." autocomplete="off">
            <button type="button" class="btn-clear-tile" onclick="popLetter('p2_6')">⌫ Xóa</button>
            <button type="button" class="btn-audio" onclick="speak(document.getElementById('p2_6').value || 'year')">🔊</button>
          </div>
          <div class="feedback-tip" id="fb-p2_6" style="width:100%; margin-left:36px;">Đáp án: <b>year</b> (năm / tuổi)</div>
        </div>

        <!-- 7. funny -->
        <div class="unscramble-item">
          <span class="unscramble-num">7.</span>
          <div class="letter-tiles" id="tiles-p2_7">
            <button type="button" class="tile-btn" onclick="appendLetter('p2_7', 'u')">u</button>
            <button type="button" class="tile-btn" onclick="appendLetter('p2_7', 'f')">f</button>
            <button type="button" class="tile-btn" onclick="appendLetter('p2_7', 'n')">n</button>
            <button type="button" class="tile-btn" onclick="appendLetter('p2_7', 'n')">n</button>
            <button type="button" class="tile-btn" onclick="appendLetter('p2_7', 'y')">y</button>
          </div>
          <div class="unscramble-input-wrap">
            <input type="text" id="p2_7" data-answer="funny" placeholder="Từ hoàn chỉnh..." autocomplete="off">
            <button type="button" class="btn-clear-tile" onclick="popLetter('p2_7')">⌫ Xóa</button>
            <button type="button" class="btn-audio" onclick="speak(document.getElementById('p2_7').value || 'funny')">🔊</button>
          </div>
          <div class="feedback-tip" id="fb-p2_7" style="width:100%; margin-left:36px;">Đáp án: <b>funny</b> (vui nhộn, buồn cười)</div>
        </div>
      </div>
    </section>
"""

part3_html = """
    <!-- PART III -->
    <section class="part-section" id="section-3">
      <div class="part-header">
        <div>
          <div class="part-title">
            <span class="part-badge">PART III</span>
            III. Write the word that completes each sentence.
          </div>
          <p class="part-vi">Chọn từ trong khung từ vựng điền vào chỗ trống để hoàn thành câu.</p>
        </div>
        <button type="button" class="btn-audio" onclick="speak('Part three: Write the word that completes each sentence.')">
          🔊 Nghe đề bài
        </button>
      </div>

      <div class="word-bank" id="wordbank-p3">
        <span class="word-bank-label">🔤 Word Bank:</span>
        <button type="button" class="word-chip" data-word="does" onclick="handleWordChipClick(this, 'p3')">does</button>
        <button type="button" class="word-chip" data-word="light" onclick="handleWordChipClick(this, 'p3')">light</button>
        <button type="button" class="word-chip" data-word="chore" onclick="handleWordChipClick(this, 'p3')">chore</button>
        <button type="button" class="word-chip" data-word="him" onclick="handleWordChipClick(this, 'p3')">him</button>
        <button type="button" class="word-chip" data-word="own" onclick="handleWordChipClick(this, 'p3')">own</button>
        <button type="button" class="word-chip" data-word="yellow" onclick="handleWordChipClick(this, 'p3')">yellow</button>
        <button type="button" class="word-chip" data-word="hold" onclick="handleWordChipClick(this, 'p3')">hold</button>
      </div>

      <div class="sentence-list">
        <!-- 1 -->
        <div class="sentence-item">
          <span>1. Look at</span>
          <input type="text" id="p3_1" data-answer="him" placeholder="..." style="width: 110px;" autocomplete="off">
          <span>! He can dance.</span>
          <button type="button" class="btn-audio" onclick="speak('Look at him! He can dance.')">🔊</button>
          <div class="sentence-vi-hint">Dịch nghĩa: Nhìn cậu ấy kìa! Cậu ấy có thể nhảy múa. (him)</div>
          <div class="feedback-tip" id="fb-p3_1" style="width: 100%; margin-left: 28px;">Đáp án: <b>him</b></div>
        </div>

        <!-- 2 -->
        <div class="sentence-item">
          <span>2. Do you have your</span>
          <input type="text" id="p3_2" data-answer="own" placeholder="..." style="width: 110px;" autocomplete="off">
          <span>computer?</span>
          <button type="button" class="btn-audio" onclick="speak('Do you have your own computer?')">🔊</button>
          <div class="sentence-vi-hint">Dịch nghĩa: Bạn có máy tính của riêng bạn không? (own)</div>
          <div class="feedback-tip" id="fb-p3_2" style="width: 100%; margin-left: 28px;">Đáp án: <b>own</b></div>
        </div>

        <!-- 3 -->
        <div class="sentence-item">
          <span>3. I clean the kitchen sink. It is my</span>
          <input type="text" id="p3_3" data-answer="chore" placeholder="..." style="width: 120px;" autocomplete="off">
          <span>.</span>
          <button type="button" class="btn-audio" onclick="speak('I clean the kitchen sink. It is my chore.')">🔊</button>
          <div class="sentence-vi-hint">Dịch nghĩa: Tôi lau rửa bồn rửa bát. Đó là việc nhà của tôi. (chore)</div>
          <div class="feedback-tip" id="fb-p3_3" style="width: 100%; margin-left: 28px;">Đáp án: <b>chore</b></div>
        </div>

        <!-- 4 -->
        <div class="sentence-item">
          <span>4. Sally</span>
          <input type="text" id="p3_4" data-answer="does" placeholder="..." style="width: 110px;" autocomplete="off">
          <span>not like sports.</span>
          <button type="button" class="btn-audio" onclick="speak('Sally does not like sports.')">🔊</button>
          <div class="sentence-vi-hint">Dịch nghĩa: Sally không thích thể thao. (does not like)</div>
          <div class="feedback-tip" id="fb-p3_4" style="width: 100%; margin-left: 28px;">Đáp án: <b>does</b></div>
        </div>

        <!-- 5 -->
        <div class="sentence-item">
          <span>5. Mel’s house is</span>
          <input type="text" id="p3_5" data-answer="yellow" placeholder="..." style="width: 130px;" autocomplete="off">
          <span>.</span>
          <button type="button" class="btn-audio" onclick="speak('Mel’s house is yellow.')">🔊</button>
          <div class="sentence-vi-hint">Dịch nghĩa: Ngôi nhà của Mel màu vàng. (yellow)</div>
          <div class="feedback-tip" id="fb-p3_5" style="width: 100%; margin-left: 28px;">Đáp án: <b>yellow</b></div>
        </div>

        <!-- 6 -->
        <div class="sentence-item">
          <span>6. A fish is</span>
          <input type="text" id="p3_6" data-answer="light" placeholder="..." style="width: 110px;" autocomplete="off">
          <span>.</span>
          <button type="button" class="btn-audio" onclick="speak('A fish is light.')">🔊</button>
          <div class="sentence-vi-hint">Dịch nghĩa: Một con cá thì nhẹ. (light)</div>
          <div class="feedback-tip" id="fb-p3_6" style="width: 100%; margin-left: 28px;">Đáp án: <b>light</b></div>
        </div>

        <!-- 7 -->
        <div class="sentence-item">
          <span>7. I can</span>
          <input type="text" id="p3_7" data-answer="hold" placeholder="..." style="width: 110px;" autocomplete="off">
          <span>my pencil.</span>
          <button type="button" class="btn-audio" onclick="speak('I can hold my pencil.')">🔊</button>
          <div class="sentence-vi-hint">Dịch nghĩa: Tôi có thể cầm chiếc bút chì của mình. (hold)</div>
          <div class="feedback-tip" id="fb-p3_7" style="width: 100%; margin-left: 28px;">Đáp án: <b>hold</b></div>
        </div>
      </div>
    </section>
"""

part4_html = f"""
    <!-- PART IV -->
    <section class="part-section" id="section-4">
      <div class="part-header">
        <div>
          <div class="part-title">
            <span class="part-badge">PART IV</span>
            IV. Look at the picture. Label the word correctly.
          </div>
          <p class="part-vi">Nhìn tranh và viết từ đúng vào ô tương ứng.</p>
        </div>
        <button type="button" class="btn-audio" onclick="speak('Part four: Look at the picture. Label the word correctly.')">
          🔊 Nghe đề bài
        </button>
      </div>

      <div class="word-bank" id="wordbank-p4">
        <span class="word-bank-label">🔤 Word Bank:</span>
        <button type="button" class="word-chip" data-word="ink" onclick="handleWordChipClick(this, 'p4')">ink</button>
        <button type="button" class="word-chip" data-word="bag" onclick="handleWordChipClick(this, 'p4')">bag</button>
        <button type="button" class="word-chip" data-word="shoes" onclick="handleWordChipClick(this, 'p4')">shoes</button>
        <button type="button" class="word-chip" data-word="dig" onclick="handleWordChipClick(this, 'p4')">dig</button>
        <button type="button" class="word-chip" data-word="sheep" onclick="handleWordChipClick(this, 'p4')">sheep</button>
        <button type="button" class="word-chip" data-word="ax" onclick="handleWordChipClick(this, 'p4')">ax</button>
      </div>

      <div class="pic-grid" style="grid-template-columns: repeat(3, 1fr);">
        <!-- 1. ax -->
        <div class="pic-card" id="card-p4-1">
          <div class="pic-card-num">1</div>
          <div class="pic-img-wrap">
            <img src="{images['p2_ax.png']}" alt="Ax" onclick="speak('ax')">
          </div>
          <div class="input-slot">
            <input type="text" class="text-input" id="p4_1" data-answer="ax" placeholder="Type word..." autocomplete="off">
            <div class="feedback-tip" id="fb-p4_1">Đáp án: <b>ax</b> (cái rìu)</div>
          </div>
        </div>

        <!-- 2. dig -->
        <div class="pic-card" id="card-p4-2">
          <div class="pic-card-num">2</div>
          <div class="pic-img-wrap">
            <img src="{images['p2_dig.png']}" alt="Dig" onclick="speak('dig')">
          </div>
          <div class="input-slot">
            <input type="text" class="text-input" id="p4_2" data-answer="dig" placeholder="Type word..." autocomplete="off">
            <div class="feedback-tip" id="fb-p4_2">Đáp án: <b>dig</b> (đào đất)</div>
          </div>
        </div>

        <!-- 3. shoes -->
        <div class="pic-card" id="card-p4-3">
          <div class="pic-card-num">3</div>
          <div class="pic-img-wrap">
            <img src="{images['p2_shoes.png']}" alt="Shoes" onclick="speak('shoes')">
          </div>
          <div class="input-slot">
            <input type="text" class="text-input" id="p4_3" data-answer="shoes" placeholder="Type word..." autocomplete="off">
            <div class="feedback-tip" id="fb-p4_3">Đáp án: <b>shoes</b> (đôi giày)</div>
          </div>
        </div>

        <!-- 4. bag -->
        <div class="pic-card" id="card-p4-4">
          <div class="pic-card-num">4</div>
          <div class="pic-img-wrap">
            <img src="{images['p2_bag.png']}" alt="Bag" onclick="speak('bag')">
          </div>
          <div class="input-slot">
            <input type="text" class="text-input" id="p4_4" data-answer="bag" placeholder="Type word..." autocomplete="off">
            <div class="feedback-tip" id="fb-p4_4">Đáp án: <b>bag</b> (ba lô / túi xách)</div>
          </div>
        </div>

        <!-- 5. ink -->
        <div class="pic-card" id="card-p4-5">
          <div class="pic-card-num">5</div>
          <div class="pic-img-wrap">
            <img src="{images['p2_ink.png']}" alt="Ink" onclick="speak('ink')">
          </div>
          <div class="input-slot">
            <input type="text" class="text-input" id="p4_5" data-answer="ink" placeholder="Type word..." autocomplete="off">
            <div class="feedback-tip" id="fb-p4_5">Đáp án: <b>ink</b> (lọ mực)</div>
          </div>
        </div>

        <!-- 6. sheep -->
        <div class="pic-card" id="card-p4-6">
          <div class="pic-card-num">6</div>
          <div class="pic-img-wrap">
            <img src="{images['p2_sheep.png']}" alt="Sheep" onclick="speak('sheep')">
          </div>
          <div class="input-slot">
            <input type="text" class="text-input" id="p4_6" data-answer="sheep" placeholder="Type word..." autocomplete="off">
            <div class="feedback-tip" id="fb-p4_6">Đáp án: <b>sheep</b> (con cừu)</div>
          </div>
        </div>
      </div>
    </section>
"""

part5_html = f"""
    <!-- PART V -->
    <section class="part-section" id="section-5">
      <div class="part-header">
        <div>
          <div class="part-title">
            <span class="part-badge">PART V</span>
            V. Look at the picture. Complete the word with a, i, o, wh or sh.
          </div>
          <p class="part-vi">Nhìn tranh và hoàn thành từ bằng cách điền chữ cái: a, i, o, wh hoặc sh.</p>
        </div>
        <button type="button" class="btn-audio" onclick="speak('Part five: Look at the picture. Complete the word with a, i, o, w h, or s h.')">
          🔊 Nghe đề bài
        </button>
      </div>

      <div class="fill-grid">
        <!-- 1. ant -->
        <div class="fill-card">
          <div class="pic-card-num">1</div>
          <div class="fill-img-wrap">
            <img src="{images['p3_ant.png']}" alt="Ant" onclick="speak('ant')">
          </div>
          <div class="fill-word-prompt">
            <input type="text" id="p5_1" data-answer="a" maxlength="2" style="width: 50px; text-align:center; font-weight:800; font-size:1.2rem; border:2px solid #cbd5e1; border-radius:8px; padding:4px;" autocomplete="off">
            <span>nt</span>
          </div>
          <div class="letter-options">
            <button type="button" class="letter-btn" onclick="fillPart5('p5_1', 'a')">a</button>
            <button type="button" class="letter-btn" onclick="fillPart5('p5_1', 'i')">i</button>
            <button type="button" class="letter-btn" onclick="fillPart5('p5_1', 'o')">o</button>
            <button type="button" class="letter-btn" onclick="fillPart5('p5_1', 'wh')">wh</button>
            <button type="button" class="letter-btn" onclick="fillPart5('p5_1', 'sh')">sh</button>
          </div>
          <div class="feedback-tip" id="fb-p5_1">Đáp án: <b>a</b>nt (con kiến)</div>
        </div>

        <!-- 2. ship -->
        <div class="fill-card">
          <div class="pic-card-num">2</div>
          <div class="fill-img-wrap">
            <img src="{images['p3_ship.png']}" alt="Ship" onclick="speak('ship')">
          </div>
          <div class="fill-word-prompt">
            <input type="text" id="p5_2" data-answer="sh" maxlength="2" style="width: 50px; text-align:center; font-weight:800; font-size:1.2rem; border:2px solid #cbd5e1; border-radius:8px; padding:4px;" autocomplete="off">
            <span>ip</span>
          </div>
          <div class="letter-options">
            <button type="button" class="letter-btn" onclick="fillPart5('p5_2', 'a')">a</button>
            <button type="button" class="letter-btn" onclick="fillPart5('p5_2', 'i')">i</button>
            <button type="button" class="letter-btn" onclick="fillPart5('p5_2', 'o')">o</button>
            <button type="button" class="letter-btn" onclick="fillPart5('p5_2', 'wh')">wh</button>
            <button type="button" class="letter-btn" onclick="fillPart5('p5_2', 'sh')">sh</button>
          </div>
          <div class="feedback-tip" id="fb-p5_2">Đáp án: <b>sh</b>ip (tàu thủy)</div>
        </div>

        <!-- 3. on -->
        <div class="fill-card">
          <div class="pic-card-num">3</div>
          <div class="fill-img-wrap">
            <img src="{images['p3_on.png']}" alt="Ball on table" onclick="speak('on')">
          </div>
          <div class="fill-word-prompt">
            <input type="text" id="p5_3" data-answer="o" maxlength="2" style="width: 50px; text-align:center; font-weight:800; font-size:1.2rem; border:2px solid #cbd5e1; border-radius:8px; padding:4px;" autocomplete="off">
            <span>n</span>
          </div>
          <div class="letter-options">
            <button type="button" class="letter-btn" onclick="fillPart5('p5_3', 'a')">a</button>
            <button type="button" class="letter-btn" onclick="fillPart5('p5_3', 'i')">i</button>
            <button type="button" class="letter-btn" onclick="fillPart5('p5_3', 'o')">o</button>
            <button type="button" class="letter-btn" onclick="fillPart5('p5_3', 'wh')">wh</button>
            <button type="button" class="letter-btn" onclick="fillPart5('p5_3', 'sh')">sh</button>
          </div>
          <div class="feedback-tip" id="fb-p5_3">Đáp án: <b>o</b>n (ở trên ghế/bàn)</div>
        </div>

        <!-- 4. pot -->
        <div class="fill-card">
          <div class="pic-card-num">4</div>
          <div class="fill-img-wrap">
            <img src="{images['p3_pot.png']}" alt="Pot" onclick="speak('pot')">
          </div>
          <div class="fill-word-prompt">
            <span>p</span>
            <input type="text" id="p5_4" data-answer="o" maxlength="2" style="width: 50px; text-align:center; font-weight:800; font-size:1.2rem; border:2px solid #cbd5e1; border-radius:8px; padding:4px;" autocomplete="off">
            <span>t</span>
          </div>
          <div class="letter-options">
            <button type="button" class="letter-btn" onclick="fillPart5('p5_4', 'a')">a</button>
            <button type="button" class="letter-btn" onclick="fillPart5('p5_4', 'i')">i</button>
            <button type="button" class="letter-btn" onclick="fillPart5('p5_4', 'o')">o</button>
            <button type="button" class="letter-btn" onclick="fillPart5('p5_4', 'wh')">wh</button>
            <button type="button" class="letter-btn" onclick="fillPart5('p5_4', 'sh')">sh</button>
          </div>
          <div class="feedback-tip" id="fb-p5_4">Đáp án: p<b>o</b>t (cái nồi)</div>
        </div>

        <!-- 5. cat -->
        <div class="fill-card">
          <div class="pic-card-num">5</div>
          <div class="fill-img-wrap">
            <img src="{images['p3_cat.png']}" alt="Cat" onclick="speak('cat')">
          </div>
          <div class="fill-word-prompt">
            <span>c</span>
            <input type="text" id="p5_5" data-answer="a" maxlength="2" style="width: 50px; text-align:center; font-weight:800; font-size:1.2rem; border:2px solid #cbd5e1; border-radius:8px; padding:4px;" autocomplete="off">
            <span>t</span>
          </div>
          <div class="letter-options">
            <button type="button" class="letter-btn" onclick="fillPart5('p5_5', 'a')">a</button>
            <button type="button" class="letter-btn" onclick="fillPart5('p5_5', 'i')">i</button>
            <button type="button" class="letter-btn" onclick="fillPart5('p5_5', 'o')">o</button>
            <button type="button" class="letter-btn" onclick="fillPart5('p5_5', 'wh')">wh</button>
            <button type="button" class="letter-btn" onclick="fillPart5('p5_5', 'sh')">sh</button>
          </div>
          <div class="feedback-tip" id="fb-p5_5">Đáp án: c<b>a</b>t (con mèo)</div>
        </div>

        <!-- 6. pig -->
        <div class="fill-card">
          <div class="pic-card-num">6</div>
          <div class="fill-img-wrap">
            <img src="{images['p3_pig.png']}" alt="Pig" onclick="speak('pig')">
          </div>
          <div class="fill-word-prompt">
            <span>p</span>
            <input type="text" id="p5_6" data-answer="i" maxlength="2" style="width: 50px; text-align:center; font-weight:800; font-size:1.2rem; border:2px solid #cbd5e1; border-radius:8px; padding:4px;" autocomplete="off">
            <span>g</span>
          </div>
          <div class="letter-options">
            <button type="button" class="letter-btn" onclick="fillPart5('p5_6', 'a')">a</button>
            <button type="button" class="letter-btn" onclick="fillPart5('p5_6', 'i')">i</button>
            <button type="button" class="letter-btn" onclick="fillPart5('p5_6', 'o')">o</button>
            <button type="button" class="letter-btn" onclick="fillPart5('p5_6', 'wh')">wh</button>
            <button type="button" class="letter-btn" onclick="fillPart5('p5_6', 'sh')">sh</button>
          </div>
          <div class="feedback-tip" id="fb-p5_6">Đáp án: p<b>i</b>g (con lợn)</div>
        </div>

        <!-- 7. whip / whisk -->
        <div class="fill-card">
          <div class="pic-card-num">7</div>
          <div class="fill-img-wrap">
            <img src="{images['p3_whip.png']}" alt="Whisk / whip" onclick="speak('whip')">
          </div>
          <div class="fill-word-prompt">
            <span>wh</span>
            <input type="text" id="p5_7" data-answer="ip|i|wh|isk" maxlength="4" style="width: 60px; text-align:center; font-weight:800; font-size:1.2rem; border:2px solid #cbd5e1; border-radius:8px; padding:4px;" autocomplete="off">
          </div>
          <div class="letter-options">
            <button type="button" class="letter-btn" onclick="fillPart5('p5_7', 'ip')">ip (whip)</button>
            <button type="button" class="letter-btn" onclick="fillPart5('p5_7', 'i')">i</button>
            <button type="button" class="letter-btn" onclick="fillPart5('p5_7', 'wh')">wh</button>
            <button type="button" class="letter-btn" onclick="fillPart5('p5_7', 'isk')">isk</button>
          </div>
          <div class="feedback-tip" id="fb-p5_7">Đáp án: wh<b>ip</b> hoặc wh<b>isk</b> (đánh trứng/kem)</div>
        </div>

        <!-- 8. box -->
        <div class="fill-card">
          <div class="pic-card-num">8</div>
          <div class="fill-img-wrap">
            <img src="{images['p3_box.png']}" alt="Box" onclick="speak('box')">
          </div>
          <div class="fill-word-prompt">
            <span>b</span>
            <input type="text" id="p5_8" data-answer="o" maxlength="2" style="width: 50px; text-align:center; font-weight:800; font-size:1.2rem; border:2px solid #cbd5e1; border-radius:8px; padding:4px;" autocomplete="off">
            <span>x</span>
          </div>
          <div class="letter-options">
            <button type="button" class="letter-btn" onclick="fillPart5('p5_8', 'a')">a</button>
            <button type="button" class="letter-btn" onclick="fillPart5('p5_8', 'i')">i</button>
            <button type="button" class="letter-btn" onclick="fillPart5('p5_8', 'o')">o</button>
            <button type="button" class="letter-btn" onclick="fillPart5('p5_8', 'wh')">wh</button>
            <button type="button" class="letter-btn" onclick="fillPart5('p5_8', 'sh')">sh</button>
          </div>
          <div class="feedback-tip" id="fb-p5_8">Đáp án: b<b>o</b>x (cái hộp)</div>
        </div>
      </div>
    </section>
"""

part6_html = """
    <!-- PART VI -->
    <section class="part-section" id="section-6">
      <div class="part-header">
        <div>
          <div class="part-title">
            <span class="part-badge">PART VI</span>
            VI. Read these stories. Then circle the correct answer.
          </div>
          <p class="part-vi">Đọc hai mẩu chuyện ngắn và chọn đáp án đúng nhất.</p>
        </div>
        <button type="button" class="btn-audio" onclick="speak('Part six: Read these stories. Then circle the correct answer.')">
          🔊 Nghe đề bài
        </button>
      </div>

      <!-- Story 1 -->
      <div class="story-box">
        <div class="story-text">
          “Gramps has a bag of soap. Dan can wash a sock. Dan and Gramps can wash and clean.”
        </div>
        <div class="story-controls">
          <button type="button" class="btn-audio" onclick="speak('Gramps has a bag of soap. Dan can wash a sock. Dan and Gramps can wash and clean.')">
            🔊 Nghe đọc truyện (Gramps & Dan)
          </button>
          <span style="font-size:0.92rem; color:#854d0e; font-weight:600;">(Dịch: Ông Gramps có một túi xà phòng. Dan có thể giặt một chiếc tất. Dan và ông có thể giặt và dọn dẹp sạch sẽ.)</span>
        </div>
      </div>

      <!-- Q 1.1 -->
      <div class="question-block" id="block-p6_1">
        <div class="q-title">
          <span>1. What does Gramps have?</span>
          <button type="button" class="btn-audio" onclick="speak('What does Gramps have?')">🔊</button>
        </div>
        <div class="options-row">
          <div class="radio-card" data-q="p6_1" data-val="a" data-correct="true" onclick="selectRadio('p6_1', 'a')">
            <div class="radio-dot"></div>
            <span>a. a bag of soap</span>
          </div>
          <div class="radio-card" data-q="p6_1" data-val="b" data-correct="false" onclick="selectRadio('p6_1', 'b')">
            <div class="radio-dot"></div>
            <span>b. a sock</span>
          </div>
        </div>
        <div class="feedback-tip" id="fb-p6_1">Đáp án đúng: <b>a. a bag of soap</b> (Gramps has a bag of soap)</div>
      </div>

      <!-- Q 1.2 -->
      <div class="question-block" id="block-p6_2">
        <div class="q-title">
          <span>2. What can Dan do?</span>
          <button type="button" class="btn-audio" onclick="speak('What can Dan do?')">🔊</button>
        </div>
        <div class="options-row">
          <div class="radio-card" data-q="p6_2" data-val="a" data-correct="true" onclick="selectRadio('p6_2', 'a')">
            <div class="radio-dot"></div>
            <span>a. wash a sock</span>
          </div>
          <div class="radio-card" data-q="p6_2" data-val="b" data-correct="false" onclick="selectRadio('p6_2', 'b')">
            <div class="radio-dot"></div>
            <span>b. wash a shirt</span>
          </div>
        </div>
        <div class="feedback-tip" id="fb-p6_2">Đáp án đúng: <b>a. wash a sock</b> (Dan can wash a sock)</div>
      </div>

      <!-- Q 1.3 -->
      <div class="question-block" id="block-p6_3">
        <div class="q-title">
          <span>3. What can Dan and Gramps do?</span>
          <button type="button" class="btn-audio" onclick="speak('What can Dan and Gramps do?')">🔊</button>
        </div>
        <div class="options-row">
          <div class="radio-card" data-q="p6_3" data-val="a" data-correct="false" onclick="selectRadio('p6_3', 'a')">
            <div class="radio-dot"></div>
            <span>a. sit and wait</span>
          </div>
          <div class="radio-card" data-q="p6_3" data-val="b" data-correct="true" onclick="selectRadio('p6_3', 'b')">
            <div class="radio-dot"></div>
            <span>b. wash and clean</span>
          </div>
        </div>
        <div class="feedback-tip" id="fb-p6_3">Đáp án đúng: <b>b. wash and clean</b> (Dan and Gramps can wash and clean)</div>
      </div>

      <!-- Story 2 -->
      <div class="story-box" style="margin-top: 28px;">
        <div class="story-text">
          “Mom and Dad live in a house. Five people can fit in the house. It has a den and a desk. The house is red and yellow.”
        </div>
        <div class="story-controls">
          <button type="button" class="btn-audio" onclick="speak('Mom and Dad live in a house. Five people can fit in the house. It has a den and a desk. The house is red and yellow.')">
            🔊 Nghe đọc truyện (Mom and Dad)
          </button>
          <span style="font-size:0.92rem; color:#854d0e; font-weight:600;">(Dịch: Bố và Mẹ sống trong một ngôi nhà. Có 5 người có thể ở vừa. Nhà có phòng làm việc và bàn làm việc. Ngôi nhà màu đỏ và vàng.)</span>
        </div>
      </div>

      <!-- Q 2.1 -->
      <div class="question-block" id="block-p6_4">
        <div class="q-title">
          <span>1. Where do Mom and Dad live?</span>
          <button type="button" class="btn-audio" onclick="speak('Where do Mom and Dad live?')">🔊</button>
        </div>
        <div class="options-row">
          <div class="radio-card" data-q="p6_4" data-val="a" data-correct="false" onclick="selectRadio('p6_4', 'a')">
            <div class="radio-dot"></div>
            <span>a. in an apartment</span>
          </div>
          <div class="radio-card" data-q="p6_4" data-val="b" data-correct="true" onclick="selectRadio('p6_4', 'b')">
            <div class="radio-dot"></div>
            <span>b. in a house</span>
          </div>
        </div>
        <div class="feedback-tip" id="fb-p6_4">Đáp án đúng: <b>b. in a house</b> (Mom and Dad live in a house)</div>
      </div>

      <!-- Q 2.2 -->
      <div class="question-block" id="block-p6_5">
        <div class="q-title">
          <span>2. How many people can fit in the house?</span>
          <button type="button" class="btn-audio" onclick="speak('How many people can fit in the house?')">🔊</button>
        </div>
        <div class="options-row">
          <div class="radio-card" data-q="p6_5" data-val="a" data-correct="true" onclick="selectRadio('p6_5', 'a')">
            <div class="radio-dot"></div>
            <span>a. five people</span>
          </div>
          <div class="radio-card" data-q="p6_5" data-val="b" data-correct="false" onclick="selectRadio('p6_5', 'b')">
            <div class="radio-dot"></div>
            <span>b. four people</span>
          </div>
        </div>
        <div class="feedback-tip" id="fb-p6_5">Đáp án đúng: <b>a. five people</b> (Five people can fit in the house)</div>
      </div>

      <!-- Q 2.3 -->
      <div class="question-block" id="block-p6_6">
        <div class="q-title">
          <span>3. What color is the house?</span>
          <button type="button" class="btn-audio" onclick="speak('What color is the house?')">🔊</button>
        </div>
        <div class="options-row">
          <div class="radio-card" data-q="p6_6" data-val="a" data-correct="true" onclick="selectRadio('p6_6', 'a')">
            <div class="radio-dot"></div>
            <span>a. red and yellow</span>
          </div>
          <div class="radio-card" data-q="p6_6" data-val="b" data-correct="false" onclick="selectRadio('p6_6', 'b')">
            <div class="radio-dot"></div>
            <span>b. red and black</span>
          </div>
        </div>
        <div class="feedback-tip" id="fb-p6_6">Đáp án đúng: <b>a. red and yellow</b> (The house is red and yellow)</div>
      </div>
    </section>
"""

part7_html = f"""
    <!-- PART VII -->
    <section class="part-section" id="section-7">
      <div class="part-header">
        <div>
          <div class="part-title">
            <span class="part-badge">PART VII</span>
            VII. Look at the picture. Write Yes or No.
          </div>
          <p class="part-vi">Quan sát bức tranh gia đình sum họp và chọn Yes (Đúng) hoặc No (Sai).</p>
        </div>
        <button type="button" class="btn-audio" onclick="speak('Part seven: Look at the picture. Write Yes or No.')">
          🔊 Nghe đề bài
        </button>
      </div>

      <div class="part7-layout">
        <!-- Picture -->
        <div class="p7-img-wrapper">
          <img src="{images['p4_family.png']}" alt="Family eating together" onclick="speak('A happy family together around the dining table')">
          <div style="font-size:0.88rem; color:#64748b; margin-top:8px; font-weight:600;">(Bấm vào hình để nghe đọc mô tả)</div>
        </div>

        <!-- Yes / No Statements -->
        <div class="yesno-list">
          <!-- 1 -->
          <div class="yesno-item" id="item-p7_1">
            <div class="yesno-text">1. There are five people in the picture.</div>
            <div class="yesno-buttons">
              <button type="button" class="btn-yn" data-q="p7_1" data-val="Yes" onclick="selectYesNo('p7_1', 'Yes')">Yes</button>
              <button type="button" class="btn-yn" data-q="p7_1" data-val="No" onclick="selectYesNo('p7_1', 'No')">No</button>
              <button type="button" class="btn-audio" onclick="speak('There are five people in the picture.')">🔊</button>
            </div>
            <div class="feedback-tip" id="fb-p7_1" style="width:100%;">Đáp án: <b>Yes</b> (Đúng, có 5 người trong tranh)</div>
          </div>

          <!-- 2 -->
          <div class="yesno-item" id="item-p7_2">
            <div class="yesno-text">2. They are happy.</div>
            <div class="yesno-buttons">
              <button type="button" class="btn-yn" data-q="p7_2" data-val="Yes" onclick="selectYesNo('p7_2', 'Yes')">Yes</button>
              <button type="button" class="btn-yn" data-q="p7_2" data-val="No" onclick="selectYesNo('p7_2', 'No')">No</button>
              <button type="button" class="btn-audio" onclick="speak('They are happy.')">🔊</button>
            </div>
            <div class="feedback-tip" id="fb-p7_2" style="width:100%;">Đáp án: <b>Yes</b> (Đúng, mọi người đều cười rất vui)</div>
          </div>

          <!-- 3 -->
          <div class="yesno-item" id="item-p7_3">
            <div class="yesno-text">3. The children are cleaning the floor.</div>
            <div class="yesno-buttons">
              <button type="button" class="btn-yn" data-q="p7_3" data-val="Yes" onclick="selectYesNo('p7_3', 'Yes')">Yes</button>
              <button type="button" class="btn-yn" data-q="p7_3" data-val="No" onclick="selectYesNo('p7_3', 'No')">No</button>
              <button type="button" class="btn-audio" onclick="speak('The children are cleaning the floor.')">🔊</button>
            </div>
            <div class="feedback-tip" id="fb-p7_3" style="width:100%;">Đáp án: <b>No</b> (Sai, các bé đang đứng chơi đùa chứ không lau sàn)</div>
          </div>

          <!-- 4 -->
          <div class="yesno-item" id="item-p7_4">
            <div class="yesno-text">4. There is a pet in the picture.</div>
            <div class="yesno-buttons">
              <button type="button" class="btn-yn" data-q="p7_4" data-val="Yes" onclick="selectYesNo('p7_4', 'Yes')">Yes</button>
              <button type="button" class="btn-yn" data-q="p7_4" data-val="No" onclick="selectYesNo('p7_4', 'No')">No</button>
              <button type="button" class="btn-audio" onclick="speak('There is a pet in the picture.')">🔊</button>
            </div>
            <div class="feedback-tip" id="fb-p7_4" style="width:100%;">Đáp án: <b>No</b> (Sai, không có con thú cưng nào trong tranh)</div>
          </div>

          <!-- 5 -->
          <div class="yesno-item" id="item-p7_5">
            <div class="yesno-text">5. The old man is eating chicken.</div>
            <div class="yesno-buttons">
              <button type="button" class="btn-yn" data-q="p7_5" data-val="Yes" onclick="selectYesNo('p7_5', 'Yes')">Yes</button>
              <button type="button" class="btn-yn" data-q="p7_5" data-val="No" onclick="selectYesNo('p7_5', 'No')">No</button>
              <button type="button" class="btn-audio" onclick="speak('The old man is eating chicken.')">🔊</button>
            </div>
            <div class="feedback-tip" id="fb-p7_5" style="width:100%;">Đáp án: <b>Yes</b> (Đúng, người đàn ông lớn tuổi đang cầm chiếc đùi gà ăn)</div>
          </div>

          <!-- 6 -->
          <div class="yesno-item" id="item-p7_6">
            <div class="yesno-text">6. The girl is wearing a hat.</div>
            <div class="yesno-buttons">
              <button type="button" class="btn-yn" data-q="p7_6" data-val="Yes" onclick="selectYesNo('p7_6', 'Yes')">Yes</button>
              <button type="button" class="btn-yn" data-q="p7_6" data-val="No" onclick="selectYesNo('p7_6', 'No')">No</button>
              <button type="button" class="btn-audio" onclick="speak('The girl is wearing a hat.')">🔊</button>
            </div>
            <div class="feedback-tip" id="fb-p7_6" style="width:100%;">Đáp án: <b>No</b> (Sai, bạn nữ tóc ngắn không hề đội mũ)</div>
          </div>
        </div>
      </div>
    </section>
"""

template_footer = """
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

  <!-- Score & Celebration Modal -->
  <div class="modal-backdrop" id="scoreModal">
    <div class="modal-card">
      <div class="modal-trophy" id="modalTrophy">🏆</div>
      <h2 class="modal-title" id="modalTitle">Tuyệt vời! Hoàn thành xuất sắc!</h2>
      <p style="color: #64748b; font-weight: 700;" id="modalStudentName"></p>
      
      <div class="modal-score" id="modalScoreDisplay">48 / 48</div>
      <p style="font-weight: 800; color: #10b981; font-size: 1.15rem;" id="modalMessage">Bé rất giỏi! Đã sẵn sàng cho kì thi giữa kì 1!</p>

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

  <!-- Canvas for celebration confetti -->
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

    let lastActiveInput = null;

    document.addEventListener('focusin', (e) => {
      if (e.target.tagName === 'INPUT' && e.target.type === 'text') {
        lastActiveInput = e.target;
      }
    });

    function handleWordChipClick(btn, partPrefix) {
      const word = btn.dataset.word;
      speak(word);

      if (lastActiveInput && lastActiveInput.id.startsWith(partPrefix)) {
        lastActiveInput.value = word;
        lastActiveInput.dispatchEvent(new Event('input'));
        focusNextInput(lastActiveInput);
      } else {
        const inputs = Array.from(document.querySelectorAll(`input[id^="${partPrefix}_"]`));
        const emptyInput = inputs.find(inp => !inp.value.trim());
        if (emptyInput) {
          emptyInput.value = word;
          emptyInput.dispatchEvent(new Event('input'));
          focusNextInput(emptyInput);
        }
      }
      updateWordBankUsage(partPrefix);
    }

    function focusNextInput(currentInput) {
      const allInputs = Array.from(document.querySelectorAll('.part-section input[type="text"]'));
      const currentIndex = allInputs.indexOf(currentInput);
      if (currentIndex >= 0 && currentIndex < allInputs.length - 1) {
        allInputs[currentIndex + 1].focus();
      }
    }

    function updateWordBankUsage(partPrefix) {
      const inputs = Array.from(document.querySelectorAll(`input[id^="${partPrefix}_"]`));
      const enteredValues = inputs.map(i => i.value.trim().toLowerCase());
      const chips = document.querySelectorAll(`#wordbank-${partPrefix} .word-chip`);
      chips.forEach(chip => {
        const w = chip.dataset.word.toLowerCase();
        if (enteredValues.includes(w)) {
          chip.classList.add('used');
        } else {
          chip.classList.remove('used');
        }
      });
    }

    function appendLetter(inputId, letter) {
      const inp = document.getElementById(inputId);
      inp.value += letter;
      inp.dispatchEvent(new Event('input'));
      playTone(440, 0.05, 'sine');
    }

    function popLetter(inputId) {
      const inp = document.getElementById(inputId);
      inp.value = inp.value.slice(0, -1);
      inp.dispatchEvent(new Event('input'));
      playTone(330, 0.05, 'sine');
    }

    function fillPart5(inputId, val) {
      const inp = document.getElementById(inputId);
      inp.value = val;
      inp.dispatchEvent(new Event('input'));
      playTone(520, 0.08, 'triangle');
    }

    const radioAnswers = {};

    function selectRadio(questionId, val) {
      radioAnswers[questionId] = val;
      const cards = document.querySelectorAll(`.radio-card[data-q="${questionId}"]`);
      cards.forEach(card => {
        if (card.dataset.val === val) {
          card.classList.add('selected');
        } else {
          card.classList.remove('selected');
        }
      });
      playTone(480, 0.07, 'sine');
      saveProgress();
    }

    const yesNoAnswers = {};

    function selectYesNo(questionId, val) {
      yesNoAnswers[questionId] = val;
      const buttons = document.querySelectorAll(`button[data-q="${questionId}"]`);
      buttons.forEach(btn => {
        if (btn.dataset.val === val) {
          if (val === 'Yes') {
            btn.classList.add('active-yes');
            btn.classList.remove('active-no');
          } else {
            btn.classList.add('active-no');
            btn.classList.remove('active-yes');
          }
        } else {
          btn.classList.remove('active-yes', 'active-no');
        }
      });
      playTone(val === 'Yes' ? 587.33 : 440, 0.08, 'triangle');
      saveProgress();
    }

    const correctAnswers = {
      'p1_1': 'chores',
      'p1_2': 'house',
      'p1_3': 'map',
      'p1_4': 'eat',
      'p1_5': 'buy',
      'p1_6': 'apartment',
      'p1_7': 'five',
      'p1_8': 'grown-up',

      'p2_1': 'townhouse',
      'p2_2': ['own', 'now'],
      'p2_3': 'yellow',
      'p2_4': 'five',
      'p2_5': 'baby',
      'p2_6': 'year',
      'p2_7': 'funny',

      'p3_1': 'him',
      'p3_2': 'own',
      'p3_3': 'chore',
      'p3_4': 'does',
      'p3_5': 'yellow',
      'p3_6': 'light',
      'p3_7': 'hold',

      'p4_1': 'ax',
      'p4_2': 'dig',
      'p4_3': 'shoes',
      'p4_4': 'bag',
      'p4_5': 'ink',
      'p4_6': 'sheep',

      'p5_1': 'a',
      'p5_2': 'sh',
      'p5_3': 'o',
      'p5_4': 'o',
      'p5_5': 'a',
      'p5_6': 'i',
      'p5_7': ['ip', 'i', 'wh', 'isk'],
      'p5_8': 'o',

      'p6_1': 'a',
      'p6_2': 'a',
      'p6_3': 'b',
      'p6_4': 'b',
      'p6_5': 'a',
      'p6_6': 'a',

      'p7_1': 'Yes',
      'p7_2': 'Yes',
      'p7_3': 'No',
      'p7_4': 'No',
      'p7_5': 'Yes',
      'p7_6': 'No'
    };

    function gradeAll() {
      let score = 0;
      let partScores = { p1: 0, p2: 0, p3: 0, p4: 0, p5: 0, p6: 0, p7: 0 };
      let partTotals = { p1: 8, p2: 7, p3: 7, p4: 6, p5: 8, p6: 6, p7: 6 };

      for (let p = 1; p <= 5; p++) {
        const inputs = document.querySelectorAll(`input[id^="p${p}_"]`);
        inputs.forEach(inp => {
          const id = inp.id;
          const userVal = inp.value.trim().toLowerCase().replace(/[-_]/g, '');
          const expected = correctAnswers[id];
          let isCorrect = false;

          if (Array.isArray(expected)) {
            isCorrect = expected.some(exp => exp.replace(/[-_]/g, '') === userVal);
          } else {
            isCorrect = expected.replace(/[-_]/g, '') === userVal;
          }

          inp.classList.remove('correct', 'wrong');
          const fb = document.getElementById(`fb-${id}`);

          if (isCorrect) {
            inp.classList.add('correct');
            score++;
            partScores[`p${p}`]++;
            if (fb) fb.classList.remove('show-wrong');
          } else {
            inp.classList.add('wrong');
            if (fb) fb.classList.add('show-wrong');
          }
        });
      }

      for (let i = 1; i <= 6; i++) {
        const qId = `p6_${i}`;
        const userChoice = radioAnswers[qId];
        const expected = correctAnswers[qId];
        const fb = document.getElementById(`fb-${qId}`);
        const cards = document.querySelectorAll(`.radio-card[data-q="${qId}"]`);

        cards.forEach(card => card.classList.remove('correct', 'wrong'));

        if (userChoice === expected) {
          score++;
          partScores.p6++;
          const selected = document.querySelector(`.radio-card[data-q="${qId}"][data-val="${userChoice}"]`);
          if (selected) selected.classList.add('correct');
          if (fb) fb.classList.remove('show-wrong');
        } else {
          if (userChoice) {
            const selected = document.querySelector(`.radio-card[data-q="${qId}"][data-val="${userChoice}"]`);
            if (selected) selected.classList.add('wrong');
          }
          if (fb) fb.classList.add('show-wrong');
        }
      }

      for (let i = 1; i <= 6; i++) {
        const qId = `p7_${i}`;
        const userChoice = yesNoAnswers[qId];
        const expected = correctAnswers[qId];
        const fb = document.getElementById(`fb-${qId}`);

        if (userChoice === expected) {
          score++;
          partScores.p7++;
          if (fb) fb.classList.remove('show-wrong');
        } else {
          if (fb) fb.classList.add('show-wrong');
        }
      }

      document.getElementById('currentScore').innerText = score;

      if (score === 48) {
        playVictoryFanfare();
        triggerConfetti();
      } else if (score >= 40) {
        playCorrectChime();
        triggerConfetti();
      } else {
        playTone(440, 0.2, 'triangle');
      }

      showScoreModal(score, partScores, partTotals);
    }

    function showScoreModal(score, partScores, partTotals) {
      const studentName = document.getElementById('studentName').value.trim();
      document.getElementById('modalStudentName').innerText = studentName ? `Học sinh: ${studentName}` : '';
      document.getElementById('modalScoreDisplay').innerText = `${score} / 48 Điểm`;

      let trophy = '🏆';
      let title = 'Tuyệt vời!';
      let msg = 'Bé hoàn thành rất tốt!';

      if (score === 48) {
        trophy = '🌟';
        title = 'Xuất Sắc! Điểm Tuyệt Đối!';
        msg = 'Bé đạt điểm 100%! Bé rất chăm chỉ và thông minh!';
      } else if (score >= 40) {
        trophy = '🥇';
        title = 'Giỏi Quá!';
        msg = 'Bé làm đúng gần hết rồi, xem lại vài câu chưa đúng nhé!';
      } else if (score >= 30) {
        trophy = '🥈';
        title = 'Cố Gắng Lên!';
        msg = 'Bé đã làm rất tốt, hãy xem lại đáp án và luyện tập thêm nhé!';
      } else {
        trophy = '💪';
        title = 'Cần Ôn Tập Thêm!';
        msg = 'Đừng nản lòng nhé! Hãy bấm nút Xem đáp án để học từ vựng nha!';
      }

      document.getElementById('modalTrophy').innerText = trophy;
      document.getElementById('modalTitle').innerText = title;
      document.getElementById('modalMessage').innerText = msg;

      const breakdownEl = document.getElementById('modalBreakdown');
      breakdownEl.innerHTML = `
        <div class="breakdown-row"><span>Part I (Label pictures):</span> <b>${partScores.p1} / ${partTotals.p1}</b></div>
        <div class="breakdown-row"><span>Part II (Unscramble words):</span> <b>${partScores.p2} / ${partTotals.p2}</b></div>
        <div class="breakdown-row"><span>Part III (Complete sentences):</span> <b>${partScores.p3} / ${partTotals.p3}</b></div>
        <div class="breakdown-row"><span>Part IV (Label pictures):</span> <b>${partScores.p4} / ${partTotals.p4}</b></div>
        <div class="breakdown-row"><span>Part V (Phonics / Fill letters):</span> <b>${partScores.p5} / ${partTotals.p5}</b></div>
        <div class="breakdown-row"><span>Part VI (Read stories):</span> <b>${partScores.p6} / ${partTotals.p6}</b></div>
        <div class="breakdown-row"><span>Part VII (Picture Yes/No):</span> <b>${partScores.p7} / ${partTotals.p7}</b></div>
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
      if (confirm('Bé có muốn làm lại đề thi từ đầu không?')) {
        document.querySelectorAll('input[type="text"]').forEach(inp => {
          if (inp.id !== 'studentName' && inp.id !== 'studentClass') {
            inp.value = '';
            inp.classList.remove('correct', 'wrong');
          }
        });

        for (let k in radioAnswers) delete radioAnswers[k];
        document.querySelectorAll('.radio-card').forEach(c => c.classList.remove('selected', 'correct', 'wrong'));

        for (let k in yesNoAnswers) delete yesNoAnswers[k];
        document.querySelectorAll('.btn-yn').forEach(b => b.classList.remove('active-yes', 'active-no'));

        document.querySelectorAll('.word-chip').forEach(c => c.classList.remove('used'));
        document.querySelectorAll('.feedback-tip').forEach(t => t.classList.remove('show-correct', 'show-wrong'));

        document.getElementById('currentScore').innerText = '0';
        showingAnswers = false;
        document.getElementById('toggleAnswersText').innerText = 'Xem đáp án';

        try { localStorage.removeItem(STORAGE_KEY); } catch(e) {}

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
      const colors = ['#f43f5e', '#3b82f6', '#10b981', '#f59e0b', '#8b5cf6', '#ec4899'];

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

    const STORAGE_KEY = 'eng2_midterm1_answers';
    function saveProgress() {
      const data = {
        name: document.getElementById('studentName').value,
        className: document.getElementById('studentClass').value,
        inputs: {},
        radios: radioAnswers,
        yesnos: yesNoAnswers
      };
      document.querySelectorAll('input[type="text"]').forEach(inp => {
        data.inputs[inp.id] = inp.value;
      });
      try {
        localStorage.setItem(STORAGE_KEY, JSON.stringify(data));
      } catch(e) {}
    }

    function loadProgress() {
      try {
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
        if (data.radios) {
          for (let q in data.radios) selectRadio(q, data.radios[q]);
        }
        if (data.yesnos) {
          for (let q in data.yesnos) selectYesNo(q, data.yesnos[q]);
        }
        ['p1', 'p3', 'p4'].forEach(updateWordBankUsage);
      } catch(e) {}
    }

    document.addEventListener('input', () => {
      ['p1', 'p3', 'p4'].forEach(updateWordBankUsage);
      saveProgress();
    });

    window.addEventListener('load', () => {
      loadProgress();
    });
  </script>
</body>
</html>
"""

full_html = template_head + part1_html + part2_html + part3_html + part4_html + part5_html + part6_html + part7_html + template_footer

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(full_html)

print(f"Generated index.html successfully with {len(full_html)} bytes.")
