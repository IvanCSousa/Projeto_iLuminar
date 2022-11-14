kubectl create ns kong
openssl req -new -x509 -nodes -newkey ec:<(openssl ecparam -name secp384r1) \
-keyout /tmp/cluster.key -out /tmp/cluster.crt \
-days 1095 -subj "/CN=kong_clustering"

kubectl -n kong create secret generic kong-superuser-password --from-literal=password=kongiluminar

echo '{"cookie_name":"admin_session","cookie_samesite":"off","secret":" ","cookie_secure":true,"storage":"kong"}' > ./admin_gui_session_conf
echo '{"cookie_name":"portal_session","cookie_samesite":"off","secret":" ","cookie_secure":true,"storage":"kong"}' > ./portal_session_conf

kubectl -n kong create secret generic kong-session-config --from-file=./admin_gui_session_conf --from-file=./portal_session_conf

helm repo remove kong
helm repo add kong https://charts.konghq.com
helm repo update

helm -n kong upgrade --install api-gateway kong/kong --values tradicional.yaml

kubectl -n kong delete jobs --all

kubectl -n kong port-forward svc/kong-kong-admin 8001:8001 &
