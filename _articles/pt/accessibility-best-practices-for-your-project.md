---
lang: pt
title: Boas Práticas de Acessibilidade para o Seu Projeto
description: Passos práticos e acionáveis para tornar seu projeto open source utilizável por todas as pessoas, especialmente pessoas com deficiência.
class: accessibility-best-practices
order: -1
image: /assets/images/cards/accessibility-best-practices.png
---

Acessibilidade (frequentemente abreviada como _a11y_) significa que as pessoas podem usar o seu projeto independentemente de deficiência, tecnologia assistiva, ambiente ou dispositivo. Isso inclui — mas não se limita a — suporte a leitores de tela, navegação somente por teclado, legendas/transcrições, contraste de cores suficiente e estrutura clara de conteúdo.

## Trabalhe em parceria com pessoas com deficiência

**"Nada sobre nós sem nós"** — A coisa mais importante que você pode fazer pela acessibilidade é colocar no centro as pessoas a quem ela serve. Usuários, contribuidores e testadores com deficiência compreendem barreiras de um jeito que diretrizes e ferramentas automatizadas não conseguem. Busque a experiência vivida dessas pessoas cedo e com frequência.

### Coloque em prática

Decisões tomadas sem as pessoas afetadas por elas tendem a errar o alvo. Construir com pessoas com deficiência, em vez de para elas, resulta em software melhor para todo mundo.

Aqui estão algumas formas de centrar a experiência vivida:

* Convide contribuidores com deficiência para as discussões de design, não apenas para a triagem de bugs.
* Envolva pessoas com deficiência em testes de usabilidade e feedback sempre que puder.
* Escute quando alguém descrever como usa o seu projeto, mesmo quando isso desafiar as suas suposições.
* Trate relatos de acessibilidade como conhecimento especializado, não como reclamações — eles podem representar mais gente do que você imagina.

### Acessibilidade beneficia todo mundo

