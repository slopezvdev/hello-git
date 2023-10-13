print("New Hello Git!")

'''
touch para crear ficero
git init para inicializar git en el proyecto
git status para ver el estado de nuestro proyecto
git add para añadir
git add . añade todos los ficheros pendientes
git checkout hellogit.py devuelve el fichero al ultimo commit
git log para ver todos los commits
git log --graph para ver mas grafico
git log --graph --pretty=oneline sale a una linea
git log --graph --decorate --all --oneline el hash sale resumido y sale a una linea
git config --global alias.tree "log --graph --decorate --all --oneline" para guardar esa forma de ver los commits con un alias
git tree para usarlo
touch .gitignore para crear un fichero donde vamos a meter otros ficheros que no queremos tener en cuenta en git
en el .gitignore ponemos **/ y el nombre del archivo a ignorar, como **/.DS_Store (es un archivo que genera automaticamente mac en todas las carpetas)
el .gitignore se debe añadir a git

'''