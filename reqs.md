### Objetivo Principal:

- Permitir o usuário jogar "Forca" usando uma interface de texto. 

### Requisitos:

- O usuário poderá selecionar um nível de dificuldade: `fácil`, `normal` ou `difícil`.
:heavy_check_mark: - Selecionar uma palacra aleatoriamente a partir de um banco de palavras estático. 
- O tamanho da palavra varia de acordo com a difuculdade selecionada:
  - fácil: de 3 a 5 caracteres.
  - normal: de 6 a 10 caractres.
  - difícil: mais de 10 caracteres. 

- Quantidade de chances que o usuŕio terá para adivinhar uma palavra varia de acordo com o nível de dificuldade, sendo o valor arredondado mais próximo do float:
- Quantidate básica: 1.5 vezes o tamanho da palavra selecionada. 

  - fácil: quantidade básica +2
  - normal: quantidade básica
  - difícil: quantidade básica -2
