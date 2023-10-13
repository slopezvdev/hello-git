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
git revert borra un commit en concreto y crea uno ultimo con los cambios realizados (buscar info)
git branch login crea una rama diferente a main, llamada login, en el mismo commit en el que estamos, teniendo el head en el main y aparte tenemos el login
git switch login hace que el head este en login y el main queda aparte (creamo otra rama para no mezclar cosas, en este caso para hacer un log in)
    si hacemos un commit se guardara en la rama login, sin afectar a la rama main
    si volvemos a la rama main, no veremos las modificaciones guardadas dentro de la rama login y viceversa, aunque estan guardadas en esa rama
git merge main desde la rama login lo que hace es traer los cambios realizados en la rama del comando (main) a la rama actual en la que estamos (login)
cuando dos "equipos" modifican la misma linea de codigo del mismo fichero, porque el equipo de una rama ha modificado ficheros de la otra rama, git no deja
    hacer un merge, nos dice en que se diferencia cada fichero y tenemos que elegir con que version nos quedamos
git stash guarda teporalmente algo en lo que estamos trabajando, sin hacer commit, para si por ejemplo estamos trabajando en una rama y queremos ir a otra,
    sin hacer commit porque las modificaciones que estamos realizando estan incompletas. Al hacer stash automaticamente la rama enla que estamos vuelve al commit anterior y lo que hubieramos cambiado se queda guardado en el stash
git stash list nos muestra una lista de los stash
git pop nos devuelve al stash, recuperando las modificaciones que habiamos guardado en el
git drop borra el stash
'''