/* =========================================================
   TORNOMEC - Interações do site
   ========================================================= */
(function () {
  'use strict';

  /* ---- Header scroll state ---- */
  const header = document.querySelector('.header');
  const onScroll = () => {
    if (header) header.classList.toggle('scrolled', window.scrollY > 24);
    const top = document.querySelector('.to-top');
    if (top) top.classList.toggle('show', window.scrollY > 560);
  };
  onScroll();
  window.addEventListener('scroll', onScroll, { passive: true });

  /* ---- Mobile menu ---- */
  const toggle = document.querySelector('.nav-toggle');
  const menu = document.querySelector('.nav-menu');
  const backdrop = document.querySelector('.nav-backdrop');
  const setMenu = (open) => {
    if (!menu) return;
    menu.classList.toggle('open', open);
    toggle.classList.toggle('open', open);
    if (backdrop) backdrop.classList.toggle('show', open);
    document.body.style.overflow = open ? 'hidden' : '';
    toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
  };
  if (toggle) toggle.addEventListener('click', () => setMenu(!menu.classList.contains('open')));
  if (backdrop) backdrop.addEventListener('click', () => setMenu(false));
  document.querySelectorAll('.nav-link').forEach(l => l.addEventListener('click', () => setMenu(false)));
  document.addEventListener('keydown', e => { if (e.key === 'Escape') setMenu(false); });

  /* ---- Reveal on scroll ---- */
  const reveals = document.querySelectorAll('.reveal');
  if ('IntersectionObserver' in window && reveals.length) {
    const io = new IntersectionObserver((entries) => {
      entries.forEach(en => {
        if (en.isIntersecting) { en.target.classList.add('in'); io.unobserve(en.target); }
      });
    }, { threshold: 0.12, rootMargin: '0px 0px -40px 0px' });
    reveals.forEach(r => io.observe(r));
  } else {
    reveals.forEach(r => r.classList.add('in'));
  }

  /* ---- Footer year ---- */
  const yr = document.getElementById('year');
  if (yr) yr.textContent = new Date().getFullYear();

  /* ---- Category live search ---- */
  const search = document.getElementById('catSearch');
  if (search) {
    const cards = Array.from(document.querySelectorAll('.cat-card'));
    const empty = document.querySelector('.cat-empty');
    const norm = s => (s || '').toLowerCase().normalize('NFD').replace(/[̀-ͯ]/g, '');
    search.addEventListener('input', () => {
      const q = norm(search.value.trim());
      let shown = 0;
      cards.forEach(c => {
        const hit = norm(c.dataset.name + ' ' + c.textContent).includes(q);
        c.style.display = hit ? '' : 'none';
        if (hit) shown++;
      });
      if (empty) empty.style.display = shown ? 'none' : 'block';
    });
  }

  /* ---- Lightbox (gallery) ---- */
  const lb = document.querySelector('.lightbox');
  if (lb) {
    const lbImg = lb.querySelector('img');
    const lbCap = lb.querySelector('.lightbox__cap');
    const open = (src, cap) => {
      lbImg.src = src; lbCap.textContent = cap || ''; lb.classList.add('open');
      document.body.style.overflow = 'hidden';
    };
    const close = () => { lb.classList.remove('open'); document.body.style.overflow = ''; };
    document.querySelectorAll('.gal-item').forEach(it => {
      it.addEventListener('click', () => {
        const img = it.querySelector('img');
        const cap = it.querySelector('.gal-item__cap strong');
        open(img.src, cap ? cap.textContent : '');
      });
    });
    lb.addEventListener('click', e => { if (e.target === lb || e.target.classList.contains('lightbox__close')) close(); });
    document.addEventListener('keydown', e => { if (e.key === 'Escape') close(); });
  }

  /* ---- Contact form -> compose e-mail / WhatsApp ---- */
  const form = document.getElementById('contactForm');
  if (form) {
    const toast = (msg) => {
      const t = document.querySelector('.toast');
      if (!t) return;
      t.querySelector('span').textContent = msg;
      t.classList.add('show');
      setTimeout(() => t.classList.remove('show'), 4200);
    };
    const buildText = (d) => {
      return `Nome: ${d.nome}\nEmpresa: ${d.empresa || '-'}\nE-mail: ${d.email}\nTelefone: ${d.telefone || '-'}\nInteresse: ${d.assunto}\n\nMensagem:\n${d.mensagem}`;
    };
    form.addEventListener('submit', (e) => {
      e.preventDefault();
      const d = Object.fromEntries(new FormData(form).entries());
      if (!d.nome || !d.email || !d.mensagem) { toast('Preencha nome, e-mail e mensagem.'); return; }
      const subject = `Contato pelo site - ${d.assunto || 'Solicitação'}`;
      const body = buildText(d);
      const mailto = `mailto:contato@tornomec.com.br?subject=${encodeURIComponent(subject)}&body=${encodeURIComponent(body)}`;
      window.location.href = mailto;
      toast('Abrindo seu aplicativo de e-mail…');
    });

    const waBtn = document.getElementById('sendWhats');
    if (waBtn) waBtn.addEventListener('click', () => {
      const d = Object.fromEntries(new FormData(form).entries());
      if (!d.nome || !d.mensagem) { toast('Preencha pelo menos nome e mensagem.'); return; }
      const txt = `Olá, TORNOMEC!%0A%0A${encodeURIComponent(buildText(d))}`;
      window.open(`https://wa.me/553133828405?text=${txt}`, '_blank');
    });
  }
})();
