# Prerequisite

  - minikube: latest (v0.28.2)
  - kubectl: latest (1.11.2)
  - helm: latest
  - gettext

# Local Dev

1. Config `minikube` for testing on local

  ```
  $ ifconfig # and find vboxnet0 inet <INET-IP>
  $ export K8S_INET_IP=<INET-IP>
  $ minikube start --insecure-registry=$K8S_INET_IP:5000
  $ eval $(minikube docker-env)
  $ kubectl config use-context docker-for-desktop # to use kubectl command to access the minikube
  ```

2. Setting up:
  
  Build the production image then init `helm`

  ```
  $ sh build.sh
  $ helm init --service-account=default
  ```

  Set up the hostname:
  ```
  $ kubectl cluster-info # and get the <CLUSTER-IP>

  # Open `/etc/hosts`:
  $ vim /etc/hosts

  # Then put the `<CLUSTER-IP>` into it:
  ...
  <CLUSTER-IP>  django-example.local
  ...
  ```

  We use this hostname to access the app

3. Deploy:

  Config `ALLOWED_HOSTS`:

  ```
  $ . ./scripts/export-local.sh # for Linux base
  $ eval $(sh ./scripts/export-local.sh) # for Mac base
  $ export HELM_ALLOWED_HOSTS=$K8S_INET_IP,django-example.local,django-example,localhost,127.0.0.1
  ```

  Then:

  ```
  $ cd helm-charts/django-app && helm dep update && cd ../..
  $ envsubst <$HELM_CHART_PATH/override.tpl.yaml >$HELM_CHART_PATH/override.yaml
  $ kubectl delete job $HELM_RELEASE_NAME-migration
  $ helm upgrade --install $HELM_RELEASE_NAME $HELM_CHART_PATH \
      -f $HELM_CHART_PATH/values.yaml \
      -f $HELM_CHART_PATH/override.yaml \
      --namespace=$HELM_K8S_NAMESPACE
  ```

Override.yaml file is created with customized values to override the defaul values from the values.yaml file

Open `http://django-example.local/`


# Cloud Deploy

You can apply the same flow to deploy to cloud k8s cluster (GKE for example)


# Config dependencies

  more at https://docs.helm.sh/developing_charts/#scope-dependencies-and-values
