---
lang: pt
title: Boas Práticas de Segurança para o Seu Projeto
description: Fortaleça o futuro do seu projeto construindo confiança por meio de práticas essenciais de segurança — da MFA e da verificação de código à gestão segura de dependências e ao relato privado de vulnerabilidades.
class: security-best-practices
order: -1
image: /assets/images/cards/security-best-practices.png
---

Deixando de lado bugs e novas funcionalidades, a longevidade de um projeto depende não só da sua utilidade, mas também da confiança que ele conquista dos usuários. Medidas fortes de segurança são importantes para manter essa confiança viva. Aqui estão algumas ações importantes que você pode tomar para melhorar significativamente a segurança do seu projeto.

## Garanta que todos os contribuidores privilegiados tenham habilitado a Autenticação Multifator (MFA)

### Um agente malicioso que consiga se passar por um contribuidor privilegiado do seu projeto causará danos catastróficos.

Uma vez obtido o acesso privilegiado, esse agente pode modificar o seu código para que ele execute ações indesejadas (por exemplo, minerar criptomoedas), distribuir malware para a infraestrutura dos seus usuários ou acessar repositórios de código privados para exfiltrar propriedade intelectual e dados sensíveis, incluindo credenciais de outros serviços.

A MFA fornece uma camada adicional de segurança contra o sequestro de contas. Com ela habilitada, você precisa entrar com o seu usuário e senha e fornecer outra forma de autenticação que só você conhece ou à qual só você tem acesso.

## Proteja o seu código como parte do fluxo de desenvolvimento

### Vulnerabilidades de segurança no seu código são mais baratas de corrigir quando detectadas cedo no processo do que mais tarde, quando já estão sendo exploradas em produção.

Use uma ferramenta de Static Application Security Testing (SAST) para detectar vulnerabilidades de segurança no seu código. Essas ferramentas operam no nível do código e não precisam de um ambiente de execução; portanto, podem rodar cedo no processo e se integrar naturalmente ao seu fluxo habitual de desenvolvimento, durante o build ou durante o code review.

É como ter um especialista habilidoso revisando o seu repositório, ajudando a encontrar vulnerabilidades comuns que podem estar escondidas à vista de todos enquanto você programa.

Como escolher a sua ferramenta SAST?
Verifique a licença: algumas ferramentas são gratuitas para projetos open source. Por exemplo, GitHub CodeQL ou SemGrep.
Verifique a cobertura para a(s) sua(s) linguagem(ns)

* Escolha uma que se integre facilmente às ferramentas que você já usa, ao seu processo existente. Por exemplo, é melhor que os alertas apareçam dentro do seu processo e ferramenta atuais de code review, em vez de você precisar ir a outra ferramenta para vê-los.
* Cuidado com os falsos positivos! Você não quer que a ferramenta atrase o seu trabalho sem motivo!
* Verifique os recursos: algumas ferramentas são muito poderosas e fazem taint tracking (exemplo: GitHub CodeQL), algumas propõem sugestões de correção geradas por IA, outras facilitam a escrita de consultas personalizadas (exemplo: SemGrep).

## Não compartilhe os seus segredos

### Dados sensíveis, como chaves de API, tokens e senhas, às vezes acabam sendo enviados acidentalmente em um commit para o seu repositório.

Imagine este cenário: você é a pessoa mantenedora de um projeto open source popular, com contribuições de desenvolvedores do mundo todo. Um dia, um contribuidor, sem perceber, faz um commit no repositório com chaves de API de um serviço de terceiros. Dias depois, alguém encontra essas chaves e as usa para entrar no serviço sem permissão. O serviço é comprometido, os usuários do seu projeto enfrentam indisponibilidade e a reputação do projeto sofre um golpe. Como mantenedor, você agora encara as tarefas árduas de revogar os segredos comprometidos, investigar que ações maliciosas o invasor pode ter executado com aquele segredo, notificar os usuários afetados e implementar correções.

Para prevenir incidentes assim, existem soluções de "secret scanning" (verificação de segredos) que ajudam a detectar esses segredos no seu código. Algumas ferramentas, como o GitHub Secret Scanning e o Trufflehog, da Truffle Security, podem impedir que você os envie para branches remotas logo de início, e algumas revogam automaticamente certos segredos para você.

