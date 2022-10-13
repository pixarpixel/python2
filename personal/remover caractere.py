
string = '''- [ ] quem tratar com falta de respeito e racismo, independente da cor, raça, etnia ficará de detenção o ano inteiro. (a detenção é obrigatória, se não levará multa). uma pessoa será imparcial e julgará conversando com a vítima e dar o veredito final para detenção do culpado ou não.
- [ ] tudo nesse país é por mérito, ou seja, todos tem a mesmas oportunidades, só basta correr atrás para conseguir. 
- [ ] a comida que será montada levará em consideração as opiniões das pessoas, mas não será totalmente baseada nisso. 
- [ ] Nesse país não terá punição coletiva (todos são inocentes até q se prove ao contrario), pois colocaremos câmeras nas salas que serão gravadas e vigiadas. 
- [ ] aumentar o tempo do lanche, para a melhoria do desempenho escolar e a disponibilização de bolas 
- [ ] absorvente gratuito no banheiro (com condição de todos trazerem e contribuírem pq não tiramos absorvente de árvore)
- [ ] entrada permitida com pelo menos 1 peça do uniforme
- [ ] apoiar esportes e aulas interativas com aproveitamento externo 
- [ ] apoiamos os direitos o humanos e qualquer violação de tais direitos terá detenção até segunda ordem
- [ ] todos têm direito a fazer recuperação, porém os com nota maior que 7, a recuperação é mais difícil 
- [ ] nosso ministério será composto por interesses diferentes: o ministério da educação e atenção, ministério dos jogos, ministério da conversa e celular, ministério da zoação.
- [ ] a tecnologia será usada de forma benéfica com permissão do supremo tribunal federal (professor)
- [ ] interclasses será julgado por terceiros.'''

b = "[]}"
for i in range(0,len(b)):
    string = string.replace(b[i],"")
print(string)
