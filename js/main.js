/* Fieldline website concept v2: shared interactions */
(() => {
  const $ = (s, el = document) => el.querySelector(s);
  const $$ = (s, el = document) => [...el.querySelectorAll(s)];
  const reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  const desktop = window.matchMedia('(min-width: 1081px)');
  document.documentElement.classList.add('js');

  /* Year */
  $$('[data-year]').forEach(el => { el.textContent = new Date().getFullYear(); });

  /* Header shadow on scroll */
  const header = $('[data-header]');
  const onScroll = () => header && header.classList.toggle('is-scrolled', window.scrollY > 8);
  onScroll();
  window.addEventListener('scroll', onScroll, { passive: true });

  /* ---------- Navigation ---------- */
  const nav = $('[data-nav]');
  const toggle = $('[data-nav-toggle]');
  const triggers = $$('[data-mega-trigger]');
  let closeTimer;

  const closeAll = except => {
    triggers.forEach(t => {
      if (t === except) return;
      t.setAttribute('aria-expanded', 'false');
      const panel = document.getElementById(t.getAttribute('aria-controls'));
      panel && panel.classList.remove('is-open');
    });
  };
  const openMenu = t => {
    closeAll(t);
    t.setAttribute('aria-expanded', 'true');
    document.getElementById(t.getAttribute('aria-controls')).classList.add('is-open');
  };

  triggers.forEach(t => {
    const panel = document.getElementById(t.getAttribute('aria-controls'));
    t.addEventListener('click', () => {
      const open = t.getAttribute('aria-expanded') === 'true';
      open ? closeAll() : openMenu(t);
    });
    // Hover intent on desktop only
    const item = t.closest('.nav-item');
    item.addEventListener('mouseenter', () => { if (!desktop.matches) return; clearTimeout(closeTimer); openMenu(t); });
    item.addEventListener('mouseleave', () => { if (!desktop.matches) return; closeTimer = setTimeout(() => closeAll(), 160); });
    panel.addEventListener('keydown', e => {
      if (e.key === 'Escape') { closeAll(); t.focus(); }
    });
  });
  document.addEventListener('keydown', e => {
    if (e.key !== 'Escape') return;
    closeAll();
    if (nav && nav.classList.contains('is-open')) setMobile(false);
  });
  document.addEventListener('click', e => { if (desktop.matches && !e.target.closest('.nav-item')) closeAll(); });

  const setMobile = open => {
    toggle.setAttribute('aria-expanded', String(open));
    nav.classList.toggle('is-open', open);
    document.body.classList.toggle('nav-open', open);
    if (!open) closeAll();
  };
  toggle && toggle.addEventListener('click', () => setMobile(toggle.getAttribute('aria-expanded') !== 'true'));
  desktop.addEventListener('change', () => { setMobile(false); closeAll(); });

  /* ---------- Hero video ---------- */
  const video = $('[data-hero-video]');
  const vToggle = $('[data-video-toggle]');
  if (video) {
    if (reduceMotion) {
      video.removeAttribute('autoplay');
      video.pause();
    } else {
      const p = video.play();
      if (p && p.catch) p.catch(() => {});
    }
    const sync = () => {
      const paused = video.paused;
      if (vToggle) {
        vToggle.setAttribute('aria-pressed', String(paused));
        $('.visually-hidden', vToggle).textContent = paused ? 'Play background video' : 'Pause background video';
      }
    };
    video.addEventListener('play', sync);
    video.addEventListener('pause', sync);
    sync();
    vToggle && vToggle.addEventListener('click', () => { video.paused ? video.play() : video.pause(); });
  }
  // Any inline section videos: play when visible, pause when not
  const inlineVideos = $$('video[data-inview]');
  if (inlineVideos.length && 'IntersectionObserver' in window && !reduceMotion) {
    const vio = new IntersectionObserver(entries => {
      entries.forEach(en => { en.isIntersecting ? en.target.play().catch(() => {}) : en.target.pause(); });
    }, { threshold: 0.25 });
    inlineVideos.forEach(v => vio.observe(v));
  }

  /* ---------- Reveal on scroll ---------- */
  const reveals = $$('.reveal');
  if (reveals.length && 'IntersectionObserver' in window && !reduceMotion) {
    const io = new IntersectionObserver(entries => {
      entries.forEach(en => { if (en.isIntersecting) { en.target.classList.add('is-in'); io.unobserve(en.target); } });
    }, { rootMargin: '0px 0px 5% 0px', threshold: 0 });
    reveals.forEach(el => io.observe(el));
  } else {
    reveals.forEach(el => el.classList.add('is-in'));
  }

  /* ---------- Count-up stats ---------- */
  const counters = $$('[data-count]');
  const runCount = el => {
    const end = Number(el.dataset.count);
    const suffix = el.dataset.suffix || '';
    const dur = 1200; const start = performance.now();
    const tick = now => {
      const t = Math.min(1, (now - start) / dur);
      const eased = 1 - Math.pow(1 - t, 3);
      el.textContent = Math.round(end * eased).toLocaleString() + suffix;
      if (t < 1) requestAnimationFrame(tick);
    };
    requestAnimationFrame(tick);
  };
  if (counters.length) {
    if (reduceMotion || !('IntersectionObserver' in window)) {
      counters.forEach(el => { el.textContent = Number(el.dataset.count).toLocaleString() + (el.dataset.suffix || ''); });
    } else {
      const cio = new IntersectionObserver(entries => {
        entries.forEach(en => { if (en.isIntersecting) { runCount(en.target); cio.unobserve(en.target); } });
      }, { threshold: 0.6 });
      counters.forEach(el => cio.observe(el));
    }
  }

  /* ---------- Tabs ---------- */
  $$('[data-tabs]').forEach(root => {
    const tabs = $$('[role="tab"]', root);
    const select = (tab, focus) => {
      tabs.forEach(t => {
        const on = t === tab;
        t.setAttribute('aria-selected', String(on));
        t.tabIndex = on ? 0 : -1;
        const panel = document.getElementById(t.getAttribute('aria-controls'));
        panel.hidden = !on;
        const v = $('video', panel);
        if (v && !reduceMotion) { on ? v.play().catch(() => {}) : v.pause(); }
      });
      if (focus) tab.focus();
    };
    tabs.forEach((t, i) => {
      t.addEventListener('click', () => select(t));
      t.addEventListener('keydown', e => {
        const horiz = !window.matchMedia('(min-width: 901px)').matches;
        const next = horiz ? 'ArrowRight' : 'ArrowDown';
        const prev = horiz ? 'ArrowLeft' : 'ArrowUp';
        if (e.key === next) { e.preventDefault(); select(tabs[(i + 1) % tabs.length], true); }
        if (e.key === prev) { e.preventDefault(); select(tabs[(i - 1 + tabs.length) % tabs.length], true); }
        if (e.key === 'Home') { e.preventDefault(); select(tabs[0], true); }
        if (e.key === 'End') { e.preventDefault(); select(tabs[tabs.length - 1], true); }
      });
    });
  });

  /* ---------- Blog filter ---------- */
  $$('[data-filter]').forEach(bar => {
    const chips = $$('.chip', bar);
    const items = $$(bar.dataset.filter);
    chips.forEach(c => c.addEventListener('click', () => {
      chips.forEach(x => x.setAttribute('aria-pressed', String(x === c)));
      const cat = c.dataset.cat;
      items.forEach(it => { it.hidden = cat !== 'all' && it.dataset.cat !== cat; });
    }));
  });

  /* ---------- Forms (demo only: validates, then shows a confirmation) ---------- */
  $$('form[data-demo-form]').forEach(form => {
    form.addEventListener('submit', e => {
      e.preventDefault();
      let firstBad = null;
      $$('[required]', form).forEach(input => {
        const field = input.closest('.field');
        const bad = !input.value.trim() || (input.type === 'email' && !/^\S+@\S+\.\S+$/.test(input.value));
        field.classList.toggle('has-error', bad);
        input.setAttribute('aria-invalid', String(bad));
        if (bad && !firstBad) firstBad = input;
      });
      if (firstBad) { firstBad.focus(); return; }
      form.classList.add('is-sent');
      const ok = $('.form-success', form);
      ok.setAttribute('tabindex', '-1');
      ok.focus();
    });
  });

  /* ---------- Investigation demo ---------- */
  const demo = $('[data-demo]');
  if (!demo) return;

  const DATA = {
    regions: [
      { name: 'North', margin: 28.4, change: 0.6 },
      { name: 'Central', margin: 24.1, change: -2.1, outlier: true },
      { name: 'South', margin: 27.2, change: 0.2 },
      { name: 'East', margin: 26.8, change: -0.3 }
    ],
    routes: [
      { name: 'Route 11', margin: 25.9, change: -0.4 },
      { name: 'Route 12', margin: 25.2, change: -0.8 },
      { name: 'Route 14', margin: 19.6, change: -6.3, outlier: true },
      { name: 'Route 17', margin: 24.8, change: -0.9 }
    ],
    drivers: [
      { name: 'Promotion depth on 12-packs', impact: -3.4 },
      { name: 'Cost-to-serve from new low-volume stops', impact: -2.2 },
      { name: 'Other', impact: -1.0 },
      { name: 'List price', impact: 0.0 },
      { name: 'Product mix', impact: 0.3 }
    ],
    note: 'The 12-pack promotion ran two weeks longer on Route 14 than planned, and three low-volume stops were added in August. Review promotion end dates and stop consolidation with the route team.'
  };
  const LEVELS = [
    { crumbs: ['All regions'], title: 'Gross margin by region', sub: 'Last 13 weeks, change vs. last year', prompt: 'Central is down 2.1 points while the other regions held steady. Select Central to follow the question.' },
    { crumbs: ['All regions', 'Central'], title: 'Gross margin by route, Central region', sub: 'Last 13 weeks, change vs. last year', prompt: 'Route 14 accounts for most of the drop. Select it to see what is driving the change.' },
    { crumbs: ['All regions', 'Central', 'Route 14'], title: 'What changed on Route 14', sub: 'Contribution to margin change, in points', prompt: 'Promotion depth and cost-to-serve explain most of the 6.3-point drop. Now it\u2019s your call.' },
    { crumbs: ['All regions', 'Central', 'Route 14', 'Your note'], title: 'Apply what you know', sub: 'Add the context only your team has', prompt: 'The data showed where and why. You decide what happens next.' }
  ];

  const body = $('[data-demo-body]', demo);
  const title = $('[data-demo-title]', demo);
  const sub = $('[data-demo-sub]', demo);
  const prompt = $('[data-demo-prompt]', demo);
  const crumbs = $('[data-crumbs]', demo);
  const steps = $$('[data-step]');
  let level = 0;

  const fmt = c => `<small class="${c < -1 ? 'neg' : ''}">${c > 0 ? '+' : ''}${c.toFixed(1)} pts</small>`;
  const barRows = rows => `<div class="bars">${rows.map(r => {
    const tag = r.outlier ? 'button' : 'div';
    const attrs = r.outlier ? `type="button" data-drill aria-label="${r.name}, ${r.margin}% margin, ${r.change} points. Drill in."` : '';
    return `<${tag} class="bar-row${r.outlier ? ' is-outlier' : ''}" ${attrs}>
      <span class="bar-label">${r.name}</span>
      <span class="bar-track"><span class="bar-fill" style="--w:${(r.margin / 30 * 100).toFixed(1)}%"></span></span>
      <span class="bar-value"><b>${r.margin.toFixed(1)}%</b>${fmt(r.change)}</span></${tag}>`;
  }).join('')}</div>`;
  const driverRows = rows => `<div class="drivers">${rows.map(d => {
    const pct = Math.min(Math.abs(d.impact) / 4, 1) * 50;
    const style = d.impact < 0 ? `right:50%;width:${pct}%` : `left:50%;width:${pct}%`;
    return `<div class="driver"><span>${d.name}</span>
      <span class="driver-axis" aria-hidden="true"><span class="driver-fill${d.impact > 0 ? ' pos' : ''}" style="${style}"></span></span>
      <span class="driver-val">${d.impact > 0 ? '+' : ''}${d.impact.toFixed(1)}</span></div>`;
  }).join('')}</div>
  <div class="apply-actions"><button type="button" class="btn btn-primary" data-drill>Add your context</button></div>`;
  const applyView = () => `<div class="apply">
    <label for="demo-note">Note for the Monday route review</label>
    <textarea id="demo-note">${DATA.note}</textarea>
    <div class="apply-actions">
      <button type="button" class="btn btn-primary" data-share>Share with district manager</button>
      <button type="button" class="link-btn" data-restart>Start over</button>
      <span class="apply-status" data-status role="status"></span>
    </div></div>`;

  const render = focusBody => {
    const L = LEVELS[level];
    title.textContent = L.title; sub.textContent = L.sub; prompt.textContent = L.prompt;
    crumbs.innerHTML = L.crumbs.map((c, i) => i === L.crumbs.length - 1
      ? `<span aria-current="page">${c}</span>`
      : `<button type="button" data-goto="${i}">${c}</button><span class="sep" aria-hidden="true">/</span>`).join('');
    body.innerHTML = level === 0 ? barRows(DATA.regions) : level === 1 ? barRows(DATA.routes) : level === 2 ? driverRows(DATA.drivers) : applyView();
    steps.forEach((s, i) => i === level ? s.setAttribute('aria-current', 'step') : s.removeAttribute('aria-current'));
    if (!reduceMotion) {
      $$('.bar-fill', body).forEach(f => {
        const w = f.style.getPropertyValue('--w');
        f.style.setProperty('--w', '0%');
        requestAnimationFrame(() => requestAnimationFrame(() => f.style.setProperty('--w', w)));
      });
    }
    if (focusBody) { const t = $('[data-drill], textarea', body); t && t.focus({ preventScroll: true }); }
  };
  const go = (n, focusBody = true) => { level = Math.max(0, Math.min(3, n)); render(focusBody); };

  body.addEventListener('click', e => {
    if (e.target.closest('[data-drill]')) go(level + 1);
    if (e.target.closest('[data-restart]')) go(0);
    if (e.target.closest('[data-share]')) $('[data-status]', body).textContent = 'Shared with district manager';
  });
  crumbs.addEventListener('click', e => { const b = e.target.closest('[data-goto]'); if (b) go(Number(b.dataset.goto)); });
  steps.forEach(s => s.addEventListener('click', () => go(Number(s.dataset.step), false)));
  render(false);
})();
