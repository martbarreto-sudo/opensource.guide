---
lang: pt
title: Melhores Práticas de Segurança para o seu Projeto
description: Fortaleça o futuro do seu projeto construindo confiança por meio de práticas essenciais de segurança — de MFA e varredura de código à gestão segura de dependências e ao relato privado de vulnerabilidades.
class: security-best-practices
order: -1
image: /assets/images/cards/security-best-practices.png
---

Bugs e novas funcionalidades à parte, a longevidade de um projeto depende não só da sua utilidade, mas também da confiança que ele conquista de seus usuários. Medidas de segurança robustas são importantes para manter essa confiança viva. Aqui estão algumas ações importantes que você pode adotar para melhorar significativamente a segurança do seu projeto.

## Garanta que todos os contribuidores com privilégios tenham ativado a Autenticação Multifator (MFA)

### Um agente malicioso que consiga se passar por um contribuidor com privilégios no seu projeto causará danos catastróficos.

Uma vez que obtém o acesso privilegiado, esse agente pode modificar o seu código para que ele execute ações indesejadas (por exemplo, minerar criptomoedas), ou distribuir malware para a infraestrutura dos seus usuários, ou ainda acessar repositórios de código privados para exfiltrar propriedade intelectual e dados sensíveis, incluindo credenciais de outros serviços.

A MFA fornece uma camada adicional de segurança contra o sequestro de contas. Uma vez ativada, você precisa entrar com seu nome de usuário e senha e fornecer outra forma de autenticação que só você conhece ou à qual só você tem acesso.

## Proteja seu código como parte do seu workflow de desenvolvimento

### Vulnerabilidades de segurança no seu código são mais baratas de corrigir quando detectadas cedo no processo do que mais tarde, quando já estão em produção.

Use uma ferramenta de Teste Estático de Segurança de Aplicações (SAST) para detectar vulnerabilidades de segurança no seu código. Essas ferramentas operam no nível do código e não precisam de um ambiente de execução e, portanto, podem ser executadas cedo no processo e integradas de forma transparente ao seu workflow habitual de desenvolvimento, durante o build ou durante as fases de revisão de código.

É como ter um especialista experiente examinando o seu repositório de código, ajudando você a encontrar vulnerabilidades de segurança comuns que poderiam estar escondidas à vista de todos enquanto você programa.

Como escolher a sua ferramenta SAST?
Verifique a licença: algumas ferramentas são gratuitas para projetos open source. Por exemplo, GitHub CodeQL ou SemGrep.
Verifique a cobertura para a(s) sua(s) linguagem(ns)

* Escolha uma que se integre facilmente às ferramentas que você já usa, ao seu processo atual. Por exemplo, é melhor que os alertas apareçam como parte do seu processo e ferramenta de revisão de código já existentes, em vez de você ter que ir a outra ferramenta para vê-los.
* Cuidado com os falsos positivos! Você não quer que a ferramenta te atrase sem motivo!
* Verifique os recursos: algumas ferramentas são muito poderosas e fazem rastreamento de contaminação (taint tracking) (exemplo: GitHub CodeQL), algumas propõem sugestões de correção geradas por IA, e outras facilitam a escrita de consultas personalizadas (exemplo: SemGrep).

## Não compartilhe seus secrets

### Dados sensíveis, como chaves de API, tokens e senhas, às vezes podem acabar sendo commitados acidentalmente no seu repositório.

Imagine este cenário: você é o mantenedor de um projeto open source popular, com contribuições de desenvolvedores do mundo todo. Um dia, um contribuidor, sem perceber, faz commit no repositório de algumas chaves de API de um serviço de terceiros. Dias depois, alguém encontra essas chaves e as usa para acessar o serviço sem permissão. O serviço é comprometido, os usuários do seu projeto sofrem com indisponibilidade e a reputação do seu projeto é abalada. Como mantenedor, você agora enfrenta as árduas tarefas de revogar os secrets comprometidos, investigar quais ações maliciosas o atacante pode ter realizado com esse secret, notificar os usuários afetados e implementar correções.

Para evitar esses incidentes, existem soluções de "secret scanning" que ajudam você a detectar esses secrets no seu código. Algumas ferramentas, como o GitHub Secret Scanning e o Trufflehog, da Truffle Security, podem impedir que você faça push deles para branches remotos logo de início, e algumas ferramentas revogam automaticamente alguns secrets para você.

