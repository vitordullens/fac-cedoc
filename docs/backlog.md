# Product Backlog
![cabecalho](assets/cabecalho.png)

1. Receber envio de metadados
2. Receber arquvios de imagem, vídeo e texto junto com os metadados
3. Salvar informações recebidas num banco de dados
4. Definir tipos diferentes de documentos com metadados próprios
    1. Tipos de documentos vagamente definidos (audio, vídeo e texto)     
---------------------------------------------------------------------- 
1. Cadastrar usuários com nome, email e senha
2. Validar emails de usuários para permitir apenas email da UnB
3. Definir permissões limitadas para usuários comuns do sistema
4. Relacionar os contribuidores do documento com o documento (relação 1 para N)
5. Permitir edição dos documentos recebidos       
---------------------------------------------------------------------- 
1. Definir modelos de documentos conforme especificado
    1. AUDIOVISUAL - video e audio
    2. JORNAL CAMPUS - texto
    3. CAMPUS REPORTER - texto
2. Validar arquivos recebidos de acordo com extensões válidas
3. Permitir validação dos documentos recebidos por superusuários
4. Começar a melhorar a interface do sistema       
---------------------------------------------------------------------- 
1. Permitir opções de documentos sem arquivo junto, mas com url ou indicação de arquivo físico
2. Adicionar campos extras para modelos diferentes:
    1. AUDIOVISUAL - certificados (1:N) e categorias (N:N)
    2. JORNAL CAMPUS - índices (1:N)
3. Permitir edição dos contribuidores na edição do arquivo
4. Continuação das melhorias na interface do sistema      
---------------------------------------------------------------------- 
1. Permitir edição de campos extras durante a edição do arquivo
2. Documentar o funcionamento do sistema
3. Configurar sistema para utilizar o PostGres
4. Finalizar interface do sistema

## Melhorias Futuras
1. Validação de Novo Usuário por email (token de validação)
2. Envio de email para o dono do documento quando este for validado
3. Integração com o Sistema Koha (FAC)
4. Integração com o Sistema Omeka (BCE)

# Notas
O presente arquivo reflete uma evolução temporal do desenvolvimento do sistema. Cada linha horizontal marca o fim de uma **sprint.** 


Questões de comunicação e logística impediram que as sprints tivessem exatamente o mesmo tamanho, mas os prazos foram próximos uns dos outros. 

O cliente pediu que fossem anotados os pontos que achavamos que deveriam ser adicionados no futuro, para que outro time possa dar continuidade ao sistema. Esses pontos não faziam parte do escopo combinado inicialmente para o projeto, e foram decididos como menos importantes do que os pontos trabalhados.