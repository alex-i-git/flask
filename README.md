добавить локальный образ в k3s

crictl images

docker save hello-flask:latest -o hello-flask.tar
k3s ctr images import hello-flask.tar 
k3s ctr images list|grep flask