## Verifique e atualize as suas dependências

### As dependências do seu projeto podem ter vulnerabilidades que comprometem a segurança dele. Manter as dependências atualizadas manualmente pode consumir muito tempo.

Visualize a cena: um projeto construído sobre a fundação sólida de uma biblioteca amplamente usada. Mais tarde, a biblioteca descobre um problema grave de segurança, mas as pessoas que construíram a aplicação usando essa biblioteca não ficam sabendo. Dados sensíveis de usuários ficam expostos quando um invasor se aproveita dessa fraqueza e os captura. Isso não é um caso teórico: foi exatamente o que aconteceu com a Equifax em 2017. Eles deixaram de atualizar a dependência do Apache Struts depois da notificação de que uma vulnerabilidade severa havia sido detectada. Ela foi explorada, e a infame violação da Equifax afetou os dados de 144 milhões de usuários.

Para prevenir cenários assim, ferramentas de Software Composition Analysis (SCA), como o Dependabot e o Renovate, verificam automaticamente as suas dependências em busca de vulnerabilidades conhecidas publicadas em bases públicas, como a NVD ou o GitHub Advisory Database, e então criam pull requests para atualizá-las para versões seguras. Manter-se em dia com as versões seguras mais recentes das dependências protege o seu projeto de riscos potenciais.

## Entenda e gerencie os riscos de licenças open source

### Licenças open source vêm com termos, e ignorá-los pode gerar riscos jurídicos e de reputação.

