# -*- coding: utf-8 -*-
"""Generate sobre.html, produtos.html and contato.html reusing the icon sprite,
   header and footer blocks defined in index.html to guarantee consistency."""
import os, urllib.parse

os.chdir(os.path.dirname(os.path.abspath(__file__)))
src = open('index.html', encoding='utf-8').read()

def between(a, b):
    i = src.index(a); j = src.index(b)
    return src[i:j]

SPRITE = between('<!-- ===== ICON SPRITE ===== -->', '<!-- ===== HEADER ===== -->').rstrip() + "\n"
TAIL   = src[src.index('<!-- ===== FOOTER ====='):]  # footer + floats + scripts + </body></html>

ADDRESS = "Av. Senador Levindo Coelho, 1698, Distrito Industrial do Jatobá, Belo Horizonte - MG, 30664-006"
ADDR_Q  = urllib.parse.quote(ADDRESS)

def head(title, desc):
    return f'''<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="theme-color" content="#1d3c5e">
<link rel="icon" type="image/png" href="assets/img/favicon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@600;700;800&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/css/style.css">
</head>
<body>

'''

def header(active):
    def cls(name): return 'nav-link active' if name == active else 'nav-link'
    return f'''<!-- ===== HEADER ===== -->
<header class="header">
  <div class="container">
    <nav class="nav">
      <a href="index.html" class="brand" aria-label="Tornomec - início">
        <img src="assets/img/logo.png" alt="Tornomec - Acessórios para Ferragista e Usinagem">
      </a>
      <ul class="nav-menu">
        <li><a href="index.html" class="{cls('inicio')}">Início</a></li>
        <li><a href="sobre.html" class="{cls('sobre')}">Sobre Nós</a></li>
        <li><a href="produtos.html" class="{cls('produtos')}">Produtos</a></li>
        <li><a href="contato.html" class="{cls('contato')}">Contato</a></li>
        <li class="nav-cta"><a href="contato.html" class="btn btn--primary">Fale Conosco <svg width="18" height="18"><use href="#i-arrow"/></svg></a></li>
      </ul>
      <button class="nav-toggle" aria-label="Abrir menu" aria-expanded="false"><span></span><span></span><span></span></button>
    </nav>
  </div>
</header>
<div class="nav-backdrop"></div>

'''

def page_hero(crumb, eyebrow, h1, p):
    return f'''<!-- ===== PAGE HERO ===== -->
<section class="page-hero">
  <div class="container">
    <div class="page-hero__inner">
      <nav class="breadcrumb"><a href="index.html">Início</a> <svg><use href="#i-arrow"/></svg> <span>{crumb}</span></nav>
      <span class="eyebrow">{eyebrow}</span>
      <h1>{h1}</h1>
      <p>{p}</p>
    </div>
  </div>
</section>

'''

def write(fname, title, desc, active, hero, body):
    out = head(title, desc) + SPRITE + header(active) + hero + body + TAIL
    open(fname, 'w', encoding='utf-8').write(out)
    print('wrote', fname, len(out), 'bytes')

# ---------------------------------------------------------------------------
# SOBRE NÓS
# ---------------------------------------------------------------------------
valores = [
 ("01","Qualidade","Produtos resistentes e bem acabados, feitos para o uso intenso do dia a dia."),
 ("02","Fabricação própria","Controle de todo o processo, do material à peça final."),
 ("03","Pronta entrega","Regularidade no fornecimento e estoque das principais linhas."),
 ("04","Atendimento técnico","Relação próxima com o ferragista, a serralheria e a indústria."),
 ("05","Precisão","Usinagem com tolerâncias exatas, conforme o projeto de cada peça."),
 ("06","Flexibilidade","Peças de linha e sob demanda, adaptadas à necessidade do cliente."),
 ("07","Confiança","Parcerias de longo prazo construídas com honestidade e compromisso."),
]
val_cards = "\n".join(
 f'''      <article class="card value-card reveal" data-delay="{i%4}"><span class="num">{n}</span><h3>{t}</h3><p>{d}</p></article>'''
 for i,(n,t,d) in enumerate(valores))

