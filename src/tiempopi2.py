
#! encoding: UTF-8
import time
import timeit
import modulo
import matplotlib.pylab as pl
x=[]
y1=[]
y2=[]
def error(nro_intervalos,nro_test,umbral):
  fallos=0
  for i in range (nro_test):
    s=modulo.aproxpi(nro_intervalos)
    error=abs(s-modulo.pi)
    if error>=umbral:
      fallos=fallos+1
  return ((fallos/nro_test)*100)
if __name__=="__main__":
   import sys
   if (len(sys.argv)==4):
     p1=int(sys.argv[1])
     p2=int(sys.argv[2])
     p3=float(sys.argv[3])
   else:
     print "Usted debe proporcionar tres valores, errorpi.py y tres valores numéricos, ahora se ejecutará por defecto con los valores 5 5 0.1"
     p1=5
     p2=5
     p3=0.1 
   print "Introduzca el nombre del fichero para almacenar los resultados:"
   nombre_fichero= raw_input();
   f=open(nombre_fichero, 'w')
   
   for i in range(1,6):
    p1=p1*i
    p3=p3*i
    start=time.time()
    s=error(p1,p2,p3)
    finish=time.time()-start
    print "El porcentaje de error es de: %5.3f" %s
    print "El tiempo que tarda en realizarse es: %14.13f" %finish
    x=x+[finish]
    y1=y1+[p1]
    y2=y2+[s]
    
    f.write(str(finish) + '\n')
    f.write(str(s) + '\n') 
   f.close()
   
   graf1=pl.subplot(211) 
   pl.title('Tiempo respecto al numero de intervalos') 
   pl.xlabel('Tiempo')
   pl.ylabel('Numero de intervalos')
   pl.plot (x,y1, marker='o',linestyle=':',color='r', label='funcion 1')
   pl.legend(loc=4)

   graf2=pl.subplot(212) 
   pl.title('Umbral respecto al error')
   pl.xlabel('Umbral') 
   pl.ylabel('Error')
   pl.plot (x,y2, marker='*',linestyle='-',color='m',label='funcion 2')
   pl.legend()
    
   pl.savefig("grafica.eps", dpi=100) 
   pl.show()