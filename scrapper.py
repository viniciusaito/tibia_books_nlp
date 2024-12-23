"""

CSV = 

Nome: 1001 Ways to Use Energy Beams (Book)
Descrição: A long book with many different uses for the energy beam spell.
Adicionado:	5.1 (23 de dezembro de 1999)
Texto: 1001 ways to use energy beams Written by Hrmumundus Grofrukle...

1001 Ways to Use Energy Beams (Book),A long book with many different uses for the energy beam spell.,5.1 (23 de dezembro de 1999),1001 ways to use energy beams Written by Hrmumundus Grofrukle...
"""

from httpx import get

response = get("https://www.tibiawiki.com.br/wiki/0152551751_(Book)")

print(response.text)
