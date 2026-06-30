# Site Tornomec

Site institucional da **Tornomec — Acessórios para Ferragista e Usinagem**.
São 4 páginas, em HTML/CSS/JS estático (sem dependências de build, sem framework):

| Página | Arquivo | Conteúdo |
|--------|---------|----------|
| Início | `index.html` | Apresentação, diferenciais, linhas de produtos, público-alvo |
| Sobre Nós | `sobre.html` | História, missão/visão/propósito, valores |
| Produtos | `produtos.html` | Linhas de produtos (com busca), **catálogo folheável** (flipbook) e download do PDF |
| Contato | `contato.html` | Formulário, dados de contato e **mapa do Google Maps** |

## Como visualizar localmente

Na pasta do site, rode um servidor estático e abra no navegador:

```bash
python -m http.server 5578
# depois acesse http://localhost:5578
```

(Também é possível abrir o `index.html` direto no navegador.)

## Como publicar

É um site estático: basta enviar **todos os arquivos** (HTML + a pasta `assets/`)
para qualquer hospedagem — por exemplo o domínio `www.tornomec.com.br`.

## Como editar o conteúdo

- O **cabeçalho, rodapé e os ícones** ficam em `index.html` (página mestre).
- As páginas **sobre / produtos / contato** são geradas a partir de `index.html`
  pelo script `_build.py`, para manter tudo consistente. Depois de editar textos
  nesse script, rode:

```bash
python _build.py
```

## Imagens e marca

- `assets/img/logo.png` — logo (texto escuro) para fundos claros (cabeçalho)
- `assets/img/logo-white.png` — logo (texto branco) para o rodapé escuro
- `assets/img/emblem.png` / `favicon.png` — símbolo da marca
- `assets/img/hero.jpg` e `usinagem.jpg` — foto de peças usinadas (do catálogo)
- `assets/img/catalogo/` — páginas do catálogo (p01…p15) usadas no visualizador folheável
- `assets/js/page-flip.browser.js` — biblioteca do flipbook (StPageFlip), embutida localmente
- `assets/docs/catalogo-tornomec.pdf` — catálogo completo para download

> O visualizador folheável é gerado a partir das imagens em `assets/img/catalogo/`. Se o
> catálogo PDF mudar, gere as páginas novamente com o `page-flip.browser.js` apontando para
> os novos JPGs (ou peça para reprocessar o PDF).

## Mapa (Google Maps)

A página de contato usa o **embed gratuito do Google Maps** (não exige chave de API)
apontando para o endereço da empresa. Em alguns ambientes de pré-visualização
automatizada o mapa pode não carregar, mas ele funciona normalmente em um
navegador comum.

Para usar a **Google Maps Embed API oficial** (recomendado em produção), gere uma
chave em https://console.cloud.google.com e troque o `src` do iframe em
`contato.html` / `_build.py` por:

```
https://www.google.com/maps/embed/v1/place?key=SUA_CHAVE_API&q=ENDERECO&zoom=16&language=pt-BR
```

## ⚠️ Itens a confirmar antes de publicar

Estes dados foram preenchidos com base no catálogo/logo. Confirme e ajuste se preciso:

- **E-mail:** `contato@tornomec.com.br` (padrão presumido — confirmar)
- **WhatsApp:** usa o mesmo número do telefone, (31) 3382-8405 — confirmar se há
  WhatsApp nesse número (aparece no botão flutuante, CTA e formulário)
- **Facebook:** `facebook.com/tornomec` — confirmar a URL real
- **Horário de atendimento:** Seg. a Sex., das 7:30h às 17:18h

Dados confirmados pelo catálogo: telefone (31) 3382-8405, site www.tornomec.com.br,
endereço Av. Senador Levindo Coelho, 1698 — Distrito Industrial do Jatobá, BH/MG.