## Verifique e atualize suas dependências

### As dependências do seu projeto podem ter vulnerabilidades que comprometem a segurança dele. Manter as dependências atualizadas manualmente pode ser uma tarefa demorada.

Imagine o seguinte: um projeto construído sobre a base sólida de uma biblioteca amplamente utilizada. Mais tarde, a biblioteca descobre um grande problema de segurança, mas as pessoas que construíram a aplicação usando-a não ficam sabendo. Dados sensíveis dos usuários ficam expostos quando um atacante se aproveita dessa fraqueza, agindo rápido para capturá-los. Este não é um caso teórico. Foi exatamente o que aconteceu com a Equifax em 2017: eles não atualizaram sua dependência do Apache Struts após a notificação de que uma vulnerabilidade grave havia sido detectada. Ela foi explorada, e o infame vazamento da Equifax afetou os dados de 144 milhões de usuários.

Para evitar esses cenários, ferramentas de Análise de Composição de Software (SCA), como Dependabot e Renovate, verificam automaticamente suas dependências em busca de vulnerabilidades conhecidas publicadas em bancos de dados públicos, como o NVD ou o GitHub Advisory Database, e então criam pull requests para atualizá-las para versões seguras. Manter-se em dia com as versões seguras mais recentes das dependências protege o seu projeto de riscos potenciais.

## Entenda e gerencie os riscos das licenças open source

### As licenças open source vêm com termos, e ignorá-los pode gerar riscos jurídicos e de reputação.

