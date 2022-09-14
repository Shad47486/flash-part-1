ssh Reshad@20.226.76.149 #(azure)
#allows connection to VM from my ssh
sudo apt-get update
sudo apt install python3-pip
sudo apt install python3-flask
#sudo cause its not installed yet and needs higher admins. privliage
pip3 install flask
#now installed can do normal pip3 install 
nano app.py
#allows to open .py folder 
#paste codes in respected VM station 