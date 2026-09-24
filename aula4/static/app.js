// Interface do cinema. Tudo aqui consome a REST API -- nenhum dado vem
// embutido no HTML.
//
// Padrao para os TODOs: cada entidade tem uma funcao `carregarX()` que
// (1) chama api(), (2) monta o HTML, (3) joga no container. Siga o formato
// de carregarFilmes(), que esta completo como referencia.

const API = ""; // mesma origem do servidor; troque se a API subir em outra porta

/** GET/POST/PUT/DELETE na API. Lanca Error com a mensagem do backend. */
async function api(caminho, opcoes = {}) {
  const resposta = await fetch(`${API}${caminho}`, {
    headers: { "Content-Type": "application/json" },
    ...opcoes,
  });

  if (!resposta.ok) {
    const corpo = await resposta.json().catch(() => ({}));
    throw new Error(corpo.detail || `Erro ${resposta.status}`);
  }

  return resposta.status === 204 ? null : resposta.json();
}

/** Escapa texto que veio da API antes de injetar no HTML. */
function esc(valor) {
  return String(valor ?? "").replace(/[&<>"']/g, (c) => ({
    "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;",
  }[c]));
}

function erro(container, e) {
  container.innerHTML = `<p class="erro">Falha ao carregar: ${esc(e.message)}</p>`;
}

const SEM_CARTAZ = "/static/sem-cartaz.svg";

// --- filmes (REFERENCIA COMPLETA) ---------------------------------------
async function carregarFilmes() {
  const container = document.getElementById("filmes");
  try {
    const filmes = await api("/filmes");

    if (filmes.length === 0) {
      container.innerHTML = "<p class='vazio'>Nenhum filme cadastrado.</p>";
      return;
    }

    container.innerHTML = filmes.map((filme) => `
      <article class="cartao-filme">
        <img class="cartaz"
             src="${esc(filme.cartaz_url || SEM_CARTAZ)}"
             alt="Cartaz de ${esc(filme.nome)}"
             onerror="this.src='${SEM_CARTAZ}'">
        <h3>${esc(filme.nome)}</h3>
        <dl>
          <dt>Codigo</dt><dd>${esc(filme.codigo)}</dd>
          <dt>Duracao</dt><dd>${esc(filme.duracao)} min</dd>
          <dt>Em cartaz</dt><dd>${esc(filme.data_estreia)} a ${esc(filme.data_saida)}</dd>
        </dl>
      </article>
    `).join("");
  } catch (e) {
    erro(container, e);
  }
}

// --- sessoes ------------------------------------------------------------
async function carregarSessoes() {
  const container = document.getElementById("sessoes");
  try {
    const [sessoes, filmes] = await Promise.all([
      api("/sessoes"),
      api("/filmes"),
    ]);

    if (sessoes.length === 0) {
      container.innerHTML = "<p class='vazio'>Nenhuma sessão cadastrada.</p>";
      return;
    }

    const nomesFilmes = new Map(
      filmes.map((filme) => [filme.codigo, filme.nome])
    );
    
    container.innerHTML = `
      <table>
        <thead>
          <tr>
            <th>Código</th>
            <th>Filme</th>
            <th>Sala</th>
            <th>Data</th>
            <th>Início</th>
          </tr>
        </thead>
        <tbody>
          ${sessoes.map((sessao) => `
            <tr>
              <td>${esc(sessao.codigo)}</td>
              <td>${esc(nomesFilmes.get(sessao.filme_codigo) ?? `Filme ${sessao.filme_codigo}`)}</td>
              <td>${esc(sessao.sala_numero)}</td>
              <td>${esc(sessao.data)}</td>
              <td>${esc(sessao.hora_inicio.slice(0, 5))}</td>
            </tr>
          `).join("")}
        </tbody>
      </table>
    `;
  } catch (e) {
    erro(container, e);
  }
}

// --- salas --------------------------------------------------------------
async function carregarSalas() {
  const container = document.getElementById("salas");
  try {
    const salas = await api("/salas");
    // TODO(salas): montar tabela com numero, capacidade, tipo (2D/3D).
    container.innerHTML = `<pre class="stub">${esc(JSON.stringify(salas, null, 2))}</pre>`;
  } catch (e) {
    erro(container, e);
  }
}

// --- tipos de ingresso --------------------------------------------------
async function carregarIngressos() {
  const container = document.getElementById("ingressos");
  try {
    const tipos = await api("/tipos-ingresso");
    // TODO(ingressos): montar tabela com codigo, tipo (0=inteira, 1=meia)
    // e preco formatado em reais.
    container.innerHTML = `<pre class="stub">${esc(JSON.stringify(tipos, null, 2))}</pre>`;
  } catch (e) {
    erro(container, e);
  }
}

// --- navegacao entre abas ----------------------------------------------
const CARREGADORES = {
  filmes: carregarFilmes,
  sessoes: carregarSessoes,
  salas: carregarSalas,
  ingressos: carregarIngressos,
};

document.querySelectorAll(".aba").forEach((aba) => {
  aba.addEventListener("click", () => {
    const alvo = aba.dataset.painel;

    document.querySelectorAll(".aba").forEach((b) => b.classList.remove("ativa"));
    document.querySelectorAll(".painel").forEach((p) => p.classList.remove("ativo"));

    aba.classList.add("ativa");
    document.getElementById(`painel-${alvo}`).classList.add("ativo");

    CARREGADORES[alvo]();
  });
});

carregarFilmes();
