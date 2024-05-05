## Trabalho 3 - Transcrição de uma Reunião

Este projeto foi inspirado no recurso de transcrição de reuniões apresentado na ferramenta [Read AI](https://www.read.ai).

A ideia do trabalho consiste em transcrever uma reunião e permitir fazer buscas em aspectos tratados na reunião.

- A transcrição pode ser feita manualmente (não recomendado), ou automaticamente. Na forma automática, pode ser codificado um script para transcrever ou utilizado a [WebUI da Whisper](https://huggingface.co/spaces/aadnk/whisper-webui). Atente para utilizar o recurso de diarização (Diarization), definindo o número de pessoas presentes na conversa (precisará de pelo menos duas pessoas no áudio).
- Você precisará carregar a transcrição para a próxima etapa. Pode ser feita qualquer manipulação para organizar a transcrição. Por exemplo, pode ser separada cada frase anotando antes quem fala a frase; pode ser feita uma matriz tendo na primeira coluna quem falou, seguida da frase; etc.
- A partir da transcrição da reunião, você precisa fazer uma ferramenta de chat que realize pesquisas associadas com a reunião. Seu chat precisa atender a três pedidos especiais de busca:

    1. **Quem falou "tais termos" na reunião:** fazer uma busca pelo(s) termo(s) de busca e indicar quem utilizou o(s) termo(s) em uma mesma frase (lembrando que haverá duas ou mais pessoas na reunião, então é preciso retornar se foi a pessoa 1, pessoa 2, etc. quem falou a frase).
        - No caso de vários termos, esses não precisam ser encontrados em ordem, nem em sequência. Por exemplo, os termos "hoje trabalhador dia" são termos encontrados na frase "Hoje é dia do trabalhador".
        - A busca pode ser feita pelo termo exato, ou por similaridade, ou utilizar a lematização. Você escolhe o que será utilizado.
        - Caso mais de uma frase contenha o(s) termo(s), pode ser considerada apenas uma delas (mais fácil) ou retornado todos os que falaram aquelas frases. Você escolhe o que será feito nesse item.
    2. **Onde foi falado sobre "tal coisa":** retornar a frase que contenha a "tal coisa" procurada. Utilize o recurso de similaridade para encontrar a frase e retornar essa frase.
        - Caso mais de uma frase "empate" na similaridade, pode ser considerada apenas uma delas (mais fácil) ou retornado todos as frases. Você escolhe o que será feito nesse item.
    3. **Solicitar o sentimento associado com a frase obtida no item anterior:** a partir de uma frase retornada no item anterior, mostrar o sentimento associado com a frase.
        - Se mais de uma frase foi mostrada no item anterior, pode ser retornado o sentimento da primeira delas, ou o sentimento de cada frase. Você escolhe o que será feito nesse item.

A forma como o usuário poderá interagir com o chat para realizar cada uma das opções é livre para ser determinada por você. Podem ser oferecidos um menu de opções (possivelmente a forma mais fácil de implementação), ou outras formas. Também pode ser exigida uma forma específica de escrita (o que facilita uma extração do pedido por expressões regulares), como o formato “mostrar (frase|frases) com: tal coisa” (exemplo de uso: “mostrar frases com: dia do trabalhador”).
