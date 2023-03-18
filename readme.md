#Aplikacja z serwerem opartym na Localstack

Aplikacja korzysta z usług AWS (AWS Lambda, AWS EC2, AWS ECS oraz dodatkowych usług) lokalnie za pomocą narzędzia Localstack. W tym README znajdziesz informacje, jak skonfigurować i uruchomić te usługi.

#Wymagania

- Python 3.6 lub nowszy
- Localstack
- AWS CLI (dla lokalnych operacji na usługach AWS)

#Instalacja

1. Zainstaluj Localstack:

pip install localstack

2. Zainstaluj AWS CLI (jeśli jeszcze tego nie zrobiłeś):

pip install awscli

#Konfiguracja

1. Skopiuj plik `localstack-config.yaml` do głównego katalogu projektu.

2. Przygotuj swoje funkcje Lambda, instancje EC2, zadania ECS oraz inne usługi AWS w odpowiednich skryptach (np. `hello_lambda.py`, `launch_ec2_instance.py`, `launch_ecs_task.py`).

#Uruchomienie

1. Uruchom Localstack, używając pliku konfiguracyjnego:

localstack start --config localstack-config.yaml

2. Utwórz i uruchom swoje funkcje Lambda, instancje EC2, zadania ECS oraz inne usługi AWS, korzystając z odpowiednich skryptów:

- AWS Lambda:

aws --endpoint-url=http://localhost:4574 lambda create-function --function-name helloLambda --runtime python3.8 --role anyrole --handler hello_lambda.lambda_handler --zip-file fileb://hello_lambda.zip

- AWS EC2:

python launch_ec2_instance.py

- AWS ECS:

python launch_ecs_task.py
