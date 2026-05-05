<!DOCTYPE html>
<html lang="en" dir="ltr">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>Buhoor — Arabic Poetry Meter Classifier</title>
  <link href="https://fonts.googleapis.com/css2?family=Amiri:ital,wght@0,400;0,700;1,400&family=Playfair+Display:wght@400;700;900&family=JetBrains+Mono:wght@400;600&display=swap" rel="stylesheet"/>
  <style>
    :root {
      --ink: #1a1008;
      --parchment: #f5eed8;
      --parchment-dark: #ede4c8;
      --gold: #c9933a;
      --gold-light: #e8b96a;
      --gold-dim: #7a5820;
      --crimson: #8b1a1a;
      --sand: #d4bc8a;
      --deep: #2d1f0e;
      --text: #3d2b10;
      --muted: #7a6540;
    }

    *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

    body {
      background-color: var(--parchment);
      color: var(--text);
      font-family: 'Playfair Display', serif;
      min-height: 100vh;
      overflow-x: hidden;
      position: relative;
    }

    /* Parchment texture overlay */
    body::before {
      content: '';
      position: fixed;
      inset: 0;
      background-image:
        url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='400' height='400'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.75' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='400' height='400' filter='url(%23n)' opacity='0.04'/%3E%3C/svg%3E");
      pointer-events: none;
      z-index: 0;
    }

    .wrapper {
      position: relative;
      z-index: 1;
      max-width: 860px;
      margin: 0 auto;
      padding: 60px 32px 100px;
    }

    /* ── HEADER ── */
    .hero {
      text-align: center;
      padding: 60px 0 40px;
      border-bottom: 2px solid var(--sand);
      position: relative;
    }

    .hero::before, .hero::after {
      content: '✦';
      color: var(--gold);
      font-size: 1.4rem;
      position: absolute;
      bottom: -0.75rem;
      background: var(--parchment);
      padding: 0 12px;
    }
    .hero::before { left: 50%; transform: translateX(-50%); }

    .arabic-title {
      font-family: 'Amiri', serif;
      font-size: clamp(2.8rem, 7vw, 5rem);
      color: var(--gold);
      line-height: 1.1;
      letter-spacing: 0.02em;
      text-shadow: 2px 3px 0 var(--gold-dim), 0 0 40px rgba(201,147,58,0.15);
      animation: fadeDown 0.9s ease both;
    }

    .latin-title {
      font-size: clamp(1rem, 2.5vw, 1.4rem);
      color: var(--muted);
      letter-spacing: 0.25em;
      text-transform: uppercase;
      margin-top: 10px;
      animation: fadeDown 0.9s 0.15s ease both;
      font-weight: 400;
    }

    .tagline {
      font-family: 'Amiri', serif;
      font-style: italic;
      color: var(--gold-dim);
      font-size: 1.15rem;
      margin-top: 18px;
      animation: fadeDown 0.9s 0.3s ease both;
    }

    @keyframes fadeDown {
      from { opacity: 0; transform: translateY(-18px); }
      to   { opacity: 1; transform: translateY(0); }
    }

    /* ── DIVIDERS ── */
    .ornament {
      text-align: center;
      color: var(--gold);
      font-size: 1.2rem;
      letter-spacing: 0.6em;
      margin: 48px 0;
      opacity: 0.6;
    }

    /* ── SECTIONS ── */
    section {
      margin-bottom: 56px;
      animation: fadeUp 0.7s ease both;
    }

    @keyframes fadeUp {
      from { opacity: 0; transform: translateY(22px); }
      to   { opacity: 1; transform: translateY(0); }
    }

    .section-label {
      display: flex;
      align-items: center;
      gap: 12px;
      margin-bottom: 24px;
    }

    .section-label::before, .section-label::after {
      content: '';
      flex: 1;
      height: 1px;
      background: linear-gradient(to right, transparent, var(--sand));
    }
    .section-label::after {
      background: linear-gradient(to left, transparent, var(--sand));
    }

    .section-label h2 {
      font-size: 0.75rem;
      letter-spacing: 0.35em;
      text-transform: uppercase;
      color: var(--gold);
      white-space: nowrap;
      font-family: 'Playfair Display', serif;
      font-weight: 700;
    }

    /* ── WHY BUHOOR ── */
    .intro-text {
      font-family: 'Amiri', serif;
      font-size: 1.18rem;
      line-height: 1.9;
      color: var(--text);
      margin-bottom: 28px;
    }

    .steps-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
      gap: 16px;
      margin: 28px 0;
    }

    .step-card {
      background: var(--parchment-dark);
      border: 1px solid var(--sand);
      border-top: 3px solid var(--gold);
      padding: 20px 18px;
      border-radius: 2px;
      transition: transform 0.25s, box-shadow 0.25s;
    }

    .step-card:hover {
      transform: translateY(-4px);
      box-shadow: 0 8px 24px rgba(42, 22, 0, 0.12);
    }

    .step-num {
      font-family: 'JetBrains Mono', monospace;
      font-size: 0.7rem;
      color: var(--gold);
      letter-spacing: 0.2em;
      margin-bottom: 8px;
    }

    .step-arabic {
      font-family: 'Amiri', serif;
      font-size: 1rem;
      color: var(--crimson);
      margin-bottom: 4px;
      direction: rtl;
    }

    .step-desc {
      font-size: 0.82rem;
      color: var(--muted);
      line-height: 1.6;
    }

    .highlight-box {
      background: linear-gradient(135deg, var(--deep), #3d2008);
      color: var(--gold-light);
      padding: 22px 28px;
      border-radius: 2px;
      font-family: 'Amiri', serif;
      font-size: 1.1rem;
      line-height: 1.75;
      border-left: 4px solid var(--gold);
      margin-top: 20px;
    }

    /* ── VIDEO ── */
    .video-wrap {
      position: relative;
      border-radius: 4px;
      overflow: hidden;
      border: 2px solid var(--sand);
      box-shadow: 0 12px 40px rgba(42, 22, 0, 0.2), 0 0 0 6px var(--parchment-dark);
    }

    .video-wrap video {
      width: 100%;
      display: block;
    }

    /* ── MODEL OVERVIEW ── */
    .arch-list {
      list-style: none;
      display: flex;
      flex-direction: column;
      gap: 12px;
    }

    .arch-list li {
      display: flex;
      align-items: flex-start;
      gap: 14px;
      background: var(--parchment-dark);
      border: 1px solid var(--sand);
      padding: 16px 20px;
      border-radius: 2px;
    }

    .arch-icon {
      font-size: 1.3rem;
      flex-shrink: 0;
      margin-top: 2px;
    }

    .arch-label {
      font-family: 'JetBrains Mono', monospace;
      font-size: 0.82rem;
      color: var(--gold);
      font-weight: 600;
      margin-bottom: 3px;
    }

    .arch-desc {
      font-size: 0.88rem;
      color: var(--muted);
      line-height: 1.6;
    }

    /* ── ACCURACY ── */
    .accuracy-block {
      text-align: center;
      padding: 40px 20px;
      background: linear-gradient(135deg, var(--deep), #3d2008);
      border-radius: 4px;
      border: 1px solid var(--gold-dim);
    }

    .accuracy-num {
      font-size: clamp(3.5rem, 10vw, 6rem);
      font-weight: 900;
      color: var(--gold);
      line-height: 1;
      text-shadow: 0 0 40px rgba(201,147,58,0.4);
      letter-spacing: -0.02em;
    }

    .accuracy-label {
      color: var(--sand);
      font-size: 0.9rem;
      letter-spacing: 0.3em;
      text-transform: uppercase;
      margin-top: 10px;
    }

    .accuracy-sub {
      font-family: 'Amiri', serif;
      font-style: italic;
      color: var(--gold-dim);
      margin-top: 14px;
      font-size: 1rem;
    }

    /* ── CODE ── */
    pre {
      background: var(--ink);
      color: #e8d5a3;
      font-family: 'JetBrains Mono', monospace;
      font-size: 0.82rem;
      padding: 28px 32px;
      border-radius: 2px;
      overflow-x: auto;
      line-height: 1.8;
      border-left: 3px solid var(--gold);
      position: relative;
    }

    pre .comment { color: var(--gold-dim); }
    pre .cmd { color: var(--gold-light); }

    .copy-btn {
      position: absolute;
      top: 12px;
      right: 12px;
      background: var(--gold-dim);
      color: var(--parchment);
      border: none;
      padding: 5px 12px;
      font-family: 'JetBrains Mono', monospace;
      font-size: 0.7rem;
      border-radius: 2px;
      cursor: pointer;
      letter-spacing: 0.1em;
      transition: background 0.2s;
    }
    .copy-btn:hover { background: var(--gold); }

    /* ── DATASET BADGE ── */
    .dataset-card {
      display: flex;
      align-items: center;
      gap: 20px;
      background: var(--parchment-dark);
      border: 1px solid var(--sand);
      padding: 22px 26px;
      border-radius: 2px;
    }

    .dataset-icon { font-size: 2.4rem; flex-shrink: 0; }

    .dataset-title {
      font-family: 'Amiri', serif;
      font-size: 1.2rem;
      color: var(--crimson);
      direction: rtl;
    }

    .dataset-sub {
      font-size: 0.84rem;
      color: var(--muted);
      margin-top: 4px;
    }

    /* ── FOOTER ── */
    footer {
      text-align: center;
      padding-top: 48px;
      border-top: 1px solid var(--sand);
      color: var(--muted);
      font-family: 'Amiri', serif;
      font-size: 0.95rem;
      font-style: italic;
    }

    footer a {
      color: var(--gold);
      text-decoration: none;
    }
    footer a:hover { text-decoration: underline; }
  </style>
</head>
<body>
<div class="wrapper">

  <!-- HERO -->
  <header class="hero">
    <div class="arabic-title">بُحور</div>
    <div class="latin-title">Buhoor · Arabic Poetry Meter Classifier</div>
    <div class="tagline">An intelligent deep learning system that understands the rhythm of Arabic poetry.</div>
  </header>

  <div class="ornament">· · ✦ · ·</div>

  <!-- WHY BUHOOR -->
  <section>
    <div class="section-label"><h2>Why Buhoor?</h2></div>
    <p class="intro-text">
      Traditionally, identifying a poetic meter is a grueling manual process requiring four distinct stages of <strong>Prosody (علم العروض)</strong>:
    </p>

    <div class="steps-grid">
      <div class="step-card">
        <div class="step-num">STEP 01</div>
        <div class="step-arabic">الكتابة العروضية</div>
        <div class="step-desc">Rewriting the verse phonetically — e.g., writing <em>Shaddah</em> as two separate letters.</div>
      </div>
      <div class="step-card">
        <div class="step-num">STEP 02</div>
        <div class="step-arabic">الترميز</div>
        <div class="step-desc">Mapping every single letter to a moving (/) or silent (o) stroke by hand.</div>
      </div>
      <div class="step-card">
        <div class="step-num">STEP 03</div>
        <div class="step-arabic">التفاعيل</div>
        <div class="step-desc">Deciphering how symbols group into rhythmic units like <em>Fa'ulun</em> or <em>Mustaf'ilun</em>.</div>
      </div>
      <div class="step-card">
        <div class="step-num">STEP 04</div>
        <div class="step-arabic">المطابقة</div>
        <div class="step-desc">Matching the resulting pattern against all 16 classical Arabic meters.</div>
      </div>
    </div>

    <div class="highlight-box">
      <strong>Buhoor eliminates this entire workflow.</strong> You simply enter the raw verse, and the deep learning model skips the manual encoding — instantly identifying the rhythm through its trained "musical ear."
    </div>
  </section>

  <!-- HOW IT WORKS -->
  <section>
    <div class="section-label"><h2>How It Works</h2></div>
    <p class="intro-text">
      The system reads the input verse as a sequence of characters and learns hidden patterns in Arabic poetic structure using a deep neural network. It then predicts the most likely meter from the 16 classical Arabic meters — <span style="font-family:'Amiri',serif; color:var(--crimson);">بحور الشعر</span>.
    </p>
  </section>

  <!-- DEMO VIDEO -->
  <section>
    <div class="section-label"><h2>Demo</h2></div>
    <div class="video-wrap">
      <video
        src="https://github.com/nashatfr/Buhoor/raw/main/assets/demo.mp4"
        autoplay
        muted
        loop
        playsinline
        controls
      ></video>
    </div>
  </section>

  <!-- MODEL OVERVIEW -->
  <section>
    <div class="section-label"><h2>Model Architecture</h2></div>
    <ul class="arch-list">
      <li>
        <div class="arch-icon">🔤</div>
        <div>
          <div class="arch-label">Embedding Layer</div>
          <div class="arch-desc">Converts input characters into dense, meaningful vector representations that capture linguistic proximity.</div>
        </div>
      </li>
      <li>
        <div class="arch-icon">↔️</div>
        <div>
          <div class="arch-label">Bidirectional LSTM Layers</div>
          <div class="arch-desc">Capture the full poetic structure by reading each verse forwards and backwards simultaneously.</div>
        </div>
      </li>
      <li>
        <div class="arch-icon">⚖️</div>
        <div>
          <div class="arch-label">Layer Normalization + Dropout</div>
          <div class="arch-desc">Improve training stability and prevent overfitting to rare meter patterns.</div>
        </div>
      </li>
      <li>
        <div class="arch-icon">🎯</div>
        <div>
          <div class="arch-label">Dense Softmax Output</div>
          <div class="arch-desc">Outputs a probability distribution across all classical poetic meters for final classification.</div>
        </div>
      </li>
    </ul>
  </section>

  <!-- DATASET -->
  <section>
    <div class="section-label"><h2>Dataset</h2></div>
    <div class="dataset-card">
      <div class="dataset-icon">📚</div>
      <div>
        <div class="dataset-title">أشعار — Ashaar Dataset</div>
        <div class="dataset-sub">A curated collection of classical Arabic poetry used for learning and evaluating Arabic poetic meters.</div>
      </div>
    </div>
  </section>

  <!-- PERFORMANCE -->
  <section>
    <div class="section-label"><h2>Model Performance</h2></div>
    <div class="accuracy-block">
      <div class="accuracy-num">94.96%</div>
      <div class="accuracy-label">Test Accuracy</div>
      <div class="accuracy-sub">Evaluated on a held-out test set — reliably classifying Arabic poetic meters across diverse verse patterns.</div>
    </div>
  </section>

  <!-- TRY IT -->
  <section>
    <div class="section-label"><h2>Try It Yourself</h2></div>
    <p class="intro-text">
      Run the Streamlit app locally and enter your favorite Arabic verses — <span style="font-family:'Amiri',serif; color:var(--crimson);">بيوت شعرية</span> — to see the predicted meter instantly.
    </p>
    <div style="position:relative;">
      <pre id="codeblock"><span class="comment"># Clone the repository</span>
<span class="cmd">git clone</span> https://github.com/nashatfr/Buhoor.git

<span class="comment"># Install dependencies</span>
<span class="cmd">pip install</span> -r requirements.txt

<span class="comment"># Launch the app</span>
<span class="cmd">streamlit run</span> app.py</pre>
      <button class="copy-btn" onclick="copyCode()">COPY</button>
    </div>
  </section>

  <div class="ornament">· · ✦ · ·</div>

  <footer>
    <p>Built with care for the beauty of Arabic poetry &nbsp;·&nbsp; <a href="https://github.com/nashatfr/Buhoor" target="_blank">github.com/nashatfr/Buhoor</a></p>
  </footer>

</div>

<script>
  function copyCode() {
    const code = `# Clone the repository
git clone https://github.com/nashatfr/Buhoor.git

# Install dependencies
pip install -r requirements.txt

# Launch the app
streamlit run app.py`;
    navigator.clipboard.writeText(code).then(() => {
      const btn = document.querySelector('.copy-btn');
      btn.textContent = 'COPIED!';
      setTimeout(() => btn.textContent = 'COPY', 2000);
    });
  }

  // Stagger section animations
  document.querySelectorAll('section').forEach((s, i) => {
    s.style.animationDelay = `${0.1 + i * 0.1}s`;
  });
</script>
</body>
</html>