Usar dependências open source pode acelerar o desenvolvimento, mas cada pacote inclui uma licença que define como ele pode ser usado, modificado ou distribuído. [Algumas licenças são permissivas](https://opensource.guide/legal/#which-open-source-license-is-appropriate-for-my-project), enquanto outras (como a AGPL ou a SSPL) impõem restrições que podem não ser compatíveis com os objetivos do seu projeto ou com as necessidades dos seus usuários.

Imagine o seguinte: você adiciona uma biblioteca poderosa ao seu projeto, sem saber que ela usa uma licença restritiva. Mais tarde, uma empresa quer adotar o seu projeto, mas levanta preocupações sobre conformidade de licença. O resultado? Você perde adoção, precisa refatorar o código e a reputação do seu projeto é abalada.

Para evitar essas armadilhas, considere incluir verificações automáticas de licença como parte do seu workflow de desenvolvimento. Essas verificações podem ajudar a identificar licenças incompatíveis cedo no processo, evitando que dependências problemáticas sejam introduzidas no seu projeto.

Outra abordagem poderosa é gerar uma Lista de Materiais de Software (SBOM). Uma SBOM lista todos os componentes e seus metadados (incluindo licenças) em um formato padronizado. Ela oferece visibilidade clara da sua cadeia de suprimentos de software e ajuda a revelar riscos de licenciamento de forma proativa.

Assim como as vulnerabilidades de segurança, os problemas de licença são mais fáceis de corrigir quando descobertos cedo. Automatizar esse processo mantém o seu projeto saudável e seguro.

## Evite alterações indesejadas com branches protegidos

### O acesso irrestrito aos seus branches principais pode levar a alterações acidentais ou maliciosas que podem introduzir vulnerabilidades ou comprometer a estabilidade do seu projeto.

Um novo contribuidor recebe acesso de escrita ao branch principal e, acidentalmente, faz push de alterações que não foram testadas. Uma falha grave de segurança é então revelada, cortesia das últimas alterações. Para evitar esse tipo de problema, as regras de proteção de branch garantem que alterações não possam ser enviadas (push) ou mescladas (merge) em branches importantes sem antes passar por revisões e pelos status checks especificados. Você fica mais seguro e em melhor situação com essa medida extra em vigor, garantindo qualidade de primeira sempre.

## Facilite (e torne seguro) o relato de problemas de segurança

### É uma boa prática facilitar que seus usuários relatem bugs, mas a grande questão é: quando esse bug tem impacto de segurança, como eles podem relatá-lo a você com segurança, sem colocar um alvo nas suas costas para hackers maliciosos?

Imagine o seguinte: um pesquisador de segurança descobre uma vulnerabilidade no seu projeto, mas não encontra uma forma clara ou segura de relatá-la. Sem um processo designado, ele pode criar uma issue pública ou discutir o assunto abertamente nas redes sociais. Mesmo que tenha boas intenções e ofereça uma correção, se fizer isso por meio de um pull request público, outras pessoas o verão antes de ser mesclado! Essa divulgação pública vai expor a vulnerabilidade a agentes maliciosos antes que você tenha a chance de resolvê-la, podendo levar a um exploit de dia zero (zero-day), atacando o seu projeto e seus usuários.

### Política de Segurança

Para evitar isso, publique uma política de segurança. Uma política de segurança, definida em um arquivo `SECURITY.md`, detalha os passos para relatar preocupações de segurança, criando um processo transparente de divulgação coordenada e estabelecendo as responsabilidades da equipe do projeto no tratamento dos problemas relatados. Essa política de segurança pode ser tão simples quanto "Por favor, não publique detalhes em uma issue ou PR pública; envie-nos um e-mail privado para security@example.com", mas também pode conter outros detalhes, como em quanto tempo a pessoa deve esperar receber uma resposta sua. Qualquer coisa que possa ajudar na eficácia e na eficiência do processo de divulgação.

### Relato Privado de Vulnerabilidades

Em algumas plataformas, você pode simplificar e fortalecer o seu processo de gestão de vulnerabilidades, do recebimento à divulgação, com issues privadas. No GitLab, isso pode ser feito com issues privadas. No GitHub, isso se chama relato privado de vulnerabilidades (private vulnerability reporting, PVR). O PVR permite que mantenedores recebam e tratem relatos de vulnerabilidades, tudo dentro da plataforma do GitHub. O GitHub cria automaticamente um fork privado para escrever as correções e um rascunho de aviso de segurança (security advisory). Tudo isso permanece confidencial até você decidir divulgar os problemas e publicar as correções. Para fechar o ciclo, os avisos de segurança serão publicados e vão informar e proteger todos os seus usuários por meio da ferramenta SCA deles.

### Defina seu modelo de ameaças para ajudar usuários e pesquisadores a entender o escopo

Antes que pesquisadores de segurança possam relatar problemas de forma eficaz, eles precisam entender quais riscos estão no escopo. Um modelo de ameaças leve pode ajudar a definir os limites do seu projeto, o comportamento esperado e as premissas.

Um modelo de ameaças não precisa ser complexo. Até mesmo um documento simples descrevendo o que o seu projeto faz, no que ele confia e como ele poderia ser mal utilizado já ajuda muito. Ele também ajuda você, como mantenedor, a refletir sobre possíveis armadilhas e riscos herdados de dependências upstream.

Um ótimo exemplo é o [modelo de ameaças do Node.js](https://github.com/nodejs/node/security/policy#the-nodejs-threat-model), que define claramente o que é e o que não é considerado uma vulnerabilidade no contexto do projeto.

Se isso é novo para você, o [Processo de Modelagem de Ameaças da OWASP](https://owasp.org/www-community/Threat_Modeling_Process) oferece uma introdução útil para construir o seu próprio.

Publicar um modelo de ameaças básico junto com a sua política de segurança melhora a clareza para todos.

## Prepare um processo leve de resposta a incidentes

### Ter um plano básico de resposta a incidentes ajuda você a manter a calma e agir com eficiência, garantindo a segurança dos seus usuários e consumidores.

A maioria das vulnerabilidades é descoberta por pesquisadores e relatada de forma privada. Mas, às vezes, um problema já está sendo explorado na prática antes de chegar até você. Quando isso acontece, quem está em risco são os seus consumidores downstream, e ter um plano de resposta a incidentes leve e bem definido pode fazer uma diferença crítica.

<aside markdown="1" class="pquote">
  <img src="https://avatars.githubusercontent.com/ulisesgascon?s=180" class="pquote-avatar" alt="avatar">
  Uma vulnerabilidade é basicamente uma falha, uma configuração incorreta de segurança ou um ponto fraco no nosso sistema que pode ser explorado por terceiros para fazê-lo se comportar de maneiras não intencionais.
  <p markdown="1" class="pquote-credit">
— [@UlisesGascon](https://github.com/ulisesgascon), ["What is a Vulnerability and What's Not? Making Sense of Node.js and Express Threat Models"](https://gitnation.com/contents/what-is-a-vulnerability-and-whats-not-making-sense-of-nodejs-and-express-threat-models)
  </p>
</aside>

Mesmo quando uma vulnerabilidade é relatada de forma privada, os próximos passos importam. Depois que você recebe um relato de vulnerabilidade ou detecta atividade suspeita, o que acontece em seguida?

Ter um plano básico de resposta a incidentes, mesmo que seja um checklist simples, ajuda você a manter a calma e agir com eficiência quando o tempo é importante. Também mostra aos usuários e pesquisadores que você leva os incidentes e relatos a sério.

Seu processo não precisa ser complexo. No mínimo, defina:

* Quem revisa e faz a triagem dos relatos ou alertas de segurança
* Como a severidade é avaliada e como as decisões de mitigação são tomadas
* Quais passos você segue para preparar uma correção e coordenar a divulgação
* Como você notifica os usuários, contribuidores ou consumidores downstream afetados

Um incidente ativo, se não for bem gerenciado, pode corroer a confiança dos seus usuários no seu projeto. Publicar isso (ou criar um link para isso) no seu arquivo `SECURITY.md` pode ajudar a alinhar expectativas e construir confiança.

Para se inspirar, o [Grupo de Trabalho de Segurança do Express.js](https://github.com/expressjs/security-wg/blob/main/docs/incident_response_plan.md) oferece um exemplo simples, mas eficaz, de um plano de resposta a incidentes open source.

Esse plano pode evoluir conforme o seu projeto cresce, mas ter uma estrutura básica em vigor agora pode economizar tempo e reduzir erros durante um incidente real.

## Trate a segurança como um esforço de equipe

### Segurança não é uma responsabilidade individual. Ela funciona melhor quando compartilhada por toda a comunidade do seu projeto.

Embora ferramentas e políticas sejam essenciais, uma postura de segurança forte vem de como a sua equipe e os seus contribuidores trabalham juntos. Construir uma cultura de responsabilidade compartilhada ajuda o seu projeto a identificar, triar e responder a vulnerabilidades de forma mais rápida e eficaz.

Aqui estão algumas formas de fazer da segurança um esporte de equipe:

* **Defina papéis claros**: saiba quem cuida dos relatos de vulnerabilidade, quem revisa as atualizações de dependências e quem aprova os patches de segurança.
* **Limite o acesso usando o princípio do menor privilégio**: dê acesso de escrita ou de administrador apenas a quem realmente precisa e revise as permissões regularmente.
* **Invista em educação**: incentive os contribuidores a aprender sobre práticas de código seguro, tipos comuns de vulnerabilidade e como usar as suas ferramentas (como SAST ou secret scanning).
* **Promova diversidade e colaboração**: uma equipe heterogênea traz um conjunto mais amplo de experiências, consciência de ameaças e habilidades criativas de resolução de problemas. Também ajuda a revelar riscos que outros poderiam deixar passar.
* **Engaje-se com o upstream e o downstream**: suas dependências podem afetar a sua segurança, e o seu projeto afeta outros. Participe da divulgação coordenada com os mantenedores upstream e mantenha os usuários downstream informados quando as vulnerabilidades forem corrigidas.

Segurança é um processo contínuo, não uma configuração feita uma única vez. Ao envolver a sua comunidade, incentivar práticas seguras e apoiar uns aos outros, você constrói um projeto mais forte e resiliente e um ecossistema mais seguro para todos.

## Conclusão: alguns passos para você, uma enorme melhoria para seus usuários

Esses poucos passos podem parecer fáceis ou básicos para você, mas fazem uma grande diferença para tornar o seu projeto mais seguro para seus usuários, porque oferecem proteção contra os problemas mais comuns.

Segurança não é estática. Revisite seus processos de tempos em tempos: conforme o seu projeto cresce, crescem também as suas responsabilidades e a sua superfície de ataque.

## Colaboradores

### Muito obrigado a todos os mantenedores que compartilharam suas experiências e dicas conosco para este guia!

Este guia foi escrito por [@nanzggits](https://github.com/nanzggits) e [@xcorail](https://github.com/xcorail) com contribuições de:

[@JLLeitschuh](https://github.com/JLLeitschuh), [@intrigus-lgtm](https://github.com/intrigus-lgtm), [@UlisesGascon](https://github.com/ulisesgascon) + muitos outros!
