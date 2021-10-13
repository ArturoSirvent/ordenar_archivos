import os
import numpy
import glob
import shutil
import re
#cogemos el numero y nombre de archivos que hay

mypath=os.getcwd();

#.jpg , jpeg , png , PNG
meses=('Enero','Febrero','Marzo','Abril','Mayo','Junio','Julio','Agosto','Septiembre','Octubre','Noviembre','Diciembre')
types=('*.jpg' , '*.jpeg','*.png','*.PNG');
lista_archivos=[];

for tipo in types:
	lista_archivos.extend(glob.glob(tipo));

#vamos a recorrer la lista de archivos viendo a donde debe ir cada uno de ellos, si no existiera el 
#directorio antes de mandarlo alli, lo debemos crear

#creamos el directorio de las fotos
if(not('photos_ordenadas' in os.listdir())):
	os.mkdir('photos_ordenadas')

dirgen=mypath +'/'+ 'photos_ordenadas'

for foto in lista_archivos:
	var=re.findall('[0-9]',foto);
	año1=var[0]+var[1]+var[2]+var[3]
	mes1=var[4]+var[5]
	dia1=var[6]+var[7]
	
	#comprobar si existe ese directorio de año y de mes
	lista_dir=os.listdir(dirgen)
	if(not(año1 in lista_dir)):
		os.mkdir(dirgen +'/'+ año1)

	lista_dir=os.listdir(dirgen +'/'+ año1)
	if(not(meses[int(mes1)-1] in lista_dir)):
		os.mkdir(dirgen +'/'+ año1 +'/'+ meses[int(mes1)-1])
	#ahora solo hay que moverlo
	shutil.move(mypath+'/'+ foto ,dirgen +'/'+ año1 +'/'+ meses[int(mes1)-1] +'/'+ foto)

	



