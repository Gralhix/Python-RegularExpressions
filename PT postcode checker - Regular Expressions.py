# Playing with regular expressions to improve the "PT postcode checker.py" previous code created.


# importing regular expressions
import re

# Portuguese postcode uses the following format: 1234-123. Four digits, followed by a dash and then 3 more digits.
postcoderegx = re.compile(r"\d\d\d\d-\d\d\d")


# Using "findall" to find all the postcodes instead of just the first one (which would happen if using "search" instead.
# This excerpt has been copy pasted from "https://liguem.com/curiosidades-sobre-os-codigos-postais-portugueses/"
# Will print any postcode that fits the criteria in the text below.

print(postcoderegx.findall("""Códigos postais reservados para entidades
Instituições e organizações tais como Repartições de Finanças, Conservatórias, Tribunais, Escolas, Faculdades, Universidades, Juntas de Freguesia, Câmaras Municipais, Ministérios, Secretarias de Estado, Lojas CTT, Lojas de Cidadão, Centros de Emprego e empresas que por qualquer razão comerciais assim o decidam e contactem os CTT podem ter um código postal exclusivo para si. Empresas com uma forte presença no comércio online e que recebem várias encomendas com devoluções, normalmente têm um código postal dedicado. Na teoria quando utiliza um destes códigos postais, a artéria e o número da porta é irrelevante, dado que os CTT já sabem que com aquele código postal específico, quem será o receptor da correspondência.

Os 4 primeiros dígitos dos códigos postais destas entidades podem terminar com qualquer dígito no entanto existe uma distribuição mais predominante de alguns números (terminados em 0, 1, 4, 5 e 9) e menos predominantes de outros números (terminados em 6, 7, 8). Códigos Postais terminados em 3 existe apenas um que pertence à “TIFFOSI” e terminado em 2 não existe nenhum.

O número de entidades por cada dígito final dos 4 primeiros dígitos é o seguinte: número 0 (1103 entidades), 1 (161), 2 (0), 3 (1), 4 (1122), 5 (266), 6 (24), 7 (5), 8 (25), 9 (1843).

De notar no entanto que para códigos postais terminados em 0 ou 5, a única entidade que lhe está associada é o próprio CTT (Lojas CTT, Postos de Correios, Centros de Distribuição Postal, etc) e normalmente nestes códigos postais os 3 últimos dígitos do código postal terminam com um valor entre 995 e 999 ou 000 (Centros de Distribuição Postal ou de Apoio à Distribuição)..

Exemplos de entidades:
1100-000 – Centro Distribuição Postal (CDP) 1100 (LISBOA) Lisboa
8501-857 – CONSERVATÓRIA DO REGISTO CIVIL E PREDIAL (Portimão)
4763-001 – TIFFOSI (Lousado) (único código postal terminado em 3)
9054-530 – 2ª REPARTIÇÃO DE FINANÇAS (Funchal)
2825-999 – LOJA CTT COSTA DE CAPARICA (Costa de Caparica)
1886-502 – COMANDO METROPOLITANO DA PSP DE LISBOA (Moscavide)
1067-001 – FUNDAÇÃO CALOUSTE GULBENKIAN (Lisboa)
1998-017 – VODAFONE (Lisboa)
1069-098 – ZARA PORTUGAL (Lisboa)"""))