* **Impacta muitas pessoas.** Estima-se que 1,3 bilhão de pessoas (1 em cada 6) vivam com alguma deficiência significativa, segundo a [Organização Mundial da Saúde](https://www.who.int/news-room/fact-sheets/detail/disability-and-health).
* **Faz parte da qualidade.** Produtos acessíveis tendem a ser mais usáveis para todo mundo.
* **Reduz a carga de suporte.** UI e documentação mais claras significam menos usuários confusos.
* **Amplia a sua base de contribuidores.** Quem usa tecnologia assistiva pode participar de forma mais plena.
* **Impulsiona a inovação.** Projetar para necessidades diversas costuma gerar recursos que beneficiam a todos (legendas, controle por voz e modo escuro começaram como soluções de acessibilidade).
* **Muitas vezes é obrigatória.** Muitas organizações (e alguns governos) exigem acessibilidade em compras e conformidade.
* **Nosso futuro é incerto.** Ninguém hoje pode ter certeza das habilidades que terá amanhã.

## Comece com uma declaração de acessibilidade

Antes de mergulhar no código, reserve um momento para documentar o compromisso do seu projeto com a acessibilidade. Uma declaração de acessibilidade sinaliza a usuários e contribuidores que acessibilidade é prioridade, não algo deixado para depois. Para orientação, consulte o guia [Developing an Accessibility Statement, do W3C](https://www.w3.org/WAI/planning/statements/).

Adicione uma declaração clara que estabeleça expectativas e facilite o relato de problemas pelos usuários. Você pode adicionar uma seção de acessibilidade diretamente no seu README ou criar um arquivo **ACCESSIBILITY.md** dedicado e referenciá-lo no README para dar visibilidade. Consulte este [exemplo de ACCESSIBILITY.md](https://github.com/open-source-accessibility/accessibility-toolkit/blob/main/ACCESSIBILITY.md).

### Metas

* Declare metas mensuráveis (como [WCAG AA](https://www.w3.org/TR/WCAG22/#wcag-2-layers-of-guidance), quando viável).
* As prioridades principais e como você as atende (suporte a teclado e leitor de tela, legendas e transcrições etc.).
* Quaisquer limitações conhecidas e alternativas de contorno (se existirem).

### Requisitos para contribuidores

Estabeleça diretrizes claras para que os contribuidores saibam o que se espera:

* **Testes:** toda mudança de UI deve ser testada com uma ferramenta de teste de acessibilidade (como o [Axe DevTools](https://www.deque.com/axe/devtools/extension/#:~:text=Try%20Axe%20DevTools%20Extension%20in%20your%20browser%20of%20choice)).
* **Documentação:** siga as diretrizes de acessibilidade do seu projeto para componentes como SVGs, imagens e elementos interativos.
* **CI/CD:** pull requests falharão se introduzirem violações detectadas pelo workflow de linting de acessibilidade.

### Ambientes suportados

* Liste as plataformas que você suporta (web, web mobile, iOS, Android, terminal/CLI, aplicativos desktop).
* Liste eventuais observações de suporte parcial.

### Relato de bugs de acessibilidade

* Peça que os relatos sejam abertos como issues usando o template de issue de acessibilidade.
* **Dica:** estabeleça expectativas com honestidade (como "Estamos trabalhando nisso — acompanhando na ISSUE-123"); reconheça os relatos e ofereça acompanhamento ou alternativa de contorno quando possível.

#### Por que separar a acessibilidade do seu fluxo geral de issues?

Os usuários passaram a esperar uma declaração de acessibilidade e um canal de relato dedicados — é uma convenção bem estabelecida no setor privado e em sites governamentais, e muita gente procura por isso primeiro ao encontrar uma barreira. Manter a acessibilidade separada do fluxo geral de issues importa porque:

* **O impacto é sensível ao tempo.** Um bug de acessibilidade pode impedir alguém de usar o seu projeto por completo, não apenas causar um incômodo. Um canal dedicado ajuda esses relatos a serem triados mais rápido.
* **O contexto é diferente.** Issues de acessibilidade precisam de informações específicas (tecnologia assistiva, sistema operacional, navegador, severidade) que um template genérico de bug não solicita.
* **Sinaliza compromisso.** Uma declaração visível e separada mostra a usuários e contribuidores que acessibilidade é uma preocupação de primeira classe, não algo diluído em "outros bugs".
* **Quem relata pode usar tecnologia assistiva para registrar o próprio relato.** Um processo claro e previsível (um arquivo conhecido, uma label conhecida, um template conhecido) reduz o atrito justamente para as pessoas mais afetadas.

## Torne a documentação acessível por padrão

A documentação costuma ser a primeira "UI" que os usuários tocam. Garanta que todo mundo consiga lê-la.

### Estrutura e semântica

* Use uma **hierarquia lógica de títulos** e não pule níveis (`#`, `##`, `###`, `####`, `#####` e `######`).
* Use **textos de link únicos e descritivos** ("Leia o guia de contribuição" em vez de "clique aqui").
* Use linguagem simples, evitando jargão e expandindo qualquer abreviação na primeira vez em que for usada.
* [Use **listas de verdade**](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax#lists) em vez de numeração digitada manualmente.
* Mantenha **ajuda e navegação em locais consistentes** entre as páginas, para que os usuários as encontrem de forma previsível.
* Evite transmitir significado apenas por posição ou estilo ("veja o texto vermelho à direita").

### Imagens, diagramas e vídeos

* Forneça **texto alternativo** (o "alt text") significativo para as imagens (consulte a [árvore de decisão de alt do W3C](https://www.w3.org/WAI/tutorials/images/decision-tree/)).
* Em vez de usar imagens de texto, use texto de verdade sempre que possível.
* Para imagens complexas (como diagramas de arquitetura), inclua uma **alternativa textual** adicional por perto (tópicos ou uma explicação curta).
* Se você publica demos, tutoriais, palestras ou vídeos de release:
  * Forneça **legendas** (prefira as editadas por humanos quando possível).
  * Forneça uma **transcrição**.
  * Evite áudio e vídeo com reprodução automática.
  * Descreva verbalmente as ações importantes que acontecem na tela.

### Tabelas

* Use tabelas apenas para dados tabulares, não para layout.
* Inclua **células de cabeçalho** (`<th>`) e use atributos `scope` para associar cabeçalhos às células de dados.
* Forneça uma **legenda ou resumo** descrevendo o propósito da tabela.

### Blocos de código

* Mantenha as linhas razoavelmente curtas (a quebra de linha ajuda a leitura).
* Não dependa apenas do realce por cor para indicar significado.
* Explique no texto o que o código faz e como é o resultado esperado.

## Projete interfaces acessíveis

Se o seu projeto tem uma UI web, estes padrões de alto impacto ajudarão todos os usuários.

### Suporte a teclado

* Tudo que é interativo deve ser alcançável e utilizável **somente com o teclado**.
* Garanta um **indicador de foco visível** (não remova os contornos de foco, a menos que os substitua).
* Mantenha uma **ordem de tabulação** lógica, que corresponda ao layout visual.
* Não prenda o foco dentro de componentes, a menos que você gerencie o foco intencionalmente (como em diálogos modais) e ofereça uma saída.

### Semântica em primeiro lugar

* Use elementos nativos do HTML (`<h1>`, `<button>`, `<a>`, `<input>`, `<label>`) sempre que possível.
* Use ARIA apenas quando o HTML nativo não for suficiente. Nenhum ARIA é melhor do que um ARIA ruim. Quando usar, siga a [documentação do Accessible Rich Internet Applications (ARIA)](https://www.w3.org/TR/wai-aria/) e garanta que todos os controles ARIA interativos sejam acessíveis por teclado.
* Declare o **idioma** do seu documento (como `lang="en"` no HTML) e marque quaisquer seções em um idioma diferente.

### Nomes, rótulos, instruções

* Todo controle de formulário precisa de um **rótulo** (label) associado.
* Forneça **mensagens de erro claras**, indique qual campo tem o erro e associe programaticamente a mensagem ao campo (como com `aria-describedby`).
* Para campos obrigatórios, explique os requisitos em texto (não apenas com um asterisco).

### Cor e contraste

* Não use cor como único meio de transmitir significado ("erros são vermelhos").
* Garanta contraste adequado para textos e controles de UI (consulte o [Contrast Checker do WebAIM](https://webaim.org/resources/contrastchecker/)).

### Movimento e animação

* Evite conteúdo piscante e animações rápidas.
* Evite efeitos de parallax e carrosséis com avanço automático, ou torne-os opcionais e controláveis.

### Conteúdo dinâmico

Quando o conteúdo é atualizado sem um carregamento de página, garanta que quem usa tecnologia assistiva seja informado:

* Use **regiões live do ARIA** apropriadas, com parcimônia, para os anúncios.
* Gerencie o foco ao abrir/fechar diálogos, menus e gavetas.

### Dependências e padrões

* Use bibliotecas de componentes com suporte documentado a acessibilidade.
* Acompanhe bugs de acessibilidade no upstream e crie links para eles nas suas issues.
* Tenha cautela com controles de UI personalizados. Os controles nativos (como `<button>`, `<select>`, `<input type="checkbox">`, `<details>`) já vêm com suporte a teclado, gerenciamento de foco, semântica para leitores de tela e integração com formulários que navegadores e tecnologias assistivas já entendem. Recriar esse comportamento em componentes personalizados consome tempo, é fácil de errar e adiciona custo de manutenção de longo prazo à medida que plataformas e tecnologias assistivas evoluem. Recorra a controles personalizados apenas quando um elemento nativo genuinamente não atender à necessidade.

### Considerações para mobile

* Faça alvos de toque de pelo menos **24×24 pixels CSS**.
* Ofereça alternativas de ponteiro único para gestos multiponto ou baseados em trajetória (pinçar, deslizar).
* Ofereça alternativas para operações de arrastar e soltar (botões, menus).
* Não restrinja o conteúdo a uma única orientação de tela, a menos que o conteúdo exibido precise de uma orientação específica.
* Ofereça alternativas para recursos acionados por movimento do dispositivo (como sacudir para desfazer).

## Torne as ferramentas acessíveis

Ferramentas de linha de comando e dashboards podem ser altamente acessíveis quando projetadas com cuidado.

### Ferramentas CLI

Aplicativos de linha de comando podem ser altamente acessíveis quando são previsíveis e automatizáveis por scripts.

* Suporte `--help` com exemplos claros de uso.
* Ofereça opções de **saída legível por máquina** (como `--json`) para quem não consegue interpretar tabelas com facilidade.
* Evite depender apenas de cores ANSI para transmitir sucesso/falha; inclua rótulos em texto e códigos de saída.
* Escreva mensagens de erro que:
  * Expliquem o que aconteceu,
  * Mostrem como corrigir, e
  * Apontem para a documentação, se necessário.
* Use códigos de saída padrão e garanta valor diferente de zero em caso de falha.

### Terminais, logs e dashboards

* Prefira linguagem simples a jargão.
* Evite abreviações sem explicação.
* Use formatação consistente para níveis de severidade (`ERROR`, `WARN`, `INFO`) e inclua timestamps quando forem úteis.
* Garanta que o "status" não seja comunicado apenas com cor.

## Incorpore a acessibilidade aos fluxos de contribuição

A acessibilidade é mais fácil de manter quando faz parte do seu processo habitual.

### Adicione labels e template de issue

* Crie uma label de acessibilidade (como _"accessibility"_ ou _"a11y"_).
* Crie um template de issue de acessibilidade que inclua:
  * A label de _acessibilidade_
  * Comportamento esperado versus comportamento observado
  * Passos para reproduzir (incluindo uma gravação de tela opcional)
  * Ferramentas usadas (sistema operacional, navegador, tecnologia assistiva e versão)
  * Uma taxonomia de severidade para ajudar a priorizar:
    * **Crítica:** impede o usuário de completar uma tarefa essencial (como "Não consigo finalizar a compra").
    * **Alta:** dificuldade significativa, mas existe alternativa de contorno.
    * **Média:** incômodo ou experiência inconsistente.
    * **Baixa:** problema menor, com impacto mínimo na usabilidade.
  * Instruções de contato ou escalonamento, se apropriado.

Consulte este [exemplo de template de issue de acessibilidade](https://github.com/open-source-accessibility/accessibility-toolkit/blob/main/.github/ISSUE_TEMPLATE/accessibility.yml).

### Adicione um checklist de acessibilidade aos pull requests (PRs)

Para projetos com mudanças de UI, inclua perguntas como:

* A navegação por teclado funciona de ponta a ponta
* Os estados de foco estão visíveis e lógicos
* Os formulários têm rótulos e os erros são anunciados
* A cor não é o único indicador
* A redução de movimento é respeitada (se animações foram adicionadas)
* O comportamento com leitor de tela foi verificado (pelo menos uma vez)

Consulte este [exemplo de template de PR](https://github.com/open-source-accessibility/accessibility-toolkit/blob/main/.github/PULL_REQUEST_TEMPLATE.md).

### Defina o que é "pronto"

Adicione critérios de aceitação de acessibilidade para funcionalidades e correções de bugs, para que ela não seja opcional nem deixada para a última hora.

### Aproveite o GitHub Copilot

* Crie agentes personalizados do Copilot que automatizem tarefas de acessibilidade no seu fluxo de desenvolvimento, desde auditar páginas com o [axe-core](https://github.com/dequelabs/axe-core) até acompanhar melhorias de acessibilidade entre releases. Consulte o guia [Getting Started with GitHub Copilot Custom Agents for Accessibility](https://accessibility.github.com/documentation/guide/getting-started-with-agents/).
* Ajuste as sugestões do Copilot ao seu estilo de código, às suas práticas de acessibilidade e ao contexto do projeto, para garantir que elas estejam alinhadas aos seus requisitos de acessibilidade. Consulte o guia [Optimizing GitHub Copilot for Accessibility with Custom Instructions](https://accessibility.github.com/documentation/guide/copilot-instructions/).

### Trate os relatos de acessibilidade com respeito e eficácia

Problemas de acessibilidade costumam ser difíceis de descrever, difíceis de reproduzir e sensíveis ao tempo para a capacidade de quem relata continuar usando o seu projeto. Ao lidar com relatos:

* Agradeça a quem relatou e faça perguntas de esclarecimento sem ceticismo.
* Priorize bloqueios (não conseguir completar um fluxo essencial) em relação a problemas cosméticos.
* Ofereça alternativas de contorno quando possível.
* Feche o ciclo: confirme as correções com quem relatou, se a pessoa estiver disposta.

## Teste a acessibilidade continuamente

Ferramentas automatizadas pegam regressões, mas o teste manual é o que constrói confiança de verdade.

### Verificações automatizadas (boas para pegar regressões)

* Linting de acessibilidade no código de UI.
* Varredura automatizada no CI para falhas comuns de WCAG (como o [GitHub Accessibility Scanner](https://github.com/github/accessibility-scanner)).
* Testes de unidade/integração que verifiquem [roles/names](https://www.w3.org/TR/accname-1.2/) dos componentes principais.

### Teste manual (necessário para confiança de verdade)

* Passagem **somente com teclado**: você consegue operar os fluxos principais da sua experiência sem mouse?
* Verificação pontual com **leitor de tela**:
  * macOS: [VoiceOver](https://support.apple.com/guide/voiceover/welcome/mac)
  * Windows: [NVDA](https://www.nvaccess.org/about-nvda/) (comum no open source), [JAWS](https://vispero.com/jaws-screen-reader-software/) (corporativo)
* **Zoom e reflow**: teste com 200% e com larguras estreitas.
* Modos de **alto contraste / cores forçadas**, quando aplicável.

**Dica:** adicione uma seção leve de "[smoke test](https://en.wikipedia.org/wiki/Smoke_testing_(software)) de acessibilidade" ao seu checklist de release.

## Comece com pequenas vitórias esta semana

### Você não precisa fazer tudo de uma vez; comece com algumas melhorias rápidas.

Escolha algumas:

* Adicione um `ACCESSIBILITY.md` e uma label de acessibilidade (como _"accessibility"_ ou _"a11y"_)
* Garanta que todo elemento interativo seja alcançável por teclado
* Corrija rótulos de formulário ausentes
* Declare o **idioma** do seu documento (como `lang="en"` no HTML) e marque quaisquer seções em um idioma diferente
* Adicione texto alternativo e estrutura de títulos ao README e à documentação
* Adicione um item de checklist de teclado/foco aos PRs
* Adicione legendas/transcrição ao seu vídeo mais popular
* Adicione saída `--json` a um comando da CLI

### Sugestões de arquivos para ajudar a formalizar o seu compromisso com a acessibilidade.

Considere adicionar ao seu repositório:

* `ACCESSIBILITY.md`: sua declaração de acessibilidade, como relatar problemas e qualquer orientação específica do projeto (regras de componentes, padrões, problemas conhecidos) — [exemplo de ACCESSIBILITY.md](https://github.com/open-source-accessibility/accessibility-toolkit/blob/main/ACCESSIBILITY.md)
* `.github/ISSUE_TEMPLATE/accessibility.yml`: relatos de bugs de acessibilidade — [exemplo de template de issue de acessibilidade](https://github.com/open-source-accessibility/accessibility-toolkit/blob/main/.github/ISSUE_TEMPLATE/accessibility.yml)
* `.github/pull_request_template.md`: inclua um checklist de a11y — [exemplo de template de PR](https://github.com/open-source-accessibility/accessibility-toolkit/blob/main/.github/PULL_REQUEST_TEMPLATE.md)

Consulte este [projeto para exemplos adicionais](https://github.com/mgifford/ACCESSIBILITY.md/tree/main).

## Conclusão: alguns passos para você, uma melhoria enorme para os seus usuários

Estes passos podem parecer básicos, mas fazem muita diferença para tornar o seu projeto mais acessível. Cada correção que você faz — seja um rótulo ausente, uma armadilha de teclado ou a legenda de um vídeo — abre a porta para alguém que antes não conseguia usar o seu projeto.

Acessibilidade não é uma correção única; é uma prática contínua, e você não precisa fazer tudo de uma vez. Comece pela navegação por teclado e pela semântica, mantenha as mudanças pequenas e peça revisão cedo.

O trabalho que você investe hoje significa que mais pessoas poderão aprender com o que você constrói, contribuir e depender dele. É uma vitória que vale a pena celebrar.

## Contribuidores

### Muito obrigado a todos os mantenedores que compartilharam suas experiências e dicas conosco para este guia!

Este guia foi escrito por [@mlama007](https://github.com/mlama007), com contribuições de: [@ericwbailey](https://github.com/ericwbailey), [@andyfeller](https://github.com/andyfeller), [@mgifford](https://github.com/mgifford), [smockle](https://github.com/smockle) e [weboverhauls](https://github.com/weboverhauls)
