Este iretório tem como objetivo reconstruir o _pipeline_ para análise de transcritoma de escorpião.
Este projeto já foi concluído pelo aluno Gabriel em 2015, mas pouco documentado. Logo, esta é uma reconstrução do projeto com melhor documentação para manutenção.

# Visão Geral do Pipeline

Um pipeline contém 3 estágios básicos: **1 - filtragem**, **2- montagem**, **3 - anotação**. Cada estágio possui particularidades próprias e usa programas específicos. Veremos eles em detalhes abaixo.

### Diretórios e Arquivos
Uma estrutura geral dos diretórios no Pipeline é mostrada a abaixo.
``` |
	PipelineScorpion/
		|
		|--filtragem/
		|	|
		|	|--Reads/
		|	|	|
		|	|	|--raw_reads/
		|	|
		|	|--clipped/
		|	|--trimmed/
		|	|--trimScorpio.sh
		|
		|--montagem/
		|	|
		|	|--pair1/
		|	|--pair2/
		|	|--pair3/
		|	|--scorpionAssembly.sh
		|
		|--annotation/
		|	|
		|	|--pair1/
		|	|--pair2/
		|	|--pair3/
		|	|--results/
		|
		|--README.md
		|--BulkFastqc.py
```
### Arquivos Originais
As leituras originais do sequenciador (Illumina no caso do escorpião) está no diretório `raw_reads`. Os arquivos são:
- scorpion_GCCAAT_L001_R1_001.fastq
- scorpion_GCCAAT_L001_R1_002.fastq
- scorpion_GCCAAT_L001_R1_003.fastq
- scorpion_GCCAAT_L001_R2_001.fastq
- scorpion_GCCAAT_L001_R2_002.fastq
- scorpion_GCCAAT_L001_R2_003.fastq

### Resultados Finais
Os resultados finais estão nos arquivos do diretório `results`. Eles são:
- pair1_results.xls
- pair2_results.xls
- pair3_results.xls

# Passo a passo

## 1) Filtragem

Neste estágio as leituras originais são aparadas e filtradas, preparando-as para a montagem. Esse passo é necessário para diminuir eventuais erros de sequenciamento que possam ter acontecidoe e qualquer contaminação que possa ter diminuído a qualidade das leituras.  
Para saber mais sobre os programas utilizados neste passo veja Apêndices > Filtragem

### Passos desse estágio
1. Verificação de qualidade    
    `$fastqc <filename>.fastq`
    `$w3m -dump <filename>_fastq.html`

    O comando _fastqc_ executa a verificação de qualidade de arquivos fastqc ou fasta, gerando como resultado um arquivo html e uma pasta compactada.    
    O comando _w3m_ é um visualizador de arquivos html para podermos ver a qualidade das reads.     
    Inicialmente procure o tópico "overrepresented sequences" e veja se tem algum hit. Caso tivermos, eles deverão ser removidos.   

        **NOTE**: O script `BulkFastqc.py` pode ser utilizado para executar o comando _fastqc_ para todos os arquivos .fastq de um diretório especificado. Para mais informações veja Apêndices > Filtragem > BulkFastqc 

    1. clipping     
    `$ cutadapt -e 0.15 -O 5 -m 15 -b <adapter> <input>.fastq -o clipped.fastq`

    O programa _cutadapt_ vai remover o adaptador selecionado em `<adapter>`. Lembre-se de substituir `<adapter>` com a sequência de bases, não com o nome do adaptador.    
    Ao final deste passo volte para o passo 1 até que não tenha mais hits para serem eliminados.    

2. Filtrar   
    O processo de filtragem pode ser guiado pela verificação de qualidade, mas em geral requer tentativa e erro. Para estas reads em particulara foram usados os seguintes commandos:
    `$ prinseq-lite -fastq <arquiv>o.clipped.fastq -out_format 3 -min_qual_mean 20 -out_good R1.clipped.trimmed1.fastq`
	`$ prinseq-lite -fastq R1.clipped.trimmed1.fastq -out_format 3 -trim_qual_right 20 trim_qual_window 20 -trim_qual_step 10 -trim_qual_type mean -out_good R1.clipped.trimmed2.fastq`
	`$ prinseq-lite -fastq R1.clipped.trimmed2.fastq -out_format 3 -min_len 100 -out_good R1.clipped.trimmed3.fastq`   

    **NOTE**: Repita os passos 1 e 2 até ficar as reads terem uma qualidade aceitável para prosseguir. 

## 2) Montagem

Neste estágio as reads já filtradas serão "montadas", i.e. unidas em _contigs_ de tamanho maior do que as reads originais, e que possuem maior valor biológico por isso.   
Para melhores explcações sobre os programas utilizados neste estágio veja Apêndices > Montagem

### Passos deste estágio

