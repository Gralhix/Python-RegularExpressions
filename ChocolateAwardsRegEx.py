# Regular expressions exercise
# Given a text about Feitoria do Cacao's chocolate, will use regular expressions to find the awards give to their bars bars
# Text from https://feitoriadocacao.com/pt/#feitoria-do-cacao

# Will import regular expressions.
import re

# Will specify the pattern we're looking for. In this case, capitalised words and will ignore the name of the company, "FEITORIA DO CACAO".
capsregx = re.compile(r"[A-Z][A-Z]+")

# Will find and print all the strings that match the search specified above.
# Unfortunately it also prints the brand name as it's capitalised. I'm afraid I can't figure out how to exclude those specific strings. If you know how to do it please email me (check profile) with the code, I would love to learn.
print(capsregx.findall("""A marca FEITORIA DO CACAO iniciou-se após uma viagem realizada a São Tomé e Príncipe por ambas as responsáveis da empresa, Tomoko Suga e Sue Tavares. Em São Tomé e Príncipe tivemos a oportunidade de visitar várias Roças e contactar diretamente com as pessoas que produzem o cacau. Nas visitas que tivemos o privilégio de fazer, mostraram-nos como se processa o cacau até este chegar às mãos dos produtores de chocolate, um pouco por todo o mundo. Não só aprendemos todo o processo como também nos mostraram a humildade e amarga vida dos produtores de cacau, que em nada se assemelha à imagem que temos do chocolate: doce e rico. Foi, para nós, um grande choque. Neste contacto directo, percebemos o quão importante é contribuirmos para diminuir as lacunas e diferenças económicas que existem entre os produtores de cacau e os produtores de chocolate. Assim, inspiradas por esta experiência tão sensibilizadora, colocamos mãos à obra e iniciamos o projeto FEITORIA DO CACAO.

Durante um ano estudámos, fizemos formação como Professional Chocolatier e Chocolate Maker, testes e experiências com o cacau de diferentes países até chegarmos a um produto que privilegia o carácter único e especial que cada terroir nos pode oferecer. Respeitamos a sua natureza, damos atenção a todos os detalhes do processo de fabrico de chocolate: fazemos chocolate desde o grão de cacau, em micro-lotes, Bean-to-Bar. Ao mesmo tempo que fazemos um produto único no mercado Português, uma vez que somos a empresa pioneira neste tipo de chocolate no nosso país, contribuímos para o que nos moveu desde o início do projeto: pagamos um preço justo, acima do praticado no mercado, pela matéria prima que utilizamos, contribuindo de igual forma à motivação dos produtores para um cacau de alta qualidade cujo preço é proporcional e adequado ao seu esforço e dedicação. Ganha o chocolate, ganhamos todos os que o provamos.
Em Portugal, desejamos alterar a ideia do chocolate ser apenas um doce para crianças: é um alimento dos Deuses, para todas as idades.Desde 2017, os chocolates da Feitoria do Cacao têm sido premiados pelos concursos internacionais mais conceituados no sector.

«2017»
Concurso Nacional Chocolates Tradicionais 2017
 OURO… Chocolate Negro Nicarágua Nicalizo 76%
 OURO… Chocolate de Leite Tanzânia 60% + Leite de Ovelha
Academy of Chocolate Awards 2017
 SILVER… Chocolate Negro Nicarágua Nicalizo 76%
International Chocolate Awards / European Bean to Bar 2017
 GOLD… Chocolate Negro Costa Rica Maleku 92%
 BRONZE… Chocolate de Leite Tanzânia 60% + Leite de Ovelha
Great Taste 2017
1 Estrela … Chocolate de Leite Tanzânia 60% + Leite de Ovelha
«2018»
Academy of Chocolate Awards 2018
 BRONZE… Chocolate de Leite Nicarágua 57% + Nibs
 GOLD… Packaging – Bar wrappers
International Chocolate Awards / European Bean to Bar 2018
 BRONZE… Chocolate de Leite Colômbia 58 + Café
 BRONZE… Chocolate de Leite Nicarágua 57% + Nibs
Great Taste 2018
 1 Estrela … Chocolate de Leite Colômbia 58 + Café
 1 Estrela … Chocolate de Leite Tanzânia 60% + Leite de Ovelha
«2019»
Academy of Chocolate Awards 2019
 SILVER… Chocolate de Leite Nicarágua 57% + Nibs
 BRONZE… Chocolate Branco 45% + Leite dos Açores
 BRONZE… Chocolate de Leite Tanzânia 60% + Leite de Ovelha
 COMMENDED… Chocolate Negro Peru Marañón 72%
 COMMENDED… Chocolate Negro Costa Rica Maleku 76%
International Chocolate Awards / European Bean to Bar 2019
 BRONZE… Chocolate Negro Costa Rica Maleku 76%
Great Taste 2019
 2 Estrela… Chocolate de Leite Tanzânia 60% + Leite de Ovelha
«2020»
Academy of Chocolate Awards 2020 
 SILVER… Chocolate de Leite Nicarágua 57% + Nibs
 SILVER… Chocolate de Leite Tanzânia 60% + Leite de Ovelha
 SILVER… Chocolate Negro São Tomé 72% + Flor de Sal de Aveiro
 SILVER… Chocolate Negro Costa Rica Maleku 92%
 BRONZE… Chocolat de Leite Colômbia 58% + Café
 BRONZE… Chocolate Negro Peru Marañón 72%"""))
