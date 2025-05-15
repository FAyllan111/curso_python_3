#FUNÇÃO PRINT

#  funcoes print recebe argumentos, usa a virgula para trazer novos argumentos
print("dsddad",598,256.69) # argumentos nao nomeados
# separador
print(12,34,sep="") #-> sem separador
print(12,34,sep="-") # separador personalizado , padrão " "
# quebra de linha , end => pode mudar conforme abaixo
"""
\r\n => caracteres para quebra de linha windows -> CRLF
\n -> linux e mac , unix LF
"""
print(12,34,sep="",end='\r\n')
print(12,34,sep="-",end='\n') #  sep e end sao separadores nomeados dentro do python