Usar dependências open source pode acelerar o desenvolvimento, mas cada pacote inclui uma licença que define como ele pode ser usado, modificado ou distribuído. [Algumas licenças são permissivas](https://opensource.guide/legal/#which-open-source-license-is-appropriate-for-my-project), enquanto outras (como AGPL ou SSPL) impõem restrições que podem não ser compatíveis com os objetivos do seu projeto ou com as necessidades dos seus usuários.

Imagine: você adiciona uma biblioteca poderosa ao seu projeto sem saber que ela usa uma licença restritiva. Mais tarde, uma empresa quer adotar o seu projeto, mas levanta preocupações sobre conformidade de licenças. O resultado? Você perde adoção, precisa refatorar código e a reputação do projeto sofre um golpe.

Para evitar essas armadilhas, considere incluir verificações automatizadas de licença no seu fluxo de desenvolvimento. Essas verificações ajudam a identificar licenças incompatíveis cedo no processo, impedindo que dependências problemáticas entrem no seu projeto.

Outra abordagem poderosa é gerar um Software Bill of Materials (SBOM). Um SBOM lista todos os componentes e seus metadados (incluindo licenças) em um formato padronizado. Ele oferece visibilidade clara da sua cadeia de suprimentos de software e ajuda a expor riscos de licenciamento de forma proativa.

Assim como as vulnerabilidades de segurança, problemas de licença são mais fáceis de resolver quando descobertos cedo. Automatizar esse processo mantém o seu projeto saudável e seguro.

## Evite mudanças indesejadas com branches protegidas

### Acesso irrestrito às suas branches principais pode levar a mudanças acidentais ou maliciosas que introduzam vulnerabilidades ou comprometam a estabilidade do projeto.

Um novo contribuidor recebe acesso de escrita à branch principal e, sem querer, envia mudanças que não foram testadas. Uma falha grave de segurança é então descoberta, cortesia das mudanças mais recentes. Para prevenir esse tipo de problema, as regras de proteção de branch garantem que mudanças não possam ser enviadas ou mescladas em branches importantes sem antes passar por revisões e pelas verificações de status especificadas. Você fica mais seguro e em melhor situação com essa medida extra, garantindo qualidade de primeira a cada mudança.

## Facilite (com segurança) o relato de problemas de segurança

### É uma boa prática facilitar que os seus usuários relatem bugs, mas a grande questão é: quando o bug tem impacto de segurança, como eles podem relatá-lo com segurança sem colocar um alvo nas suas costas para hackers maliciosos?

Visualize: uma pessoa pesquisadora de segurança descobre uma vulnerabilidade no seu projeto, mas não encontra um caminho claro e seguro para relatá-la. Sem um processo definido, ela pode abrir uma issue pública ou discutir o assunto abertamente nas redes sociais. Mesmo que seja bem-intencionada e ofereça uma correção, se o fizer com um pull request público, outras pessoas verão antes do merge! Essa divulgação pública expõe a vulnerabilidade a agentes maliciosos antes que você tenha a chance de corrigi-la, podendo levar a um exploit de zero-day, atacando o seu projeto e os seus usuários.

### Política de Segurança

Para evitar isso, publique uma política de segurança. Uma política de segurança, definida em um arquivo `SECURITY.md`, detalha os passos para relatar preocupações de segurança, criando um processo transparente de divulgação coordenada e estabelecendo as responsabilidades da equipe do projeto no tratamento dos relatos. Essa política pode ser tão simples quanto "Por favor, não publique detalhes em uma issue ou PR públicos; envie um e-mail privado para security@example.com", mas também pode conter outros detalhes, como quando a pessoa deve esperar receber uma resposta sua. Tudo que puder ajudar a eficácia e a eficiência do processo de divulgação.

### Relato Privado de Vulnerabilidades

Em algumas plataformas, você pode simplificar e fortalecer o seu processo de gestão de vulnerabilidades, da entrada à divulgação, com issues privadas. No GitLab, isso pode ser feito com issues privadas. No GitHub, isso se chama private vulnerability reporting (PVR). O PVR permite que mantenedores recebam e tratem relatos de vulnerabilidade inteiramente dentro da plataforma do GitHub. O GitHub criará automaticamente um fork privado para escrever as correções e um rascunho de aviso de segurança (security advisory). Tudo isso permanece confidencial até que você decida divulgar os problemas e publicar as correções. Para fechar o ciclo, os avisos de segurança serão publicados e informarão e protegerão todos os seus usuários por meio da ferramenta de SCA deles.

### Defina o seu modelo de ameaças para ajudar usuários e pesquisadores a entender o escopo

Antes que pesquisadores de segurança possam relatar problemas de forma eficaz, eles precisam entender quais riscos estão no escopo. Um modelo de ameaças leve pode ajudar a definir as fronteiras do seu projeto, o comportamento esperado e as premissas.

Um modelo de ameaças não precisa ser complexo. Mesmo um documento simples descrevendo o que o seu projeto faz, em que ele confia e como ele poderia ser mal utilizado já ajuda muito. Ele também ajuda você, como mantenedor, a refletir sobre armadilhas potenciais e riscos herdados de dependências upstream.

Um ótimo exemplo é o [modelo de ameaças do Node.js](https://github.com/nodejs/node/security/policy#the-nodejs-threat-model), que define com clareza o que é e o que não é considerado vulnerabilidade no contexto do projeto.

Se você é novo nisso, o [Threat Modeling Process da OWASP](https://owasp.org/www-community/Threat_Modeling_Process) oferece uma introdução útil para construir o seu.

Publicar um modelo de ameaças básico junto com a sua política de segurança melhora a clareza para todo mundo.

## Prepare um processo leve de resposta a incidentes

### Ter um plano básico de resposta a incidentes ajuda você a manter a calma e agir com eficiência, garantindo a segurança dos seus usuários e consumidores.

A maioria das vulnerabilidades é descoberta por pesquisadores e relatada em privado. Mas, às vezes, um problema já está sendo explorado ativamente antes de chegar até você. Quando isso acontece, quem está em risco são os seus consumidores downstream, e ter um plano de resposta a incidentes leve e bem definido pode fazer uma diferença crítica.

<aside markdown="1" class="pquote">
  <img src="https://avatars.githubusercontent.com/ulisesgascon?s=180" class="pquote-avatar" alt="avatar">
  Uma vulnerabilidade é basicamente uma falha, uma configuração insegura ou um ponto fraco no nosso sistema que pode ser explorado por terceiros para provocar comportamentos não intencionais.
  <p markdown="1" class="pquote-credit">
— [@UlisesGascon](https://github.com/ulisesgascon), ["What is a Vulnerability and What's Not? Making Sense of Node.js and Express Threat Models"](https://gitnation.com/contents/what-is-a-vulnerability-and-whats-not-making-sense-of-nodejs-and-express-threat-models)
  </p>
</aside>

Mesmo quando uma vulnerabilidade é relatada em privado, os próximos passos importam. Depois que você recebe um relato de vulnerabilidade ou detecta atividade suspeita, o que acontece em seguida?

Ter um plano básico de resposta a incidentes, mesmo que seja um checklist simples, ajuda você a manter a calma e agir com eficiência quando o tempo importa. Também mostra a usuários e pesquisadores que você leva incidentes e relatos a sério.

O seu processo não precisa ser complexo. No mínimo, defina:

* Quem revisa e faz a triagem de relatos ou alertas de segurança
* Como a severidade é avaliada e como as decisões de mitigação são tomadas
* Que passos você segue para preparar uma correção e coordenar a divulgação
* Como você notifica usuários afetados, contribuidores ou consumidores downstream

Um incidente ativo, se mal gerenciado, pode corroer a confiança dos usuários no seu projeto. Publicar esse plano (ou um link para ele) no seu arquivo `SECURITY.md` ajuda a estabelecer expectativas e a construir confiança.

Para inspiração, o [WG de Segurança do Express.js](https://github.com/expressjs/security-wg/blob/main/docs/incident_response_plan.md) oferece um exemplo simples, porém eficaz, de plano open source de resposta a incidentes.

Esse plano pode evoluir conforme o projeto cresce, mas ter uma estrutura básica desde já pode economizar tempo e reduzir erros durante um incidente real.

## Trate a segurança como um esforço de equipe

### Segurança não é uma responsabilidade solitária. Ela funciona melhor quando é compartilhada pela comunidade do projeto.

Embora ferramentas e políticas sejam essenciais, uma postura forte de segurança nasce da forma como a sua equipe e os contribuidores trabalham juntos. Construir uma cultura de responsabilidade compartilhada ajuda o projeto a identificar, triar e responder a vulnerabilidades com mais rapidez e eficácia.

Aqui estão algumas formas de fazer da segurança um esporte de equipe:

* **Atribua papéis claros**: saiba quem cuida dos relatos de vulnerabilidade, quem revisa as atualizações de dependências e quem aprova os patches de segurança.
* **Limite o acesso usando o princípio do menor privilégio**: conceda acesso de escrita ou administração apenas a quem realmente precisa e revise as permissões regularmente.
* **Invista em educação**: incentive os contribuidores a aprender práticas de código seguro, tipos comuns de vulnerabilidade e como usar as suas ferramentas (como SAST ou secret scanning).
* **Fomente diversidade e colaboração**: uma equipe heterogênea traz um conjunto mais amplo de experiências, consciência de ameaças e criatividade na resolução de problemas. Também ajuda a revelar riscos que outros poderiam não notar.
* **Engaje-se upstream e downstream**: as suas dependências podem afetar a sua segurança, e o seu projeto afeta outros. Participe da divulgação coordenada com mantenedores upstream e mantenha os usuários downstream informados quando vulnerabilidades forem corrigidas.

Segurança é um processo contínuo, não uma configuração única. Ao envolver a sua comunidade, incentivar práticas seguras e apoiar uns aos outros, você constrói um projeto mais forte e resiliente e um ecossistema mais seguro para todo mundo.

## Conclusão: alguns passos para você, uma melhoria enorme para os seus usuários

Estes poucos passos podem parecer fáceis ou básicos, mas fazem muita diferença para tornar o seu projeto mais seguro para os usuários, porque oferecem proteção contra os problemas mais comuns.

Segurança não é estática. Revisite os seus processos de tempos em tempos. À medida que o seu projeto cresce, crescem também as suas responsabilidades e a sua superfície de ataque.

## Contribuidores

### Muito obrigado a todos os mantenedores que compartilharam suas experiências e dicas conosco para este guia!

Este guia foi escrito por [@nanzggits](https://github.com/nanzggits) e [@xcorail](https://github.com/xcorail), com contribuições de:

[@JLLeitschuh](https://github.com/JLLeitschuh), [@intrigus-lgtm](https://github.com/intrigus-lgtm), [@UlisesGascon](https://github.com/ulisesgascon) + muitas outras pessoas!
