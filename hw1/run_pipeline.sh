#!/bin/bash

FILE1=${1:-"CP002410.1.fasta"}   
FILE2=${2:-"CP033071.1.fasta"}   
GC1=${3:-28.49}                  
GC2=${4:-72.65}                  

echo "=========================================="

echo "[1/5] chimera.py $FILE1 $FILE2 -o chimera.fasta -t truth_chimera.txt"
python chimera.py $FILE1 $FILE2 -o chimera.fasta -t truth_chimera.txt

echo "[2/5] cut_genomes.py $FILE1 $FILE2."
python cut_genomes.py $FILE1 $FILE2

echo "------------------------------------------"
echo "      Тест на химере"
echo "[3/5] viterbi.py chimera.fasta --gc1 $GC1 --gc2 $GC2 -o out_chimera.txt"
echo "[3/5] check.py truth_chimera.txt out_chimera.txt"
python viterbi.py chimera.fasta --gc1 $GC1 --gc2 $GC2 -o out_chimera.txt
python check.py truth_chimera.txt out_chimera.txt

echo "------------------------------------------"
echo "      Тест на бактерии 1"
echo "[4/5] viterbi.py test_bact1.fasta --gc1 $GC1 --gc2 $GC2 -o out_bact1.txt"
echo "[4/5] check.py truth_bact1.txt out_bact1.txt"
python viterbi.py test_bact1.fasta --gc1 $GC1 --gc2 $GC2 -o out_bact1.txt
python check.py truth_bact1.txt out_bact1.txt

echo "------------------------------------------"
echo "      Тест на бактерии 2"
echo "[5/5] viterbi.py test_bact2.fasta --gc1 $GC1 --gc2 $GC2 -o out_bact2.txt"
echo "[5/5] check.py truth_bact2.txt out_bact2.txt"
python viterbi.py test_bact2.fasta --gc1 $GC1 --gc2 $GC2 -o out_bact2.txt
python check.py truth_bact2.txt out_bact2.txt

echo "=========================================="