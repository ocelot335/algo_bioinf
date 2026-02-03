# run_pipeline.sh
существует скрипт для общего запуска одной командой. Его следует запускать так:
	bash run_pipeline.sh [имя fasta-файла первого генома] [имя fasta-файла второго генома] [GC-состав первого генома] [GC-состав второго генома]

например так:
	bash run_pipeline.sh CP002410.1.fasta CP033071.1.fasta 28.49 72.65


# chimera.py
Для создания химерной последовательности стоит использовать chimera.py. 
Его следует запускать такой командой:
	python chimera.py [--length LENGTH] [--mean MEAN] genome1 genome2

genome1, genome2 - названия fasta-файлов с геномами бактерий

где
	--length LENGTH, -l LENGTH	
        Длина генерируемой последовательности(по умолчанию 10000)
 	
--mean MEAN, -m MEAN  	Средняя длина фрагмента(по умолчанию 300)

код выдаёт два файла: chimera.fasta и marks.txt - химерный геном и метки, чтобы восстановить откуда какой кусок

# viterbi.py
Алгоритм витерби реализован в viterbi.py
Его следует запускать такой командой:
    viterbi.py --gc1 GC1 --gc2 GC2 [--mean MEAN] input_file

input_file - входной файл последовательности

где
  --gc1 GC1    GC% первой бактерии(e.g. 28.49)
  --gc2 GC2    GC% второй бактерии(e.g. 72.65)
  --mean MEAN  Средняя длина фрагмента(по умолчанию 300)

# cut_genomes.py
скрипт для получения участка геномов. Пример:
    python cut_genomes.py CP002410.1.fasta CP033071.1.fasta

# check.py
Скрипт для проверки работы алгоритма Витерби. Пример:
    python check.py truth_chimera.txt out_chimera.txt