sobre_body = f'''<!-- ABOUT INTRO -->
<section class="section">
  <div class="container">
    <div class="split">
      <div class="split__media reveal">
        <img src="assets/img/usinagem.jpg" alt="Peças metálicas usinadas pela Tornomec: buchas, insertos e componentes torneados">
        <div class="badge b1"><svg><use href="#i-cog"/></svg><div><strong>Sob medida</strong><span>usinagem de precisão</span></div></div>
      </div>
      <div class="split__body reveal" data-delay="1">
        <span class="eyebrow">Nossa história</span>
        <h2 class="section-title">Acessórios que fazem o portão funcionar</h2>
        <p>A <strong>Tornomec</strong> nasceu da experiência em usinagem e na fabricação de acessórios para ferragista. Hoje produzimos uma linha completa de <strong>roldanas para portões</strong>, gonzos, rolamentos, roletes, cadeados e peças de acabamento.</p>
        <p>Atendemos ferragistas, serralherias e a indústria com produtos de qualidade e pronta entrega. Com <strong>fabricação própria</strong>, também desenvolvemos peças usinadas sob demanda, torneadas e fresadas de acordo com a necessidade de cada cliente.</p>
        <ul class="checklist">
          <li><svg><use href="#i-check"/></svg> Linha completa de roldanas e acessórios para portões</li>
          <li><svg><use href="#i-check"/></svg> Usinagem de peças sob medida em aço, latão e nylon</li>
          <li><svg><use href="#i-check"/></svg> Qualidade, durabilidade e regularidade no fornecimento</li>
        </ul>
      </div>
    </div>
  </div>
</section>

<!-- MISSÃO / VISÃO / VALORES -->
<section class="section bg-alt">
  <div class="container">
    <div class="section-head center">
      <span class="eyebrow eyebrow--center">O que nos move</span>
      <h2 class="section-title">Missão, Visão e Propósito</h2>
    </div>
    <div class="mvp">
      <article class="mvp__card reveal"><div class="icon-box"><svg><use href="#i-target"/></svg></div><h3>Missão</h3><p>Fabricar e fornecer acessórios para ferragista e usinagem com qualidade, precisão e pronta entrega, atendendo ferragistas, serralherias e a indústria.</p></article>
      <article class="mvp__card reveal" data-delay="1"><div class="icon-box"><svg><use href="#i-eye"/></svg></div><h3>Visão</h3><p>Ser referência em acessórios para portões e em usinagem sob demanda, reconhecida pela qualidade dos produtos e pela confiança no atendimento.</p></article>
      <article class="mvp__card reveal" data-delay="2"><div class="icon-box"><svg><use href="#i-compass"/></svg></div><h3>Propósito</h3><p>Entregar peças que funcionam e duram, ajudando nossos clientes a montar e manter portões e equipamentos com segurança.</p></article>
    </div>
  </div>
</section>

<!-- VALORES -->
<section class="section">
  <div class="container">
    <div class="section-head center">
      <span class="eyebrow eyebrow--center">Nossos valores</span>
      <h2 class="section-title">Os princípios que guiam a Tornomec</h2>
      <p class="section-intro">Sete compromissos que sustentam a forma como fabricamos e nos relacionamos com cada cliente.</p>
    </div>
    <div class="grid grid-4">
{val_cards}
    </div>
  </div>
</section>

<!-- DIFERENCIAIS -->
<section class="section bg-alt">
  <div class="container">
    <div class="section-head center">
      <span class="eyebrow eyebrow--center">Diferenciais</span>
      <h2 class="section-title">Por que fabricar e comprar com a Tornomec</h2>
    </div>
    <div class="grid grid-3">
      <article class="card feat reveal"><div class="icon-box"><svg><use href="#i-factory"/></svg></div><h3>Fabricação própria</h3><p>Controle total sobre material, acabamento e padrão de qualidade.</p></article>
      <article class="card feat reveal" data-delay="1"><div class="icon-box"><svg><use href="#i-cog"/></svg></div><h3>Usinagem sob demanda</h3><p>Peças torneadas e fresadas sob medida, conforme o desenho do cliente.</p></article>
      <article class="card feat reveal" data-delay="2"><div class="icon-box"><svg><use href="#i-wheel"/></svg></div><h3>Linha completa</h3><p>Roldanas, gonzos, rolamentos, roletes, cadeados e acabamentos.</p></article>
      <article class="card feat reveal"><div class="icon-box"><svg><use href="#i-shield"/></svg></div><h3>Durabilidade</h3><p>Materiais e rolamentos selecionados para resistir ao uso intenso.</p></article>
      <article class="card feat reveal" data-delay="1"><div class="icon-box"><svg><use href="#i-truck"/></svg></div><h3>Pronta entrega</h3><p>Estoque das principais linhas para abastecer o ferragista.</p></article>
      <article class="card feat reveal" data-delay="2"><div class="icon-box"><svg><use href="#i-headset"/></svg></div><h3>Atendimento técnico</h3><p>Time que entende do produto e ajuda a achar a peça certa.</p></article>
    </div>
  </div>
</section>

<!-- SLOGAN -->
<section class="slogan">
  <span class="slogan__mark">QUALIDADE</span>
  <div class="container">
    <q>Cada peça é feita para girar, vedar e segurar com <span class="hl">precisão</span>, porque o seu trabalho depende disso.</q>
    <cite>Tornomec</cite>
  </div>
</section>

<!-- CTA -->
<section class="section">
  <div class="container">
    <div class="cta-band reveal">
      <h2>Vamos construir uma parceria de longo prazo</h2>
      <p>Conheça nossa linha de produtos e descubra como a Tornomec pode abastecer e atender o seu negócio.</p>
      <div class="hero__actions">
        <a href="produtos.html" class="btn btn--primary btn--lg">Ver produtos <svg><use href="#i-arrow"/></svg></a>
        <a href="contato.html" class="btn btn--ghost btn--lg">Fale conosco</a>
      </div>
    </div>
  </div>
</section>

'''

