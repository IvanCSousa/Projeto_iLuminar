watch -n 10 kubectl top pod deploy-luminar-c5b6f7654-g44bm

kubectl run --image=fortio/fortio fortio -- load -qps 30000 -t 20s -c 2000 "http://svc-luminar:5000/connect"

#qps - queries por seconds (requisições por segundo)
#t - tempo 
#c - quantas conexões concorrentes