class ContaBanco:
   def __init__(self):
      self.__numConta = None
      self._tipoConta = None
      self.__saldo = None
      self.__dono = None
      self.__status = False
   @staticmethod 
   def eNumero(numero):
     if numero.isnumeric():
       valor = num
     else:
       valor = None
     return valor

   #Getter
   @property
   def numConta(self):
      return self.__numConta

   #Setter
   @numConta.setter
   def numConta(self):
      self.__numConta = numconta

   #Getter
   @property
   def tipo(self):
      return self._tipoConta
      
   #Setter  
   @tipo.setter
   def tipo(self, tipo):
      if tipo.upper == 'CC' or 'CP':
         self._tipoConta = tipo
      else:
         print('Tipo de conta inválido só CC para Conta corrente e CP para conta poupança')
         

   #Getter
   @property
   def dono(self):
      return self.__dono
    
    #Setter  
   @dono.setter
   def dono(self):
      self.__dono = dono
   
   #Getter
   @property
   def status(self):
      return self.__status
      
    #Setter
   @status.setter
   def status(self):
      self.__status = status

   @property
   def saldo(self):
     return self.__saldo
     
     
   @saldo.setter
   def saldo(self, eNumero(valo)):
       self.__saldo = valor
      
       
   
     #else: #saldo.isnumeric() == False:
       
     
     
  
   def mostrar(self):
      print(self.__numConta)
      print(self._tipoConta)
      print(self.__dono)
      print(self.__status)
      print(f'{self.__saldo:.2f}MT'.replace( '.' , ','))
      
         
   def abrirConta(self, contaNum, tipo, dono):
      self.__numConta = contaNum
      self._tipoConta = tipo
      self.__dono = dono
      self.__status = True
      if self._tipoConta == 'CP':
        self.__saldo = 100
      
      elif self._tipoConta == 'CC':
        self.__saldo = 50
      
      else:
        self.__saldo = None


    
   def fecharConta(self):
     self.__numConta = None
     self._tipoConta = None
     self.__dono  = None
     self.__status = False

   def depositar(self, deposito):
     if self.__status == True:
       self.__saldo += deposito
     
     
   #def sacar(self, sac):
     
     
   #def pagarMensal(self):
         
  
  
   