write('sobre.html',
      'Sobre Nós | Tornomec',
      'Conheça a Tornomec: fabricante de acessórios para ferragista e usinagem em Belo Horizonte/MG. Missão, visão e os valores que guiam nossa fabricação.',
      'sobre',
      page_hero('Sobre Nós', 'Sobre a Tornomec',
                'Acessórios para ferragista e usinagem',
                'Fabricação própria de roldanas, gonzos, rolamentos e acessórios para portões, com usinagem de peças sob demanda.'),
      sobre_body)

# ---------------------------------------------------------------------------
# PRODUTOS
# ---------------------------------------------------------------------------
categorias = [
 ("Roldanas para Portão","i-wheel","Roldanas com canaleta, cubo de aço, nylon e zincadas, com e sem rolamento, para portões de correr."),
 ("Gonzos e Articuladores","i-hinge","Gonzos com chumbador, para parafusar, simples e com aba solta, além de articuladores."),
 ("Portão Basculante","i-gate","Olhos para basculante em nylon e aço, kits de núcleo, kits de rolamento e batentes."),
 ("Rolamentos e Trilhos","i-bearing","Rolamentos para trilho em aço e nylon e suportes para trilho."),
 ("Roletes e Guias","i-roller","Roletes de nylon, labirintos ICE e guias laterais em PTFE."),
 ("Suportes Stanley","i-trolley","Suportes Stanley duplos e quádruplos para portões de correr."),
 ("Curvas e Acabamentos","i-curve","Cotovelos, curvas 45°, 90° e 180°, canoplas, pontas de lança e coroações."),
 ("Cadeados","i-lock","Cadeados King e Mini King e travas laterais."),
 ("Conversão e Barras","i-ruler","Tabela de conversão polegadas/milímetros e barras redondas de aço."),
 ("Usinagem sob Demanda","i-cog","Peças torneadas e fresadas fabricadas sob medida, conforme desenho e aplicação."),
]
cat_cards = "\n".join(
 f'''      <article class="cat-card reveal" data-name="{nome}"><div class="icon-box"><svg><use href="#{ic}"/></svg></div><div><h3>{nome}</h3><p>{desc}</p></div></article>'''
 for nome,ic,desc in categorias)

# ----- catalog flipbook (page-flip, HTML mode = crisp native rendering) -----
_book_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets", "img", "catalogo")
book_pages = ["assets/img/catalogo/" + f for f in sorted(os.listdir(_book_dir)) if f.lower().endswith(".jpg")]
book_count = len(book_pages)

def _page_div(i, src):
    hard = ' data-density="hard"' if (i == 0 or i == book_count - 1) else ''
    eager = ' loading="eager"' if i < 4 else ' loading="lazy"'
    return f'<div class="page"{hard}><img src="{src}"{eager} alt="Catálogo Tornomec - página {i+1}"></div>'
book_html = "\n        ".join(_page_div(i, src) for i, src in enumerate(book_pages))

