Arquivos de programas são baseados em uma aula conceitual sobre alguns dos tipos de loops existentes no PsychoPy (https://www.youtube.com/watch?v=7qKrIhm5a84). Quatro arquivos são usados nessa demonstração: sequential_loop, pseudorandom_loop, random_loop, fullrandom_loop

O arquivo sequential_loop define o loop como sequencial (sequential). Neste caso, as tentativas que alimentam o loop serão sempre apresentadas na mesma sequência (em meu exemplo, teríamos: ABCDE, ABCDE, ABCDE, ABCDE, ABCDE).

O arquivo pseudorandom_loop implementa um loop peudoaleatório. Neste caso, o loop também é definido como sequencial (sequential) e a aleatorização dos estímulos é feita na planilha do Excel. Neste caso, usei o arquivo estimulos_pseudorandom.xlsx (nos outros três exemplos, usei estimulos.xlsx).

O arquivo random_loop implementa um loop random (aleatório). Neste caso, a cada nova iteração do loop, as tentativas são embaralhadas (por exemplo, no loop 0, podemos ter ADECB, no loop 1, podemos ter BDCAE, e assim por diante).

O arquivo fullrandom_loop implementa um loop fullRandom (totalmente aleatório). Neste caso, o número de tentativas é igual para cada estímulo, mas estímulos similares podem acontecer em sequência (por exemplo, no loop 0, podemos ter ADECA, no loop 1, podemos ter BDBCE, e assim por diante).

Em caso de dúvidas, entre em contato comigo: lima.piraju@gmail.com.