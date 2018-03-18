codigo = {
'AUA':'I', 'AUC':'I', 'AUU':'I', 'AUG':'M',
'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACU':'T',
'AAC':'N', 'AAU':'N', 'AAA':'K', 'AAG':'K',
'AGC':'S', 'AGU':'S', 'AGA':'R', 'AGG':'R',
'CUA':'L', 'CUC':'L', 'CUG':'L', 'CUU':'L',
'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCU':'P',
'CAC':'H', 'CAU':'H', 'CAA':'Q', 'CAG':'Q',
'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGU':'R',
'GUA':'V', 'GUC':'V', 'GUG':'V', 'GUU':'V',
'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCU':'A',
'GAC':'D', 'GAU':'D', 'GAA':'E', 'GAG':'E',
'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGU':'G',
'UCA':'S', 'UCC':'S', 'UCG':'S', 'UCU':'S',
'UUC':'F', 'UUU':'F', 'UUA':'L', 'UUG':'L',
'UAC':'Y', 'UAU':'Y', 'UAA':'X', 'UAG':'X',
'UGC':'C', 'UGU':'C', 'UGA':'X', 'UGG':'W'}

def creaCodigoGenetico(codigo):
  AAs=''
  Starts=''
  Base1  = ''
  Base2 = ''
  Base3 = ''
  
  lista = []
  for key, value in sorted(codigo.items(), reverse=True): 
      lista = [key.replace("U","T")]
      Base1+= lista[0][0]
      Base2+= lista[0][1]
      Base3+= lista[0][2]
      if value=="X":
        AAs+='*'
        Starts+='*'
      elif value == 'M':
        AAs+='M'
        Starts+='M'
      else:
        Starts+='-'
        AAs+=value 
        
  print 'AAs=    ','\t',AAs,'\n','Starts=','\t',Starts,'\n','Base1 =','\t',Base1,'\n','Base2=','\t', Base2,'\n','Base3 =','\t',Base3
        
  tabla =['AAs='+AAs,'Starts='+Starts,'Base1 ='+Base1,'Base2 ='+Base2,'Base3 ='+Base3]
  
  return tabla

if len(codigo)==64:
  print 'All triplete checked'
  creaCodigoGenetico(codigo)
else:
  print 'Missing triplete'