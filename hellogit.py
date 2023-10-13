print("New Hello Git with changes!")

'''
touch para crear ficero
para todos los siguientes comandos debemos estar en la carpeta deseada y en la que inicaicemos git
git init para inicializar git en el proyecto
git status para ver el estado de nuestro proyecto
git add para añadir al siguiente commit (antes tenemos que guardarlos)
git add . añade todos los ficheros pendientes
git commit -m "Comentario del commit" para hacer la "foto" de los archivos (antes hay que añadirlos con git add)
git checkout hellogit.py devuelve el fichero al ultimo commit
git reset para volver a una version anterior y descartar cambios
git log para ver todos los commits
git log --graph para ver mas grafico
git log --graph --pretty=oneline sale a una linea
git log --graph --decorate --all --oneline el hash sale resumido y sale a una linea
git config --global alias.tree "log --graph --decorate --all --oneline" para guardar esa forma de ver los commits con un alias
git tree para usarlo
touch .gitignore para crear un fichero donde vamos a meter otros ficheros que no queremos tener en cuenta en git
en el .gitignore ponemos **/ y el nombre del archivo a ignorar, como **/.DS_Store (es un archivo que genera automaticamente mac en todas las carpetas)
el .gitignore se debe añadir a git
git diff para ver las diferencias que hay entre lo guardado en commit y lo modificado
git checkout y el hash del commit deseado para volver a un guardado anterior (podemos poner el hash reducido)
git checkout head para indicar que es la nueva cabeza del proyecto (se guardan las anteriores versiones, pero en "una rama de la que hemos vuelto atras")
git guarda todo a nivel local, y cuando parece que yendo a un commit anterior borramos informacion o archivos, en realidad git lo tiene guardado
    solo que lo oculta
git reset --hard y el hash de donde queremos volver, lo que hace es llevar el head y el main al hash que hemos puesto, y "borra" lo que hemos hecho despues
git reflog muestra el historial completo de interacciones realizadas en git, donde podemos ver el hash de lo que hemos "borrado"
git reset --hard y el hash de el commit "borrado" al que queremos volver para volver a el
git tag clase_1 pone una etiqueta a el commit en el que nos encontramos
git tag nos muestra una lista de los diferentes tags
git checkout tags/clase_1 lleva el head a el tag puesto

'''