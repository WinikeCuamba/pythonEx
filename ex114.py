me = 9999
ma = 0
for n in range(1, 4):
   num = int(input('Digite um número: '))
   
   if num == me and num == má: 
      me = num
      ma = num

   else:
        if num < me:
           me = num
        if num > ma:
           ma = num

print('===' * 7)
print('O menor número foi {}'.format(me))
print('O maior número foi {}'.format(ma))
print('===' * 7)

