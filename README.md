# Elections 2018

Analyzer of tweets for the Mexican elections of 2018

## Team

- César Arturo González Pérez
- Alfonso Iraí Contreras Chávez
- José Alejandro Vázquez Sánchez
- Michelle Sagnelli D'urzo

## Getting Started

The variables with **$** you need to change them for the API values in the .env file
```
export CONSUMER_KEY=$consumer_key
export CONSUMER_SECRET=$consumer_secret
export ACCESS_TOKEN=$access_token
export ACCESS_TOKEN_SECRET=$access_token_secret
export DB_HOST=$db_host
export DB_PORT=$db_port
export DB_USER=$db_user
export DB_PASSWORD=$db_password
export DB_SCHEMA=$db_schema
export ENVIRONMENT=(DEV or PROD)
```

### Make Commands
```
make install
make setup
make run
make playground
make tests
make clean
make analyze
```

### Config files
```
elections/utils/users.txt
elections/utils/candidates.txt
elections/storage/local_storage.json
```