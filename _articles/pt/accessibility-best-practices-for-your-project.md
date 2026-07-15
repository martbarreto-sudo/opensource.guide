---
lang: pt
title: Melhores Práticas de Acessibilidade para o seu Projeto
description: Passos práticos e acionáveis para tornar o seu projeto open source utilizável por todos, especialmente pessoas com deficiência.
class: accessibility-best-practices
order: -1
image: /assets/images/cards/accessibility-best-practices.png
---

Acessibilidade (muitas vezes abreviada como _a11y_) significa que as pessoas conseguem usar o seu projeto independentemente de deficiência, tecnologia assistiva, ambiente ou dispositivo. Isso inclui — mas não se limita a — suporte a leitores de tela, navegação apenas por teclado, legendas/transcrições, contraste de cor suficiente e estrutura de conteúdo clara.

## Faça parceria com pessoas com deficiência

**"Nada sobre nós sem nós"** — A coisa mais importante que você pode fazer pela acessibilidade é colocar no centro as pessoas a quem ela serve. Usuários, contribuidores e testadores com deficiência entendem as barreiras de formas que diretrizes e ferramentas automatizadas não conseguem. Busque a experiência vivida dessas pessoas cedo e com frequência.

### Colocando em prática

Decisões tomadas sem as pessoas afetadas por elas tendem a errar o alvo. Construir com pessoas com deficiência, em vez de para elas, leva a um software melhor para todos.

Aqui estão algumas formas de colocar a experiência vivida no centro:

* Convide contribuidores com deficiência para as discussões de design, não apenas para a triagem de bugs.
* Envolva pessoas com deficiência em testes de usabilidade e feedback sempre que possível.
* Escute quando alguém descreve como usa o seu projeto, mesmo quando isso desafia as suas suposições.
* Trate os relatos de acessibilidade como expertise, não como reclamações — eles podem representar mais pessoas do que você imagina.

### A acessibilidade beneficia todo mundo

