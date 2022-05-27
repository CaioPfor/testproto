import pandas as pd
tabela =pd.read_excel("Salmonfresco.xlsx")
arq= open("tabela.html","w")
arq.write(tabela.to_html())