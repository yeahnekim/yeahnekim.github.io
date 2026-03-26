import base64

with open('hero_b64.txt', 'r') as f:
    hero_b64 = f.read().strip()

with open('logo_b64.txt', 'r') as f:
    logo_b64 = f.read().strip()

hero_src = f"data:image/png;base64,{hero_b64}"
logo_src = f"data:image/png;base64,{logo_b64}"

html = f"""<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>CMS - Construction Manager School</title>
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@300;400;500;600;700;800&family=Inter:wght@300;400;500;600;700;800&display=swap" rel="stylesheet" />
  <style>
    /* ============================================================
       CMS School — Color System (10 Palette)
       1. Deep Navy    #1A3A5C  — headers, footer bg
       2. Ocean Blue   #2B6CB0  — primary buttons, nav active
       3. Sky Blue     #4299E1  — primary brand color
       4. Bright Sky   #63B3ED  — hover states, highlights
       5. Light Sky    #90CDF4  — card borders, subtle accents
       6. Pale Blue    #BEE3F8  — section backgrounds
       7. Ice Blue     #EBF8FF  — lightest bg tint
       8. Teal Accent  #38B2AC  — ADHD special badge, CTA
       9. Soft Gold    #F6AD55  — warm accent, highlights
      10. Pure White   #FFFFFF  — text on dark, card bg
    ============================================================ */

    :root {{
      --c1: #1A3A5C;
      --c2: #2B6CB0;
      --c3: #4299E1;
      --c4: #63B3ED;
      --c5: #90CDF4;
      --c6: #BEE3F8;
      --c7: #EBF8FF;
      --c8: #38B2AC;
      --c9: #F6AD55;
      --c10: #FFFFFF;
      --font-ko: 'Noto Sans KR', sans-serif;
      --font-en: 'Inter', sans-serif;
      --radius: 16px;
      --shadow: 0 4px 24px rgba(26,58,92,0.10);
      --shadow-lg: 0 8px 48px rgba(26,58,92,0.18);
    }}

    *, *::before, *::after {{ box-sizing: border-box; margin: 0; padding: 0; }}

    html {{ scroll-behavior: smooth; }}

    body {{
      font-family: var(--font-ko);
      background: var(--c10);
      color: var(--c1);
      overflow-x: hidden;
    }}

    /* ── TOP UTILITY BAR ─────────────────────────────────────── */
    .top-bar {{
      background: var(--c1);
      color: rgba(255,255,255,0.75);
      font-size: 0.78rem;
      padding: 6px 0;
      font-family: var(--font-en);
    }}
    .top-bar .inner {{
      max-width: 1280px;
      margin: 0 auto;
      padding: 0 24px;
      display: flex;
      justify-content: space-between;
      align-items: center;
    }}
    .top-bar a {{ color: rgba(255,255,255,0.75); text-decoration: none; margin-left: 16px; }}
    .top-bar a:hover {{ color: var(--c9); }}

    /* ── NAVBAR ─────────────────────────────────────────────── */
    .navbar {{
      position: sticky;
      top: 0;
      z-index: 1000;
      background: rgba(255,255,255,0.97);
      backdrop-filter: blur(12px);
      border-bottom: 2px solid var(--c6);
      box-shadow: 0 2px 16px rgba(26,58,92,0.08);
      transition: box-shadow 0.3s;
    }}
    .navbar.scrolled {{ box-shadow: 0 4px 32px rgba(26,58,92,0.16); }}
    .navbar .inner {{
      max-width: 1280px;
      margin: 0 auto;
      padding: 0 24px;
      display: flex;
      align-items: center;
      height: 72px;
      gap: 0;
    }}
    .logo-wrap {{
      display: flex;
      align-items: center;
      gap: 12px;
      text-decoration: none;
      flex-shrink: 0;
      margin-right: auto;
    }}
    .logo-wrap img {{
      height: 52px;
      width: auto;
      object-fit: contain;
    }}
    .logo-text {{
      display: flex;
      flex-direction: column;
      line-height: 1.2;
    }}
    .logo-text .abbr {{
      font-family: var(--font-en);
      font-weight: 800;
      font-size: 1.5rem;
      color: var(--c2);
      letter-spacing: 2px;
    }}
    .logo-text .full {{
      font-size: 0.68rem;
      color: var(--c3);
      font-weight: 500;
      letter-spacing: 0.5px;
    }}

    .nav-links {{
      display: flex;
      list-style: none;
      gap: 0;
      align-items: stretch;
      height: 72px;
    }}
    .nav-links li {{
      position: relative;
      display: flex;
      align-items: center;
    }}
    .nav-links a {{
      display: flex;
      align-items: center;
      padding: 0 20px;
      height: 100%;
      font-size: 0.95rem;
      font-weight: 600;
      color: var(--c1);
      text-decoration: none;
      transition: color 0.2s;
      white-space: nowrap;
      position: relative;
    }}
    .nav-links a::after {{
      content: '';
      position: absolute;
      bottom: 0;
      left: 50%;
      transform: translateX(-50%);
      width: 0;
      height: 3px;
      background: var(--c3);
      border-radius: 3px 3px 0 0;
      transition: width 0.25s ease;
    }}
    .nav-links a:hover {{ color: var(--c3); }}
    .nav-links a:hover::after {{ width: 60%; }}
    .nav-links li.active a {{ color: var(--c2); }}
    .nav-links li.active a::after {{ width: 60%; background: var(--c2); }}
    .nav-links li.adhd a {{
      color: var(--c8);
      font-weight: 700;
    }}
    .nav-links li.adhd a::after {{ background: var(--c8); }}
    .nav-links li.adhd a:hover {{ color: #2C7A7B; }}

    .nav-cta {{
      margin-left: 20px;
      padding: 10px 22px;
      background: linear-gradient(135deg, var(--c3), var(--c2));
      color: white !important;
      border-radius: 50px;
      font-weight: 700 !important;
      font-size: 0.88rem !important;
      transition: transform 0.2s, box-shadow 0.2s !important;
      box-shadow: 0 4px 16px rgba(66,153,225,0.35);
    }}
    .nav-cta::after {{ display: none !important; }}
    .nav-cta:hover {{
      transform: translateY(-2px) !important;
      box-shadow: 0 6px 24px rgba(66,153,225,0.45) !important;
      color: white !important;
    }}

    .hamburger {{
      display: none;
      flex-direction: column;
      gap: 5px;
      cursor: pointer;
      padding: 8px;
      margin-left: auto;
    }}
    .hamburger span {{
      display: block;
      width: 26px;
      height: 2.5px;
      background: var(--c1);
      border-radius: 2px;
      transition: all 0.3s;
    }}

    /* ── HERO SECTION ───────────────────────────────────────── */
    .hero {{
      position: relative;
      min-height: 100vh;
      background: linear-gradient(160deg, var(--c1) 0%, var(--c2) 40%, var(--c3) 100%);
      overflow: hidden;
      display: flex;
      align-items: center;
    }}
    .hero-bg-pattern {{
      position: absolute;
      inset: 0;
      background-image:
        radial-gradient(circle at 20% 50%, rgba(99,179,237,0.15) 0%, transparent 50%),
        radial-gradient(circle at 80% 20%, rgba(56,178,172,0.12) 0%, transparent 40%),
        radial-gradient(circle at 60% 80%, rgba(246,173,85,0.08) 0%, transparent 35%);
    }}
    .hero-particles {{
      position: absolute;
      inset: 0;
      overflow: hidden;
    }}
    .particle {{
      position: absolute;
      border-radius: 50%;
      background: rgba(255,255,255,0.15);
      animation: float linear infinite;
    }}
    @keyframes float {{
      0% {{ transform: translateY(100vh) rotate(0deg); opacity: 0; }}
      10% {{ opacity: 1; }}
      90% {{ opacity: 1; }}
      100% {{ transform: translateY(-100px) rotate(720deg); opacity: 0; }}
    }}

    .hero .inner {{
      max-width: 1280px;
      margin: 0 auto;
      padding: 120px 24px 80px;
      display: grid;
      grid-template-columns: 1fr 1.2fr;
      gap: 60px;
      align-items: center;
      position: relative;
      z-index: 2;
      width: 100%;
    }}
    .hero-content {{ color: white; }}
    .hero-badge {{
      display: inline-flex;
      align-items: center;
      gap: 8px;
      background: rgba(255,255,255,0.15);
      border: 1px solid rgba(255,255,255,0.3);
      border-radius: 50px;
      padding: 6px 16px;
      font-size: 0.82rem;
      font-weight: 600;
      color: var(--c9);
      margin-bottom: 24px;
      backdrop-filter: blur(8px);
      letter-spacing: 0.5px;
    }}
    .hero-badge .dot {{
      width: 7px;
      height: 7px;
      background: var(--c9);
      border-radius: 50%;
      animation: pulse 2s infinite;
    }}
    @keyframes pulse {{
      0%, 100% {{ transform: scale(1); opacity: 1; }}
      50% {{ transform: scale(1.4); opacity: 0.7; }}
    }}
    .hero-title {{
      font-size: clamp(2.2rem, 4vw, 3.4rem);
      font-weight: 800;
      line-height: 1.2;
      margin-bottom: 12px;
      letter-spacing: -0.5px;
    }}
    .hero-title .highlight {{
      color: var(--c9);
      position: relative;
    }}
    .hero-title .highlight::after {{
      content: '';
      position: absolute;
      bottom: 2px;
      left: 0;
      right: 0;
      height: 3px;
      background: var(--c9);
      border-radius: 2px;
      opacity: 0.5;
    }}
    .hero-subtitle {{
      font-size: 1.15rem;
      font-weight: 400;
      color: rgba(255,255,255,0.85);
      margin-bottom: 20px;
      line-height: 1.7;
    }}
    .hero-desc {{
      font-size: 0.95rem;
      color: rgba(255,255,255,0.7);
      line-height: 1.8;
      margin-bottom: 36px;
      max-width: 480px;
    }}
    .hero-actions {{
      display: flex;
      gap: 16px;
      flex-wrap: wrap;
    }}
    .btn-primary {{
      padding: 14px 32px;
      background: var(--c9);
      color: var(--c1);
      border: none;
      border-radius: 50px;
      font-size: 1rem;
      font-weight: 700;
      cursor: pointer;
      text-decoration: none;
      display: inline-flex;
      align-items: center;
      gap: 8px;
      transition: transform 0.2s, box-shadow 0.2s;
      box-shadow: 0 4px 20px rgba(246,173,85,0.4);
      font-family: var(--font-ko);
    }}
    .btn-primary:hover {{
      transform: translateY(-3px);
      box-shadow: 0 8px 32px rgba(246,173,85,0.5);
    }}
    .btn-secondary {{
      padding: 14px 32px;
      background: rgba(255,255,255,0.15);
      color: white;
      border: 2px solid rgba(255,255,255,0.4);
      border-radius: 50px;
      font-size: 1rem;
      font-weight: 600;
      cursor: pointer;
      text-decoration: none;
      display: inline-flex;
      align-items: center;
      gap: 8px;
      transition: all 0.2s;
      backdrop-filter: blur(8px);
      font-family: var(--font-ko);
    }}
    .btn-secondary:hover {{
      background: rgba(255,255,255,0.25);
      border-color: rgba(255,255,255,0.7);
      transform: translateY(-2px);
    }}
    .hero-stats {{
      display: flex;
      gap: 32px;
      margin-top: 48px;
      padding-top: 32px;
      border-top: 1px solid rgba(255,255,255,0.2);
    }}
    .stat-item {{ text-align: center; }}
    .stat-num {{
      font-size: 2rem;
      font-weight: 800;
      color: var(--c9);
      font-family: var(--font-en);
      display: block;
    }}
    .stat-label {{
      font-size: 0.8rem;
      color: rgba(255,255,255,0.7);
      margin-top: 2px;
    }}

    .hero-visual {{
      position: relative;
      display: flex;
      align-items: center;
      justify-content: center;
    }}
    .hero-img-wrap {{
      position: relative;
      border-radius: 24px;
      overflow: hidden;
      box-shadow: 0 24px 80px rgba(0,0,0,0.35);
      animation: heroFloat 6s ease-in-out infinite;
    }}
    @keyframes heroFloat {{
      0%, 100% {{ transform: translateY(0px); }}
      50% {{ transform: translateY(-12px); }}
    }}
    .hero-img-wrap img {{
      width: 100%;
      max-width: 600px;
      height: auto;
      display: block;
    }}
    .hero-img-badge {{
      position: absolute;
      bottom: 24px;
      left: 24px;
      background: rgba(255,255,255,0.95);
      border-radius: 14px;
      padding: 12px 18px;
      display: flex;
      align-items: center;
      gap: 10px;
      box-shadow: 0 4px 20px rgba(0,0,0,0.15);
      backdrop-filter: blur(8px);
    }}
    .hero-img-badge .icon {{
      width: 40px;
      height: 40px;
      background: linear-gradient(135deg, var(--c3), var(--c8));
      border-radius: 10px;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 1.3rem;
    }}
    .hero-img-badge .text .label {{
      font-size: 0.72rem;
      color: var(--c3);
      font-weight: 600;
      text-transform: uppercase;
      letter-spacing: 0.5px;
    }}
    .hero-img-badge .text .value {{
      font-size: 0.95rem;
      font-weight: 700;
      color: var(--c1);
    }}
    .hero-scroll {{
      position: absolute;
      bottom: 32px;
      left: 50%;
      transform: translateX(-50%);
      display: flex;
      flex-direction: column;
      align-items: center;
      gap: 8px;
      color: rgba(255,255,255,0.6);
      font-size: 0.75rem;
      z-index: 2;
      cursor: pointer;
      animation: bounce 2s infinite;
    }}
    @keyframes bounce {{
      0%, 100% {{ transform: translateX(-50%) translateY(0); }}
      50% {{ transform: translateX(-50%) translateY(6px); }}
    }}
    .scroll-arrow {{
      width: 28px;
      height: 28px;
      border: 2px solid rgba(255,255,255,0.4);
      border-radius: 50%;
      display: flex;
      align-items: center;
      justify-content: center;
    }}

    /* ── SECTION COMMON ─────────────────────────────────────── */
    section {{ padding: 96px 0; }}
    .section-inner {{
      max-width: 1280px;
      margin: 0 auto;
      padding: 0 24px;
    }}
    .section-tag {{
      display: inline-block;
      background: var(--c7);
      color: var(--c3);
      font-size: 0.78rem;
      font-weight: 700;
      letter-spacing: 1.5px;
      text-transform: uppercase;
      padding: 5px 14px;
      border-radius: 50px;
      margin-bottom: 16px;
      border: 1px solid var(--c5);
    }}
    .section-title {{
      font-size: clamp(1.8rem, 3vw, 2.6rem);
      font-weight: 800;
      color: var(--c1);
      line-height: 1.25;
      margin-bottom: 16px;
    }}
    .section-desc {{
      font-size: 1.05rem;
      color: #4A5568;
      line-height: 1.8;
      max-width: 640px;
    }}
    .section-header {{ margin-bottom: 56px; }}
    .section-header.center {{ text-align: center; }}
    .section-header.center .section-desc {{ margin: 0 auto; }}

    /* ── QUOTE BAND ─────────────────────────────────────────── */
    .quote-band {{
      background: linear-gradient(135deg, var(--c7) 0%, var(--c6) 100%);
      padding: 72px 0;
      border-top: 1px solid var(--c5);
      border-bottom: 1px solid var(--c5);
    }}
    .quote-band .inner {{
      max-width: 900px;
      margin: 0 auto;
      padding: 0 24px;
      text-align: center;
    }}
    .quote-mark {{
      font-size: 6rem;
      line-height: 0.5;
      color: var(--c5);
      font-family: Georgia, serif;
      margin-bottom: 24px;
      display: block;
    }}
    .quote-text {{
      font-size: clamp(1.2rem, 2.5vw, 1.7rem);
      font-weight: 700;
      color: var(--c1);
      line-height: 1.6;
      margin-bottom: 20px;
    }}
    .quote-sub {{
      font-size: 1rem;
      color: var(--c2);
      font-weight: 500;
    }}

    /* ── FEATURE CARDS ──────────────────────────────────────── */
    .features {{ background: var(--c10); }}
    .features-grid {{
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 24px;
    }}
    .feature-card {{
      background: var(--c10);
      border: 2px solid var(--c6);
      border-radius: var(--radius);
      padding: 36px 28px;
      text-align: center;
      transition: all 0.3s ease;
      cursor: pointer;
      position: relative;
      overflow: hidden;
    }}
    .feature-card::before {{
      content: '';
      position: absolute;
      top: 0;
      left: 0;
      right: 0;
      height: 4px;
      background: linear-gradient(90deg, var(--c3), var(--c4));
      transform: scaleX(0);
      transition: transform 0.3s ease;
    }}
    .feature-card:hover {{
      border-color: var(--c4);
      box-shadow: var(--shadow-lg);
      transform: translateY(-6px);
    }}
    .feature-card:hover::before {{ transform: scaleX(1); }}
    .feature-card.adhd-card {{
      border-color: var(--c8);
      background: linear-gradient(135deg, rgba(56,178,172,0.05), rgba(56,178,172,0.02));
    }}
    .feature-card.adhd-card::before {{
      background: linear-gradient(90deg, var(--c8), #4FD1C5);
    }}
    .feature-card.adhd-card:hover {{ border-color: var(--c8); }}
    .card-icon {{
      width: 72px;
      height: 72px;
      border-radius: 20px;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 2rem;
      margin: 0 auto 20px;
      background: var(--c7);
    }}
    .feature-card.adhd-card .card-icon {{
      background: rgba(56,178,172,0.12);
    }}
    .card-title {{
      font-size: 1.1rem;
      font-weight: 700;
      color: var(--c1);
      margin-bottom: 10px;
    }}
    .card-desc {{
      font-size: 0.88rem;
      color: #718096;
      line-height: 1.7;
    }}
    .card-link {{
      display: inline-flex;
      align-items: center;
      gap: 4px;
      margin-top: 16px;
      font-size: 0.85rem;
      font-weight: 600;
      color: var(--c3);
      text-decoration: none;
      transition: gap 0.2s;
    }}
    .feature-card.adhd-card .card-link {{ color: var(--c8); }}
    .card-link:hover {{ gap: 8px; }}

    /* ── ABOUT SECTION ──────────────────────────────────────── */
    .about {{
      background: linear-gradient(160deg, var(--c1) 0%, #1e4976 100%);
      color: white;
      position: relative;
      overflow: hidden;
    }}
    .about::before {{
      content: '';
      position: absolute;
      top: -100px;
      right: -100px;
      width: 500px;
      height: 500px;
      background: radial-gradient(circle, rgba(66,153,225,0.15) 0%, transparent 70%);
      border-radius: 50%;
    }}
    .about-grid {{
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 80px;
      align-items: center;
    }}
    .about-content .section-title {{ color: white; }}
    .about-content .section-tag {{
      background: rgba(255,255,255,0.1);
      color: var(--c5);
      border-color: rgba(255,255,255,0.2);
    }}
    .about-content .section-desc {{ color: rgba(255,255,255,0.8); max-width: none; }}
    .about-values {{
      margin-top: 40px;
      display: flex;
      flex-direction: column;
      gap: 16px;
    }}
    .value-item {{
      display: flex;
      align-items: flex-start;
      gap: 16px;
      padding: 16px 20px;
      background: rgba(255,255,255,0.07);
      border-radius: 12px;
      border: 1px solid rgba(255,255,255,0.1);
      transition: background 0.2s;
    }}
    .value-item:hover {{ background: rgba(255,255,255,0.12); }}
    .value-icon {{
      width: 44px;
      height: 44px;
      background: linear-gradient(135deg, var(--c3), var(--c4));
      border-radius: 12px;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 1.3rem;
      flex-shrink: 0;
    }}
    .value-text .vt {{ font-size: 0.95rem; font-weight: 700; color: white; margin-bottom: 4px; }}
    .value-text .vd {{ font-size: 0.83rem; color: rgba(255,255,255,0.65); line-height: 1.6; }}

    .about-visual {{
      position: relative;
    }}
    .about-card-stack {{
      position: relative;
    }}
    .about-card {{
      background: rgba(255,255,255,0.08);
      border: 1px solid rgba(255,255,255,0.15);
      border-radius: 20px;
      padding: 32px;
      backdrop-filter: blur(10px);
    }}
    .about-card-title {{
      font-size: 1.1rem;
      font-weight: 700;
      color: var(--c9);
      margin-bottom: 20px;
      display: flex;
      align-items: center;
      gap: 10px;
    }}
    .about-card-title::before {{
      content: '';
      display: block;
      width: 4px;
      height: 20px;
      background: var(--c9);
      border-radius: 2px;
    }}
    .about-list {{
      list-style: none;
      display: flex;
      flex-direction: column;
      gap: 12px;
    }}
    .about-list li {{
      display: flex;
      align-items: center;
      gap: 12px;
      font-size: 0.92rem;
      color: rgba(255,255,255,0.85);
    }}
    .about-list li::before {{
      content: '✓';
      width: 24px;
      height: 24px;
      background: rgba(66,153,225,0.3);
      border-radius: 50%;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 0.75rem;
      color: var(--c4);
      flex-shrink: 0;
    }}
    .about-card-2 {{
      margin-top: 20px;
      background: rgba(56,178,172,0.12);
      border-color: rgba(56,178,172,0.3);
    }}
    .about-card-2 .about-card-title {{ color: #4FD1C5; }}
    .about-card-2 .about-card-title::before {{ background: #4FD1C5; }}
    .about-card-2 .about-list li::before {{
      background: rgba(56,178,172,0.3);
      color: #4FD1C5;
    }}

    /* ── ADHD SPECIAL ───────────────────────────────────────── */
    .adhd-section {{ background: var(--c7); }}
    .adhd-header {{
      display: flex;
      align-items: flex-end;
      justify-content: space-between;
      margin-bottom: 56px;
      gap: 24px;
      flex-wrap: wrap;
    }}
    .adhd-badge {{
      display: inline-flex;
      align-items: center;
      gap: 8px;
      background: var(--c8);
      color: white;
      font-size: 0.8rem;
      font-weight: 700;
      letter-spacing: 1px;
      text-transform: uppercase;
      padding: 6px 16px;
      border-radius: 50px;
      margin-bottom: 16px;
    }}
    .adhd-grid {{
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 28px;
    }}
    .adhd-card {{
      background: white;
      border-radius: var(--radius);
      overflow: hidden;
      box-shadow: var(--shadow);
      transition: all 0.3s;
    }}
    .adhd-card:hover {{
      transform: translateY(-6px);
      box-shadow: var(--shadow-lg);
    }}
    .adhd-card-top {{
      height: 8px;
      background: linear-gradient(90deg, var(--c8), #4FD1C5);
    }}
    .adhd-card-body {{ padding: 28px; }}
    .adhd-card-num {{
      font-size: 2.5rem;
      font-weight: 800;
      color: var(--c6);
      font-family: var(--font-en);
      line-height: 1;
      margin-bottom: 12px;
    }}
    .adhd-card-title {{
      font-size: 1.05rem;
      font-weight: 700;
      color: var(--c1);
      margin-bottom: 10px;
    }}
    .adhd-card-desc {{
      font-size: 0.87rem;
      color: #718096;
      line-height: 1.75;
    }}
    .adhd-card-tag {{
      display: inline-block;
      margin-top: 16px;
      padding: 4px 12px;
      background: rgba(56,178,172,0.1);
      color: var(--c8);
      border-radius: 50px;
      font-size: 0.78rem;
      font-weight: 600;
    }}

    /* ── NEWS / GALLERY ─────────────────────────────────────── */
    .news-section {{ background: white; }}
    .news-grid {{
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 28px;
    }}
    .news-card {{
      border-radius: var(--radius);
      overflow: hidden;
      border: 1px solid var(--c6);
      transition: all 0.3s;
      cursor: pointer;
    }}
    .news-card:hover {{
      box-shadow: var(--shadow-lg);
      transform: translateY(-4px);
    }}
    .news-card-img {{
      height: 200px;
      background: linear-gradient(135deg, var(--c6), var(--c5));
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 3rem;
      position: relative;
      overflow: hidden;
    }}
    .news-card-img .overlay {{
      position: absolute;
      inset: 0;
      background: linear-gradient(to bottom, transparent 50%, rgba(26,58,92,0.5));
    }}
    .news-card-body {{ padding: 24px; }}
    .news-category {{
      display: inline-block;
      padding: 3px 10px;
      background: var(--c7);
      color: var(--c3);
      border-radius: 50px;
      font-size: 0.75rem;
      font-weight: 700;
      margin-bottom: 10px;
    }}
    .news-title {{
      font-size: 1rem;
      font-weight: 700;
      color: var(--c1);
      line-height: 1.5;
      margin-bottom: 8px;
    }}
    .news-excerpt {{
      font-size: 0.85rem;
      color: #718096;
      line-height: 1.7;
      margin-bottom: 16px;
    }}
    .news-meta {{
      font-size: 0.78rem;
      color: #A0AEC0;
      display: flex;
      align-items: center;
      gap: 8px;
    }}

    /* ── CTA BAND ───────────────────────────────────────────── */
    .cta-band {{
      background: linear-gradient(135deg, var(--c2) 0%, var(--c3) 50%, var(--c8) 100%);
      padding: 96px 0;
      text-align: center;
      position: relative;
      overflow: hidden;
    }}
    .cta-band::before {{
      content: '';
      position: absolute;
      inset: 0;
      background: url("data:image/svg+xml,%3Csvg width='60' height='60' viewBox='0 0 60 60' xmlns='http://www.w3.org/2000/svg'%3E%3Cg fill='none' fill-rule='evenodd'%3E%3Cg fill='%23ffffff' fill-opacity='0.04'%3E%3Cpath d='M36 34v-4h-2v4h-4v2h4v4h2v-4h4v-2h-4zm0-30V0h-2v4h-4v2h4v4h2V6h4V4h-4zM6 34v-4H4v4H0v2h4v4h2v-4h4v-2H6zM6 4V0H4v4H0v2h4v4h2V6h4V4H6z'/%3E%3C/g%3E%3C/g%3E%3C/svg%3E");
    }}
    .cta-band .inner {{ position: relative; z-index: 1; max-width: 800px; margin: 0 auto; padding: 0 24px; }}
    .cta-band h2 {{
      font-size: clamp(1.8rem, 3.5vw, 2.8rem);
      font-weight: 800;
      color: white;
      margin-bottom: 16px;
      line-height: 1.3;
    }}
    .cta-band p {{
      font-size: 1.1rem;
      color: rgba(255,255,255,0.85);
      margin-bottom: 40px;
      line-height: 1.7;
    }}
    .cta-actions {{ display: flex; gap: 16px; justify-content: center; flex-wrap: wrap; }}
    .btn-white {{
      padding: 15px 36px;
      background: white;
      color: var(--c2);
      border: none;
      border-radius: 50px;
      font-size: 1rem;
      font-weight: 700;
      cursor: pointer;
      text-decoration: none;
      display: inline-flex;
      align-items: center;
      gap: 8px;
      transition: all 0.2s;
      box-shadow: 0 4px 20px rgba(0,0,0,0.15);
      font-family: var(--font-ko);
    }}
    .btn-white:hover {{ transform: translateY(-3px); box-shadow: 0 8px 32px rgba(0,0,0,0.2); }}
    .btn-outline-white {{
      padding: 15px 36px;
      background: transparent;
      color: white;
      border: 2px solid rgba(255,255,255,0.6);
      border-radius: 50px;
      font-size: 1rem;
      font-weight: 600;
      cursor: pointer;
      text-decoration: none;
      display: inline-flex;
      align-items: center;
      gap: 8px;
      transition: all 0.2s;
      font-family: var(--font-ko);
    }}
    .btn-outline-white:hover {{ background: rgba(255,255,255,0.15); border-color: white; transform: translateY(-2px); }}

    /* ── CONTACT SECTION ────────────────────────────────────── */
    .contact-section {{ background: var(--c7); }}
    .contact-grid {{
      display: grid;
      grid-template-columns: 1fr 1.4fr;
      gap: 60px;
      align-items: start;
    }}
    .contact-info {{ }}
    .contact-item {{
      display: flex;
      gap: 16px;
      align-items: flex-start;
      margin-bottom: 28px;
    }}
    .contact-icon {{
      width: 48px;
      height: 48px;
      background: var(--c3);
      border-radius: 12px;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 1.3rem;
      flex-shrink: 0;
      color: white;
    }}
    .contact-text .ct {{ font-size: 0.8rem; font-weight: 600; color: var(--c3); text-transform: uppercase; letter-spacing: 0.5px; }}
    .contact-text .cv {{ font-size: 0.95rem; color: var(--c1); font-weight: 500; margin-top: 2px; }}

    .contact-form {{
      background: white;
      border-radius: 20px;
      padding: 40px;
      box-shadow: var(--shadow);
    }}
    .form-title {{
      font-size: 1.3rem;
      font-weight: 700;
      color: var(--c1);
      margin-bottom: 28px;
    }}
    .form-row {{ display: grid; grid-template-columns: 1fr 1fr; gap: 16px; margin-bottom: 16px; }}
    .form-group {{ margin-bottom: 16px; }}
    .form-group label {{
      display: block;
      font-size: 0.85rem;
      font-weight: 600;
      color: var(--c1);
      margin-bottom: 6px;
    }}
    .form-group input,
    .form-group select,
    .form-group textarea {{
      width: 100%;
      padding: 12px 16px;
      border: 2px solid var(--c6);
      border-radius: 10px;
      font-size: 0.92rem;
      font-family: var(--font-ko);
      color: var(--c1);
      transition: border-color 0.2s;
      outline: none;
      background: white;
    }}
    .form-group input:focus,
    .form-group select:focus,
    .form-group textarea:focus {{
      border-color: var(--c3);
      box-shadow: 0 0 0 3px rgba(66,153,225,0.15);
    }}
    .form-group textarea {{ resize: vertical; min-height: 120px; }}
    .form-submit {{
      width: 100%;
      padding: 15px;
      background: linear-gradient(135deg, var(--c3), var(--c2));
      color: white;
      border: none;
      border-radius: 10px;
      font-size: 1rem;
      font-weight: 700;
      cursor: pointer;
      font-family: var(--font-ko);
      transition: all 0.2s;
      margin-top: 8px;
    }}
    .form-submit:hover {{ transform: translateY(-2px); box-shadow: 0 6px 24px rgba(66,153,225,0.35); }}

    /* ── FOOTER ─────────────────────────────────────────────── */
    footer {{
      background: var(--c1);
      color: rgba(255,255,255,0.75);
      padding: 64px 0 32px;
    }}
    .footer-grid {{
      max-width: 1280px;
      margin: 0 auto;
      padding: 0 24px;
      display: grid;
      grid-template-columns: 1.5fr 1fr 1fr 1fr;
      gap: 48px;
      margin-bottom: 48px;
    }}
    .footer-brand .logo-wrap {{ margin-bottom: 16px; }}
    .footer-brand .logo-wrap .logo-text .abbr {{ color: var(--c4); }}
    .footer-brand .logo-wrap .logo-text .full {{ color: var(--c5); }}
    .footer-brand p {{ font-size: 0.87rem; line-height: 1.8; color: rgba(255,255,255,0.6); }}
    .footer-col h4 {{
      font-size: 0.9rem;
      font-weight: 700;
      color: white;
      margin-bottom: 16px;
      padding-bottom: 10px;
      border-bottom: 1px solid rgba(255,255,255,0.1);
    }}
    .footer-col ul {{ list-style: none; }}
    .footer-col ul li {{ margin-bottom: 10px; }}
    .footer-col ul li a {{
      color: rgba(255,255,255,0.6);
      text-decoration: none;
      font-size: 0.87rem;
      transition: color 0.2s;
    }}
    .footer-col ul li a:hover {{ color: var(--c4); }}
    .footer-bottom {{
      max-width: 1280px;
      margin: 0 auto;
      padding: 24px 24px 0;
      border-top: 1px solid rgba(255,255,255,0.1);
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 12px;
    }}
    .footer-bottom p {{ font-size: 0.82rem; color: rgba(255,255,255,0.4); }}
    .footer-social {{ display: flex; gap: 12px; }}
    .social-btn {{
      width: 36px;
      height: 36px;
      background: rgba(255,255,255,0.08);
      border-radius: 8px;
      display: flex;
      align-items: center;
      justify-content: center;
      color: rgba(255,255,255,0.6);
      text-decoration: none;
      font-size: 1rem;
      transition: all 0.2s;
    }}
    .social-btn:hover {{ background: var(--c3); color: white; }}

    /* ── SCROLL ANIMATIONS ──────────────────────────────────── */
    .fade-up {{
      opacity: 0;
      transform: translateY(30px);
      transition: opacity 0.6s ease, transform 0.6s ease;
    }}
    .fade-up.visible {{
      opacity: 1;
      transform: translateY(0);
    }}
    .fade-up-delay-1 {{ transition-delay: 0.1s; }}
    .fade-up-delay-2 {{ transition-delay: 0.2s; }}
    .fade-up-delay-3 {{ transition-delay: 0.3s; }}
    .fade-up-delay-4 {{ transition-delay: 0.4s; }}

    /* ── MOBILE NAV ─────────────────────────────────────────── */
    .mobile-nav {{
      display: none;
      position: fixed;
      top: 0;
      left: 0;
      right: 0;
      bottom: 0;
      background: rgba(26,58,92,0.97);
      z-index: 2000;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      gap: 24px;
      backdrop-filter: blur(12px);
    }}
    .mobile-nav.open {{ display: flex; }}
    .mobile-nav a {{
      color: white;
      text-decoration: none;
      font-size: 1.4rem;
      font-weight: 700;
      transition: color 0.2s;
    }}
    .mobile-nav a:hover {{ color: var(--c9); }}
    .mobile-nav .close-btn {{
      position: absolute;
      top: 24px;
      right: 24px;
      background: none;
      border: none;
      color: white;
      font-size: 2rem;
      cursor: pointer;
    }}

    /* ── RESPONSIVE ─────────────────────────────────────────── */
    @media (max-width: 1024px) {{
      .features-grid {{ grid-template-columns: repeat(2, 1fr); }}
      .adhd-grid {{ grid-template-columns: repeat(2, 1fr); }}
      .footer-grid {{ grid-template-columns: 1fr 1fr; }}
    }}
    @media (max-width: 768px) {{
      .nav-links {{ display: none; }}
      .hamburger {{ display: flex; }}
      .hero .inner {{ grid-template-columns: 1fr; text-align: center; padding-top: 100px; }}
      .hero-visual {{ order: -1; }}
      .hero-actions {{ justify-content: center; }}
      .hero-stats {{ justify-content: center; }}
      .hero-desc {{ margin: 0 auto 36px; }}
      .about-grid {{ grid-template-columns: 1fr; }}
      .features-grid {{ grid-template-columns: 1fr; }}
      .adhd-grid {{ grid-template-columns: 1fr; }}
      .news-grid {{ grid-template-columns: 1fr; }}
      .contact-grid {{ grid-template-columns: 1fr; }}
      .footer-grid {{ grid-template-columns: 1fr; gap: 32px; }}
      .form-row {{ grid-template-columns: 1fr; }}
      section {{ padding: 64px 0; }}
    }}
  </style>
</head>
<body>

<!-- TOP BAR -->
<div class="top-bar">
  <div class="inner">
    <span>Construction Manager School — 온전히 회복된 사람이 세상을 세웁니다</span>
    <div>
      <a href="#contact">📞 문의하기</a>
      <a href="#enroll">📋 등록안내</a>
    </div>
  </div>
</div>

<!-- NAVBAR -->
<nav class="navbar" id="navbar">
  <div class="inner">
    <a href="#" class="logo-wrap">
      <img src="{logo_src}" alt="CMS Logo" />
      <div class="logo-text">
        <span class="abbr">CMS</span>
        <span class="full">Construction Manager School</span>
      </div>
    </a>
    <ul class="nav-links">
      <li class="active"><a href="#">홈</a></li>
      <li><a href="#about">학교소개</a></li>
      <li id="enroll"><a href="#enroll-section">등록안내</a></li>
      <li class="adhd"><a href="#adhd">ADHD특색교육</a></li>
      <li><a href="#news">교육정보</a></li>
      <li><a href="#school-life">학교생활</a></li>
      <li><a href="#contact" class="nav-cta">문의하기</a></li>
    </ul>
    <div class="hamburger" id="hamburger" onclick="openMobileNav()">
      <span></span><span></span><span></span>
    </div>
  </div>
</nav>

<!-- MOBILE NAV -->
<div class="mobile-nav" id="mobileNav">
  <button class="close-btn" onclick="closeMobileNav()">✕</button>
  <a href="#" onclick="closeMobileNav()">홈</a>
  <a href="#about" onclick="closeMobileNav()">학교소개</a>
  <a href="#enroll-section" onclick="closeMobileNav()">등록안내</a>
  <a href="#adhd" onclick="closeMobileNav()">ADHD특색교육</a>
  <a href="#news" onclick="closeMobileNav()">교육정보</a>
  <a href="#school-life" onclick="closeMobileNav()">학교생활</a>
  <a href="#contact" onclick="closeMobileNav()">문의하기</a>
</div>

<!-- HERO SECTION -->
<section class="hero" id="hero">
  <div class="hero-bg-pattern"></div>
  <div class="hero-particles" id="particles"></div>
  <div class="inner">
    <div class="hero-content fade-up">
      <div class="hero-badge">
        <span class="dot"></span>
        학교부적응 청소년 · ADHD 특색교육
      </div>
      <h1 class="hero-title">
        한 사람의 회복이<br />
        <span class="highlight">세상을 세웁니다</span>
      </h1>
      <p class="hero-subtitle">
        Construction Manager School
      </p>
      <p class="hero-desc">
        문제 가운데 있던 한 사람이 온전히 회복된 사람(Constructed House)이 되면,
        다른 사람들도 살릴 수 있는 <strong>Construction Manager</strong>가 됩니다.
        CMS는 그 CM을 키우는 학교입니다.
      </p>
      <div class="hero-actions">
        <a href="#about" class="btn-primary">학교 알아보기 →</a>
        <a href="#enroll-section" class="btn-secondary">등록 문의하기</a>
      </div>
      <div class="hero-stats">
        <div class="stat-item">
          <span class="stat-num">CM</span>
          <span class="stat-label">Construction Manager</span>
        </div>
        <div class="stat-item">
          <span class="stat-num">100%</span>
          <span class="stat-label">개인 맞춤 교육</span>
        </div>
        <div class="stat-item">
          <span class="stat-num">ADHD</span>
          <span class="stat-label">특색교육 전문</span>
        </div>
      </div>
    </div>
    <div class="hero-visual fade-up fade-up-delay-2">
      <div class="hero-img-wrap">
        <img src="{hero_src}" alt="다양한 인종의 사람들이 모여 세계를 이루는 일러스트레이션" />
        <div class="hero-img-badge">
          <div class="icon">🏠</div>
          <div class="text">
            <div class="label">CMS Vision</div>
            <div class="value">Tenant → CM</div>
          </div>
        </div>
      </div>
    </div>
  </div>
  <div class="hero-scroll" onclick="document.getElementById('quote').scrollIntoView({{behavior:'smooth'}})">
    <span>아래로 스크롤</span>
    <div class="scroll-arrow">↓</div>
  </div>
</section>

<!-- QUOTE BAND -->
<div class="quote-band" id="quote">
  <div class="inner">
    <span class="quote-mark">"</span>
    <p class="quote-text">
      온전히 회복된 한 사람이<br />
      다른 이들의 집을 짓는 Construction Manager가 됩니다
    </p>
    <p class="quote-sub">— CMS 건학 이념 · 학교 부적응 청소년과 ADHD 학생을 위한 특색 있는 교육 —</p>
  </div>
</div>

<!-- FEATURE CARDS -->
<section class="features" id="features">
  <div class="section-inner">
    <div class="section-header center fade-up">
      <span class="section-tag">CMS 주요 프로그램</span>
      <h2 class="section-title">우리가 제공하는 교육</h2>
      <p class="section-desc">학교 부적응 청소년과 ADHD 학생들이 자신만의 가능성을 발견하고 세상을 변화시키는 CM으로 성장할 수 있도록 돕습니다.</p>
    </div>
    <div class="features-grid">
      <div class="feature-card fade-up fade-up-delay-1">
        <div class="card-icon">🏫</div>
        <div class="card-title">학교소개</div>
        <div class="card-desc">CMS의 건학 이념과 교육 철학, 그리고 우리가 꿈꾸는 회복과 성장의 이야기를 소개합니다.</div>
        <a href="#about" class="card-link">자세히 보기 →</a>
      </div>
      <div class="feature-card fade-up fade-up-delay-2">
        <div class="card-icon">📋</div>
        <div class="card-title">등록안내</div>
        <div class="card-desc">입학 자격, 등록 절차, 필요 서류 등 CMS 입학에 관한 모든 정보를 안내해 드립니다.</div>
        <a href="#enroll-section" class="card-link">등록 알아보기 →</a>
      </div>
      <div class="feature-card adhd-card fade-up fade-up-delay-3">
        <div class="card-icon">🧠</div>
        <div class="card-title">ADHD 특색교육</div>
        <div class="card-desc">ADHD 학생들의 강점을 발견하고 개인 맞춤형 학습 환경을 제공하는 CMS만의 특별한 교육 프로그램입니다.</div>
        <a href="#adhd" class="card-link">특색교육 보기 →</a>
      </div>
      <div class="feature-card fade-up fade-up-delay-4">
        <div class="card-icon">🌍</div>
        <div class="card-title">교육정보 & 학교생활</div>
        <div class="card-desc">CMS의 다양한 교육 활동, 학교생활 모습, 그리고 학생들의 성장 이야기를 담았습니다.</div>
        <a href="#news" class="card-link">더 알아보기 →</a>
      </div>
    </div>
  </div>
</section>

<!-- ABOUT SECTION -->
<section class="about" id="about">
  <div class="section-inner">
    <div class="about-grid">
      <div class="about-content fade-up">
        <span class="section-tag">학교소개</span>
        <h2 class="section-title">CMS는 어떤 학교인가요?</h2>
        <p class="section-desc">
          Construction Manager School은 학교 부적응 청소년, ADHD 학생, 그리고 다양한 어려움 속에 있는 청소년들이
          온전히 회복되어 다른 이들을 세우는 <strong>Construction Manager(CM)</strong>로 성장하는 것을 돕는 학교입니다.
          Tenant(세입자)가 아닌 CM이 되는 여정, CMS가 함께합니다.
        </p>
        <div class="about-values">
          <div class="value-item">
            <div class="value-icon">🏠</div>
            <div class="value-text">
              <div class="vt">회복 (Restoration)</div>
              <div class="vd">문제 가운데 있던 사람이 온전히 회복된 Constructed House가 되는 과정을 지원합니다.</div>
            </div>
          </div>
          <div class="value-item">
            <div class="value-icon">🤝</div>
            <div class="value-text">
              <div class="vt">연결 (Connection)</div>
              <div class="vd">흑인, 백인, 다양한 인종과 배경의 학생들이 함께 모여 서로를 세우는 공동체를 만듭니다.</div>
            </div>
          </div>
          <div class="value-item">
            <div class="value-icon">🌏</div>
            <div class="value-text">
              <div class="vt">영향력 (Impact)</div>
              <div class="vd">회복된 한 사람의 영향력이 원을 이루고, 그 원이 퍼져 세계를 변화시킵니다.</div>
            </div>
          </div>
        </div>
      </div>
      <div class="about-visual fade-up fade-up-delay-2">
        <div class="about-card-stack">
          <div class="about-card">
            <div class="about-card-title">교육 목표</div>
            <ul class="about-list">
              <li>자기 자신을 이해하고 수용하는 사람</li>
              <li>어려움을 강점으로 전환하는 회복력 있는 사람</li>
              <li>다른 사람의 집을 지을 수 있는 Construction Manager</li>
              <li>다양성을 존중하고 세상에 영향력을 미치는 사람</li>
            </ul>
          </div>
          <div class="about-card about-card-2">
            <div class="about-card-title">핵심 가치</div>
            <ul class="about-list">
              <li>모든 학생은 고유한 가능성을 가지고 있다</li>
              <li>회복은 배움의 시작이다</li>
              <li>다름은 약점이 아닌 강점이다</li>
              <li>한 사람의 변화가 세상을 바꾼다</li>
            </ul>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- ADHD SPECIAL EDUCATION -->
<section class="adhd-section" id="adhd">
  <div class="section-inner">
    <div class="adhd-header fade-up">
      <div>
        <div class="adhd-badge">🧠 ADHD 특색교육</div>
        <h2 class="section-title">ADHD는 다름입니다, 약점이 아닙니다</h2>
        <p class="section-desc">CMS는 ADHD 학생들의 독특한 사고방식과 에너지를 강점으로 전환하는 특별한 교육 환경을 제공합니다.</p>
      </div>
      <a href="#contact" class="btn-primary" style="flex-shrink:0;">상담 신청하기 →</a>
    </div>
    <div class="adhd-grid">
      <div class="adhd-card fade-up fade-up-delay-1">
        <div class="adhd-card-top"></div>
        <div class="adhd-card-body">
          <div class="adhd-card-num">01</div>
          <div class="adhd-card-title">개인 맞춤형 학습 계획</div>
          <div class="adhd-card-desc">각 학생의 주의력 패턴, 학습 스타일, 강점을 분석하여 개인에게 최적화된 학습 계획을 수립합니다. 획일적인 교육이 아닌, 나만을 위한 교육입니다.</div>
          <span class="adhd-card-tag">개별화 교육</span>
        </div>
      </div>
      <div class="adhd-card fade-up fade-up-delay-2">
        <div class="adhd-card-top"></div>
        <div class="adhd-card-body">
          <div class="adhd-card-num">02</div>
          <div class="adhd-card-title">감각통합 & 움직임 기반 학습</div>
          <div class="adhd-card-desc">ADHD 학생들에게 효과적인 움직임 기반 학습, 감각통합 활동, 마음챙김 훈련을 통해 집중력과 자기조절 능력을 향상시킵니다.</div>
          <span class="adhd-card-tag">감각통합 치료</span>
        </div>
      </div>
      <div class="adhd-card fade-up fade-up-delay-3">
        <div class="adhd-card-top"></div>
        <div class="adhd-card-body">
          <div class="adhd-card-num">03</div>
          <div class="adhd-card-title">강점 발견 & 진로 탐색</div>
          <div class="adhd-card-desc">ADHD의 창의성, 과집중력, 독창적 사고를 강점으로 활용하여 학생 고유의 재능을 발견하고 미래 진로를 함께 설계합니다.</div>
          <span class="adhd-card-tag">강점 기반 교육</span>
        </div>
      </div>
      <div class="adhd-card fade-up fade-up-delay-1">
        <div class="adhd-card-top"></div>
        <div class="adhd-card-body">
          <div class="adhd-card-num">04</div>
          <div class="adhd-card-title">소규모 집중 지원 환경</div>
          <div class="adhd-card-desc">소규모 학급 운영으로 교사 1인당 학생 비율을 낮추어 개별 학생에게 충분한 관심과 지원을 제공합니다.</div>
          <span class="adhd-card-tag">소규모 학급</span>
        </div>
      </div>
      <div class="adhd-card fade-up fade-up-delay-2">
        <div class="adhd-card-top"></div>
        <div class="adhd-card-body">
          <div class="adhd-card-num">05</div>
          <div class="adhd-card-title">가족 연계 상담 프로그램</div>
          <div class="adhd-card-desc">학생뿐 아니라 가족 전체가 ADHD를 이해하고 함께 성장할 수 있도록 부모 교육 및 가족 상담 프로그램을 운영합니다.</div>
          <span class="adhd-card-tag">가족 지원</span>
        </div>
      </div>
      <div class="adhd-card fade-up fade-up-delay-3">
        <div class="adhd-card-top"></div>
        <div class="adhd-card-body">
          <div class="adhd-card-num">06</div>
          <div class="adhd-card-title">사회성 & 정서 발달 프로그램</div>
          <div class="adhd-card-desc">또래 관계, 감정 조절, 자존감 향상을 위한 그룹 활동과 개인 상담을 통해 건강한 사회적 관계를 형성하도록 돕습니다.</div>
          <span class="adhd-card-tag">정서 발달</span>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- ENROLLMENT SECTION -->
<section class="features" id="enroll-section" style="background: var(--c6);">
  <div class="section-inner">
    <div class="section-header center fade-up">
      <span class="section-tag">등록안내</span>
      <h2 class="section-title">CMS 입학 안내</h2>
      <p class="section-desc">학교 부적응 청소년, ADHD 학생, 그리고 새로운 교육 환경이 필요한 모든 청소년을 환영합니다.</p>
    </div>
    <div class="features-grid">
      <div class="feature-card fade-up fade-up-delay-1" style="background: white;">
        <div class="card-icon" style="font-size: 2.5rem;">📅</div>
        <div class="card-title">입학 시기</div>
        <div class="card-desc">수시 모집으로 연중 입학이 가능합니다. 학기 중에도 전입이 가능하며, 개인 상황에 맞춰 유연하게 시작할 수 있습니다.</div>
      </div>
      <div class="feature-card fade-up fade-up-delay-2" style="background: white;">
        <div class="card-icon" style="font-size: 2.5rem;">📝</div>
        <div class="card-title">지원 자격</div>
        <div class="card-desc">중학교 및 고등학교 과정 청소년 누구나 지원 가능합니다. 학교 부적응, ADHD, 학습 어려움을 겪는 학생들을 우선 지원합니다.</div>
      </div>
      <div class="feature-card fade-up fade-up-delay-3" style="background: white;">
        <div class="card-icon" style="font-size: 2.5rem;">🗂️</div>
        <div class="card-title">제출 서류</div>
        <div class="card-desc">입학 신청서, 학교생활기록부, 건강기록부 등 기본 서류와 함께 상담 신청서를 제출하시면 됩니다. 자세한 안내는 문의 주세요.</div>
      </div>
      <div class="feature-card fade-up fade-up-delay-4" style="background: white;">
        <div class="card-icon" style="font-size: 2.5rem;">💬</div>
        <div class="card-title">입학 상담</div>
        <div class="card-desc">입학 전 1:1 상담을 통해 학생의 상황을 파악하고 최적의 교육 계획을 함께 수립합니다. 부담 없이 문의해 주세요.</div>
      </div>
    </div>
  </div>
</section>

<!-- NEWS / EDUCATION INFO -->
<section class="news-section" id="news">
  <div class="section-inner">
    <div class="section-header fade-up">
      <span class="section-tag">교육정보 & 학교생활</span>
      <h2 class="section-title">CMS의 이야기</h2>
      <p class="section-desc">학생들의 성장과 변화, 그리고 CMS의 다양한 교육 활동을 소개합니다.</p>
    </div>
    <div class="news-grid" id="school-life">
      <div class="news-card fade-up fade-up-delay-1">
        <div class="news-card-img" style="background: linear-gradient(135deg, #BEE3F8, #90CDF4); font-size: 4rem;">🌱</div>
        <div class="news-card-body">
          <span class="news-category">학교생활</span>
          <div class="news-title">회복의 여정 — 한 학생의 변화 이야기</div>
          <div class="news-excerpt">학교 부적응으로 힘들었던 한 학생이 CMS에서 자신만의 강점을 발견하고 CM으로 성장해가는 이야기를 담았습니다.</div>
          <div class="news-meta">📅 2025년 3월 · CMS 교육팀</div>
        </div>
      </div>
      <div class="news-card fade-up fade-up-delay-2">
        <div class="news-card-img" style="background: linear-gradient(135deg, #C6F6D5, #9AE6B4); font-size: 4rem;">🧠</div>
        <div class="news-card-body">
          <span class="news-category">ADHD 교육</span>
          <div class="news-title">ADHD 학생의 과집중력을 강점으로</div>
          <div class="news-excerpt">ADHD의 특성인 과집중력을 활용한 프로젝트 기반 학습 사례와 그 효과에 대해 소개합니다.</div>
          <div class="news-meta">📅 2025년 2월 · 특색교육팀</div>
        </div>
      </div>
      <div class="news-card fade-up fade-up-delay-3">
        <div class="news-card-img" style="background: linear-gradient(135deg, #FEF3C7, #FDE68A); font-size: 4rem;">🌍</div>
        <div class="news-card-body">
          <span class="news-category">교육정보</span>
          <div class="news-title">다양성 교육 — 우리가 함께 이루는 세계</div>
          <div class="news-excerpt">다양한 배경을 가진 학생들이 서로를 이해하고 함께 성장하는 CMS의 다양성 교육 프로그램을 소개합니다.</div>
          <div class="news-meta">📅 2025년 1월 · CMS 교육팀</div>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- CTA BAND -->
<div class="cta-band">
  <div class="inner">
    <h2>지금, 새로운 시작을 함께하세요</h2>
    <p>CMS는 모든 학생의 가능성을 믿습니다.<br />어떤 어려움 속에 있더라도, 회복과 성장의 여정은 시작될 수 있습니다.</p>
    <div class="cta-actions">
      <a href="#contact" class="btn-white">📞 무료 상담 신청</a>
      <a href="#about" class="btn-outline-white">학교 더 알아보기</a>
    </div>
  </div>
</div>

<!-- CONTACT SECTION -->
<section class="contact-section" id="contact">
  <div class="section-inner">
    <div class="section-header fade-up">
      <span class="section-tag">문의하기</span>
      <h2 class="section-title">언제든지 연락주세요</h2>
      <p class="section-desc">입학 상담, 교육 프로그램 문의, ADHD 특색교육에 관한 모든 질문에 친절히 답변해 드립니다.</p>
    </div>
    <div class="contact-grid">
      <div class="contact-info fade-up">
        <div class="contact-item">
          <div class="contact-icon">📍</div>
          <div class="contact-text">
            <div class="ct">주소</div>
            <div class="cv">서울특별시 (상세 주소 추후 안내)</div>
          </div>
        </div>
        <div class="contact-item">
          <div class="contact-icon">📞</div>
          <div class="contact-text">
            <div class="ct">전화</div>
            <div class="cv">02-000-0000</div>
          </div>
        </div>
        <div class="contact-item">
          <div class="contact-icon">✉️</div>
          <div class="contact-text">
            <div class="ct">이메일</div>
            <div class="cv">info@cmsschool.kr</div>
          </div>
        </div>
        <div class="contact-item">
          <div class="contact-icon">🕐</div>
          <div class="contact-text">
            <div class="ct">상담 시간</div>
            <div class="cv">평일 09:00 — 18:00<br />토요일 10:00 — 14:00</div>
          </div>
        </div>
      </div>
      <div class="contact-form fade-up fade-up-delay-2">
        <div class="form-title">📬 상담 신청서</div>
        <div class="form-row">
          <div class="form-group">
            <label>학생 이름</label>
            <input type="text" placeholder="이름을 입력하세요" />
          </div>
          <div class="form-group">
            <label>연락처</label>
            <input type="tel" placeholder="010-0000-0000" />
          </div>
        </div>
        <div class="form-group">
          <label>문의 유형</label>
          <select>
            <option value="">선택해 주세요</option>
            <option>입학 상담</option>
            <option>ADHD 특색교육 문의</option>
            <option>학교 부적응 상담</option>
            <option>교육 프로그램 문의</option>
            <option>기타 문의</option>
          </select>
        </div>
        <div class="form-group">
          <label>문의 내용</label>
          <textarea placeholder="문의하실 내용을 자유롭게 작성해 주세요. 학생의 현재 상황을 간략히 알려주시면 더 도움이 됩니다."></textarea>
        </div>
        <button class="form-submit" onclick="handleSubmit()">상담 신청하기 →</button>
      </div>
    </div>
  </div>
</section>

<!-- FOOTER -->
<footer>
  <div class="footer-grid">
    <div class="footer-brand">
      <a href="#" class="logo-wrap" style="margin-bottom: 16px; display: flex;">
        <img src="{logo_src}" alt="CMS Logo" style="height: 44px; filter: brightness(0) invert(1) opacity(0.8);" />
        <div class="logo-text">
          <span class="abbr" style="color: #90CDF4;">CMS</span>
          <span class="full" style="color: #63B3ED;">Construction Manager School</span>
        </div>
      </a>
      <p>온전히 회복된 한 사람이 세상을 세웁니다.<br />Tenant가 아닌 Construction Manager를 키우는 학교, CMS입니다.</p>
    </div>
    <div class="footer-col">
      <h4>학교 안내</h4>
      <ul>
        <li><a href="#about">학교소개</a></li>
        <li><a href="#about">건학 이념</a></li>
        <li><a href="#about">교육 목표</a></li>
        <li><a href="#about">핵심 가치</a></li>
      </ul>
    </div>
    <div class="footer-col">
      <h4>교육 프로그램</h4>
      <ul>
        <li><a href="#adhd">ADHD 특색교육</a></li>
        <li><a href="#enroll-section">등록안내</a></li>
        <li><a href="#news">교육정보</a></li>
        <li><a href="#school-life">학교생활</a></li>
      </ul>
    </div>
    <div class="footer-col">
      <h4>지원 & 문의</h4>
      <ul>
        <li><a href="#contact">입학 상담</a></li>
        <li><a href="#contact">ADHD 상담</a></li>
        <li><a href="#contact">학교 부적응 상담</a></li>
        <li><a href="#contact">문의하기</a></li>
      </ul>
    </div>
  </div>
  <div class="footer-bottom">
    <p>© 2025 Construction Manager School (CMS). All rights reserved.</p>
    <div class="footer-social">
      <a href="#" class="social-btn">📘</a>
      <a href="#" class="social-btn">📸</a>
      <a href="#" class="social-btn">▶️</a>
    </div>
  </div>
</footer>

<script>
  // ── Navbar scroll effect
  const navbar = document.getElementById('navbar');
  window.addEventListener('scroll', () => {{
    if (window.scrollY > 50) navbar.classList.add('scrolled');
    else navbar.classList.remove('scrolled');
  }});

  // ── Scroll animations
  const observer = new IntersectionObserver((entries) => {{
    entries.forEach(entry => {{
      if (entry.isIntersecting) {{
        entry.target.classList.add('visible');
      }}
    }});
  }}, {{ threshold: 0.1 }});
  document.querySelectorAll('.fade-up').forEach(el => observer.observe(el));

  // ── Particle generator
  function createParticles() {{
    const container = document.getElementById('particles');
    for (let i = 0; i < 20; i++) {{
      const p = document.createElement('div');
      p.className = 'particle';
      const size = Math.random() * 8 + 4;
      p.style.cssText = `
        width: ${{size}}px;
        height: ${{size}}px;
        left: ${{Math.random() * 100}}%;
        animation-duration: ${{Math.random() * 15 + 10}}s;
        animation-delay: ${{Math.random() * 10}}s;
      `;
      container.appendChild(p);
    }}
  }}
  createParticles();

  // ── Mobile nav
  function openMobileNav() {{
    document.getElementById('mobileNav').classList.add('open');
    document.body.style.overflow = 'hidden';
  }}
  function closeMobileNav() {{
    document.getElementById('mobileNav').classList.remove('open');
    document.body.style.overflow = '';
  }}

  // ── Form submit
  function handleSubmit() {{
    const btn = document.querySelector('.form-submit');
    btn.textContent = '✅ 상담 신청이 완료되었습니다!';
    btn.style.background = 'linear-gradient(135deg, #38B2AC, #2C7A7B)';
    setTimeout(() => {{
      btn.textContent = '상담 신청하기 →';
      btn.style.background = '';
    }}, 3000);
  }}

  // ── Smooth active nav on scroll
  const sections = document.querySelectorAll('section[id], div[id]');
  const navLinks = document.querySelectorAll('.nav-links a');
  window.addEventListener('scroll', () => {{
    let current = '';
    sections.forEach(section => {{
      const sectionTop = section.offsetTop - 100;
      if (window.scrollY >= sectionTop) current = section.getAttribute('id');
    }});
  }});

  // ── Counter animation for stats
  function animateCounter(el, target, suffix) {{
    let start = 0;
    const duration = 2000;
    const step = target / (duration / 16);
    const timer = setInterval(() => {{
      start += step;
      if (start >= target) {{
        el.textContent = target + suffix;
        clearInterval(timer);
      }} else {{
        el.textContent = Math.floor(start) + suffix;
      }}
    }}, 16);
  }}
</script>
</body>
</html>"""

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("HTML file written successfully!")
print(f"File size: {{len(html):,}} characters")