1. Montagem das reads   
    `$ ./scorpionAssembly.sh`

    Este script executa o programa _Trinity_ - o montador propriamente dito, usando diferentes tamanhos de kmer para comparação. O comando usado no Trinity pode ser visto no apêndice.     
    Escolhemos vários tamanhos de kmer porque esta escolha afeta bastante a montagem. Como não sabemos de antemão qual o melhor temos que testar vários e analisar depois.   
    Neste paso são criados vários diretórios com as diferentes montagens, para cada kmer diferente.

    **NOTE**: Este passo demora várias horas para cada uma das execuções, e são várias.

2. Escolher a melhor montagem
    Para casa uma das diferentes montagens temos que executar
    `$ $TRINITY_HOME/util/TrinityStats.pl  Trinity.fasta`

    Este comando produz um resumo da qualidade do arquivo `Trinity.fasta`. Compare as qualidades baseado no valor de N50, escolhendo o maior deles.

## 3) Anotação
Neste estágio os contigs criados são testados contra um banco de dados de sequências conhecidas para que sejam identificados. Este é o último estágio.

### Passos deste estágio
0. [opcional] Definir variável $TRINOTATE_HOME
    `$ export TRINOTATE_HOME='/opt/Trinotate-Trinotate-v3.1.1/'`

1. Preparar os bancos de dados
    `$ $TRINOTATE_HOME/admin/Build_Trinotate_Boilerplate_SQLite_db.pl  Trinotate`    

    Este comando irá baixar os bancos de dados necessários para os próximos testes. Os arquivos gerados são:     
    
    `Trinotate.sqlite`
	`uniprot_sprot.pep`
	`Pfam-A.hmm.gz`

    Alguns passos ainda tem que ser tomados com esses arquivos.     
    1. Preparar banco de dados do blast        
    `$ makeblastdb -in uniprot_sprot.pep -dbtype prot`

    2. Descomprimir e preparar banco de dados do hmmscan     
    `$ gunzip Pfam-A.hmm.gz && hmmpress Pfam-A.hmm`

2. Gerando os arquivos necessários        
    Precisamos dos seguintes arquivos:
    - Trinity.fasta (gerado no estágio anterior)
	- Trinity.fasta.transdecoder.pep (faremos agora)
	- gene_trans_map

    1. Executar Transdecoder
    **No diretório em que você montou suas reads**      
    `$ Transdecoder.LongOrfs -t target_transcripts.fasta`
	`$ TransDecoder.Predict -t target_transcripts.fasta`     

    Isso vai gerar o arquivo Trinity.fasta.transdecoder.pep que precisamos. Os outros arquivos gerados não são importantes. 

    2. Gerar gene_trans_map      
    ```	$ $TRINITY_HOME/util/support_scripts/get_Trinity_gene_to_trans_map.pl Trinity.fasta >  Trinity.fasta.gene_trans_map ```

    TRINITY_HOME é o diretório em que o Trinity está instalado. (veja Apêndices)

3. Rodando as reads no banco de dados       
    Usaremos dois bancos: um de transcritos e um de proteínas.            
	`$ blastx -query Trinity.fasta -db uniprot_sprot.pep -num_threads 8 -max_target_seqs 1 -outfmt 6 > blastx.outfmt6 `    
	`$ blastp -query transdecoder.pep -db uniprot_sprot.pep -num_threads 8 -max_target_seqs 1 -outfmt 6 > blastp.outfmt6`        

    Isso vai gerar os matches do banco de dados   

4. Rodar HMMER para identificar domínios proteicos           
    `$ hmmscan --cpu 8 --domtblout TrinotatePFAM.out Pfam-A.hmm transdecoder.pep > pfam.log`

5. Carregar resultados no banco de dados      
	`$ Trinotate Trinotate.sqlite init --gene_trans_map Trinity.fasta.gene_trans_map --transcript_fasta Trinity.fasta --transdecoder_pep transdecoder.pep`
	`$ Trinotate Trinotate.sqlite LOAD_swissprot_blastp blastp.outfmt6`
	`$ Trinotate Trinotate.sqlite LOAD_swissprot_blastx blastx.outfmt6`
	`$ Trinotate Trinotate.sqlite LOAD_pfam TrinotatePFAM.out`

    Esta sequência de comandos vai carregar todos os arquivos criados anteriormente para o banco de dados.

6. Gerar resultados
	`$ Trinotate Trinotate.sqlite report > trinotate_annotation_report.xls`

Este é o último passo do Pipeline. Depois deste passo o arquivo `trinotate_annotation_report.xls` vai conter os resultados do matching com os bancos de dados.

# Apêndice

## FILTRAGEM

#### Cutadapt
Programa usado para fazer o clipping de adaptadores. Para mais informações: http://cutadapt.readthedocs.io/en/stable/guide.html

Comando básico: cutadapt -a AACCGGTT -o output.fastq input.fastq
 (trocar AACCGGTT pela sequência que será  cortada)

