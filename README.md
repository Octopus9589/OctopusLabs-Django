# Requirements - OctopusLabs technical challenge

## 1. Support two environments: local​ (for docker-compose) and production​ (for kubernetes).
Opening the application (GET /) in each should print out either “running in local” or
“running in production” accordingly.

- docker-compose.yaml file is created for local setup with different services

- I use environment variable config `DEV_MODE`, when it's available, we print "running on local",
  otherwise, "running in production" when (GET /) is accessed.


## 2. Include Mysql, Redis and Memcached in the cluster and demonstrate their usage inside Django app (e.g. for session storage or publishing an event, nothing too complicated).

1. Setup the enviroment

- docker-compose.yml file is created with different docker images to be used.
 + the dev service with our `django-dev:develop` image which is built from the build-dev.sh file.
    We use this file to build the development environment for django app (with the Dockerfile-dev file)
  + Other services (db, memcached, redis) is added with standard docker images. We can use the service
    names as hostname to connect to these services.

- `Pipfile` is used to install python package dependencies to be used for the django app (https://github.com/pypa/pipfile)

- We use environment variables for configurating the app, .env and .env-dev is used to create env vars
  for `dev` and `db` services in the docker-compose.yml file (https://docs.docker.com/compose/environment-variables/#the-env_file-configuration-option)

- `app` directory is the django app entry point; `home` and `polls` are all standard Django applications.

- we use run-dev.sh bash script to run the dev service

- we use run-migration.sh bash script to run any migration for the django app

2. Run the app

To run the app, we need to run the following commands:

  ```
  $ sh build-dev.sh
  $ docker-compose up -d dev
  $ docker-compose logs -f dev # for logging
  $ docker-compose exec dev pipenv run python manage.py createsuperuser
  $ docker-compose exec dev pipenv run sh run-migration.sh
  ```

3. Run command within the dev container

  ```
  $ docker-compose exec dev sh
  ...
  $ docker-compose exec dev pipenv run <cmd>
  ```

- mysql, redis and memcahed are installed via helm chart dependencies (see https://github.com/Octopus9589/OctopusLabs/blob/master/helm-charts/django-app/requirements.yaml)

- to access these services, we use env variables:
  + https://github.com/Octopus9589/OctopusLabs/blob/master/helm-charts/django-app/templates/deployment.yaml#L36
  + configmap is created by https://github.com/Octopus9589/OctopusLabs/blob/master/helm-charts/django-app/templates/configmap.yaml
  + secrets is created by https://github.com/Octopus9589/OctopusLabs/blob/master/helm-charts/django-app/templates/secrets.yaml
  + default helm chart value is from the values.yaml file
  + you can override the values.yaml for customization with override.tpl.yaml file which is a template file
    to generate override.yaml file from environment variable from the host machine.

- Open GET /mysql to see if the database is connected https://github.com/Octopus9589/OctopusLabs/blob/master/home/views.py#L28
  
  To check the database connection, I call `User.objects.all()`. If it's ok, "Throw no error! The app have been connected to mysql server successfuly" will be printed.


- To use Redis, make sure to have `REDIS_ENABLED` env var set with "enabled" value,
  then open GET /redis which will call this view function https://github.com/Octopus9589/OctopusLabs/blob/master/home/views.py#L44

  the view function will cache the timestamp of the request within 10 seconds and display that cache value.


- To use memcached, make sure to have `MEMCACHED_ENABLED` env var set with "enabled" value,
  then open GET /memcached which will call this view function https://github.com/Octopus9589/OctopusLabs/blob/master/home/views.py#L33

  the view function will cache the timestamp of the request within 10 seconds and display that cache value.



## 3. The application should auto scale​ based on cpu usage. Both the web server (e.g.Nginx) and the chosen wsgi should scale independently.

autoscaler is added with the scaler.yaml file for the wsgi app deployment (helm-charts/django-app/templates/scaler.yaml)

For the nginx (from nginx ingress), we can use the smilar configuration for the deployment.


## 4. Application needs to include a secret key​ to communicate with a hypothetical external service (e.g. Stripe). Please demonstrate storing this secret inside the cluster and then using it from inside the Django app.

I use https://github.com/dj-stripe/dj-stripe django app and configure it with environment variables.

k8s secrets are used to store the secrets:
- https://github.com/Octopus9589/OctopusLabs/blob/master/helm-charts/django-app/values.yaml#L32
- https://github.com/Octopus9589/OctopusLabs/blob/master/helm-charts/django-app/templates/secrets.yaml#L12
- https://github.com/Octopus9589/OctopusLabs/blob/master/helm-charts/django-app/templates/deployment.yaml#L45



## 5. Create Jenkins configuration to build and upload images to a chosen registry, as well as deploy the application to Kubernetes (master branch only).
NA

## 6. Store the code in a Github repository. Bonus points 1. Demonstrate usage of Helm Charts. 2. Demonstrate usage of Prometheus.
NA