flip_script = """
<!-- CATÁLOGO - VISUALIZADOR (page-flip, HTML mode) -->
<script src="assets/js/page-flip.browser.js"></script>
<script>
(function(){
  function start(){
    var el = document.getElementById('flipbook');
    if(!el){ return; }
    var loader = document.getElementById('flipLoading');
    var counter = document.getElementById('flipCount');
    var pages = el.querySelectorAll('.page');
    var total = pages.length;
    function upd(i){ if(counter){ counter.textContent = (Math.max(0, i) + 1) + ' / ' + total; } }
    function reveal(){ if(loader){ loader.style.display = 'none'; } el.classList.add('ready'); }
    function fallback(){ reveal(); el.classList.add('flip-fallback'); }
    if(typeof St === 'undefined' || !St.PageFlip){ fallback(); return; }
    try{
      var pf = new St.PageFlip(el, {
        width: 500, height: 707, size: 'stretch',
        minWidth: 315, maxWidth: 650, minHeight: 445, maxHeight: 920,
        maxShadowOpacity: 0.5, showCover: true, usePortrait: true,
        mobileScrollSupport: false, drawShadow: true, flippingTime: 650,
        startZIndex: 5
      });
      pf.loadFromHTML(pages);
      pf.on('init', function(){ reveal(); });
      pf.on('flip', function(e){ upd(e.data); });
      var bp = document.getElementById('flipPrev'), bn = document.getElementById('flipNext');
      if(bp){ bp.addEventListener('click', function(){ pf.flipPrev(); }); }
      if(bn){ bn.addEventListener('click', function(){ pf.flipNext(); }); }
      document.addEventListener('keydown', function(e){
        if(e.key === 'ArrowLeft'){ pf.flipPrev(); }
        else if(e.key === 'ArrowRight'){ pf.flipNext(); }
      });
      window.__flip = pf;
    }catch(err){ if(window.console){ console.error('flipbook init failed', err); } fallback(); }
  }
  if(document.readyState === 'loading'){ document.addEventListener('DOMContentLoaded', start); }
  else { start(); }
})();
</script>
"""

produtos_body = f'''<!-- SERVIÇOS -->
<section class="section">
  <div class="container">
    <div class="section-head center">
      <span class="eyebrow eyebrow--center">O que oferecemos</span>
      <h2 class="section-title">Fabricação, usinagem e fornecimento</h2>
      <p class="section-intro">Muito além de vender peças: fabricamos, usinamos sob medida e mantemos estoque para abastecer o seu negócio.</p>
    </div>
    <div class="svc">
      <article class="card reveal"><div class="icon-box"><svg><use href="#i-factory"/></svg></div><h3>Fabricação própria</h3><p>Produzimos nossas linhas com controle de material, acabamento e qualidade.</p></article>
      <article class="card reveal" data-delay="1"><div class="icon-box"><svg><use href="#i-cog"/></svg></div><h3>Usinagem sob demanda</h3><p>Peças torneadas e fresadas conforme o desenho e a aplicação do cliente.</p></article>
      <article class="card reveal" data-delay="2"><div class="icon-box"><svg><use href="#i-truck"/></svg></div><h3>Pronta entrega</h3><p>Estoque das principais linhas para fornecimento ágil e regular.</p></article>
      <article class="card reveal" data-delay="3"><div class="icon-box"><svg><use href="#i-headset"/></svg></div><h3>Atendimento técnico</h3><p>Apoio para identificar a peça certa para cada portão ou equipamento.</p></article>
    </div>
  </div>
</section>

<!-- CATEGORIAS -->
<section class="section bg-alt">
  <div class="container">
    <div class="section-head center">
      <span class="eyebrow eyebrow--center">Linhas de produtos</span>
      <h2 class="section-title">Catálogo de acessórios Tornomec</h2>
      <p class="section-intro">Conheça as linhas que cobrem roldanas, gonzos, rolamentos, acabamentos, cadeados e usinagem sob demanda.</p>
    </div>
    <div class="cat-toolbar">
      <div class="cat-search">
        <svg><use href="#i-search"/></svg>
        <input type="text" id="catSearch" placeholder="Buscar linha de produto…" aria-label="Buscar linha de produto">
      </div>
    </div>
    <div class="cat-grid">
{cat_cards}
    </div>
    <p class="cat-empty">Nenhuma linha encontrada. Tente outro termo.</p>
  </div>
</section>

<!-- CATÁLOGO (FLIPBOOK) -->
<section class="section">
  <div class="container">
    <div class="section-head center">
      <span class="eyebrow eyebrow--center">Catálogo</span>
      <h2 class="section-title">Folheie o nosso catálogo</h2>
      <p class="section-intro">Navegue pelas páginas como em um livro: use as setas, arraste as páginas ou clique nas bordas.</p>
    </div>
    <div class="flipbook-wrap">
      <div class="flipbook-stage">
        <div id="flipbook" class="flipbook">
        {book_html}
        </div>
        <div class="flip-loading" id="flipLoading">Carregando catálogo…</div>
      </div>
      <div class="flip-controls">
        <button id="flipPrev" type="button" aria-label="Página anterior"><svg width="18" height="18" style="transform:rotate(180deg)"><use href="#i-arrow"/></svg> Anterior</button>
        <span class="flip-count" id="flipCount">1 / {book_count}</span>
        <button id="flipNext" type="button" aria-label="Próxima página">Próxima <svg width="18" height="18"><use href="#i-arrow"/></svg></button>
      </div>
    </div>
  </div>
</section>

<!-- CATALOGO CTA -->
<section class="section bg-alt">
  <div class="container">
    <div class="cta-band reveal">
      <h2>Baixe o catálogo completo</h2>
      <p>Tenha em mãos todas as linhas da Tornomec, com medidas, códigos e referências para facilitar o seu pedido.</p>
      <div class="hero__actions">
        <a href="assets/docs/catalogo-tornomec.pdf" target="_blank" rel="noopener" class="btn btn--primary btn--lg"><svg><use href="#i-doc"/></svg> Baixar catálogo (PDF)</a>
        <a href="contato.html" class="btn btn--ghost btn--lg">Solicitar orçamento</a>
      </div>
    </div>
  </div>
</section>

{flip_script}
'''