* **Ela impacta muita gente.** Estima-se que 1,3 bilhão de pessoas (1 em cada 6) vivenciam alguma deficiência significativa, segundo a [Organização Mundial da Saúde](https://www.who.int/news-room/fact-sheets/detail/disability-and-health).
* **Ela faz parte da qualidade.** Produtos acessíveis tendem a ser mais utilizáveis para todos.
* **Ela reduz a carga de suporte.** Interfaces e documentação mais claras significam menos usuários confusos.
* **Ela amplia a sua base de contribuidores.** Usuários de tecnologia assistiva conseguem participar de forma mais plena.
* **Ela impulsiona a inovação.** Projetar para necessidades diversas muitas vezes leva a recursos que beneficiam todos (legendas, controle por voz e o modo escuro, por exemplo, começaram todos como soluções de acessibilidade).
* **Muitas vezes ela é obrigatória.** Muitas organizações (e alguns governos) exigem acessibilidade para compras e conformidade.
* **Nosso futuro é incerto.** Ninguém hoje pode ter certeza sobre as capacidades que teremos amanhã.

## Comece com uma declaração de acessibilidade

Antes de mergulhar no código, reserve um momento para documentar o compromisso do seu projeto com a acessibilidade. Uma declaração de acessibilidade sinaliza a usuários e contribuidores que a acessibilidade é uma prioridade, não algo deixado para depois. Para orientações, consulte o [guia da W3C para elaborar uma declaração de acessibilidade](https://www.w3.org/WAI/planning/statements/).

Adicione uma declaração clara que alinhe expectativas e facilite o relato de problemas pelos usuários. Você pode incluir uma seção de acessibilidade diretamente no seu README ou criar um arquivo dedicado **ACCESSIBILITY.md** e vinculá-lo a partir do README para dar visibilidade. Veja este [exemplo de ACCESSIBILITY.md](https://github.com/open-source-accessibility/accessibility-toolkit/blob/main/ACCESSIBILITY.md).

### Objetivos

* Declare objetivos mensuráveis (como o [WCAG AA](https://www.w3.org/TR/WCAG22/#wcag-2-layers-of-guidance), quando viável).
* As prioridades principais e como você as atende (suporte a teclado e leitor de tela, legendas e transcrições etc.).
* Quaisquer limitações conhecidas e soluções alternativas (se houver).

### Requisitos para contribuidores

Estabeleça diretrizes claras para que os contribuidores saibam o que se espera:

* **Testes:** todas as mudanças de interface devem ser testadas com uma ferramenta de teste de acessibilidade (como o [Axe DevTools](https://www.deque.com/axe/devtools/extension/#:~:text=Try%20Axe%20DevTools%20Extension%20in%20your%20browser%20of%20choice)).
* **Documentação:** siga as diretrizes de acessibilidade do seu projeto para componentes como SVGs, imagens e elementos interativos.
* **CI/CD:** os PRs falharão se introduzirem violações detectadas pelo workflow de linting de acessibilidade.

### Ambientes suportados

* Liste as plataformas que você suporta (web, web mobile, iOS, Android, terminal/CLI, aplicativos desktop).
* Liste quaisquer observações de suporte parcial.

### Relatando bugs de acessibilidade

* Peça que as pessoas abram issues usando o template de issue de acessibilidade.
* **Dica:** alinhe expectativas com honestidade (por exemplo, "Estamos trabalhando nisso — acompanhando em ISSUE-123"); reconheça os relatos e ofereça retorno ou solução alternativa quando possível.

#### Por que separar a acessibilidade do seu processo geral de issues?

Os usuários passaram a esperar uma declaração de acessibilidade dedicada e um caminho próprio para relatos — é uma convenção bem estabelecida no setor privado e em sites de governo, e muitos usuários procuram por isso primeiro quando esbarram em uma barreira. Manter a acessibilidade separada do seu fluxo geral de issues importa porque:

* **O impacto é urgente.** Um bug de acessibilidade pode impedir completamente que um usuário use o seu projeto, não apenas incomodá-lo. Um caminho dedicado ajuda esses problemas relatados a passarem pela triagem mais rápido.
* **O contexto é diferente.** Problemas de acessibilidade relatados precisam de informações específicas (tecnologia assistiva, SO, navegador, severidade) que um template de bug genérico não solicita.
* **Ela sinaliza compromisso.** Uma declaração visível e separada diz a usuários e contribuidores que a acessibilidade é uma preocupação de primeira classe, não algo diluído em "outros bugs".
* **Quem relata pode usar tecnologia assistiva para registrar o próprio relato.** Um processo claro e previsível (um arquivo conhecido, um rótulo conhecido, um template conhecido) reduz o atrito para as pessoas mais afetadas.

## Torne a documentação acessível por padrão

A documentação costuma ser a primeira "interface" que os usuários tocam. Garanta que todos consigam lê-la.

### Estrutura e semântica

* Use uma **hierarquia lógica de títulos** e não pule níveis (`#`, `##`, `###`, `####`, `#####` e `######`).
* Use **texto de link único e descritivo** ("Leia o guia de contribuição" em vez de "clique aqui").
* Use linguagem simples, evitando jargões e explicando qualquer abreviação na primeira vez em que ela for usada.
* [Use **listas de verdade**](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax#lists) em vez de numeração digitada manualmente.
* Mantenha **a ajuda e a navegação em locais consistentes** entre as páginas, para que os usuários as encontrem de forma previsível.
* Evite transmitir significado apenas por posição ou estilo ("veja o texto vermelho à direita").

### Imagens, diagramas e vídeos

* Forneça **texto alternativo** significativo (muitas vezes abreviado como "alt text") para imagens (consulte a [árvore de decisão de alt da W3C](https://www.w3.org/WAI/tutorials/images/decision-tree/)).
* Em vez de usar imagens de texto, use texto de verdade sempre que possível.
* Para imagens complexas (como diagramas de arquitetura), inclua uma **alternativa textual** adicional por perto (uma lista de tópicos ou uma explicação curta).
* Se você publica demos, tutoriais, palestras ou vídeos de lançamento:
  * Forneça **legendas** (prefira as editadas por humanos quando possível).
  * Forneça uma **transcrição**.
  * Evite reprodução automática de áudio e vídeo.
  * Descreva verbalmente as ações importantes que acontecem na tela.

### Tabelas

* Use tabelas apenas para dados tabulares, não para layout.
* Inclua **células de cabeçalho** (`<th>`) e use atributos `scope` para associar os cabeçalhos às células de dados.
* Forneça uma **legenda ou resumo** descrevendo o propósito da tabela.

### Blocos de código

* Mantenha as linhas razoavelmente curtas (a quebra de linha ajuda na legibilidade).
* Não dependa apenas do destaque por cor para indicar significado.
* Explique no texto o que o código faz e como é um resultado bem-sucedido.

## Projete interfaces acessíveis

Se o seu projeto tem uma interface web, estes padrões de alto impacto vão ajudar todos os usuários.

### Suporte a teclado

* Tudo que é interativo deve ser alcançável e utilizável **apenas com o teclado**.
* Garanta um **indicador de foco visível** (não remova os contornos de foco a menos que você os substitua).
* Mantenha uma **ordem de tabulação** lógica que corresponda ao layout visual.
* Não prenda o foco dentro de componentes, a menos que você gerencie o foco intencionalmente (como em diálogos modais) e ofereça uma saída.

### Semântica primeiro

* Use elementos HTML nativos (`<h1>`, `<button>`, `<a>`, `<input>`, `<label>`) sempre que possível.
* Use ARIA apenas quando o HTML nativo não for suficiente. Nenhum ARIA é melhor do que um ARIA ruim. Quando usar, siga a [documentação do Accessible Rich Internet Applications (ARIA)](https://www.w3.org/TR/wai-aria/) e garanta que todos os controles ARIA interativos sejam acessíveis por teclado.
* Declare o **idioma** do seu documento (como `lang="pt"` no HTML) e marque quaisquer trechos em outro idioma.

### Nomes, rótulos e instruções

* Todo controle de formulário precisa de um **rótulo** (label) associado.
* Forneça **mensagens de erro claras**, indique qual campo tem o erro e associe a mensagem ao campo de forma programática (como com `aria-describedby`).
* Para campos obrigatórios, explique os requisitos em texto (não apenas com um asterisco).

### Cor e contraste

* Não use a cor como único meio de transmitir significado ("os erros são vermelhos").
* Garanta contraste adequado para texto e controles de interface (consulte o [verificador de contraste do WebAIM](https://webaim.org/resources/contrastchecker/)).

### Movimento e animação

* Evite conteúdo piscante e animações rápidas.
* Evite efeitos de parallax e carrosséis que avançam sozinhos, ou torne-os opcionais e controláveis.

### Conteúdo dinâmico

Quando o conteúdo é atualizado sem recarregar a página, garanta que os usuários de tecnologia assistiva sejam informados:

* Use **regiões dinâmicas do ARIA** (ARIA live regions) apropriadas, com moderação, para anúncios.
* Gerencie o foco ao abrir/fechar diálogos, menus e painéis laterais.

### Dependências e padrões

* Use bibliotecas de componentes com suporte a acessibilidade documentado.
* Acompanhe bugs de acessibilidade no upstream e crie links para eles nas suas issues.
* Tenha cautela com controles de interface personalizados. Controles nativos (como `<button>`, `<select>`, `<input type="checkbox">`, `<details>`) já vêm com suporte a teclado, gerenciamento de foco, semântica para leitores de tela e integração com formulários que os navegadores e as tecnologias assistivas já entendem. Recriar esse comportamento em componentes personalizados é trabalhoso, fácil de errar e adiciona custo de manutenção de longo prazo à medida que as plataformas e a tecnologia assistiva evoluem. Recorra a controles personalizados apenas quando um elemento nativo realmente não atender à necessidade.

### Considerações para mobile

* Faça alvos de toque de pelo menos **24×24 pixels CSS**.
* Forneça alternativas de um único ponto para gestos multiponto ou baseados em trajetória (pinça, deslize).
* Ofereça alternativas para operações de arrastar e soltar (botões, menus).
* Não restrinja o conteúdo a uma única orientação de tela, a menos que o conteúdo exibido precise de uma orientação específica.
* Forneça alternativas para recursos acionados pelo movimento do dispositivo (como agitar para desfazer).

## Torne as ferramentas acessíveis

Ferramentas de linha de comando e dashboards podem ser altamente acessíveis quando projetados com cuidado.

### Ferramentas de CLI

Aplicações de linha de comando podem ser altamente acessíveis quando são previsíveis e automatizáveis por scripts.

* Ofereça `--help` com exemplos de uso claros.
* Ofereça opções de **saída legível por máquina** (como `--json`) para usuários que não conseguem interpretar tabelas facilmente.
* Evite depender apenas de cor ANSI para transmitir sucesso/falha; inclua rótulos de texto e códigos de saída.
* Escreva mensagens de erro que:
  * Expliquem o que aconteceu,
  * Mostrem como corrigir e
  * Vinculem à documentação se necessário.
* Use códigos de saída padrão e garanta um valor diferente de zero em caso de falha.

### Terminais, logs e dashboards

* Prefira linguagem simples a jargões.
* Evite abreviações sem explicação.
* Use formatação consistente para os níveis de severidade (`ERROR`, `WARN`, `INFO`) e inclua timestamps quando forem úteis.
* Garanta que o "status" não seja comunicado apenas por cor.

## Incorpore a acessibilidade aos fluxos de contribuição

A acessibilidade é mais fácil de manter quando faz parte do seu processo habitual.

### Adicione rótulos e um template de issue

* Crie um rótulo de acessibilidade (como _"accessibility"_ ou _"a11y"_).
* Crie um template de issue de acessibilidade que inclua:
  * O rótulo _accessibility_
  * Comportamento esperado versus comportamento real
  * Passos para reproduzir (incluindo uma gravação de tela opcional)
  * Ferramentas usadas (SO, navegador, tecnologia assistiva e versão)
  * Uma taxonomia de severidade para ajudar a priorizar os problemas:
    * **Crítica:** impede um usuário de concluir uma tarefa essencial (como "Não consigo finalizar a compra").
    * **Alta:** dificuldade significativa, mas existe uma solução alternativa.
    * **Média:** incômodo ou experiência inconsistente.
    * **Baixa:** problema menor, com impacto mínimo na usabilidade.
  * Instruções de contato ou de escalonamento, se apropriado.

Veja este [exemplo de template de issue de acessibilidade](https://github.com/open-source-accessibility/accessibility-toolkit/blob/main/.github/ISSUE_TEMPLATE/accessibility.yml).

### Adicione um checklist de acessibilidade aos pull requests (PRs)

Para projetos com mudanças de interface, inclua perguntas como:

* A navegação por teclado funciona de ponta a ponta
* Os estados de foco são visíveis e lógicos
* Os formulários têm rótulos e os erros são anunciados
* A cor não é o único indicador
* A preferência por movimento reduzido é respeitada (se foram adicionadas animações)
* O comportamento com leitor de tela foi verificado (ao menos uma vez)

Veja este [exemplo de template de PR](https://github.com/open-source-accessibility/accessibility-toolkit/blob/main/.github/PULL_REQUEST_TEMPLATE.md).

### Defina o "pronto"

Adicione critérios de aceitação de acessibilidade para funcionalidades e correções de bugs, para que ela não seja opcional nem de última hora.

### Aproveite o GitHub Copilot

* Crie agentes especializados do Copilot que automatizam tarefas de acessibilidade no seu workflow de desenvolvimento, desde auditar páginas com o [axe-core](https://github.com/dequelabs/axe-core) até acompanhar melhorias de acessibilidade ao longo dos lançamentos. Consulte o [guia de introdução aos agentes personalizados do GitHub Copilot para acessibilidade](https://accessibility.github.com/documentation/guide/getting-started-with-agents/).
* Ajuste as sugestões do Copilot ao seu estilo de código, às suas práticas de acessibilidade e ao contexto do projeto para garantir que elas estejam alinhadas aos seus requisitos de acessibilidade. Consulte o [guia para otimizar o GitHub Copilot para acessibilidade com instruções personalizadas](https://accessibility.github.com/documentation/guide/copilot-instructions/).

### Trate os problemas de acessibilidade relatados com respeito e eficácia

Os problemas de acessibilidade costumam ser difíceis de descrever, difíceis de reproduzir e urgentes para a capacidade de quem relata usar o seu projeto. Ao lidar com os relatos:

* Agradeça a quem relatou e faça perguntas esclarecedoras sem ceticismo.
* Priorize os bloqueios (não conseguir concluir um fluxo essencial) em vez de problemas cosméticos.
* Ofereça soluções alternativas quando possível.
* Feche o ciclo: confirme as correções com quem relatou, se a pessoa estiver disposta.

## Teste a acessibilidade continuamente

Ferramentas automatizadas detectam regressões, mas o teste manual constrói confiança de verdade.

### Verificações automatizadas (boas para detectar regressões)

* Linting de acessibilidade no código da interface.
* Varredura automatizada no CI em busca de falhas comuns de WCAG (como o [GitHub Accessibility Scanner](https://github.com/github/accessibility-scanner)).
* Testes de unidade/integração que verificam [papéis/nomes](https://www.w3.org/TR/accname-1.2/) dos componentes principais.

### Teste manual (necessário para confiança de verdade)

* Passagem **apenas por teclado**: você consegue operar com sucesso os principais fluxos da sua experiência sem um mouse?
* Verificação pontual com **leitor de tela**:
  * macOS: [VoiceOver](https://support.apple.com/guide/voiceover/welcome/mac)
  * Windows: [NVDA](https://www.nvaccess.org/about-nvda/) (comum no open source), [JAWS](https://vispero.com/jaws-screen-reader-software/) (corporativo)
* **Zoom e reflow**: teste em 200% e com larguras estreitas.
* Modos de **alto contraste / cores forçadas**, quando aplicável.

**Dica:** adicione uma seção leve de "[teste de fumaça](https://en.wikipedia.org/wiki/Smoke_testing_(software)) de acessibilidade" ao seu checklist de lançamento.

## Comece com pequenas vitórias esta semana

### Você não precisa fazer tudo de uma vez; comece com algumas melhorias rápidas.

Escolha algumas:

* Adicione um `ACCESSIBILITY.md` e um rótulo de acessibilidade (como _"accessibility"_ ou _"a11y"_)
* Garanta que todo elemento interativo seja alcançável por teclado
* Corrija rótulos de formulário ausentes
* Declare o **idioma** do seu documento (como `lang="pt"` no HTML) e marque quaisquer trechos em outro idioma
* Adicione texto alternativo e estrutura de títulos ao README e à documentação
* Adicione um item de checklist de PR para teclado/foco
* Adicione legendas/transcrição ao seu vídeo mais popular
* Adicione saída `--json` a um comando de CLI

### Arquivos sugeridos para ajudar a formalizar o seu compromisso com a acessibilidade.

Considere adicionar estes ao seu repositório:

* `ACCESSIBILITY.md`: a sua declaração de acessibilidade, como relatar problemas e quaisquer orientações específicas do projeto (regras de componentes, padrões, problemas conhecidos) — [exemplo de ACCESSIBILITY.md](https://github.com/open-source-accessibility/accessibility-toolkit/blob/main/ACCESSIBILITY.md)
* `.github/ISSUE_TEMPLATE/accessibility.yml`: relatos de bugs de acessibilidade — [exemplo de template de issue de acessibilidade](https://github.com/open-source-accessibility/accessibility-toolkit/blob/main/.github/ISSUE_TEMPLATE/accessibility.yml)
* `.github/pull_request_template.md`: inclua um checklist de a11y — [exemplo de template de PR](https://github.com/open-source-accessibility/accessibility-toolkit/blob/main/.github/PULL_REQUEST_TEMPLATE.md)

Veja este [projeto com exemplos adicionais](https://github.com/mgifford/ACCESSIBILITY.md/tree/main).

## Conclusão: alguns passos para você, uma enorme melhoria para seus usuários

Esses passos podem parecer básicos, mas fazem uma grande diferença para tornar o seu projeto mais acessível. Cada correção que você faz — seja um rótulo ausente, uma armadilha de foco de teclado ou uma legenda em um vídeo — abre a porta para alguém que não conseguia usar o seu projeto antes.

Acessibilidade não é uma correção única, é uma prática contínua, e você não precisa fazer tudo de uma vez. Comece pela navegação por teclado e pela semântica, mantenha as mudanças pequenas e peça revisão cedo.

O trabalho que você faz hoje significa que mais pessoas podem aprender com, contribuir para e confiar naquilo que você constrói. Essa é uma vitória que vale a pena celebrar.

## Colaboradores

### Muito obrigado a todos os mantenedores que compartilharam suas experiências e dicas conosco para este guia!

Este guia foi escrito por [@mlama007](https://github.com/mlama007) com contribuições de: [@ericwbailey](https://github.com/ericwbailey), [@andyfeller](https://github.com/andyfeller), [@mgifford](https://github.com/mgifford), [smockle](https://github.com/smockle) e [weboverhauls](https://github.com/weboverhauls)