|**Tipo de Adapter**	|	**Comando**|
|-------------------|--------------------------|
|3' adapter	|	-a ADAPTER|
|5' adapter	|	-g ADAPTER|
|Anchored 3' adapter	|-a ADAPTER$|
|Anchored 5' adapter	|-g ^ADAPTER|
|5' or 3' (both)		|-b ADAPTER|
|Linked adapter		|-a ADAPTER1...ADAPTER2|
|Non-anchored link    |  	-g ADAPTER1...ADAPTER2|

**Opções**      
| **Opção** | **Descrição**|
|------------|----------------|
|--cut, -u	|Cuts n bases from beginning|
|-q		|Remove reads with quality below specified value|
|-l, --length	|Shortens reads to l bases|
|-m		|Drops reads smaller than m|
|-M		|Drops reads greater than M|
|-O		|Defines minimum overlap for trim|
|-e		|Error admmited for trim|

#### Prinseq     
Usado para o trimming. Para mais informações: http://prinseq.sourceforge.net/manual.html#STANDALONE    

|**Opção** | **Descrição** |
|------------|-----------------|
|-fastq		|Input file in FASTQ format|
|-out_format	|Output format. (1) Fasta, (2) Fasta and Qual, (3) Fastq|
|-out_good	|Output files will have "_prinseq_good_XXXX" in the file name|
|-min_len	|Filter sequence shorter than min_len|
|-max_len	|Filter sequence longer than max_len|
|-range_len	|Filter sequence by range|
|-min_gc		|Filter sequence with GC lower than min_gc|
|-max_gc		|Filter sequence with GC higher than max_gc|
|-min_qual_score	|Filter sequence with at least one quality score below value|
|-max_qual_score	|Opposite of min_qual_score|
|-min_qual_mean	|Filter sequence with quality score mean below value|
|-max_qual_mean	|Opposite of min_qual_mean
|-trim_qual_right	|Trim sequence by quality score from the 3'-end with this threshold score|
|-trim_qual_type		|Type of quality score calculation to use|
|-trim_qual_window	|The sliding window size used to calculate quality score by type|
|-trim_qual_step		|Step size used to move the window|

#### BulkFasetqc

Este programa roda a análise _fastqc_ para todos os arquivos .fastq de um diretório. O diretório a ser analisado pode ser passado como argumento para o programa.

**RODE COM PYTHON3**

Exemplo: `$ python3 BulkFastqc.py /path/to/example`   

*NOTE*: Dependendo do tamanho de arquivos .fastq no diretório a execução pode demorar.

#### trimScorpio

Este script simplesmente roda os comandos prinseq para os arquivos do escorpião como especificado. Serve para automarizar o processo de trimming.

## MONTAGEM     

#### Trinity 
Trinity é um montador de sequências de transcritos ara dados sequenciados por Illumina RNA-Seq.        
Website: https://github.com/trinityrnaseq/trinityrnaseq/wiki     
TRINITY_HOME in dna: /opt/trinityrnaseq-2.1.0/   
Comando típico para Trinity:        
`$ Trinity --seqType fq --left reads_1.fq --right reads_2.fq --CPU 6 --max_memory 20G --KMER_SIZE k_size --output trinity_k_size`


|**Opções** |  **Descrição** | **Necessário** |
|------------|-----------------|---------------|
|--seqType 	 |	:type of reads: ( fa, or fq ) |				*REQUIRED*|
|--max_memory |	:suggested max memory to use by Trinity	|	*REQUIRED*|
|If paired-end: |
|--left  	 |   :left reads	|								*REQUIRED*|
|--right 	 |   :right reads	|							*REQUIRED*|
|If single-end :|
|--single 	  |  :single reads	|							*REQUIRED*|
|--KMER_SIZE|		:size of kmer (max 32)|
|--output   |     :name of directory for output (must contain 'trinity' in it)|
|--full_cleanup | :only retain the Trinity fasta file, rename as ${output_dir}.Trinity.fasta|
|--show_full_usage_info  | :show the many many more options available for running Trinity (expert usage).|

#### scorpionAssembly

Este script roda o programa acima (Trinity) para os arquivos especificados.

## ANOTAÇÃO

#### Trinotate
Website: https://trinotate.github.io/       
TRINOTATE_HOME in dna: /opt/Trinotate-Trinotate-v3.1.1/      

O site do Trinotate é muito completo e feito no estilo passo a passo. Recomendamos ver o site para mais informações.

#### Transdecoder
Website: https://github.com/TransDecoder/TransDecoder/wiki   
TRANSDECODER_HOME in dna: /opt/TransDecoder-TransDecoder-v5.2.0/      

Nós utilizamos apenas os 2 primeiros passos mostrados no site. Se quiser saber mais, recomendamos olhar o site.


-----------------------------------------------------------
Created: Brasília, 09 de Abril de 2018           
Last updated: Brasília, 16 de Maio de 2018