write('produtos.html',
      'Produtos | Tornomec - Roldanas, Gonzos, Rolamentos e Usinagem',
      'Catálogo Tornomec: roldanas para portão, gonzos, rolamentos, roletes, cadeados, curvas e acabamentos, além de usinagem de peças sob demanda.',
      'produtos',
      page_hero('Produtos', 'Produtos e Linhas',
                'Tudo para portões e usinagem',
                'Uma linha ampla de acessórios para ferragista, com fabricação própria e a opção de usinagem de peças sob medida.'),
      produtos_body)

# ---------------------------------------------------------------------------
# CONTATO
# ---------------------------------------------------------------------------
contato_body = f'''<!-- CONTATO -->
<section class="section">
  <div class="container">
    <div class="contact-grid">
      <!-- FORM -->
      <div class="form-card reveal">
        <span class="eyebrow">Envie uma mensagem</span>
        <h2 class="section-title" style="font-size:1.7rem;margin-bottom:8px">Solicite um orçamento</h2>
        <p style="color:var(--muted);margin-bottom:26px">Preencha o formulário e retornaremos o mais breve possível. Os campos marcados com * são obrigatórios.</p>
        <form id="contactForm" novalidate>
          <div class="form-row">
            <div class="field"><label for="nome">Nome *</label><input type="text" id="nome" name="nome" placeholder="Seu nome" required></div>
            <div class="field"><label for="empresa">Empresa</label><input type="text" id="empresa" name="empresa" placeholder="Nome da empresa"></div>
          </div>
          <div class="form-row">
            <div class="field"><label for="email">E-mail *</label><input type="email" id="email" name="email" placeholder="voce@empresa.com.br" required></div>
            <div class="field"><label for="telefone">Telefone / WhatsApp</label><input type="tel" id="telefone" name="telefone" placeholder="(31) 90000-0000"></div>
          </div>
          <div class="field">
            <label for="assunto">Interesse</label>
            <select id="assunto" name="assunto">
              <option>Roldanas para portão</option>
              <option>Gonzos e rolamentos</option>
              <option>Portão basculante</option>
              <option>Cadeados</option>
              <option>Usinagem sob demanda</option>
              <option>Catálogo completo</option>
              <option>Outro assunto</option>
            </select>
          </div>
          <div class="field"><label for="mensagem">Mensagem *</label><textarea id="mensagem" name="mensagem" placeholder="Conte-nos qual produto ou peça você procura…" required></textarea></div>
          <div class="hero__actions">
            <button type="submit" class="btn btn--primary btn--lg"><svg><use href="#i-mail"/></svg> Enviar por e-mail</button>
            <button type="button" id="sendWhats" class="btn btn--wa btn--lg"><svg><use href="#i-wa"/></svg> Enviar no WhatsApp</button>
          </div>
          <p class="form-note"><svg><use href="#i-info"/></svg> Ao enviar, abriremos seu aplicativo de e-mail ou o WhatsApp com a mensagem pronta. Nenhum dado é armazenado neste site.</p>
        </form>
      </div>

      <!-- SIDE -->
      <div class="contact-side">
        <div class="contact-info reveal" data-delay="1">
          <h3>Atendimento direto</h3>
          <p>Estamos prontos para atender ferragistas, serralherias, indústria e projetos sob medida.</p>
          <div class="person">
            <div class="person__av"><svg><use href="#i-headset"/></svg></div>
            <div>
              <h4>Atendimento comercial</h4>
              <div class="role">Vendas e orçamentos</div>
              <a href="tel:+553133828405"><svg><use href="#i-phone"/></svg> (31) 3382-8405</a>
              <a href="https://wa.me/553133828405" target="_blank" rel="noopener"><svg><use href="#i-wa"/></svg> WhatsApp (31) 3382-8405</a>
              <a href="mailto:contato@tornomec.com.br"><svg><use href="#i-mail"/></svg> contato@tornomec.com.br</a>
            </div>
          </div>
        </div>

        <div class="contact-meta reveal" data-delay="2">
          <div class="row"><div class="icon-box"><svg><use href="#i-globe"/></svg></div><div><strong>Website</strong><span>www.tornomec.com.br</span></div></div>
          <div class="row"><div class="icon-box"><svg><use href="#i-pin"/></svg></div><div><strong>Endereço</strong><span>Av. Senador Levindo Coelho, 1698<br>Distrito Industrial do Jatobá<br>Belo Horizonte - MG, 30664-006</span></div></div>
          <div class="row"><div class="icon-box"><svg><use href="#i-clock"/></svg></div><div><strong>Horário</strong><span>Seg. a Sex., das 7:30h às 17:18h</span></div></div>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- LOCALIZAÇÃO -->
<section class="section--tight" style="padding-top:0">
  <div class="container">
    <div class="map-block reveal">
      <div class="map-block__info">
        <div class="icon-box"><svg><use href="#i-pin"/></svg></div>
        <h3>Onde estamos</h3>
        <p>Av. Senador Levindo Coelho, 1698<br>Distrito Industrial do Jatobá<br>Belo Horizonte - MG, 30664-006</p>
        <a class="btn btn--primary" href="https://www.google.com/maps/dir/?api=1&destination={ADDR_Q}" target="_blank" rel="noopener">Como chegar <svg><use href="#i-arrow"/></svg></a>
      </div>
      <div class="map-block__map">
        <!--
          MAPA - GOOGLE MAPS
          Endereço: {ADDRESS}
          Abaixo usamos o embed gratuito do Google Maps (não exige chave de API).
          Para usar a Google Maps Embed API oficial (com a sua própria chave), troque o src por:
          https://www.google.com/maps/embed/v1/place?key=SUA_CHAVE_API&q={ADDR_Q}&zoom=16&language=pt-BR
        -->
        <iframe title="Mapa - {ADDRESS}"
          src="https://maps.google.com/maps?q={ADDR_Q}&t=&z=16&hl=pt-BR&ie=UTF8&iwloc=B&output=embed"
          loading="lazy" referrerpolicy="no-referrer-when-downgrade" allowfullscreen></iframe>
      </div>
    </div>
  </div>
</section>

<!-- TOAST -->
<div class="toast"><svg><use href="#i-check-c"/></svg><span>Mensagem pronta!</span></div>

'''

write('contato.html',
      'Contato | Tornomec - Acessórios para Ferragista e Usinagem',
      'Fale com a Tornomec em Belo Horizonte/MG. Telefone (31) 3382-8405, WhatsApp, e-mail e mapa de localização. Atendimento a ferragistas, serralherias e indústria.',
      'contato',
      page_hero('Contato', 'Fale Conosco',
                'Vamos falar sobre o que você precisa',
                'Atendimento a ferragistas, serralherias, indústria e projetos sob medida. Estamos prontos para ajudar.'),
      contato_body)

print("ALL PAGES GENERATED")
